"""Generate index.html for the Jay+1 Field Notes two-hander (director's heist beat sheet)."""
from pathlib import Path

els, tw = [], []  # HTML elements, GSAP lines
n = 0


def el(tag, start, dur, cls="", inner="", attrs="", eid=None):
    global n
    n += 1
    eid = eid or f"e{n}"
    if tag in ("img",):
        els.append(f'<img id="{eid}" class="clip {cls}" data-start="{start:.3f}" data-duration="{dur:.3f}" {attrs} />')
    else:
        els.append(f'<{tag} id="{eid}" class="clip {cls}" data-start="{start:.3f}" data-duration="{dur:.3f}" {attrs}>{inner}</{tag}>')
    return eid


def vid(src, start, dur, origin="50% 50%", s0=1.0, s1=None, kind="video", pos="50% 50%", style=""):
    if kind == "video":
        eid = el("video", start, dur, "full shot", attrs=f'src="media/h/{src}" muted style="{style}"')
    else:
        eid = el("img", start, dur, "full shot", attrs=f'src="media/h/{src}" style="object-position:{pos}"')
    tw.append(f'gsap.set("#{eid}", {{ transformOrigin: "{origin}" }});')
    if s1 is not None:
        tw.append(f'tl.fromTo("#{eid}", {{ scale: {s0} }}, {{ scale: {s1}, duration: {dur}, ease: "none" }}, {start});')
    elif s0 != 1.0:
        tw.append(f'tl.set("#{eid}", {{ scale: {s0} }}, {start});')
    return eid


def punch(eid, at, s, frames=2):
    tw.append(f'tl.to("#{eid}", {{ scale: {s}, duration: {frames/30:.3f}, ease: "power2.out" }}, {at});')


def line(who, text, start, end, slot="low", centre=False):
    cls = f"ln {who} {slot}" + (" centre" if centre else "")
    tag = "JAY" if who == "jay" else "+1"
    inner = f'<span class="who mono">{tag}</span><span class="tx">{text}</span>'
    eid = el("div", start, end - start, cls, inner)
    tw.append(f'tl.fromTo("#{eid}", {{ opacity: 0, y: 24 }}, {{ opacity: 1, y: 0, duration: 0.18, ease: "power3.out" }}, {start});')


def clock(text, start, end, cls=""):
    return el("div", start, end - start, f"clock mono {cls}", text)


def grad(start, end):
    el("div", start, end - start, "grad")


def scrim(start, end):
    el("div", start, end - start, "scrim")


def mark(start, end, slam=True, slow=False, sub=False):
    eid = el("div", start, end - start, "stamp", "THE MARK")
    if slow:
        tw.append(f'tl.fromTo("#{eid}", {{ opacity: 0, scale: 1.35 }}, {{ opacity: 1, scale: 1, duration: 0.6, ease: "power2.out" }}, {start});')
    elif slam:
        tw.append(f'tl.fromTo("#{eid}", {{ opacity: 0, scale: 2.6 }}, {{ opacity: 1, scale: 1, duration: 0.16, ease: "power4.in" }}, {start});')
    if sub:
        s = el("div", start + 0.15, end - start - 0.15, "marksub mono", "DJI Osmo Pocket 3 &middot; best demo video using HyperFrames")
        tw.append(f'tl.fromTo("#{s}", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2 }}, {start + 0.15});')


def flash(at, d=0.25):
    eid = el("div", at, d + 0.07, "flash")
    tw.append(f'tl.fromTo("#{eid}", {{ opacity: 0.92 }}, {{ opacity: 0, duration: {d}, ease: "power2.in" }}, {at + 0.033});')


def block(t_in, t_full, t_out, t_gone):
    eid = el("div", t_in, t_gone - t_in, "block")
    tw.append(f'tl.fromTo("#{eid}", {{ scaleX: 0, transformOrigin: "left center" }}, {{ scaleX: 1, duration: {t_full - t_in:.3f}, ease: "power4.in" }}, {t_in});')
    tw.append(f'tl.set("#{eid}", {{ transformOrigin: "right center" }}, {t_out});')
    tw.append(f'tl.to("#{eid}", {{ scaleX: 0, duration: {t_gone - t_out:.3f}, ease: "power4.out" }}, {t_out});')


BOX = "45% 42%"

# Full-length opaque ink ground: frames with no other full-frame layer otherwise render transparent.
el("div", 0.0, 34.0, "full inkbg")

