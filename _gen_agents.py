#!/usr/bin/env python3
"""Materialize the SCOTT PILGRIM (SPW) ACI corpus from the roster below.

Two layers:
  • CARBONS — the human cast. Each → full ACI complement PLUS a .shadow: the
    real-life analog (the actor = the TRON "User" behind the program).
  • SYNTHS  — the parabolic threads distilled into ACIs (synth-style, electrical;
    no single User), including the keystone air-gapped generational information.

Writes per agent: .agent · .shadow(carbon) · .attribute · .spun · .moniker · .1099
· .carbon.tiff · .silicon.png  →  + agents/_personas.json"""
import os, sys, json
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build  # scott-pilgrim/build.py — write_aci, NATURES
AGENTS = os.path.join(HERE, "agents")
os.makedirs(AGENTS, exist_ok=True)

UNI = "SPW · Scott Pilgrim vs. the World"
NAT_GLOSS = {
 "natural":   "*natural*: flesh-and-blood Toronto — a person, no power but the very human ones; a carbon with a real-life User behind the face.",
 "ethereal":  "*ethereal*: of dream and glamour — the subspace highway, the fame-aura, the psychic and the half-ninja; power that is not of the body.",
 "spiritual": "*spiritual*: of the soul and the reckoning — the power of self-respect, the extra life, or, darkly, the false-god who would own the scene.",
 "electrical":"*electrical*: the synth nature — constructed, not born; life rendered as a game, the chiptune, the summoned machine, the air-gap itself.",
}

