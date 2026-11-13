# Jay+1 Field Notes

**A video used to need a studio. Today it needs a hackathon.** One person plus one intelligence, door to film in
sixty minutes, written in HTML and rendered with HyperFrames.

Built at the **AIE x MLH Hackathon @ Code Summit**, Friday 13 November 2026, San Francisco.

- **The app:** https://claude.ai/artifact/JBtfJ25EHPkXH6SbQ3EMgq (the control room: monitors, rundown, crew,
  and a distribution desk; source in [`artifact/field-notes.html`](artifact/field-notes.html))
- **The film:** https://youtu.be/ZP9PZGTm5_E
- **Channel:** https://www.youtube.com/@jayplusone

## What it does

John walks the room and records what he hears and sees (Granola, iPhone). His plus-one turns the recordings
into field notes and a short film. The film is a set of HyperFrames compositions: HTML and CSS with a scripted
timeline, rendered locally to 1080p MP4. There is no timeline editor and no After Effects in the loop.

The control room page is the app. YouTube is the one live output today. The other buttons on its distribution
desk (Milbird.com, Instagram, TikTok, LinkedIn, X) show the intended flow and are marked as a demo.

## How HyperFrames was used

- Every shot, title, caption and transition is HTML with a GSAP timeline, in [`video/`](video/).
- Directed in film terms: cold open, jump cuts, smash cut to title, freeze-frame punch-in with a stamp,
  montage, end-card button.
- A 31-second cut renders in about 20 seconds, so the story was rewritten four times in under half an hour
  by editing HTML and re-rendering.
- `video/bumper` is the 10-second series bumper, `video/stills-cut` the 31-second stills film,
  `video/thanks` a two-second clip. Footage, photos and renders are kept out of the repo.

## How AI was used

Built with Claude Code. Claude Fable 5.2 produced the page, the notes and the stills film; Claude Opus 5.5
sessions acted as director and editor for the footage cut. John chose the story, the jokes and every cut that
went out.

## Event

- Event: https://www.mlh.com/events/aie-x-mlh-hackathon-code-summit
- Event facts, schedule and prizes: [`.hackathon/event.json`](.hackathon/event.json)
