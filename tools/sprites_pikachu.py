"""
sprites_pikachu.py
All 40 Pikachu sprites across 4 variants:
- teen_neat (10 sprites): disciplined, symmetrical upright stance, neat tail
- teen_scruffy (10 sprites): playful rebel, cocked left ear, spiky cheek fur, jaunty swagger
- adult_ok (10 sprites): canonical cheerful Pikachu, open friendly smile, broad lightning tail
- adult_gremlin (10 sprites): cheeky cat smirk, electric cheek spark (FFFF99), sneaky skitter (matches active pet!)
"""

from generate_pikagotchi_sprites import PIKACHU_PALETTE

# ==============================================================================
# TEEN NEAT (10 Sprites)
# ==============================================================================

TEEN_NEAT_IDLE_A = """
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD...
...DYYD.DYYD....
...DYYYYYYYD.YY.
..DYWDYYYDWYDYD.
..DYDYDYYDYDYD..
.DRYYDYYYDYYRD..
..DYYYDMYDYYDB..
...DYYYYYYYD.B..
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

TEEN_NEAT_IDLE_B = """
................
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD...
...DYYD.DYYD.YY.
...DYYYYYYYDDYD.
..DYWDYYYDWYDYD.
..DYDYDYYDYDYD..
.DRYYDYYYDYYRDB.
..DYYYDMYDYYDB..
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

TEEN_NEAT_WALK_A = """
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD...
...DYYD.DYYD.YY.
...DYYYYYYYDDYD.
..DYWDYYYDWYDYD.
..DYDYDYYDYDYD..
.DRYYDYYYDYYRD..
..DYYYDMYDYYDB..
...DYYYYYYYD.B..
..DYYBBYYBBYD...
.DYYD.DYYD......
.DYYD..DYYD.....
.DYYD...DD......
..DD............
"""

TEEN_NEAT_WALK_B = """
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD...
...DYYD.DYYD....
...DYYYYYYYD.YY.
..DYWDYYYDWYDYD.
..DYDYDYYDYDYD..
.DRYYDYYYDYYRD..
..DYYYDMYDYYDB..
...DYYYYYYYD.B..
..DYYBBYYBBYD...
.....DYYD.DYYD..
....DYYD..DYYD..
......DD...DYYD.
............DD..
"""

# Rear climbing view with two brown back stripes and reaching paws
TEEN_NEAT_CLIMB_A = """
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD...
.DD.DYYD.DYYD...
.DYDYYYYYYYD.YY.
.DYYDYYYYYDYYD..
.DYYBBYYBBYD.B..
..DYYYYYYYYD....
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYyYYyYYD....
..DYYD...DYYD...
..DYD.....DYD...
.DWYD.....DWYD..
..DD.......DD...
"""

TEEN_NEAT_CLIMB_B = """
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD...
...DYYD.DYYD.DD.
...DYYYYYYYDYD..
..DYYDYYYYYDYYD.
..DYYBBYYBBYD...
..DYYYYYYYYD.YY.
..DYYBBYYBBYDB..
..DYYYYYYYYD....
..DYYyYYyYYD....
...DYD...DYD....
...DYD...DYD....
..DWYD...DWYD...
...DD.....DD....
"""

TEEN_NEAT_EAT_A = """
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD...
...DYYD.DYYD....
...DYYYYYYYD.YY.
..DYWDYYYDWYDYD.
..DYDYDYYDYDYD..
.DRYYDAAYDYYRD..
..DYYDAAADYD.B..
...DYYDMYDYYDB..
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

TEEN_NEAT_EAT_B = """
................
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD...
...DYYD.DYYD.YY.
...DYYYYYYYDDYD.
..DYDDYYYDDYDYD.
..DRYYDYYYDYYRD.
.DRYYDAAYDYYRDB.
..DYYYmmmyYD.B..
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

# Curled sleeping pose with neat tucked tail and closed eyes
TEEN_NEAT_SLEEP_A = """
................
................
................
................
....DD.....DD...
...DYD.....DYD..
..DYYD.....DYYD.
.DYYYYD...DYYYYD
.DYYYDYDDYDYyYYD
.DRDDYYYYYDDYyRD
.DRYYYYYYYYYYyRD
..DYYBBYYBBYD...
.DYYYYYYYYYYYBD.
.DYYBBYYBBYYYYD.
.DYYYYyYYYYyYYD.
..DDD......DDD..
"""

