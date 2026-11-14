# Jay+1 Field Notes: adversarial design review

Reviewed 13 Nov 2026 against `artifact/field-notes.html` (511 lines), rendered in headless Chrome at 1440x900 and 390x844. The proposal is built at `artifact/field-notes-simplified.html`. Nothing existing was edited, published or committed.

## Verdict

The page is a convincing picture of a control room and a poor way to watch a film: the real video sits below the fold on desktop and nearly two screens down on a phone, behind a text mock-up of the film, a preview of the mock-up, and a list of rejected cuts. Ten titled panels, 80 uppercase labels and 21 buttons compete for a visitor who needs three things: press play, read five notes, see where it goes. Make the real film the program monitor, keep the two voices and the tally light, and put everything about how it was made in a drawer.

## What is working and must survive

- **The two voices.** `+1` in cyan mono, `JAY` in white serif. "You have no project." / "Let's discuss ideas." is the best copy on the page and explains the product faster than the paragraph beside it.
- **The headline.** "One person, plus one intelligence, at a hackathon."
- **The red program tally** on the monitor, and the reel list as a switcher. These are the control room. Most of the rest is set dressing.
- **All black with cyan.** It reads as cool and deliberate.
- **The honest demo label** on the distribution desk, and the five notes, which are specific and worth reading.
- **"Rejected: declarative"** in the playout stack is funny, but only to John.

## Seat A: a hackathon judge with 30 seconds

1. **The first thing that looks like a film is not a film.** The Program monitor is styled text. A judge looks for a play button on it, finds none, and has to work out that the playable video is the "Screening room" panel, whose top edge is at the bottom of a 900px screen.
2. **No primary action above the fold.** Measured at 1440x900: two controls are in view (the top sliver of the video and the first reel), and neither is a call to action. "Publish everywhere", the only filled button, is a demo, and it is the loudest button on the page.
3. **The lede contradicts the player.** The intro says "a 31-second film". The player says 1:21. The screening room lists six reels. A judge cannot tell which one is the submission.
4. **Status lamps report nothing a judge can use.** "Cut v2 rendered" is internal. "On air" is unlit, so the page says it is off air while the lamp beside it says YouTube is live.
5. **Preview monitor and playout stack** take the whole right column of the first screen to show the next line of a mock-up and two cuts nobody should watch.
6. **"This is the gallery the film was cut in"** is not true of a web page and uses "gallery" in a sense most people do not know.
7. **The rundown's instruction, "Select a cue to take it to program",** is jargon, and the result of clicking happens 1,300px up the page, out of sight.

Did they get it? Probably yes, from the headline, and then they scroll past the film.

## Seat B: a non-technical viewer on a phone, arriving from YouTube

1. **The video starts about 1,500px down**, after the address of the venue, three lamps, a text monitor, a second text monitor and the playout stack. Nothing in the first screen can be tapped.
2. **They have just watched the film.** The page opens by re-enacting it in text. What they do not have yet is the notes, and those are last: about 5,900px down a 7,100px page.
3. **Monitor captions are 7.5 to 9px.** The `JAY` and `+1` speaker tags, which carry the whole joke, are the smallest text on the screen.
4. **Vocabulary.** Program, preview, playout stack, patch bay, router outputs, TC, PGM, PVW, take. None is explained and none is needed to watch or read.
5. **Six social cards stack to a full screen of buttons that do nothing**, between the film and anything else real.
6. **Crew, clocks, sources and outputs** are four more screens before the notes.

## Seat C: John in three months, publishing the next field notes

1. **It cannot publish.** The desk is a simulation. That is fine for a demo and is the gap between this and a real app; the page should not look more finished than it is.
2. **Content is duplicated by hand.** The cold open exists twice in the markup (monitor and rundown). The film URL appears three times. The date, venue and cut length are scattered through eight places. Changing the event means a careful find-and-replace across about 250 lines.
3. **Hackathon-day state is frozen into the layout.** v0, v1, v2, "rejected", "~20 sec a render", 2:04 and 3:00 are all structure, not content. Next time they are wrong or empty.
4. **The timeline is typed in as flex numbers** (`flex-grow:8`, `2`, `4`...), separately from the cue durations it is meant to show.
5. **After a demo run, the desk is stuck.** Buttons disable and there is no reset without reloading, which is awkward when showing it to a second person.
6. **No slot for the thing he will reuse most:** the notes and the film. They are the last panel and the third.

In the simplified file each piece of content appears once and is marked with an `EDIT` comment (nine of them).

## Seat D: accessibility and legibility