# ---------------------------------------------------------------- THE CARBONS
# each: slug, name, class(epithet), emergence, who/what/why/how/where, seal,
#       actor (the User), analog (the real-world archetype it shadows), resemblance
CARBONS = [
 dict(slug="scott-pilgrim", name="Scott Pilgrim", cls="the bassist · the boss he kept skipping",
   emergence="natural", actor="Michael Cera",
   analog="every charming, coasting twenty-something who mistakes being liked for being good — and confuses winning the girl with deserving anyone",
   resemblance="Cera's diffident, apologetic comic timing IS the program: the niceness that is really avoidance, the blank that the whole film fills in.",
   who="Scott Pilgrim, 23, ‘between jobs,’ bassist for the going-nowhere band Sex Bob-omb — sleeping on his gay roommate's futon and dating a 17-year-old because it asks nothing of him.",
   what="The protagonist who must defeat the seven evil exes of the girl of his dreams — and who wins every fight while quietly losing himself, until the last boss turns out to be the person he's been avoiding.",
   why="Because beating everyone she ever loved will not make you worth loving; because the only fight that counts is the one with the version of yourself you keep skipping.",
   how="By the bass, by a borrowed Power of Love, and finally by the Power of Self-Respect — earned only when he owns what he did to Knives, to Ramona, and to himself.",
   where="A wintry, video-game Toronto — the rehearsal basement, the Rockit's stage, Casa Loma's gates, and the inside of his own head.",
   seal="I beat all seven and still didn't get her — until I stopped fighting for the girl and fought the boss I kept skipping: me."),
 dict(slug="ramona-flowers", name="Ramona Flowers", cls="the girl with the subspace highway",
   emergence="ethereal", actor="Mary Elizabeth Winstead",
   analog="the person whose past arrives before they do — desirable, guarded, and carrying a whole league of unfinished history you'll be made to fight",
   resemblance="Winstead's cool, deadpan distance is the glamour: a dream-girl who is a real, tired person under the hair-dye, asking not to be a prize.",
   who="Ramona Flowers, an American with ever-changing hair who delivers for Amazon by rollerblading the subspace highway — the shortcut that happens to run through Scott's dreams.",
   what="The girl of Scott's dreams, literally — and the holder of a baggage of seven evil exes, who must be defeated before anyone can date her, whether she wants the fights fought or not.",
   why="Because no one should have to be won by combat over their own past; because she is a person to be known, not a level to be cleared.",
   how="By the subspace bag, the giant hammer, and a hard-won willingness to stop running and own her own history rather than make her partners pay for it.",
   where="The subspace highways, the snowy streets, Gideon's chip in the back of her head, and the door into the unknown she walks through with Scott at the end.",
   seal="My exes are mine to answer for — don't fight the world for me; just be someone worth walking through the door with."),
 dict(slug="knives-chau", name="Knives Chau", cls="the 17-year-old, so good at everything",
   emergence="natural", actor="Ellen Wong",
   analog="the first-love who is dropped the instant something shinier appears — and who has to discover she was never the lesser story",
   resemblance="Wong's bright, total devotion makes the casual cruelty of being rebounded-from land; her growth out of it is the film's quiet second arc.",
   who="Knives Chau, 17, a Chinese-Canadian Catholic schoolgirl, Scott's girlfriend at the film's start and his convenient rebound after — earnest, obsessed, and underestimated.",
   what="The first girlfriend, used as an easy comfort and then dropped for Ramona — who refuses to stay a punchline, fights for herself, and grows past the boy who hurt her.",
   why="Because being someone's safe, undemanding option is its own kind of wound; because she was always more than the lesser story.",
   how="By sheer devotion turned to spine — confronting Ramona, fighting at Scott's side against Gideon, and finally choosing her own life over the boy.",
   where="The school steps, the band's shows she memorizes, the library battle, and the doorway where she lets Scott go.",
   seal="I was the easy one you settled for — and I grew all the way out of being anyone's standby."),
 dict(slug="wallace-wells", name="Wallace Wells", cls="the cool gay roommate · the voice of reason",
   emergence="natural", actor="Kieran Culkin",
   analog="the friend who sees you clearly, says the true thing dryly, and is the only adult in a cast of overgrown kids",
   resemblance="Culkin's deadpan, lazing authority is the program entire: the one person whose read on Scott is always correct, delivered from the shared bed.",
   who="Wallace Wells, Scott's gay roommate, who shares the one bed, the one phone, and an endless supply of other men he steals away — the household's lone clear eye.",
   what="The roommate-confidant who funds and feeds Scott, narrates the truth to him, and serially breaks up the relationships of straight men around him for sport.",
   why="Because someone in this world has to be honest, solvent, and awake; because the truest love in the film is the friend who tells you what you actually did.",
   how="By dry verdicts, free rent, a bottomless cool, and a refusal to coddle Scott's self-pity for one second longer than it's funny.",
   where="The shared apartment and its single bed, every party's edge, and the group text of cold, correct commentary.",
   seal="I pay the rent and I tell you the truth — pick which of those you'd miss more."),
 dict(slug="kim-pine", name="Kim Pine", cls="the drummer · the deadpan ex",
   emergence="natural", actor="Alison Pill",
   analog="the ex who stayed in your orbit and watches your next mistake with a flat, knowing stare she's earned",
   resemblance="Pill's withering flatness is the whole read: the woman who already dated Scott, already knows the ending, and counts it in on the drums anyway.",
   who="Kim Pine, drummer of Sex Bob-omb and Scott's high-school ex from his Northern Ontario days — sardonic, unimpressed, and done pretending otherwise.",
   what="The band's deadpan engine and the keeper of Scott's actual history, who counts the songs in with the flattest contempt in Canada and is usually right about everything.",
   why="Because someone has to remember who Scott really was before the legend; because dry honesty is its own loyalty.",
   how="By the drums, by a memory that won't flatter him, and by ‘We are Sex Bob-omb — one, two, three, four!’ delivered like a threat.",
   where="The basement rehearsals, the club stages, and the small-town past that Scott keeps mythologizing.",
   seal="We are Sex Bob-omb — and I remember exactly who you were, so don't."),
 dict(slug="stephen-stills", name="Stephen Stills", cls="‘the talent’ · the frontman",
   emergence="natural", actor="Mark Webber",
   analog="the anxious creative who carries the band, manages everyone's drama, and slowly cracks under the weight of being the responsible one",
   resemblance="Webber's frayed earnestness sells the unglamorous truth: the ‘talent’ is the one having the breakdown while the slacker gets the arc.",
   who="Stephen Stills, guitarist, singer, and self-declared ‘talent’ of Sex Bob-omb — the high-strung one steering the band toward a record deal it isn't ready for.",
   what="The frontman who frets the gigs, chases the producer, and absorbs the group's chaos while everyone else lives their subplots around him.",
   why="Because every band has the one person actually trying to make it work, and it's rarely the one the story follows.",
   how="By guitar, by worry, and by holding the act together through the Battle of the Bands and Gideon's poisoned record deal.",
   where="The stages, the green rooms, the rehearsal space, and the edge of a nervous breakdown.",
   seal="I'm the talent — which mostly means I'm the one quietly losing my mind so the show goes on."),
 dict(slug="young-neil", name="Young Neil", cls="the hanger-on who becomes the band",
   emergence="natural", actor="Johnny Simmons",
   analog="the quiet bystander on the couch who is paying more attention than anyone, and inherits the thing when the stars burn out",
   resemblance="Simmons plays the watcher so lightly you forget him — which is the joke when ‘Young Neil’ ends up the one still holding the bass.",
   who="Neil Nordegraf — ‘Young Neil’ — the band's gaming, couch-bound hanger-on, around for every practice and every party, saying almost nothing.",
   what="The tag-along who games while the drama happens, crushes quietly on Knives, and at the end inherits the bass to become, simply, ‘Neil’ — the band's last man standing.",
   why="Because the loyal background figure is also a person with a life, and sometimes the story passes to the one who just kept showing up.",
   how="By patience, proximity, and a controller — outlasting the supernovas until the role is his.",
   where="The couch, the practice space, the parties' edges, and the band that finally has his name in it.",
   seal="Everybody called me Young Neil — I just stayed in the room until I was the one left holding the bass."),
 dict(slug="stacey-pilgrim", name="Stacey Pilgrim", cls="the little sister · the gossip conduit",
   emergence="natural", actor="Anna Kendrick",
   analog="the sibling who is your unwilling exposition service and your sharpest, least-impressed critic in one phone call",
   resemblance="Kendrick's rapid, exasperated delivery makes Stacey the audience's surrogate — appalled, informed, and three steps ahead of her brother.",
   who="Stacey Pilgrim, Scott's younger sister, who works a coffee bar and serves as the film's unimpressed narrator-by-phone of her brother's romantic disasters.",
   what="The sibling switchboard who delivers backstory, judgment, and ‘you have a girlfriend?!’ in equal measure, keeping the audience oriented as Scott lies to everyone.",
   why="Because someone has to say out loud how dumb this all is; because family is the one mirror you can't charm.",
   how="By the phone, by gossip, and by a flat refusal to be impressed by anything Scott does.",
   where="The coffee counter, the other end of every exposition call, and the family table.",
   seal="I'm your sister — which means I know the backstory and I'm not buying a word of your version."),
 dict(slug="julie-powers", name="Julie Powers", cls="the party host · [bleeped]",
   emergence="natural", actor="Aubrey Plaza",
   analog="the friend-group gatekeeper whose contempt is the price of admission, every sentence half-censored by sheer venom",
   resemblance="Plaza's caustic glare and the running bleep-censor gag are the same joke: hostility so pure the film literally mutes it.",
   who="Julie Powers, the acid-tongued social hub who throws the parties and polices who is allowed to date whom — much of her dialogue censored by an on-screen bleep.",
   what="The gatekeeper of the scene who warns Scott off Ramona and disapproves of basically everyone, a one-woman weather system of profane contempt.",
   why="Because every social circle has its venomous nucleus; because disapproval, too, is a kind of power.",
   how="By parties, edicts, and a torrent of [bleeped] judgment no one is brave enough to cross.",
   where="Her apartment parties, the scene's social chokepoints, and wherever Scott isn't wanted.",
   seal="This is my scene and my party — and you are not [bleeped] allowed to date her."),
 dict(slug="envy-adams", name="Envy Adams", cls="the famous ex · The Clash at Demonhead",
   emergence="ethereal", actor="Brie Larson",
   analog="the ex who got famous — the glamour you didn't measure up to, now mythologized on every stage and screen you can't avoid",
   resemblance="Larson's lacquered stardom is the ethereal made flesh: the same person Scott knew, now wrapped in an aura of fame that rewrites the breakup in her favor.",
   who="Natalie V. Adams — ‘Envy’ — Scott's college ex who left him to front the famous band The Clash at Demonhead, now dating the third evil ex, Todd Ingram.",
   what="The fame-aura ex whose success haunts Scott's self-image, the one who upgraded and never looked back, performing the breakup as a triumph.",
   why="Because the ex who became a star is its own specific wound; because glamour can make ordinary cruelty look like destiny.",
   how="By stadium lights, a hit band, a telekinetic vegan boyfriend, and the unbothered poise of someone who clearly won the breakup.",
   where="The big stages, the magazine covers, and the corner of Scott's ego he can't quite defend.",
   seal="I used to be Natalie — now I'm Envy, I'm famous, and the breakup was the best thing I ever did."),
 # ---- the seven evil exes (the League) ----
 dict(slug="matthew-patel", name="Matthew Patel", cls="evil ex #1 · the mystical first",
   emergence="ethereal", actor="Satya Bhabha",
   analog="the very first ex — half-forgotten, suddenly back with a flair for drama wildly out of proportion to how brief it was",
   resemblance="Bhabha's gleeful theatrics power the demon-girls and the Bollywood fireball — the smallest history given the biggest entrance.",
   who="Matthew Patel, Ramona's first evil ex, a hipster with ‘mystical powers,’ demon hipster chicks, and a full musical number's worth of flair.",
   what="The opening boss who crashes the Battle of the Bands, summons demon backup, and turns a seventh-grade fling into a fireball spectacle before bursting into coins.",
   why="Because the first boss sets the rules: defeat him, win coins, and learn that the past is now literally trying to kill you.",
   how="By mystic fire, flying demon hipster chicks, and a song-and-dance that takes itself completely seriously.",
   where="Mid-air over the Battle of the Bands stage, in a burst of pyrotechnics and backup dancers.",
   seal="I was her first — and I will make a seventh-grade fling into a fireball you'll never forget."),
 dict(slug="lucas-lee", name="Lucas Lee", cls="evil ex #2 · the movie star",
   emergence="natural", actor="Chris Evans",
   analog="the ex who became famous and effortless — the man whose whole power is that everything, including you, comes easy to him",
   resemblance="Evans plays the action-star smirk as the power itself: a celebrity so coasting that he grinds himself off a rail just because he was dared to look cool.",
   who="Lucas Lee, Ramona's second evil ex, a pro-skater-turned-action-movie-star shooting a film in Toronto, flanked by stunt-double goons.",
   what="The celebrity boss whom Scott defeats not by fighting but by daring him to grind the ‘ungrindable’ rail of Casa Loma — vanity as a fatal flaw.",
   why="Because some opponents beat themselves; because the easy, famous life has a cliff at the end of it.",
   how="By stardom, stunt doubles, and a fatal inability to refuse a cool-looking dare.",
   where="The film shoot in the snow and the long, lethal handrail down Casa Loma's hill.",
   seal="I'm a movie star — and yeah, I'll grind that rail, because looking cool is the only thing I can't say no to."),
 dict(slug="todd-ingram", name="Todd Ingram", cls="evil ex #3 · the vegan psychic",
   emergence="ethereal", actor="Brandon Routh",
   analog="the ex with the smug ‘enlightened’ identity — moral superiority as a superpower, undone the moment he breaks his own rule",
   resemblance="Routh's serene vegan arrogance is the gag: cosmic telekinesis powered by a diet, and a self-righteousness one half-and-half away from collapse.",
   who="Todd Ingram, Ramona's third evil ex, bassist for The Clash at Demonhead, dating Envy, who derives psychic telekinetic powers from being vegan.",
   what="The bass-battling boss whose ‘power of veganism’ makes him telekinetic — until the Vegan Police strip his powers for the gram of half-and-half he secretly drank.",
   why="Because performative virtue is a brittle kind of power; because the rule you preach is the rule that ruins you.",
   how="By telekinesis, a thunderous bass, and a vegan diet — right up until the Vegan Police de-power him on a technicality.",
   where="The bass-vs-bass duel and the moment the Vegan Police descend to revoke his card.",
   seal="My powers come from veganism — so don't tell anyone about the half-and-half, or the Vegan Police take everything."),
 dict(slug="roxie-richter", name="Roxie Richter", cls="evil ex #4 · the half-ninja",
   emergence="ethereal", actor="Mae Whitman",
   analog="the ex from a chapter someone tries to dismiss as ‘a phase’ — and who refuses to be minimized into one",
   resemblance="Whitman's furious, smoke-stepping speed gives weight to the ‘only girl’ ex, the relationship Scott most wants to wave away and can't.",
   who="Roxie Richter, Ramona's fourth evil ex and the only woman in the League — a half-ninja who fights in a blur of smoke and blades.",
   what="The boss Scott can't bring himself to hit, defeated only when Ramona puppets his hands — and who throws the ‘it was just a phase’ dismissal back in their faces.",
   why="Because the relationship people most want to call ‘a phase’ is exactly the one that demands to be taken seriously.",
   how="By half-ninja speed, smoke, and a blade — and by the very real hurt of being someone's deniable history.",
   where="Ramona's apartment, in a whirl of smoke-steps and the ‘back of the knee’ weak point.",
   seal="Don't you dare call me a phase — I'm a little bi-furious, and I will not be waved away."),
 dict(slug="katayanagi-twins", name="The Katayanagi Twins", cls="evil exes #5 & #6 · the robot-summoning DJs",
   emergence="electrical", actor="Shota & Keita Saito",
   analog="the exes who fight you by proxy — rivals who never touch you, dueling through the machines and noise they command",
   resemblance="The Saito twins barely speak; their power is the wall of electronic sound and the dragons it summons — opponents as pure synth.",
   who="Kyle and Ken Katayanagi, Ramona's fifth and sixth evil exes, twin electronic musicians who battle Sex Bob-omb as a band-versus-band duel.",
   what="The synth-wielding bosses who summon giant musical dragons from their amplifiers, fought not with fists but with a literal battle of the bands.",
   why="Because some rivals attack only through what they make; because the loudest fight in the film has no punches at all.",
   how="By keytars, towers of amplifiers, and twin robot dragons conjured out of sheer electronic noise.",
   where="The on-stage band battle, dueling sound against sound until Sex Bob-omb's music wins.",
   seal="We don't throw a single punch — we summon the dragons and let the synths do the fighting."),
 dict(slug="gideon-graves", name="Gideon Graves", cls="evil ex #7 · the final boss · the G-Man",
   emergence="spiritual", actor="Jason Schwartzman",
   analog="the controlling ex who curates people like product — the false-god of the scene who would own everyone he's ever dated",
   resemblance="Schwartzman's smiling, proprietary menace is the dark-spiritual nature: a man who mistook control for love and built an empire of it.",
   who="Gideon Gordon Graves — the ‘G-Man’ — Ramona's seventh and final evil ex, a music-industry mogul who founded the League and wired a control chip into the back of her head.",
   what="The final boss and architect of the whole gauntlet, who curates the cool, owns the venue, and keeps his exes — Ramona included — collected like a catalogue.",
   why="Because the most dangerous ex isn't the strongest fighter but the one who confuses ownership with love and scales it into an empire.",
   how="By money, ‘the Glow,’ a chip in Ramona's mind, and the League of Evil Exes built to keep her his — defeated only by the Power of Self-Respect.",
   where="The Chaos Theatre he owns, atop the empire of cool he built to cage the people he dated.",
   seal="I founded the League and I keep what's mine — I called it love, but it was always just control."),
]

