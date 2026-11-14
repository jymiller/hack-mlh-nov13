# Jay+1 Field Notes

**A video used to need a studio. Today it needs a hackathon.** One person plus one intelligence, door to film in
sixty minutes, written in HTML and rendered with HyperFrames.

Built at the **AIE x MLH Hackathon @ Code Summit**, Friday 13 November 2026, San Francisco.

- **The app:** https://claude.ai/artifact/JBtfJ25EHPkXH6SbQ3EMgq (the control room: monitors, rundown, crew,
  and a distribution desk; source in [`artifact/field-notes.html`](artifact/field-notes.html))
- **The full film (1:21):** https://youtu.be/xk_UCyKhiY8
- **The director's cut (0:34, the submitted video):** https://youtu.be/ZP9PZGTm5_E
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
- `video/field-notes` is the director-led cut with John's footage and voice; `video/director` holds the
  treatment and the review of each cut.
- `video/movie-open` and `video/movie-close` are the movie-style opening (animated three-bird logo, joke
  credits) and closing credits. `video/kit-start` and `video/kit-end` are five-second reusable versions.
- `video/app-demo` shows the control room in use; `video/outro-a`, `-b` and `-c` are three competing endings
  that file the project into the Milbird hackathon library (A was chosen).
- `video/bumper`, `video/stills-cut` and `video/thanks` are the earlier bumper, stills film and two-second clip.
- Footage, photos, the logo image and renders are kept out of the repo, so the compositions need those
  media files added locally to render. The finished videos play in the app's screening room.

## How AI was used

Built with Claude Code. Claude Fable 5.2 produced the page, the notes and the stills film; Claude Opus 5.5
sessions acted as director and editor for the footage cut. John chose the story, the jokes and every cut that
went out.

## Event

- Event: https://www.mlh.com/events/aie-x-mlh-hackathon-code-summit
- Event facts, schedule and prizes: [`.hackathon/event.json`](.hackathon/event.json)