TEEN_NEAT_SLEEP_B = """
................
................
................
................
................
....DD.....DD...
...DYD.....DYD..
..DYYD.....DYYD.
.DYYYYD...DYYYYD
.DYYYDYDDYDYyYYD
.DRDDYYYYYDDYyRD
.DRYYYYYYYYYYyRD
..DYYBBYYBBYD...
.DYYBBYYBBYYYBD.
.DYYYYyYYYYyYYD.
..DDD......DDD..
"""

# ==============================================================================
# TEEN SCRUFFY (10 Sprites)
# ==============================================================================

# Left ear cocked sideways/bent, spiky forehead tuft, jaunty smirk
TEEN_SCRUFFY_IDLE_A = """
............DD..
.DDD.......DYD..
.DYYDDD...DYD...
..DDYYYD.DYYD...
....DYYYDYDYD...
...DYYYYYYYD.YY.
..DYWDYYYDWYDYD.
.DYDYDYYDYDYD...
.DRYYDYYYDRyRD..
..DYYYDMYyYYDB..
...DYYYYYYYD.B..
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

TEEN_SCRUFFY_IDLE_B = """
................
............DD..
.DDD.......DYD..
.DYYDDD...DYD...
..DDYYYD.DYYD.YY
....DYYYDYDYDDYD
...DYYYYYYYDYD..
..DYWDYYYDWYDYD.
.DYDYDYYDYDYD...
.DRYYDYYYDRyRDB.
..DYYYDMYyYYDB..
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

TEEN_SCRUFFY_WALK_A = """
............DD..
.DDD.......DYD..
.DYYDDD...DYD...
..DDYYYD.DYYD.YY
....DYYYDYDYDDYD
...DYYYYYYYDYD..
..DYWDYYYDWYDYD.
.DYDYDYYDYDYD...
.DRYYDYYYDRyRD..
..DYYYDMYyYYDB..
...DYYYYYYYD.B..
..DYYBBYYBBYD...
.DYYD...DYYD....
.DYYD....DYYD...
.DYYD.....DD....
..DD............
"""

TEEN_SCRUFFY_WALK_B = """
............DD..
.DDD.......DYD..
.DYYDDD...DYD...
..DDYYYD.DYYD...
....DYYYDYDYD...
...DYYYYYYYD.YY.
..DYWDYYYDWYDYD.
.DYDYDYYDYDYD...
.DRYYDYYYDRyRD..
..DYYYDMYyYYDB..
...DYYYYYYYD.B..
..DYYBBYYBBYD...
....DYYD...DYYD.
...DYYD....DYYD.
....DD.....DYYD.
............DD..
"""

TEEN_SCRUFFY_CLIMB_A = """
............DD..
.DDD.......DYD..
.DYYDDD...DYD...
..DDYYYD.DYYD...
.DD.DYYYDYDYD...
.DYDYYYYYYYD.YY.
.DYYDYYYYYDYYD..
.DYYBBYYBBYD.B..
..DYYYYYYYYD....
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYyYYyYYD....
..DYYD...DYYD...
..DYD.....DYD...
.DWYD.....DWYD..
..DD.......DD...
"""

TEEN_SCRUFFY_CLIMB_B = """
............DD..
.DDD.......DYD..
.DYYDDD...DYD...
..DDYYYD.DYYD.DD
....DYYYDYDYDDYD
...DYYYYYYYDYD..
..DYYDYYYYYDYYD.
..DYYBBYYBBYD...
..DYYYYYYYYD.YY.
..DYYBBYYBBYDB..
..DYYYYYYYYD....
..DYYyYYyYYD....
...DYD...DYD....
...DYD...DYD....
..DWYD...DWYD...
...DD.....DD....
"""