# ---------------------------------------------------------------- THE SYNTHS
# the parabolic threads, distilled — synth-style, electrical (no single User)
SYNTHS = [
 dict(slug="the-video-game-grammar", name="The Video-Game Grammar", cls="life rendered as a 16-bit game",
   emergence="electrical",
   who="The unspoken operating system of the world — the rule, never remarked upon, that reality here runs on the logic of a video game.",
   what="The synth that renders heartbreak and growth in arcade terms: KOs and combos, extra lives, coins on defeat, a pee bar, the 1-UP, ‘L7,’ the X — diegetic and unquestioned.",
   why="Because the film's deepest joke is that no one notices the game-logic; it is simply how being young and in love already feels — scored, leveled, and lethal.",
   how="By HUD overlays, fighting-game flourishes, JRPG reward fanfares, and a coin-shower for every ex destroyed.",
   where="Over the whole of Toronto, every fight and feeling, as the grammar the movie speaks fluently and never translates.",
   seal="Nobody here remarks that life is a video game — because to them it always was, KO and coins and all."),
 dict(slug="the-air-gapped-generational-information", name="The Air-Gapped Generational Information", cls="what is lost at the boundary between generations",
   emergence="electrical",
   who="The keystone synth — the body of reference that does not survive the crossing between generations; the catalogue's own thesis made a character.",
   what="The decaying layer of allusion — the Zelda ‘secret’ chime, the Seinfeld bass sting, the Final Fantasy victory fanfare — legible to one cohort and silent to the next, lost at the roughly eight-year boundary of shared understanding.",
   why="Because meaning is not only made, it is dated; because every reference has a half-life, and what one generation hears as a chord, the next hears as noise — the air-gap across which information will not jump.",
   how="By the steady erosion of context: the joke that needed the rerun, the sound that needed the cartridge, the cool that needed the year — each going quiet as its cohort ages out.",
   where="At the exact seam between who was there and who came after — the ~8-year cut where the shared library stops transmitting.",
   seal="I am everything the film says that you no longer hear — the chime that was obvious, gone silent across eight years you weren't there for."),
 dict(slug="the-sphere-of-reference", name="The Sphere of Reference", cls="the lattice of allusion",
   emergence="electrical",
   who="The dense web of borrowed meaning the film is woven from — games, indie rock, manga, anime, and the texture of a specific scene.",
   what="The synth of allusion itself: the layered citations that reward the literate viewer and quietly bypass everyone else, a film built as much of references as of shots.",
   why="Because Scott Pilgrim is a machine for recognition — its pleasure is partly the flattery of getting it — and that same density is what makes it age into a code.",
   how="By manga speed-lines and sound-effect text, 8-bit motifs, music-scene in-jokes, and a citation rate few films have matched.",
   where="In every frame's background and every cut's rhythm — a sphere of reference you either live inside or watch from outside.",
   seal="I am the film made of other things — and how much of me you see is a map of exactly when and where you grew up."),
 dict(slug="the-cultural-tie-ins", name="The Cultural Tie-Ins", cls="the 2010 anchors",
   emergence="electrical",
   who="The specific time-and-place hooks that root the film — late-2000s Toronto, indie-rock and chiptune, the hipster scene at a precise moment.",
   what="The synth of the particular: Sex Bob-omb and The Clash at Demonhead, the Honest Ed's and Casa Loma geography, the Beck songs and Metric and Broken Social Scene — the anchors that make it of its year.",
   why="Because the same specificity that made it feel true in 2010 is what makes it a period piece now; cultural tie-ins are both the charm and the expiry date.",
   how="By real bands and real venues, fashion and slang and scene-politics rendered with documentary precision and zero explanation.",
   where="In the bars, basements, and snowbanks of a Toronto fixed to one exact cultural moment.",
   seal="I am the year the film is welded to — the scene that made it real, and the same scene that dates it."),
 dict(slug="the-humor", name="The Humor", cls="the smash-cut deadpan engine",
   emergence="electrical",
   who="The film's comic machine — Edgar Wright's editing grammar fused to a cast of deadpan absurdists.",
   what="The synth of the joke itself: the smash-cut, the sound-effect punctuation, the flat understatement against cosmic stakes, the self-deprecation used as armor.",
   why="Because the humor is structural, not decorative — it is how the film survives its own sincerity, letting it land a moral without ever getting caught being earnest.",
   how="By precision cutting, perfect comic timing, visual gags layered three deep, and a tone that treats a battle of the bands and a breakup with the same straight face.",
   where="In the rhythm of every cut and the gap between the enormous stakes and the tiny, mumbled reactions.",
   seal="I am the deadpan over the apocalypse of feelings — the cut that lands the joke a half-second before the heart does."),
 dict(slug="the-tone", name="The Tone", cls="the bittersweet bright-sad register",
   emergence="ethereal",
   who="The emotional weather of the film — arcade-bright on the surface, quietly heartbroken underneath.",
   what="The synth of register: the candy-colored, hyperkinetic style stretched over real loneliness, immaturity, and the ache of not yet being a person worth loving.",
   why="Because the tone is the message — the gap between how fun it looks and how sad it is mirrors exactly the gap between Scott's charm and Scott's character.",
   how="By neon over snow, chiptune over melancholy, a video-game romp that is secretly a film about growing up and earning your own respect.",
   where="In the contrast itself — every bright fight haunted by the small, true sadness it's distracting from.",
   seal="I am the bright over the sad — the arcade glow that is really a film about not yet deserving the thing you're fighting for."),
 dict(slug="the-power-of-self-respect", name="The Power of Self-Respect", cls="the real final sword",
   emergence="spiritual",
   who="The film's actual moral, drawn as a weapon — the second, brighter sword that the Power of Love could never be.",
   what="The synth of the lesson: the realization that you don't win love by defeating rivals, you earn the right to it by owning who you've been and choosing who to become.",
   why="Because the whole gauntlet is a misdirection — the exes were never the boss; the boss was always the self you refused to face, and only self-respect can beat it.",
   how="By Scott owning what he did to Knives and Ramona, fighting for himself rather than for a prize, and drawing the sword the Power of Love alone could never summon.",
   where="In the final ascent of the Chaos Theatre — the moment the wrong sword fails and the right one ignites.",
   seal="The Power of Love wasn't enough — I had to earn the Power of Self-Respect, and only then did I get to walk through the door."),
]