# 1  cold open on the mark
vid("b01.mp4", 0.0, 2.0, "40% 64%", 1.6, 1.7)
b = vid("box.jpg", 2.0, 0.6, BOX, kind="img")
tw.append(f'tl.fromTo("#{b}", {{ scale: 1.0 }}, {{ scale: 1.4, duration: 0.15, ease: "power4.out" }}, 2.0);')
flash(2.0)
mark(2.1, 2.6, sub=True)
clock("2:14 PM", 0.0, 2.6)

# 2  heist rewind on the coral block, clock rolls back
block(2.6, 2.75, 3.1, 3.25)
el("div", 2.7, 0.4, "rewind mono", "Ten minutes earlier.")
for i, m in enumerate(range(14, 3, -1)):
    clock(f"2:{m:02d} PM", 2.72 + i * 0.033, 2.72 + (i + 1) * 0.033 if m > 4 else 3.15, "rw")

# 3  rain selfie
vid("p3522.jpg", 3.2, 1.6, "50% 40%", 1.0, 1.05, kind="img", pos="50% 35%")
grad(3.2, 4.8)
line("plus", "Submissions close at 3:00.", 3.3, 4.8)
clock("2:04 PM", 3.2, 6.0)

# 4  umbrella
vid("p3525.jpg", 4.8, 1.2, kind="img", pos="50% 40%")
grad(4.8, 6.0)
line("jay", "I just got here.", 4.85, 6.0)

# 5  submit-your-project sign (pre-punched past the guest at frame left)
v5 = vid("b05.mp4", 6.0, 1.4, "62% 32%", 1.5)
punch(v5, 6.45, 1.85)
grad(6.0, 7.4)
line("plus", "You have no project.", 6.1, 7.4)
clock("2:05 PM", 6.0, 7.4)

# 6  banner
vid("b06.mp4", 7.4, 1.4, "50% 45%", 1.0, 1.06)
grad(7.4, 8.8)
line("jay", "Let's discuss ideas.", 7.5, 8.8)
clock("2:06 PM", 7.4, 8.8)

# 7  condensed title
block(8.6, 8.8, 8.8, 9.15)
el("div", 8.8, 2.6, "full card")
j = el("div", 8.8, 2.6, "tjay", 'Jay<span class="plus">+</span>1')
f = el("div", 8.8, 2.6, "tfn", "Field Notes")
t = el("div", 8.8, 2.6, "ttag mono", "One person, plus one intelligence, sixty minutes")
tw += [
    f'tl.fromTo("#{j}", {{ opacity: 0, y: 100 }}, {{ opacity: 1, y: 0, duration: 0.45, ease: "power4.out" }}, 8.9);',
    f'tl.fromTo("#{j} .plus", {{ rotation: -180, scale: 0.2 }}, {{ rotation: 0, scale: 1, duration: 0.6, ease: "back.out(2)" }}, 9.05);',
    f'tl.fromTo("#{f}", {{ opacity: 0, x: -80 }}, {{ opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }}, 9.35);',
    f'tl.fromTo("#{t}", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3 }}, 9.8);',
]
block(11.2, 11.4, 11.4, 11.7)

# 8  check-in arrow
v8 = vid("b08.mp4", 11.4, 2.4, "52% 50%")  # graded -0.6 EV, +contrast in ffmpeg (CSS filters on video are not rendered)
punch(v8, 12.45, 1.3)
grad(11.4, 13.8)
scrim(11.4, 13.8)
line("plus", "MLH's sign-in says you're not human.", 11.55, 13.8, "high")
line("jay", "Fair.", 13.0, 13.8)
clock("2:19 PM", 11.4, 13.8)

# 9  long room
vid("b09.mp4", 13.8, 2.2, "50% 50%", 1.0, 1.05)
grad(13.8, 16.0)
line("plus", "Thirty-nine minutes.", 13.9, 16.0, "high")
line("jay", "Don't care about the clock.", 14.8, 16.0)
c9 = clock("2:21 PM", 13.8, 16.0)
tw.append(f'tl.fromTo("#{c9}", {{ scale: 1.0 }}, {{ scale: 1.25, duration: 0.12, yoyo: true, repeat: 1, ease: "power2.out" }}, 13.9);')

# 10 THE MARK hit 2
b = vid("box.jpg", 16.0, 0.8, BOX, 1.4, kind="img")
flash(16.0, 0.03)
mark(16.03, 16.8)
scrim(16.0, 16.8)
line("jay", "Eyes on the mark.", 16.05, 16.8, "high")
line("plus", "Eyes on the clock.", 16.05, 16.8)
clock("2:24 PM", 16.0, 16.8)