TEEN_SCRUFFY_EAT_A = """
............DD..
.DDD.......DYD..
.DYYDDD...DYD...
..DDYYYD.DYYD...
....DYYYDYDYD...
...DYYYYYYYD.YY.
..DYWDYYYDWYDYD.
.DYDYDYYDYDYD...
.DRYYDAAYDRyRD..
..DYYDAAADYD.B..
...DYYYMYyYYDB..
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

TEEN_SCRUFFY_EAT_B = """
................
............DD..
.DDD.......DYD..
.DYYDDD...DYD...
..DDYYYD.DYYD.YY
....DYYYDYDYDDYD
...DYYYYYYYDYD..
..DYDDYYYDDYDYD.
.DYDYDYYDYDYD...
.DRYYDAAYDRyRDB.
..DYYYmmmyYD.B..
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

TEEN_SCRUFFY_SLEEP_A = """
................
................
................
................
....DD.....DDD..
...DYD....DYYD..
..DYYD...DDYYD..
.DYYYYD.DYYYDDD.
.DYYYDYDDYDYyYYD
.DRDDYYYYYDDYyRD
.DRYYYYYYYYYYyRD
..DYYBBYYBBYD...
.DYYYYYYYYYYYBD.
.DYYBBYYBBYYYYD.
.DYYYYyYYYYyYYD.
..DDD......DDD..
"""

TEEN_SCRUFFY_SLEEP_B = """
................
................
................
................
................
....DD.....DDD..
...DYD....DYYD..
..DYYD...DDYYD..
.DYYYYD.DYYYDDD.
.DYYYDYDDYDYyYYD
.DRDDYYYYYDDYyRD
.DRYYYYYYYYYYyRD
..DYYBBYYBBYD...
.DYYBBYYBBYYYBD.
.DYYYYyYYYYyYYD.
..DDD......DDD..
"""

# ==============================================================================
# ADULT OK (10 Sprites) - Classic Canonical Pikachu
# ==============================================================================

ADULT_OK_IDLE_A = """
DD...........DD.
.DYD........DYD.
..DYD......DYD..
..DYYD....DYYD..
...DYYDDDDYYD.YY
..DYYYYYYYYYYDYY
..DYWDYYYDWYDYYD
..DYDYDYYDYDDYY.
.DRYYDYYYDYYRDYY
..DYYDmMMmDYYDB.
...DYYDmMDYYD.B.
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

ADULT_OK_IDLE_B = """
................
DD...........DD.
.DYD........DYD.
..DYD......DYD..
..DYYD....DYYDYY
...DYYDDDDYYDYDY
..DYYYYYYYYYYDYY
..DYWDYYYDWYDYYD
..DYDYDYYDYDDYY.
.DRYYDYYYDYYRDYY
..DYYDmMMmDYYDB.
...DYYDmMDYYD.B.
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DDYYDD.DDYYDD..
"""

ADULT_OK_WALK_A = """
DD...........DD.
.DYD........DYD.
..DYD......DYD..
..DYYD....DYYD..
...DYYDDDDYYD.YY
..DYYYYYYYYYYDYY
..DYWDYYYDWYDYYD
..DYDYDYYDYDDYY.
.DRYYDYYYDYYRDYY
..DYYDmMMmDYYDB.
...DYYDmMDYYD.B.
..DYYBBYYBBYD...
.DYYD.DYYD......
.DYYD..DYYD.....
.DYYD...DD......
..DD............
"""

ADULT_OK_WALK_B = """
DD...........DD.
.DYD........DYD.
..DYD......DYD..
..DYYD....DYYD..
...DYYDDDDYYD...
..DYYYYYYYYYYDYY
..DYWDYYYDWYDYYD
..DYDYDYYDYDDYY.
.DRYYDYYYDYYRDYY
..DYYDmMMmDYYDB.
...DYYDmMDYYD.B.
..DYYBBYYBBYD...
.....DYYD.DYYD..
....DYYD..DYYD..
......DD...DYYD.
............DD..
"""

ADULT_OK_CLIMB_A = """
DD...........DD.
.DYD........DYD.
..DYD......DYD..
..DYYD....DYYD..
.DD.DYYDDDDYYD..
.DYDYYYYYYYYYDYY
.DYYDYYYYYDYYDYY
.DRYBBYYBBYDDYY.
.DRDYYYYYYYYDDYY
..DYYBBYYBBYD.DB
..DYYYYYYYYD...B
..DYYyYYyYYD....
..DYYD...DYYD...
..DYD.....DYD...
.DWYD.....DWYD..
..DD.......DD...
"""

ADULT_OK_CLIMB_B = """
DD...........DD.
.DYD........DYD.
..DYD......DYD..
..DYYD....DYYD..
...DYYDDDDYYD.DD
...DYYYYYYYYDYD.
..DYYDYYYYYDYYD.
.DRYBBYYBBYD.YY.
.DRDYYYYYYYYDDYY
..DYYBBYYBBYDBYY
..DYYYYYYYYD.DB.
..DYYyYYyYYD..B.
...DYD...DYD....
...DYD...DYD....
..DWYD...DWYD...
...DD.....DD....
"""

ADULT_OK_EAT_A = """
DD...........DD.
.DYD........DYD.
..DYD......DYD..
..DYYD....DYYD..
...DYYDDDDYYD.YY
..DYYYYYYYYYYDYY
..DYWDYYYDWYDYYD
..DYDYDYYDYDDYY.
.DRYYDAAYDYYRDYY
..DYYDAAADYD.B..
...DYYDmMMmYD.B.
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