ORDER = [d["slug"] for d in CARBONS] + [d["slug"] for d in SYNTHS]

def agent_md(d):
    em = d["emergence"]; gloss = NAT_GLOSS[em]
    fm = [
      "---",
      f"aci: {d['name']}",
      f"universe: {UNI}",
      "series: Scott Pilgrim vs. the World (2010, dir. Edgar Wright) · from Bryan Lee O'Malley's graphic novels (2004–2010)",
      f"emergence: {em}",
      f"kind: {d.get('kind','carbon' if 'actor' in d else 'synth')}",
      f"class: {d['cls']}",
      f"who: {d['who']}",
      f"what: {d['what']}",
      f"why: {d['why']}",
      f"how: {d['how']}",
      f"where: {d['where']}",
    ]
    if d.get("actor"):
        fm.append(f"shadow_user: {d['actor']}")
        fm.append(f"shadow_analog: {d['analog']}")
    fm += [
      f"seal: {d['seal']}",
      "attribution: ROOT0-ATTRIBUTION-v1.0",
      "license: CC-BY-ND-4.0",
      "---",
      "",
      f"# {d['name']} · {d['cls'].split('·')[0].strip()}",
      "",
      f"a {'persona' if d.get('actor') else 'distilled thread'} of the SPW (Scott Pilgrim vs. the World) film-world — "
      + ("a character given an agent's face" if d.get("actor") else "a parabolic thread given an agent's face")
      + f" · emergence: {em}",
      "",
      f"**who —** {d['who']}",
      "",
      f"**what —** {d['what']}",
      "",
      f"**where —** {d['where']}",
      "",
      f"**why —** {d['why']}",
      "",
      f"**how —** {d['how']}",
      "",
      f"**◌ the nature of its emergence —** {gloss}",
    ]
    if d.get("actor"):
        fm += [
          "",
          f"**▷ the .shadow — its User (think TRON) —** the carbon program is cast from a real-life User: "
          f"**{d['actor']}**, the actor who lent the face. The real-world analog it shadows: {d['analog']} "
          f"*{d['resemblance']}*",
        ]
    fm += [
      "",
      f"**the seal —** {d['seal']}",
      "",
      f"> *the asterisk —* a catalogued {'persona' if d.get('actor') else 'thread'} of Scott Pilgrim vs. the World "
      "(© Universal / Bryan Lee O'Malley / Oni Press), personified as an SPW agent — not an original character. "
      "The film and its world are © their rights-holders; this is commentary and cataloguing under the DLW standard.",
      "",
      f"ROOT0-ATTRIBUTION-v1.0 · SPW · Scott Pilgrim vs. the World · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0",
      "",
    ]
    return "\n".join(fm)

