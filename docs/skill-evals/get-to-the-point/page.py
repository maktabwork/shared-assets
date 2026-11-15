import json,html,random,statistics as st
from tasks import TASKS
res=json.load(open("scored.json"))
random.seed(7)
keys=["words","first_fact","recall","jargon","filler","longest_para"]
def mean(rows,k): return st.mean(x[k] for x in rows)
def rows(**f): return [r for r in res if all(r[k]==v for k,v in f.items())]
MN={"sonnet":"Sonnet 5.5","haiku":"Haiku 5.5","nemotron":"Free model (Nemotron)"}
def cell(a,b,k,low=True,pct=False):
    f=(lambda v:f"{v*100:.0f}%") if pct else (lambda v:f"{v:.1f}")
    d=(b-a)/a*100 if a else 0
    good=(d<=0) if low else (d>=0)
    small=(a<1 and b<1 and not pct)
    cls="" if small else "good" if (abs(d)>=10 and good) else ("bad" if abs(d)>=10 else "")
    return f"<td>{f(a)}</td><td>{f(b)}</td><td class='{cls}'>{'' if not a else f'{d:+.0f}%'}</td>"
def table(title,group):
    out=f"<h3>{title}</h3><div class=tw><table><tr><th>Measure</th><th>Without</th><th>With</th><th>Change</th></tr>"
    labels=[("words","Words in the answer (lower is better)",True,False),("first_fact","Words before the first key fact (lower is better)",True,False),("longest_para","Words in the longest paragraph (lower is better)",True,False),("recall","Key facts kept (higher is better)",False,True),("jargon","Jargon words, count per answer (lower is better)",True,False),("filler","Filler phrases, count per answer (lower is better)",True,False)]
    for k,l,low,pct in labels:
        a=mean([r for r in group if r["cond"]=="without"],k); b=mean([r for r in group if r["cond"]=="with"],k)
        out+=f"<tr><td>{l}</td>{cell(a,b,k,low,pct)}</tr>"
    return out+"</table></div>"