ADULT_OK_EAT_B = """
................
DD...........DD.
.DYD........DYD.
..DYD......DYD..
..DYYD....DYYD..
...DYYDDDDYYD.YY
..DYYYYYYYYYYDYY
..DYDDYYYDDYDYYD
..DRYYDYYYDYYRD.
.DRYYDAAYDYYRDB.
..DYYDmmMMmmD.B.
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

ADULT_OK_SLEEP_A = """
................
................
................
................
..DD.........DD.
.DYD.........DYD
.DYYD.......DYYD
DYYYYD.....DYYYY
DYYYDYDDYDYDYyYD
DRDDYYYYYDDYyRD.
DRYYYYDmMDYYyYRD
..DYYBBYYBBYDDYY
.DYYYYYYYYYYYDYY
.DYYBBYYBBYYYBBD
.DYYYYyYYYYyYYD.
..DDD......DDD..
"""

ADULT_OK_SLEEP_B = """
................
................
................
................
................
..DD.........DD.
.DYD.........DYD
.DYYD.......DYYD
DYYYYD.....DYYYY
DYYYDYDDYDYDYyYD
DRDDYYYYYDDYyRD.
DRYYYYDmMDYYyYRD
..DYYBBYYBBYDDYY
.DYYBBYYBBYYYBBD
.DYYYYyYYYYyYYD.
..DDD......DDD..
"""

# ==============================================================================
# ADULT GREMLIN (10 Sprites) - Mischievous Gremlin Pikachu with Cheek Spark
# ==============================================================================
# Key features:
# - Sparking cheek pixel 'K' (#FFFF99) on cheek pouch
# - Cheeky cat smirk (:3) with fanged grin 'm'
# - Distinct from adult_ok (tested in F11.4 / F11.B1 / F11.B3)
# - Closed eyes sleeping without spark (tested in F11.B4)

ADULT_GREMLIN_IDLE_A = """
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD...
...DYYD.DYYD.KK.
...DYYYYYYYD.KY.
..DYWDYYYDWYDYD.
..DYDYDYYDYDYD..
.DRKYDYYYDYYRD..
..DYYYDmYDYYDB..
...DYYYYYYYD.B..
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