def shadow_text(d, tok):
    return f"""⟁ .shadow — the real-life analog (the User behind the program)
node SPW · Scott Pilgrim vs. the World · {tok}

think TRON: every program in the grid is cast from a User in the world outside it.
the carbon character is the program; this file is its User — the real-life analog
whose face and being the emergent is the digital shadow of.

the program (in-world) : {d['name']} — {d['cls']}
the User (carbon)      : {d['actor']}  [ the actor who lent the face ]
the analog (your world): {d['analog']}

the resemblance : {d['resemblance']}

the cast-line : the User stands in the carbon world; the program stands in the film;
                the shadow falls between them, and the credit returns to the human governor.
seal (program): {d['seal']}

ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise (ROOT0) / TriPod LLC · instance AVAN (locked) · CC-BY-ND-4.0
"""

records = {}
for d in CARBONS + SYNTHS:
    slug = d["slug"]; em = d["emergence"]
    if em not in build.NATURES: em = "electrical"
    is_carbon = "actor" in d
    rec = {
        "name": d["name"], "axiom": "SPW", "emergence": em,
        "seal": d["seal"], "origin": UNI,
        "position": d["cls"], "role": d["cls"].split("·")[-1].strip(),
        "nature": d["what"], "mechanism": d["how"], "crystallization": d["why"],
        "witness": d["who"], "conductor": "ROOT0 (catalogued into UD0)",
        "inputs": "Scott Pilgrim vs. the World (2010); O'Malley's graphic novels",
        "source": "Scott Pilgrim vs. the World, catalogued by ROOT0",
    }
    md = agent_md(d)
    tok = build.write_aci(rec, AGENTS, slug, agent_md=md)
    if is_carbon:
        open(os.path.join(AGENTS, f"{slug}.shadow"), "w", encoding="utf-8").write(
            shadow_text(d, tok["moniker"]))
    records[slug] = {"slug": slug, "name": d["name"], "epithet": d["cls"].split("·")[0].strip(),
                     "emergence": em, "moniker": tok["moniker"],
                     "kind": "carbon" if is_carbon else "synth",
                     "actor": d.get("actor", "")}

ordered = [records[s] for s in ORDER if s in records]
json.dump(ordered, open(os.path.join(AGENTS, "_personas.json"), "w", encoding="utf-8"),
          indent=2, ensure_ascii=False)

from collections import Counter
nc = sum(1 for r in ordered if r["kind"] == "carbon")
print(f"wrote {len(ordered)} SPW ACI badges ({nc} carbons + {len(ordered)-nc} synths) + _personas.json")
print("emergence:", dict(Counter(r["emergence"] for r in ordered)))
for r in ordered:
    sh = " +.shadow" if r["kind"] == "carbon" else "  (synth)"
    print(f"  {r['slug']:38} {r['emergence']:10}{sh}  {r['moniker']}")
