# Pikagotchi Credits & Licenses

## Upstream Engine

**Pikagotchi (`hihry.pikagotchi`)** is built on top of [**Omagotchi (`slcode777.omagotchi`)**](https://github.com/SLcode777/omagotchi) by **SLcode777** (MIT License) — including the virtual pet simulation loop, Quickshell bar/panel integration, Hyprland IPC window-climbing physics, and curated Freesound audio triggers.

## Full-Color Sprites & Room Decor

All 68 full-color RGBA Pokémon evolution sprites (`egg` Pokéball, `baby`/`child` Pichu, `teen_neat`/`teen_scruffy`/`adult_ok`/`adult_gremlin` Pikachu, and `adult_ace` Raichu) and 9 Pokémon-themed room decor props are procedurally generated via `tools/generate_pikagotchi_sprites.py`.

> **Trademark Notice:** *Pokémon*, *Pikachu*, *Pichu*, *Raichu*, and *Poké Ball* are trademarks and © of Nintendo, Creatures Inc., and GAME FREAK inc. Pikagotchi is a free, open-source, non-commercial fan customization created for the Omarchy Linux community.

## Sound Effects

All clips in `sounds/` come from [freesound.org](https://freesound.org) (curated by SLcode777) and retain their respective Creative Commons licenses listed below. Each file is named after the pet event it plays for (see `eventSounds` in `Service.qml`), so any sound can be swapped without modifying QML code.

| File | Event | Source |
| --- | --- | --- |
| `hatch.wav` | egg hatches | "evolve.wav" by jeckkech — https://freesound.org/s/391656/ — CC BY 4.0 |
| `evolve.wav` | evolution | "Old Video Game 4" by sonically_sound — https://freesound.org/s/624878/ — CC BY 4.0 |
| `eat.wav` | feeding | "carrotnom.wav" by j1987 — https://freesound.org/s/106392/ — CC0 |
| `wash.wav` | being scrubbed | "scrubbing" by erikwitha_k — https://freesound.org/s/754792/ — CC0 |
| `pet.wav` | petting (random pick) | "Cute creature 02.wav" by Hawkeye_Sprout — https://freesound.org/s/469067/ — CC BY 4.0 |
| `pet2.wav` | petting (random pick) | "Cute creature 01.wav" by Hawkeye_Sprout — https://freesound.org/s/469066/ — CC BY 4.0 |
| `humming.wav` | hums to itself now and then while roaming | "Cute creature humming.wav" by Hawkeye_Sprout — https://freesound.org/s/469091/ — CC BY 4.0 |
| `sleep.mp3` | falling asleep | "Old Music Box 2" by Soughtaftersounds — https://freesound.org/s/145435/ — CC BY 3.0 |
| `stun.mp3` | stunned by a big fall | "skill_dizzy_A_01.mp3" by formacat — https://freesound.org/s/550275/ — CC BY-NC 4.0 |
| `fall.wav` | thud of a big fall (right before the stun) | "Gun Shot 7 8 Bit.wav" by Mrthenoronha — https://freesound.org/s/507019/ — CC BY-NC 4.0 |
| `tractorbeam.wav` | tractor beam (out and back) | "Beam.wav" by Deatlev — https://freesound.org/s/254942/ — CC BY 3.0 |
| `balloon.wav` | the ball bounces | "ballontile9b.wav" by NoiseCollector — https://freesound.org/s/125457/ — CC BY 3.0 |
| `farewell_ace.wav` | the ace adult says goodbye | "japanese - goodbye.wav" by Reitanna — https://freesound.org/s/235107/ — CC0 |
| `farewell_ok.mp3` | the ok adult says goodbye | "bye-bye" by Alivvie — https://freesound.org/s/323361/ — CC0 |
| `farewell_gremlin.mp3` | the gremlin says goodbye | "UFO Voice Goodbye.mp3" by richmstudios — https://freesound.org/s/317015/ — CC BY-NC 3.0 |
| `subbass.wav` | tractor beam powering up | "sub bass 1 seconddddd.wav" by uzerx — https://freesound.org/s/59537/ — CC0 |
| `grab.wav` | picked up by the scruff | "74-PerritoLadraSorprendido.wav" by Caap — https://freesound.org/s/427133/ — CC0 — pitched up 3 semitones |
