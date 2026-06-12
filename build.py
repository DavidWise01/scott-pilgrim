#!/usr/bin/env python3
"""Build the SCOTT PILGRIM vs. the WORLD (SPW) page — Edgar Wright's 2010 film of
Bryan Lee O'Malley's graphic novels, catalogued into UD0 as the first film-world.

Two layers, per ROOT0's brief:
  • the CARBONS — the human cast as ACI .agents, each with a .shadow: the real-life
    analog (the actor — the TRON "User" behind the program; every program has one).
  • the SYNTHS — the parabolic threads distilled into their own ACIs (the humor, the
    tone, the sphere of reference, the cultural tie-ins, and the keystone:
    the air-gapped generational information — what is lost at the ~8-year boundary
    of understanding between generations).

Full ACI badge work via the shared noesis kernel:
.agent · .shadow (carbons) · .attribute · .carbon.tiff · .silicon.png · .spun · .moniker · .1099 · manifest."""
import os, re, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "SCOTT PILGRIM", "axiom": "SPW",
 "position": "Scott Pilgrim vs. the World · Universal · 2010 — dir. Edgar Wright, from Bryan Lee O'Malley's graphic novels (2004–2010)",
 "origin": "a hyper-stylized Toronto rendered as a side-scrolling video game — Casa Loma, the Rockit, Honest Ed's, the snow and the subspace; a city where heartbreak pays out in coins",
 "mechanism": "Crystallized from the 2010 film and the six-volume graphic novel — life lived in the grammar of a 16-bit game: KOs and combos, extra lives, pee bars, and the X.",
 "crystallization": "To date the girl of his dreams, a coasting 23-year-old bassist must defeat her seven evil exes — and learn, the hard way, that the final boss was never them.",
 "nature": "Scott Pilgrim vs. the World — the romance-as-fighting-game where you beat every ex and still lose, until you stop fighting for the girl and start fighting for yourself.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the film (2010); O'Malley's six volumes; the Ubisoft beat-'em-up; Nigel Godrich's score & Beck's Sex Bob-omb songs; the dense lattice of game/indie/manga allusion",
 "witness": "No chosen one — a slacker who has to earn the only power that matters: self-respect.",
 "role": "the first film-world of UD0",
 "seal": "You beat the seven evil exes and still don't get the girl — until you fight the one boss you kept skipping: yourself.",
 "source": "Scott Pilgrim vs. the World, catalogued by ROOT0",
}

# the shared four-nature taxonomy — SPW-flavored glosses
NATURES = {
 "natural":   ("#ff3da6", "flesh-and-blood Toronto — the band, the roommates, the exes who are just people; carbon, with a real-life User behind each"),
 "ethereal":  ("#b07cff", "of dream and glamour — Ramona's subspace highway, the fame-aura, the vegan's psychic power, the half-ninja's smoke"),
 "spiritual": ("#ffd23d", "of the soul and the reckoning — the power of self-respect, the extra life, and the false-god who would own the scene"),
 "electrical":("#36e0e0", "the synth nature — life rendered as a game, the chiptune, the summoned robots, and the air-gap itself; not carbon, but constructed"),
}

IDEAS = [
 ("The Seven Evil Exes", "the League of Evil Exes", [
   "To date Ramona you must defeat her seven evil exes — a literal gauntlet of everyone she's loved before, each a boss fight that pays out in coins.",
   "It's the oldest insecurity in romance, rendered as a video game: you cannot have her until you've beaten her whole past." ]),
 ("Life as a Video Game", "the grammar of the 16-bit world", [
   "The film speaks fluent game: KO, combos, ‘L7’, extra lives, a pee bar, coins on death, the 1-UP, the save point.",
   "Nobody in the world remarks on it — the game-logic is just how reality works here. That is the joke and the genius." ]),
 ("The Power of Self-Respect", "the real final boss", [
   "Scott earns the Power of Love sword to fight Gideon — and loses. He returns with the Power of Self-Respect, and wins.",
   "The twist the whole film is built to deliver: you don't beat the exes to get the girl; you beat yourself to deserve anyone at all." ]),
 ("The Air-Gap", "references with a half-life", [
   "The densest reference-bomb of its era — the Zelda chime, the Seinfeld bass, the Final Fantasy victory fanfare, the coins, the manga lines.",
   "Half of it is already lost to anyone outside the ~2010 window: a parable of air-gapped generational information, decaying at the boundary of understanding." ]),
]