ADULT_GREMLIN_IDLE_B = """
................
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD.KK
...DYYD.DYYD.KYD
...DYYYYYYYDYD..
..DYWDYYYDWYDYD.
..DYDYDYYDYDYD..
.DRYYDYYYDYYRDB.
..DYYYDmYDYYDB..
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

ADULT_GREMLIN_WALK_A = """
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD.KK
...DYYD.DYYD.KYD
...DYYYYYYYDYD..
..DYWDYYYDWYDYD.
..DYDYDYYDYDYD..
.DRKYDYYYDYYRD..
..DYYYDmYDYYDB..
...DYYYYYYYD.B..
..DYYBBYYBBYD...
.DYYD...DYYD....
.DYYD....DYYD...
.DYYD.....DD....
..DD............
"""

ADULT_GREMLIN_WALK_B = """
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD...
...DYYD.DYYD.KK.
...DYYYYYYYD.KY.
..DYWDYYYDWYDYD.
..DYDYDYYDYDYD..
.DRYYDYYYDYYRD..
..DYYYDmYDYYDB..
...DYYYYYYYD.B..
..DYYBBYYBBYD...
....DYYD...DYYD.
...DYYD....DYYD.
....DD.....DYYD.
............DD..
"""

ADULT_GREMLIN_CLIMB_A = """
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD.KK
.DD.DYYD.DYYD.KY
.DYDYYYYYYYD.YY.
.DYYDYYYYYDYYD..
.DYYBBYYBBYD.B..
..DYYYYYYYYD....
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYyYYyYYD....
..DYYD...DYYD...
..DYD.....DYD...
.DWYD.....DWYD..
..DD.......DD...
"""

ADULT_GREMLIN_CLIMB_B = """
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD...
...DYYD.DYYD.DD.
...DYYYYYYYDYDKK
..DYYDYYYYYDYYKY
..DYYBBYYBBYD...
..DYYYYYYYYD.YY.
..DYYBBYYBBYDB..
..DYYYYYYYYD....
..DYYyYYyYYD....
...DYD...DYD....
...DYD...DYD....
..DWYD...DWYD...
...DD.....DD....
"""

ADULT_GREMLIN_EAT_A = """
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD...
...DYYD.DYYD.KK.
...DYYYYYYYD.KY.
..DYWDYYYDWYDYD.
..DYDYDYYDYDYD..
.DRKYDAAYDYYRD..
..DYYDAAADYD.B..
...DYYYmYDYYDB..
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

ADULT_GREMLIN_EAT_B = """
................
.DD.........DD..
.DYD.......DYD..
..DYD.....DYD...
..DYYD...DYYD...
...DYYD.DYYD.KK.
...DYYYYYYYD.KY.
..DYDDYYYDDYDYD.
..DRYYDYYYDYYRD.
.DRYYDAAYDYYRDB.
..DYYYmmmyYD.B..
..DYYBBYYBBYD...
..DYYYYYYYYD....
..DYYD...DYYD...
.DYYDD...DDYYD..
..DD.......DD...
"""

# Curled mischief sleep with closed eyes (> <), spark extinguished
ADULT_GREMLIN_SLEEP_A = """
................
................
................
................
....DD.....DD...
...DYD.....DYD..
..DYYD.....DYYD.
.DYYYYD...DYYYYD
.DYYYDYDDYDYyYYD
.DRmDYYYYYDDmYRD
.DRYYYYYYYYYYyRD
..DYYBBYYBBYD...
.DYYYYYYYYYYYBD.
.DYYBBYYBBYYYYD.
.DYYYYyYYYYyYYD.
..DDD......DDD..
"""

ADULT_GREMLIN_SLEEP_B = """
................
................
................
................
................
....DD.....DD...
...DYD.....DYD..
..DYYD.....DYYD.
.DYYYYD...DYYYYD
.DYYYDYDDYDYyYYD
.DRmDYYYYYDDmYRD
.DRYYYYYYYYYYyRD
..DYYBBYYBBYD...
.DYYBBYYBBYYYBD.
.DYYYYyYYYYyYYD.
..DDD......DDD..
"""

