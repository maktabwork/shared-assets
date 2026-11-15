import json,os,sys,time,urllib.request,concurrent.futures as cf
from tasks import TASKS
os.environ.setdefault("SSL_CERT_FILE","/root/.ccr/ca-bundle.crt")
MODELS={"sonnet":"anthropic/claude-sonnet-5.5","haiku":"anthropic/claude-haiku-5.5","nemotron":"nvidia/nemotron-3.5-super-vl:free"}
SKILL=open("/home/user/shared-assets/skills/get-to-the-point/SKILL.md").read().split("---",2)[2].strip()
BASE="""You are Mo, Monjizeen's agent. An account manager (AM) works with you in Claude Code for one client at a time. Plain language with the AM: short sentences, what you did, what you need. Reply with only the text to show; no preamble about what you are doing."""
def call(model,system,user):
    body=json.dumps({"model":model,"messages":[{"role":"system","content":system},{"role":"user","content":user}],"max_tokens":1500,"temperature":0.7}).encode()
    for a in range(4):
        try:
            r=urllib.request.Request("https://openrouter.ai/api/v1/chat/completions",body,{"Content-Type":"application/json","Authorization":"Bearer dummy"})
            d=json.load(urllib.request.urlopen(r,timeout=180))
            return d["choices"][0]["message"]["content"] or ""
        except Exception as e:
            err=str(e); time.sleep(3*(a+1))
    return "ERROR "+err
jobs=[]
for m in MODELS:
    for t in TASKS:
        for cond in ("without","with"):
            for rep in (1,2):
                jobs.append((m,t["id"],cond,rep))
def run(j):
    m,tid,cond,rep=j
    t=[x for x in TASKS if x["id"]==tid][0]
    sysmsg=BASE+("\n\n# Skill: get-to-the-point\n"+SKILL if cond=="with" else "")
    return dict(model=m,task=tid,cond=cond,rep=rep,text=call(MODELS[m],sysmsg,t["prompt"]))
with cf.ThreadPoolExecutor(8) as ex: res=list(ex.map(run,jobs))
json.dump(res,open("results.json","w"),ensure_ascii=False,indent=1)
print(len(res),sum(r["text"].startswith("ERROR") for r in res),"errors")