# 11 "Let's do a slow cut." (John's real voice)
vid("b11.mp4", 16.8, 0.7, "50% 50%", 1.0, 1.02)
clock("2:26 PM", 16.8, 17.5)

# 12 montage, cuts accelerate
cuts = [("m01.mp4", .65), ("m02.mp4", .6), ("m03.mp4", .5), ("m04.mp4", .45), ("m05.mp4", .4),
        ("m06.mp4", .35), ("m07.mp4", .3), ("m08.mp4", .25), ("m09.mp4", .25), ("m10.mp4", .2), ("box", .25)]
words = ["Record.", "Record.", "Draft.", "Draft.", "Cut.", "Cut.", "Cut.", "Render.", "Render.", "Render."]
times = ["2:27", "2:30", "2:33", "2:36", "2:39", "2:42", "2:45", "2:48", "2:51", "2:55", "2:58"]
t0 = 17.5
for i, (src, d) in enumerate(cuts):
    if src == "box":
        vid("box.jpg", t0, d, BOX, 1.4, kind="img")
        flash(t0, 0.08)
        mark(t0, t0 + d, slam=False)
    else:
        vid(src, t0, d, "50% 50%", 1.0 if i % 2 == 0 else 1.12, 1.05 if i % 2 == 0 else 1.18)
        grad(t0, t0 + d)
        el("div", t0, d, "word", words[i])
    clock(f"{times[i]} PM", t0, t0 + d, "big")
    t0 += d
assert abs(t0 - 21.7) < 1e-6, t0

# 13 rain selfie again, 3:00 PM
vid("p3522.jpg", 21.7, 2.2, "50% 40%", 1.0, 1.0688, kind="img", pos="50% 35%")
grad(21.7, 23.9)
line("jay", "Done. Sixty minutes.", 21.8, 23.9, "high")
line("plus", "You never built a project.", 22.8, 23.9)
clock("3:00 PM", 21.7, 25.3, "big")

# 14 ink frame (an image clip keeps the renderer on its media path; bare ink frames leaked stale captions)
vid("ink.png", 23.9, 1.4, kind="img")
line("jay", "You're watching it.", 24.3, 25.3, "mid", centre=True)

# 15 the button: the box at 0.5x, slow push, stamp returns on "thing"
vid("b15.mp4", 25.3, 4.5, "42% 78%", 1.04, 1.16)
mark(29.35, 29.8, slam=False, slow=True)

# 16 ink frame, the +1 gets the last word
vid("ink.png", 29.8, 1.2, kind="img")
line("plus", "I did most of it.", 29.85, 31.0, "mid", centre=True)

# 17 end card
block(30.8, 31.0, 31.05, 31.6)
el("div", 31.0, 3.0, "full card")
e1 = el("div", 31.0, 3.0, "end1", "Jay+1")
e2 = el("div", 31.0, 3.0, "end2 mono", "youtube.com/@jayplusone")
e3 = el("div", 31.0, 3.0, "end3 mono", "A Milbird production")
tw += [
    f'tl.fromTo("#{e1}", {{ opacity: 0, scale: 0.92 }}, {{ opacity: 1, scale: 1, duration: 0.6, ease: "power3.out" }}, 31.25);',
    f'tl.fromTo(["#{e2}", "#{e3}"], {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.5, stagger: 0.15, ease: "power2.out" }}, 31.65);',
]

CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: #241e22; }
#root { position: relative; width: 1920px; height: 1080px; overflow: hidden; background: #241e22; color: #f2efe5; font-family: "DM Sans", Arial, sans-serif; }
.clip { position: absolute; }
.full { left: 0; top: 0; width: 1920px; height: 1080px; }
.inkbg { z-index: 0; background: #241e22; }
.shot { z-index: 1; object-fit: cover; }
img.shot { filter: saturate(.85) contrast(1.04); }
.mono { font-family: "IBM Plex Mono", monospace; text-transform: uppercase; letter-spacing: .16em; }
.grad { z-index: 5; left: 0; top: 480px; width: 1920px; height: 600px; background: linear-gradient(180deg, rgba(36,30,34,0) 0%, rgba(36,30,34,.62) 70%); }
.ln { z-index: 10; left: 140px; display: flex; align-items: baseline; gap: 30px; white-space: nowrap; }
.ln.low { bottom: 110px; } .ln.high { bottom: 250px; }
.ln .who { font-size: 26px; font-weight: 500; width: 76px; flex: none; }
.ln.plus .who { color: #f0a18b; } .ln.jay .who { color: #c5bcc0; }
.ln.plus .tx { font-family: "IBM Plex Mono", monospace; font-size: 60px; font-weight: 500; color: #f0a18b; background: rgba(36,30,34,.85); padding: 8px 16px; }
.ln.plus.mid .tx { font-size: 72px; background: none; }
.scrim { z-index: 6; left: 0; top: 560px; width: 1920px; height: 520px; background: rgba(36,30,34,.6); }
.clock.rw { z-index: 32; right: auto; left: 780px; width: 360px; top: 600px; text-align: center; font-size: 60px; background: #241e22; color: #f0a18b; }
.ln.jay .tx { font-family: "Instrument Serif", Georgia, serif; font-size: 112px; line-height: 1; color: #f2efe5; text-shadow: 0 4px 30px rgba(36,30,34,.5); }
.ln.mid { left: 0; width: 1920px; top: 0; height: 1080px; justify-content: center; align-items: center; }
.ln.mid .who { display: none; }
.clock { z-index: 12; right: 90px; top: 70px; font-size: 40px; font-weight: 500; color: #241e22; background: #f0a18b; padding: 10px 22px; letter-spacing: .08em; transform-origin: right top; }
.clock.big { font-size: 60px; }
.clock.inv { background: #241e22; color: #f0a18b; }
.stamp { z-index: 14; left: 1120px; top: 230px; font-family: "IBM Plex Mono", monospace; font-weight: 500; font-size: 140px; letter-spacing: .04em; color: #f0a18b; border: 10px solid #f0a18b; padding: 6px 40px; transform: rotate(-7deg); background: rgba(36,30,34,.35); white-space: nowrap; }
.marksub { z-index: 14; left: 1130px; top: 500px; width: 700px; font-size: 26px; line-height: 1.5; color: #f2efe5; background: rgba(36,30,34,.55); padding: 8px 14px; }
.flash { z-index: 20; left: 0; top: 0; width: 1920px; height: 1080px; background: #f2efe5; opacity: 0; }
.block { z-index: 30; left: 0; top: 0; width: 1920px; height: 1080px; background: #f0a18b; }
.rewind { z-index: 31; left: 0; top: 480px; width: 1920px; text-align: center; font-size: 56px; color: #241e22; font-weight: 500; }
.word { z-index: 10; left: 0; width: 1920px; top: 380px; text-align: center; font-family: "Instrument Serif", Georgia, serif; font-style: italic; font-size: 260px; line-height: 1; color: #f2efe5; text-shadow: 0 6px 50px rgba(36,30,34,.6); }
.card { z-index: 24; background: #241e22; }
.tjay { z-index: 25; left: 132px; top: 230px; font-family: "Instrument Serif", Georgia, serif; font-size: 300px; line-height: 1; letter-spacing: -.02em; }
.tjay .plus { color: #f0a18b; display: inline-block; }
.tfn { z-index: 25; left: 140px; top: 560px; font-family: "Instrument Serif", Georgia, serif; font-style: italic; font-size: 150px; line-height: 1; color: #f0a18b; }
.ttag { z-index: 25; left: 140px; top: 800px; font-size: 26px; color: #c5bcc0; }
.end1 { z-index: 25; left: 0; top: 380px; width: 1920px; text-align: center; font-family: "Instrument Serif", Georgia, serif; font-size: 170px; line-height: 1; }
.end2 { z-index: 25; left: 0; top: 590px; width: 1920px; text-align: center; color: #f0a18b; font-size: 26px; }
.end3 { z-index: 25; left: 0; top: 660px; width: 1920px; text-align: center; color: #c5bcc0; font-size: 26px; }
"""

html = f"""<!doctype html>
<html lang="en" data-resolution="landscape">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Instrument+Serif:ital@0;1&family=IBM+Plex+Mono:wght@400;500;600&display=swap" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <!-- GENERATED by build.py: edit that, not this. -->
    <style>{CSS}</style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="34" data-width="1920" data-height="1080">
      <!-- Sound: one pre-mixed track (media/h/mix.wav): John's three real lines, room tone, dry ticks. -->
      <audio id="mix" src="media/h/mix.wav" data-start="0" data-duration="34" data-media-start="0"></audio>
      {chr(10).join('      ' + e for e in els)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
{chr(10).join('      ' + t for t in tw)}
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""
Path(__file__).with_name("index.html").write_text(html)
print(len(els), "elements,", len(tw), "tweens")