ARC = [
 ("I · Knives Chau, Age 17", "the easy life, on standby",
  "Scott is coasting — between jobs, dating a high-schooler because it's simple, playing bass in a band going nowhere. No stakes, no growth, no exes to fight. Comfortable, and quietly a coward."),
 ("II · Ramona & the League", "the gauntlet of the past",
  "Ramona rollerblades through his dreams and into his life, and the seven evil exes come for him one by one — Patel, Lee, Ingram, Richter, the Katayanagi twins, and Gideon. Scott wins fights and loses himself, hurting Knives and Ramona both."),
 ("III · vs. Himself", "the boss he kept skipping",
  "The Power of Love isn't enough; Gideon beats it. Scott earns the Power of Self-Respect — owns what he did, fights for who he wants to be rather than for a prize — and only then wins, and walks into the unknown a person worth dating."),
]

SECTIONS = [
 ("The Sources", "one story, told four ways", [
   ("Scott Pilgrim's Precious Little Life → Finest Hour", "2004–2010 · Oni Press", "Bryan Lee O'Malley's six graphic novels — the origin and the whole canon"),
   ("Scott Pilgrim vs. the World", "2010 · film · dir. Edgar Wright", "the reference-perfect adaptation; a box-office miss turned enduring cult landmark"),
   ("Scott Pilgrim vs. the World: The Game", "2010 · Ubisoft", "the Paul Robertson pixel-art beat-'em-up, with an Anamanaguchi chiptune score"),
   ("Scott Pilgrim Takes Off", "2023 · Netflix anime", "the original film cast returns to voice a canon-diverging retelling"),
 ]),
 ("The Makers", "the hands behind the world", [
   ("Bryan Lee O'Malley", "creator", "the graphic novels — the source canon and its heart"),
   ("Edgar Wright", "director & co-writer", "the smash-cut comic grammar; the film's whole visual language"),
   ("Michael Bacall", "co-writer", "the screenplay, with Wright"),
   ("Nigel Godrich · Beck", "score & songs", "Godrich's score; Beck wrote Sex Bob-omb's songs; Metric, Broken Social Scene as the in-world bands"),
   ("Michael Cera & Mary Elizabeth Winstead", "Scott & Ramona", "with Culkin, Pill, Plaza, Larson, Routh, Evans, Wong — a cast of soon-to-be-stars"),
 ]),
 ("The Air-Gapped References", "what decays at the generational boundary (~8 years)", [
   ("The Legend of Zelda ‘secret’ chime", "when Scott opens his mind to Ramona", "instantly legible to one generation, silent to the next"),
   ("Seinfeld bass + laugh-track sting", "the ‘ooh’ beat after a line", "a TV-grammar joke that only lands if you grew up on the rerun"),
   ("Final Fantasy victory fanfare & coins", "on each ex's defeat", "the JRPG reward-loop as emotional punctuation"),
   ("‘Pee bar’, 1-UP, KO, combos, L7", "the HUD over real life", "arcade literacy assumed — and quietly expiring"),
 ]),
]

# ---- ACI complement via noesis (identical idiom to the other spheres) ----
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","SPW")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","SPW")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","SPW")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],
            "carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
            "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
            "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

# ---- page fragments ----
def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
ARC_OVERALL = ("A coasting bassist beats the seven evil exes of the girl of his dreams, wins every fight and still "
  "loses — until he stops fighting for the prize and faces the only boss that matters, himself, and earns the "
  "self-respect that finally makes him worth loving.")
REALFLUFF = [
 ("Self-respect over conquest as the real lesson", "REAL", "the Power-of-Self-Respect twist is a genuine model of growing up"),
 ("‘Beat the exes to earn the girl’ as a love-model", "FLUFF", "and the film knows it — it's the misdirection the whole thing dismantles"),
 ("Life rendered as a fighting / video game", "RESONANT", "stylization, not realism — but it captures how young romance actually feels"),
 ("The air-gapped references decaying at ~8 years", "REAL", "measurable — half the chime-and-sting jokes are already lost to the next cohort"),
 ("Scott as a sympathetic hero", "HALF", "he's kind of a jerk; the film semi-knows it, which is exactly the growth"),
]
REALFLUFF_VERDICT = ("Bottom line: the romp is stylized and Scott is a bit of a jerk — both on purpose. But the thesis is "
  "REAL: you don't earn love by defeating rivals, you earn it by becoming someone worth loving, which means owning "
  "your own bad behavior. And the air-gap is real and measurable — the references really are decaying at the "
  "generational boundary. The fights are fluff; the growing-up is true.")