1. **Size is the main failure, not contrast.** 136 text elements are under 13px; the smallest are 7.5px on a phone. Muted grey `#8a9299` on black is about 6.6:1, which passes, but not at 9px in letterspaced capitals.
2. **80 uppercase mono labels.** Capitals with wide tracking are slow to read and most of these are decoration: "In 1", "Out 3", "Pacific time", "5 inputs", "JAY serif · +1 mono".
3. **Control boundaries are invisible.** Reel buttons and channel cards are outlined in `#1e2226` on `#000`, about 1.2:1. A button's edge needs 3:1.
4. **Tap targets.** 23 of 32 controls are under 44px in one dimension, including every reel and every publish button.
5. **`aria-live` on the program monitor** makes a screen reader re-announce the whole cue each time a rundown button is pressed, after it has just read the same lines in the button.
6. **Reading order.** A screen reader hears the venue address, three status lights and a mock transcript before it reaches the video, and the notes come after 27 other controls.
7. **The timeline is `aria-hidden`** and the cue state is conveyed by colour (red, green) plus a pseudo-element label that some readers skip.
8. **Hover-only affordance** on reels; pressed state is a 1px colour change.
9. **No captions track on the video.** The script in the rundown is the only text alternative and it is for a different cut.
10. **Reduced motion is respected** (the one blink and the progress bars). Focus rings exist. Theme is pinned dark in both modes, which is a deliberate choice, not a bug.

## Cognitive load

Measured from the rendered page (text elements with their own text, visible controls).

| | Above the fold, desktop | Above the fold, phone | Whole page |
|---|---|---|---|
| Regions / panels | 6 (bar, intro, program, preview, playout, screening room edge) | 5 | 14 (10 titled panels plus bar, intro, two monitors) |
| Uppercase labels | 24 | 17 | 80 |
| Status chips and lamps | 8 | 5 | 22 |
| Type sizes | 13 | 9 | 19 |
| Text colours | 6 | 5 | 8, plus red, green and amber fills |
| Controls | 2 | 0 | 32 (20 buttons, 11 links, 1 video) |
| Calls to action that do the main job | 0 | 0 | 1 real ("Watch the film"), 1 loud demo, 19 others |

**The three things the page must let a person do, in order:**

1. Watch the film and understand in one sentence what Jay+1 is.
2. Read what the room taught (the field notes).
3. See it go out: where it is published, and follow it to the channel, the source and the library.

**What serves none of them:** the three status lamps, the text program monitor, the preview monitor, the playout stack, the timeline, the clocks, the `In`/`Out` numbering, the "who reports to whom" chain as a diagram, and the take-a-cue interaction. The crew, kit and script are worth keeping as reference, closed by default.

## Ranked changes

| # | Change | Why | Cost |
|---|---|---|---|
| 1 | **Make the real video the program monitor.** Delete the text monitor; put the red tally and "Program" tag on the `<video>`. | Fixes seats A and B at once: the thing that looks like the film is the film, above the fold on both sizes. | Loses the simulated monitor, the most "control room" object on the page. Highest taste risk. |
| 2 | **One primary button: "Play the film · 1:21".** Demote "Publish everywhere" to an outlined "Run the publish demo". | One obvious thing to press; the demo stops being the loudest element. | None. |
| 3 | **Delete preview monitor, playout stack, timeline, clocks, status lamps.** Keep one lit tally: "On air on YouTube", which is a link. | None serves a visitor. Removes 5 panels and about 30 labels. | Loses "Rejected: declarative", an in-joke. |
| 4 | **Move the notes up to second place**, in 17px type with 25px headings. | They are the product's name and were last. | None. |
| 5 | **Turn the distribution desk into six rows and one button**, with a reset. Demo rows say "Demo" before, during and after. | Six cards and seven buttons become one list; honesty is stated three ways. | Loses per-channel buttons. |
| 6 | **Fold the rundown into a closed "The script" drawer** as plain text, not buttons. | It is a transcript, useful to some, needed by none. Removes 8 buttons. | Loses the take-to-program toy. See the conflict below. |
| 7 | **Merge crew and patch bay into one closed "How it was made" drawer**: Crew, Kit. | Same information, no jack graphics or `In 3` numbering. | Loses the patch-bay look. |
| 8 | **Move router outputs to four footer links**: channel, source, event, library. | They are links, not a panel. | Drops the four older field-notes links, which were not on the list of confirmed links. |
| 9 | **Type floor of 13px, seven sizes, 44px tap targets, 3:1 control outlines.** | Seat D. | Slightly less dense; less "instrument panel". |
| 10 | **One sentence for the story**, and remove the "31-second" claim next to a 1:21 film. | Seat A item 3. | None. |
| 11 | **Each piece of content once, marked `EDIT`.** | Seat C. | None. |