sections=table("All 36 answers per side (6 tasks × 3 models × 2 tries)",res)
for m in MN: sections+=table(MN[m]+f" ({len(rows(model=m))//2} answers per side)",rows(model=m))
# blind examples
ex=""
for ti,t in enumerate(TASKS):
    for m in ("sonnet","nemotron"):
        w=rows(model=m,task=t["id"],cond="without",rep=1)[0]; s=rows(model=m,task=t["id"],cond="with",rep=1)[0]
        pair=[("without",w),("with",s)]; random.shuffle(pair)
        d="rtl" if t["lang"]=="ar" else "ltr"
        cols=""
        for lab,(cond,r) in zip("AB",pair):
            cols+=f"""<div class=ans><div class=lab>Answer {lab}</div><div class=txt dir=auto>{html.escape(r['text'].strip())}</div>
<div class=stat hidden><b>{'WITH skill' if cond=='with' else 'WITHOUT skill'}</b> · {r['words']} words · first key fact at word {r['first_fact']} · facts kept {r['recall']*100:.0f}%</div></div>"""
        ex+=f"""<section class=ex><h4>{html.escape(t['title'])} <span class=m>· {MN[m]}</span></h4>
<details><summary>The request given to Mo</summary><div class=req dir=auto>{html.escape(t['prompt'])}</div></details>
<div class=pair>{cols}</div><button onclick="reveal(this)">Show which is which</button></section>"""
page=f"""<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Get-to-the-point skill test</title>
<style>
:root{{--bg:#fafaf7;--fg:#1c1c1a;--mut:#6b6b66;--card:#fff;--line:#e3e2dc;--good:#0a7a3d;--bad:#b3261e;--acc:#1456c8}}
@media(prefers-color-scheme:dark){{:root{{--bg:#141413;--fg:#ecebe6;--mut:#9a9992;--card:#1e1e1c;--line:#34332f;--good:#5fd08a;--bad:#ff8a80;--acc:#7fa9ff}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,sans-serif}}
main{{max-width:980px;margin:0 auto;padding:24px 16px 80px}}h1{{font-size:28px;margin:0 0 4px}}h2{{margin-top:44px;font-size:22px}}h3{{margin:28px 0 8px;font-size:17px}}
.box{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px}}.box ul{{margin:6px 0 0;padding-left:20px}}
.tw{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;background:var(--card);border:1px solid var(--line);border-radius:8px}}th,td{{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;font-size:15px}}td+td,th+th{{text-align:right}}
.good{{color:var(--good);font-weight:600}}.bad{{color:var(--bad);font-weight:600}}.m{{color:var(--mut);font-weight:400;font-size:14px}}
.ex{{margin:26px 0;padding-top:6px;border-top:1px solid var(--line)}}.ex h4{{margin:10px 0}}summary{{cursor:pointer;color:var(--mut);font-size:14px}}.req{{white-space:pre-wrap;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 12px;font-size:14px;margin-top:6px}}
.pair{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}}@media(max-width:700px){{.pair{{grid-template-columns:1fr}}}}
.ans{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px}}.lab{{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--acc);font-weight:700;margin-bottom:6px}}.txt{{white-space:pre-wrap;font-size:15px}}.stat{{margin-top:10px;padding-top:8px;border-top:1px dashed var(--line);font-size:13px;color:var(--mut)}}
button{{font:inherit;background:var(--acc);color:#fff;border:0;border-radius:8px;padding:8px 14px;cursor:pointer}}
</style></head><body><main>
<h1>Does the “get to the point” skill work?</h1>
<p class=m>Test run 15 Nov 2026 · 72 answers · scored by a script, not by Claude</p>
<div class=box><b>Short answer:</b> yes for length and speed to the point, no change on jargon and filler.
<ul>
<li>Answers are about <b>38% shorter</b> (108 → 67 words).</li>
<li>The first key fact comes after <b>10 words instead of 18</b>.</li>
<li>Key facts kept: <b>98% both ways</b>, so it cut words, not content.</li>
<li>Jargon and filler were already close to zero without the skill (Mo’s one-line plain-language rule already covers them), so there is nothing to improve there.</li>
<li>It works on the weaker free model too (24% shorter, first fact after 8 words instead of 18). Two of its answers came back empty at first, a model fault that was retried. On Haiku the longest paragraph got longer (40 → 47 words), so paragraph length is not fixed by the skill on every model.</li>
</ul></div>

<h2>Numbers</h2>
<p>Green or red means a change of 10% or more. “Key facts” are 3 to 6 facts per task that must stay (for example “2.8:1 contrast”, “iPhone not checked”); a script looks for them in the answer.</p>
{sections}

<h2>Judge it yourself</h2>
<p>Each pair below is the same request answered twice. Which is better, A or B? Read both first, then press the button to see which one had the skill. Which side has the skill is random. Sonnet and the free model are shown for each of the 6 tasks (first try of each).</p>
{ex}

<h2>How the test worked, and its limits</h2>
<div class=box><ul>
<li>6 real Mo tasks: telling the AM what it understood, a step summary, a blocker, the top box of a client page, a background-run report, and an Arabic message about an unclear ticket.</li>
<li>Same request and same Mo base prompt each time. The only change: the skill text added or not. Each combination run twice.</li>
<li>Models: Sonnet 5.5, Haiku 5.5, and a free model (Nemotron 3.5), through OpenRouter.</li>
<li>The skill was written before the test and not tuned on these tasks.</li>
<li>Limits: “key facts” and the jargon list are simple word matches, so they can miss rewording or miss a jargon word. Only 6 tasks and 2 tries, so treat a change under 10% as noise. It measures length and speed to the point, not whether a person likes the answer; that is why the pairs are above. We did not test Opus, and not inside real Claude Code runs with all skills loaded.</li>
<li>Code and raw answers: <code>docs/skill-evals/get-to-the-point/</code> in shared-assets.</li>
</ul></div>
</main>
<script>function reveal(b){{b.parentNode.querySelectorAll('.stat').forEach(s=>s.hidden=false);b.remove()}}</script>
</body></html>"""
import os
os.makedirs("/mnt/project-files/get-to-the-point/",exist_ok=True)
open("/mnt/project-files/get-to-the-point/index.html","w").write(page)
print(len(page))