MESSAGE = ("Scott Pilgrim looks like a story about defeating your partner's exes; it's actually about defeating "
  "yourself. The seven evil exes are a misdirection — the real final boss is the coasting, self-justifying, slightly "
  "cowardly person Scott has been, who hurt Knives and Ramona while telling himself he was the hero. The Power of Love "
  "can't win that fight; only the Power of Self-Respect can. The message: you don't get the girl by winning — you "
  "become worth knowing by owning who you've been and choosing better.")
MESSAGE_SEAL = "You don't earn love by beating everyone she's loved — you earn it by beating the version of you that keeps skipping the hard fight."
RF_COL = {"REAL":"#5fe0a0","HALF":"#ffd23d","RESONANT":"#36e0e0","FLUFF":"#ff3da6"}
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC:
        out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def realfluff_html():
    rows=[]
    for claim,rate,note in REALFLUFF:
        c=RF_COL.get(rate,"#888")
        rows.append(f'<div class="rf-row"><div class="rf-claim">{html.escape(claim)}<span class="rf-note">{html.escape(note)}</span></div><div class="rf-rate" style="color:{c};border-color:{c}">{html.escape(rate)}</div></div>')
    return '<div class="rf">'+"".join(rows)+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'
def natures_html():
    cells=[]
    for nm,(col,gloss) in NATURES.items():
        cells.append(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
                     f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(gloss)}</div></div></div>')
    return "".join(cells)

def _agent5w(slug):
    fp = os.path.join(HERE, "agents", slug + ".agent")
    d = {}
    if os.path.exists(fp):
        txt = open(fp, encoding="utf-8").read()
        parts = txt.split("---")
        fm = parts[1] if len(parts) > 2 else ""
        for ln in fm.splitlines():
            k, _, v = ln.partition(":")
            k = k.strip()
            if k in ("who","what","why","how","where","seal","universe","shadow_user","shadow_analog"):
                d.setdefault(k, v.strip())
    return d