## Wireframes

Desktop, first screen (1440x900):

```
JAY+1 FIELD NOTES   AIE X MLH HACKATHON · SAN FRANCISCO · 13 NOV 2026      ● ON AIR ON YOUTUBE
----------------------------------------------------------------------------------------------
==== red tally =====================   One person, plus one
[PROGRAM]        THE FULL FILM · 1:21   intelligence, at a hackathon.
|                                  |
|            the film              |   John walked in at 2:04 PM. Submissions closed at 3:00...
|          (real video)            |   [ Play the film · 1:21 ]   Read the five notes
|                                  |   ----------------------------------------
| > 0:00 / 1:21                    |   +1   Submissions close at 3:00.
====================================   JAY  I just arrived.
                                       +1   You have no project.
                                       JAY  Let's discuss ideas.
[Full film][Director's][Opening][Using the app][Filed in library][Closing credits]

Field notes                                                        WHAT THE ROOM TAUGHT
1  The video prize judges the film, so the film can be about anything you built.
```

Below: notes 2 to 5; "Send it out" (one line, one demo button, six rows); two closed drawers ("The script", "How it was made"); footer links.

Phone, first screen (390x844):

```
JAY+1 FIELD NOTES    ● ON AIR ON YOUTUBE
----------------------------------------
One person, plus one
intelligence, at a hackathon.
John walked in at 2:04 PM. Submissions
closed at 3:00. He recorded the room...
[ Play the film · 1:21 ]
Read the five notes
==== red tally =========================
[PROGRAM]          THE FULL FILM · 1:21
|            the film                  |
| > 0:00 / 1:21                        |
[The full film ] [Director's cut  ]
[Movie opening ] [Using the app   ]
[Filed in lib. ] [Closing credits ]
```

Then: the cold open, the five notes, send it out, two drawers, footer.

## Before and after

| | Original | Simplified |
|---|---|---|
| Regions / panels | 14 (10 titled) | 5 (hero, notes, send it out, two closed drawers) |
| Uppercase labels | 80 | 14 |
| Status chips and lamps | 22 | 6 |
| Type sizes | 19 | 7 |
| Text under 13px | 136 elements | 0 |
| Controls | 32 | 18 |
| Controls under 44px | 23 | 0 |
| Primary calls to action above the fold, desktop | 0 | 1 (plus the video and reels) |
| Primary calls to action above the fold, phone | 0 (nothing tappable) | 1 (plus the video and reels) |
| Distance to the video on a phone | about 1,500px | about 400px |
| Words on the page | 971 | 680, of which 483 show with drawers closed |
| Page height, desktop / phone | 3,940 / 7,112px | 2,213 / 3,496px |

## What was checked, and what was not

- Rendered at both widths in headless Chrome; no horizontal scroll at 390px (scroll width 390).
- Scripted test: the reel switch changes the source and the label; the publish demo ends with all five rows at "Sent (demo)" and the button at "Reset the demo"; both drawers open and lay out at 390px.
- **Not checked:** the real artifact viewer, a real phone, video playback itself (headless Chrome does not play), a screen reader, and the "Play the film" scroll-to-video behaviour on iOS.

## Where I am unsure, and where this conflicts with John's taste

1. **The big one.** John asked for "an awesome video control room for a TV show" that feels like his "real app". This proposal keeps the tally, the program tag, the reel switcher, the two typefaces and the black, and removes most of the furniture. It may read as a film page with control-room accents and not as a control room. If that is wrong, the fix is to keep this page as the public front and put the full gallery behind a third drawer or a second page, not to restore it above the film.
2. **The take-a-cue rundown** was the only playful interaction and I removed it. It is cheap to bring back inside the script drawer, driving a small monitor there.
3. **The poster is orange.** `media/poster.jpg` sets "+" and "Field Notes" in salmon, and it is the largest coloured thing on either version. John rejected the orange look. I left the poster alone (it is not mine to change) and it should be re-rendered in cyan.
4. **Tally red.** The original `#ff5a4f` leans coral. I used a cooler `#ff4b5c`, in one place only. Taste call.
5. **Which reel is the submission?** I made the 1:21 full film the default, as the original does. The script drawer is labelled "The two-hander · 8 cues"; I could not confirm which reel those eight cues match (the intro says 31 seconds, the director's cut runs 0:34).
6. **Dropped links.** `milbird.com/field-notes` and its four dated posts are gone because they were not on the confirmed list. Easy to restore in the footer.
7. **"Send it out"** replaces "Distribution desk" as the heading. Plainer, less in character.
8. **No captions.** Neither version has a captions track; the film needs one.
