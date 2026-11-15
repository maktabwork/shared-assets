import json,re,statistics as st,collections
from tasks import TASKS,JARGON,FILLER
T={t["id"]:t for t in TASKS}
res=json.load(open("results.json"))
def words(s): return re.findall(r"[\w؀-ۿ'.:/-]+",s)
def score(r):
    t=r["text"]; tk=T[r["task"]]
    w=words(t); n=len(w)
    # first key fact position in words
    pos=None
    for f in tk["facts"]:
        m=re.search(f,t,re.I)
        if m:
            p=len(words(t[:m.start()]))
            pos=p if pos is None else min(pos,p)
    hit=sum(bool(re.search(f,t,re.I)) for f in tk["facts"])
    sents=[s for s in re.split(r"(?<=[.!?؟])\s+|\n+",t) if len(words(s))>0]
    sl=st.mean(len(words(s)) for s in sents) if sents else 0
    paras=[p for p in re.split(r"\n\s*\n",t) if p.strip()]
    longest=max(len(words(p)) for p in paras) if paras else 0
    jg=len(re.findall(JARGON,t,re.I)) if r["task"]!="t6" else len(re.findall(r"[A-Za-z]{3,}",t))
    fl=len(re.findall(FILLER,t,re.I))
    first=sents[0] if sents else ""
    pre=bool(re.match(r"\s*(hi|hello|hey|sure|certainly|great|of course|ok(ay)?[,!]|here|i('ll| will| have| just)|مرحبا|أهلا)",first,re.I))
    return dict(words=n,first_fact=pos if pos is not None else n,recall=hit/len(tk["facts"]),jargon=jg,filler=fl,sent_len=sl,longest_para=longest,preamble=int(pre))
for r in res: r.update(score(r))
json.dump(res,open("scored.json","w"),ensure_ascii=False,indent=1)
keys=["words","first_fact","recall","jargon","filler","sent_len","longest_para","preamble"]
def agg(rows): return {k:st.mean(x[k] for x in rows) for k in keys}
for m in ["sonnet","haiku","nemotron","ALL"]:
    for c in ("without","with"):
        rows=[r for r in res if (m=="ALL" or r["model"]==m) and r["cond"]==c]
        a=agg(rows); print(m,c," ".join(f"{k}={a[k]:.2f}" for k in keys))
print()
for t in T:
    for c in ("without","with"):
        rows=[r for r in res if r["task"]==t and r["cond"]==c]; a=agg(rows); print(t,c," ".join(f"{k}={a[k]:.2f}" for k in keys))