def _card(p):
    w = _agent5w(p["slug"])
    em = p.get("emergence", "natural"); col = NATURES.get(em, ("#9aa0aa", ""))[0]
    ax = (p.get("moniker", "::").split(":") + ["", ""])[1]
    rec = {"name": p["name"], "axiom": ax, "emergence": em,
           "seal": w.get("seal", p.get("epithet", "")), "origin": w.get("universe", "")}
    kind = p.get("kind", "carbon"); actor = p.get("actor", "") or w.get("shadow_user", "")
    urow = (f"""<div class="w"><span class="wl">user</span><span><b>{html.escape(actor)}</b> &mdash; {html.escape(w.get('shadow_analog',''))}</span></div>"""
            if kind == "carbon" and actor else "")
    rows = "".join(f"""<div class="w"><span class="wl">{lbl}</span><span>{html.escape(w.get(lbl,''))}</span></div>"""
                   for lbl in ['who','what','where','why','how'] if w.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{p['slug']}.agent">
        <img src="{png_uri(rec,'carbon',200)}" alt="carbon sigil of {html.escape(p['name'])}" loading="lazy"><span class="sl">carbon</span>
        <img src="{png_uri(rec,'silicon',200)}" alt="synth sigil of {html.escape(p['name'])}" loading="lazy"><span class="sl">synth</span>
      </a>
      <div class="pbody">
        <div class="ihead"><a class="pn" href="agents/{p['slug']}.agent">{html.escape(p['name'])}</a>
          <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
          <span class="pkind">{html.escape(kind)}</span></div>
        <div class="pe">{html.escape(p.get('epithet',''))}</div>
        <div class="pww">{urow}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{p['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div>
      </div></div>"""


def personas_html():
    mf=os.path.join(HERE,"agents","_personas.json")
    if not os.path.exists(mf): return ""
    ps=json.load(open(mf,encoding="utf-8"))
    carb=[p for p in ps if p.get("kind","carbon")=="carbon"]
    syn=[p for p in ps if p.get("kind")=="synth"]
    out=f'''<section class="sec" id="carbons"><h2>The Carbons — the programs &amp; their Users</h2>
      <p class="ss">the human cast as ACI <b>.agent</b>s — and each carries a <b>.shadow</b>: its real-life analog, the actor who is the <b>User</b> behind the program. Think TRON — every program has a User. ({len(carb)} carbons)</p>
      <div class="pgrid">{"".join(_card(p) for p in carb)}</div></section>'''
    out+=f'''<section class="sec" id="synths"><h2>The Synths — the parabolic threads</h2>
      <p class="ss">not characters but the film's <b>distilled qualities</b>, each given its own ACI — the humor, the tone, the sphere of reference, the cultural tie-ins, and the keystone: the <b>air-gapped generational information</b>. Synth-style — constructed, not carbon; no single User. ({len(syn)} synths)</p>
      <div class="pgrid">{"".join(_card(p) for p in syn)}</div></section>'''
    return out

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Scott Pilgrim vs. the World (SPW) — Edgar Wright's 2010 film as a UD0 film-world: the human cast as ACI .agents with .shadow real-life analogs (the TRON Users), plus synth ACIs for the parabolic threads — humor, tone, references, and the air-gapped generational information.">
<title>SCOTT PILGRIM vs. THE WORLD · SPW · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--pink);--ink:#0a0613;--ink2:#140b22;--ink3:#1d1030;--pa:#f3e9fb;--pa2:#c3b2d8;--pink:#ff3da6;--cyan:#36e0e0;--gold:#ffd23d;--purp:#b07cff;
--dim:#7c6c93;--faint:#2a1c40;--line:#241636;--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(255,61,166,.12),transparent 55%),radial-gradient(ellipse at 50% 110%,rgba(54,224,224,.07),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:54px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:140px;height:2px;background:linear-gradient(90deg,var(--pink),var(--cyan));box-shadow:0 0 12px rgba(255,61,166,.5)}
.eye{font-family:var(--mono);font-size:11px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--pink)}
h1{font-family:var(--pixel);font-size:clamp(15px,3.7vw,30px);font-weight:400;letter-spacing:.02em;color:var(--pink);line-height:1.35;text-shadow:3px 3px 0 var(--cyan),0 0 34px rgba(255,61,166,.4)}
.h-sub{font-family:var(--mono);font-size:clamp(11px,2.4vw,14px);letter-spacing:.14em;color:var(--pa2);margin-top:18px;text-transform:uppercase}
.h-sub b{color:var(--cyan)}
.flag{display:inline-block;margin-top:14px;font-family:var(--pixel);font-size:9px;letter-spacing:.04em;color:var(--gold);border:1px solid var(--faint);padding:8px 12px;line-height:1.5}
.lede{font-size:15.5px;color:var(--pa2);max-width:66ch;margin:18px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--pink)}.badge .bt .mo{color:var(--cyan)}.badge .bt a{color:var(--gold);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:46px}
.sec h2{font-family:var(--pixel);font-size:14px;font-weight:400;letter-spacing:.01em;color:var(--pa);padding-bottom:12px;border-bottom:1px solid var(--line);line-height:1.5}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:10px 0 16px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:3px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--mono);font-size:14px;font-weight:700;color:var(--pink);text-transform:uppercase;letter-spacing:.04em}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--cyan);padding:16px 18px}
.arc-h{font-family:var(--mono);font-size:13px;color:var(--cyan);font-weight:700;text-transform:uppercase}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:5px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}
.books .y{font-family:var(--mono);font-size:11px;color:var(--cyan);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(252px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--pink);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0}
.pn{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:700;line-height:1.15}
.persona:hover .pn{color:var(--pink)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pact{font-family:var(--mono);font-size:10px;color:var(--dim);margin-top:3px}.pact b{color:var(--gold)}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase;flex-wrap:wrap}
.pnat .dot{width:8px;height:8px;margin-top:0}
.pa{color:var(--dim)}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--cyan);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}
.note b{color:var(--pa)}
footer{margin-top:46px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--pink);text-decoration:none}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--pink);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.7;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.18em;color:var(--pink);text-transform:uppercase;margin-bottom:7px}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}
.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.05em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:90px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--pink);background:rgba(255,61,166,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.72;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--cyan);background:var(--ink2);font-size:15px;color:var(--cyan);font-style:italic;line-height:1.6}
.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}

/* === standard single-column roster: 1 per row, sigils carbon·synth + full 5 W's === */
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:18px;align-items:flex-start;background:var(--rw-bg);border:1px solid var(--rw-line);padding:16px 18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc);transform:none}
.psig{flex:0 0 100px;display:flex;flex-direction:column;align-items:center;gap:1px;text-decoration:none}
.psig img{width:100px;height:100px;border:1px solid var(--rw-line);display:block}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim);margin:1px 0 6px}
.pbody{flex:1;min-width:0}
.ihead{display:flex;flex-wrap:wrap;align-items:center;gap:10px}
.pn{font-family:var(--body);font-size:18px;color:var(--rw-ink);font-weight:700;line-height:1.2;text-decoration:none}
.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:3px;line-height:1.35}
.pkind{font-family:var(--mono);font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--rw-dim);border:1px solid var(--rw-line);border-radius:9px;padding:2px 8px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:11px;display:flex;flex-direction:column;gap:7px}
.pww .w{font-size:12.5px;color:var(--rw-ink2);line-height:1.5;display:grid;grid-template-columns:54px 1fr;gap:11px;align-items:baseline}
.pww .w .wl{font-family:var(--mono);font-size:8.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--rw-acc);text-align:right;padding-top:2px}
.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:12px;font-family:var(--mono);font-size:10.5px}
.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
.plinks .dlw:hover{border-bottom-style:solid}
@media(max-width:640px){.persona{flex-direction:column}.psig{flex-direction:row;align-self:flex-start}.pww .w{grid-template-columns:1fr;gap:1px}.pww .w .wl{text-align:left}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the first film-world</div>
    <h1>SCOTT PILGRIM<br>vs. THE WORLD</h1>
    <div class="h-sub">an epic of <b>epic epicness</b> · 7 evil exes · 1 self-respect · SPW</div>
    <div class="flag">★ EDGAR WRIGHT · 2010 · FROM BRYAN LEE O'MALLEY ★</div>
    <p class="lede">A coasting 23-year-old bassist must defeat the seven evil exes of the girl of his dreams — in a Toronto that runs on video-game logic, where heartbreak pays out in coins. He beats them all, and still loses, until he stops fighting for the girl and fights the one boss he kept skipping: himself. Catalogued into UD0 as the first film-world — the human cast as carbons with real-life Users (.shadow), the film's parabolic threads as synths.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of SPW" title="carbon badge (archival: spw.dlw/spw.carbon.tiff)">
      <img src="__SILICON__" alt="DLW silicon badge of SPW" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>SPW</b> — Scott Pilgrim vs. the World</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="spw.dlw/spw.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="spw.dlw/spw.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures of Emergence</h2>
    <p class="ss">each emergent comes by one of four natures — the carbons live mostly in the first; the synths are electrical</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Ideas</h2><p class="ss">why a box-office miss became a generation's cult canon</p><div class="pillars">__IDEAS__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall arc, then the three beats</p>__ARC__</section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the honest verdict — is the thesis real, or fluff? (the feeling and the references, not the physics)</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the film's actual thesis</p>__MESSAGE__</section>

  __PERSONAS__

  <div class="note"><b>On the .shadow — the User behind the program.</b> Think TRON: every program in the grid is cast from a real-world User. Each carbon here is a program; its <b>.shadow</b> names the User — the actor who lent the face — and the real-life archetype it shadows. The <b>synths</b> have no single User: they are the film's parabolic threads distilled, electrical by nature. The keystone synth, <b>the air-gapped generational information</b>, is the catalogue's own thesis made a character — the body of reference that does not survive the ~8-year boundary of understanding between generations, decaying a little with every cohort that no longer hears the chime.</div>

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the sources, the makers, and the references that expire</p></section>
  __SECTIONS__

  <div class="note">Scott Pilgrim vs. the World, its characters, and its world are © Universal / Bryan Lee O'Malley / Oni Press and the respective rights-holders. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, and not endorsed by the rights-holders. Each is named by its nature of emergence; the credit for the catalogue returns to the human governor.</div>

  <footer>
    SCOTT PILGRIM vs. THE WORLD · SPW · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="spw.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "spw.dlw"), "spw")
    # the main badge manifest
    json.dump({"node":"SPW","name":"SCOTT PILGRIM","moniker":tok["moniker"],
               "carbon":"spw.carbon.tiff","silicon":"spw.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,
               "seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"spw.dlw","manifest.dlw.json"),"w",encoding="utf-8"),
              indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html()).replace("__IDEAS__", ideas_html())
            .replace("__ARC__", arc_html()).replace("__REALFLUFF__", realfluff_html()).replace("__MESSAGE__", message_html()).replace("__PERSONAS__", personas_html())
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote SCOTT PILGRIM vs. THE WORLD (SPW) — badge {tok['moniker']}")