PIKACHU_SPRITES = {
    # Teen Neat
    "teen_neat_idle_a.png": (TEEN_NEAT_IDLE_A, PIKACHU_PALETTE),
    "teen_neat_idle_b.png": (TEEN_NEAT_IDLE_B, PIKACHU_PALETTE),
    "teen_neat_walk_a.png": (TEEN_NEAT_WALK_A, PIKACHU_PALETTE),
    "teen_neat_walk_b.png": (TEEN_NEAT_WALK_B, PIKACHU_PALETTE),
    "teen_neat_climb_a.png": (TEEN_NEAT_CLIMB_A, PIKACHU_PALETTE),
    "teen_neat_climb_b.png": (TEEN_NEAT_CLIMB_B, PIKACHU_PALETTE),
    "teen_neat_eat_a.png": (TEEN_NEAT_EAT_A, PIKACHU_PALETTE),
    "teen_neat_eat_b.png": (TEEN_NEAT_EAT_B, PIKACHU_PALETTE),
    "teen_neat_sleep_a.png": (TEEN_NEAT_SLEEP_A, PIKACHU_PALETTE),
    "teen_neat_sleep_b.png": (TEEN_NEAT_SLEEP_B, PIKACHU_PALETTE),
    # Teen Scruffy
    "teen_scruffy_idle_a.png": (TEEN_SCRUFFY_IDLE_A, PIKACHU_PALETTE),
    "teen_scruffy_idle_b.png": (TEEN_SCRUFFY_IDLE_B, PIKACHU_PALETTE),
    "teen_scruffy_walk_a.png": (TEEN_SCRUFFY_WALK_A, PIKACHU_PALETTE),
    "teen_scruffy_walk_b.png": (TEEN_SCRUFFY_WALK_B, PIKACHU_PALETTE),
    "teen_scruffy_climb_a.png": (TEEN_SCRUFFY_CLIMB_A, PIKACHU_PALETTE),
    "teen_scruffy_climb_b.png": (TEEN_SCRUFFY_CLIMB_B, PIKACHU_PALETTE),
    "teen_scruffy_eat_a.png": (TEEN_SCRUFFY_EAT_A, PIKACHU_PALETTE),
    "teen_scruffy_eat_b.png": (TEEN_SCRUFFY_EAT_B, PIKACHU_PALETTE),
    "teen_scruffy_sleep_a.png": (TEEN_SCRUFFY_SLEEP_A, PIKACHU_PALETTE),
    "teen_scruffy_sleep_b.png": (TEEN_SCRUFFY_SLEEP_B, PIKACHU_PALETTE),
    # Adult OK
    "adult_ok_idle_a.png": (ADULT_OK_IDLE_A, PIKACHU_PALETTE),
    "adult_ok_idle_b.png": (ADULT_OK_IDLE_B, PIKACHU_PALETTE),
    "adult_ok_walk_a.png": (ADULT_OK_WALK_A, PIKACHU_PALETTE),
    "adult_ok_walk_b.png": (ADULT_OK_WALK_B, PIKACHU_PALETTE),
    "adult_ok_climb_a.png": (ADULT_OK_CLIMB_A, PIKACHU_PALETTE),
    "adult_ok_climb_b.png": (ADULT_OK_CLIMB_B, PIKACHU_PALETTE),
    "adult_ok_eat_a.png": (ADULT_OK_EAT_A, PIKACHU_PALETTE),
    "adult_ok_eat_b.png": (ADULT_OK_EAT_B, PIKACHU_PALETTE),
    "adult_ok_sleep_a.png": (ADULT_OK_SLEEP_A, PIKACHU_PALETTE),
    "adult_ok_sleep_b.png": (ADULT_OK_SLEEP_B, PIKACHU_PALETTE),
    # Adult Gremlin
    "adult_gremlin_idle_a.png": (ADULT_GREMLIN_IDLE_A, PIKACHU_PALETTE),
    "adult_gremlin_idle_b.png": (ADULT_GREMLIN_IDLE_B, PIKACHU_PALETTE),
    "adult_gremlin_walk_a.png": (ADULT_GREMLIN_WALK_A, PIKACHU_PALETTE),
    "adult_gremlin_walk_b.png": (ADULT_GREMLIN_WALK_B, PIKACHU_PALETTE),
    "adult_gremlin_climb_a.png": (ADULT_GREMLIN_CLIMB_A, PIKACHU_PALETTE),
    "adult_gremlin_climb_b.png": (ADULT_GREMLIN_CLIMB_B, PIKACHU_PALETTE),
    "adult_gremlin_eat_a.png": (ADULT_GREMLIN_EAT_A, PIKACHU_PALETTE),
    "adult_gremlin_eat_b.png": (ADULT_GREMLIN_EAT_B, PIKACHU_PALETTE),
    "adult_gremlin_sleep_a.png": (ADULT_GREMLIN_SLEEP_A, PIKACHU_PALETTE),
    "adult_gremlin_sleep_b.png": (ADULT_GREMLIN_SLEEP_B, PIKACHU_PALETTE),
}
