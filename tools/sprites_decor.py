"""
sprites_decor.py
Defines the 9 Pokémon room decor props:
- decor_lamp.png (64x64): Amber incubator heat lamp preserving beam opening [1, 13, 14, 25]
- decor_mobile.png (32x32): Nursery mobile with Pokéball, Great Ball, Staryu, Togepi
- decor_ball.png (32x32): 3D shaded Great Ball toy with crimson stripes
- decor_poster.png (96x48): Kanto Championship poster with Pikachu silhouette and lightning
- decor_controller.png (16x16): Yellow Game Boy console with olive LCD screen
- decor_sock.png (16x16): Pikachu novelty striped sock with brown stripes and red spot
- decor_plant_gremlin.png (16x16): Spiky potted Cacnea / desert blossom cactus in terracotta pot
- decor_plant_ok.png (16x16): Friendly Oran berry sapling with blue berry and green leaves
- decor_plant_ace.png (32x32): Sitrus/Tamato berry bonsai tree in porcelain planter
"""

# Palette for 16x16 small decor props
DECOR_CONTROLLER_PALETTE = {
    '.': (0, 0, 0, 0),
    'Y': (250, 204, 21, 255),  # Yellow chassis (#FACC15)
    'y': (202, 138, 4, 255),   # Yellow shadow (#CA8A04)
    'D': (30, 41, 59, 255),    # Screen bezel / D-pad (#1E293B)
    'G': (132, 204, 22, 255),  # LCD Olive green (#84CC16)
    'g': (77, 124, 15, 255),   # LCD shadow / pixel Pikachu (#4D7C0F)
    'R': (239, 68, 68, 255),   # Power LED red (#EF4444)
    'M': (219, 39, 119, 255),  # Magenta A/B buttons (#DB2777)
    'S': (100, 116, 139, 255), # Select/Start slate (#64748B)
}

CONTROLLER_ASCII = """
................
................
...DDDDDDDDDD...
..DYYYYYYYYYYD..
..DYDDDDDDDDYD..
..DYDGGGGGGGYD..
..DYDRGggGGGYD..
..DYDGGGGGGGYD..
..DYDDDDDDDDYD..
..DYDDy..MyMYD..
..DYYDy.MyMYDY..
..DYDDy..y.yDY..
..DYYDSS.SSDYD..
..DYYYYYYYYYYD..
...DDDDDDDDDD...
................
"""

DECOR_SOCK_PALETTE = {
    '.': (0, 0, 0, 0),
    'D': (30, 41, 59, 255),    # Cuff/heel/toe charcoal (#1E293B)
    'Y': (250, 204, 21, 255),  # Pikachu yellow (#FACC15)
    'y': (202, 138, 4, 255),   # Yellow shadow (#CA8A04)
    'B': (120, 53, 15, 255),   # Brown stripes (#78350F)
    'R': (238, 21, 21, 255),   # Red electric cheek dot (#EE1515)
    'W': (255, 255, 255, 255), # White knit highlight (#FFFFFF)
}

SOCK_ASCII = """
................
................
........DDDD....
........DWWYD...
........DYYYD...
.......DBBBYD...
......DYYYRYD...
.....DYYRRYYD...
....DBBBYYYYD...
...DYYYYYYyD....
..DYYYYYyyD.....
..DYYyyDDDD.....
...DDDDD........
................
................
................
"""

DECOR_PLANT_GREMLIN_PALETTE = {
    '.': (0, 0, 0, 0),
    'Y': (250, 204, 21, 255),  # Desert blossom yellow (#FACC15)
    'O': (234, 88, 12, 255),   # Blossom center orange (#EA580C)
    'G': (34, 197, 94, 255),   # Cactus light green (#22C55E)
    'g': (21, 128, 61, 255),   # Cactus shadow green (#15803D)
    'D': (5, 46, 22, 255),     # Cactus dark thorns (#052E16)
    'T': (234, 88, 12, 255),   # Terracotta pot rim (#EA580C)
    't': (154, 52, 18, 255),   # Terracotta pot body (#9A3412)
    'S': (69, 26, 3, 255),     # Soil / pot shadow (#451A03)
}

PLANT_GREMLIN_ASCII = """
................
.......YY.......
......YOOY......
...D..GGgg..D...
...Dg.GggG.gD...
...DggGggGggD...
...DGGGGGGggD...
...DggggggggD...
....GggggggD....
......SSSS......
....TTTTTTTT....
....TTTTTTTT....
....DttttttD....
.....DttttD.....
.....DttttD.....
......DDDD......
"""

DECOR_PLANT_OK_PALETTE = {
    '.': (0, 0, 0, 0),
    'B': (37, 99, 235, 255),   # Oran berry blue (#2563EB)
    'b': (29, 78, 216, 255),   # Berry shadow (#1D4ED8)
    'W': (255, 255, 255, 255), # Specular highlight (#FFFFFF)
    'w': (203, 213, 225, 255), # Soft highlight (#CBD5E1)
    'G': (34, 197, 94, 255),   # Sapling leaf green (#22C55E)
    'g': (21, 128, 61, 255),   # Leaf shadow green (#15803D)
    'C': (56, 189, 248, 255),  # Ceramic pot rim sky blue (#38BDF8)
    'c': (3, 105, 161, 255),   # Ceramic pot body (#0369A1)
    'S': (69, 26, 3, 255),     # Potting soil (#451A03)
    'D': (15, 23, 42, 255),    # Outline dark (#0F172A)
}

PLANT_OK_ASCII = """
................
...........bB...
...GG.....BBWb..
..GGGG...GBBwb..
.GGGggG.GGGBb...
.GgggGgggG..G...
...gg..Gg..GGG..
..g.gg.Gg.GGggg.
.g..gg.gS.gg..g.
.g...SSSSSS.....
......SSSS......
...CCCCCCCCCC...
...DccccccccD...
...DccccccccD...
....DccccccD....
.....DDDDDD.....
"""

def generate_decor_ball():
    """Generates 32x32 3D shaded Great Ball toy."""
    w, h = 32, 32
    rows = [[(0, 0, 0, 0) for _ in range(w)] for _ in range(h)]
    cx, cy, r = 16.0, 16.5, 10.5
    
    # Shadow under ball
    for y in range(26, 30):
        for x in range(7, 25):
            dx = (x - 16.0) / 8.5
            dy = (y - 27.5) / 2.0
            if dx*dx + dy*dy <= 1.0:
                rows[y][x] = (30, 41, 59, 255)
                
    for y in range(h):
        for x in range(w):
            dx = x - cx
            dy = y - cy
            dist2 = dx*dx + dy*dy
            if dist2 <= r*r:
                # Inside ball
                dist = dist2**0.5
                nx = dx / r
                ny = dy / r
                # Diffuse light from top-left (lx=-0.5, ly=-0.7, lz=0.5)
                nz = max(0.0, (1.0 - nx*nx - ny*ny))**0.5
                diff = max(0.0, -0.4*nx - 0.6*ny + 0.7*nz)
                
                # Check equator band
                if abs(dy) <= 1.2:
                    # Central dark band
                    if abs(dx) <= 3.2 and abs(dy) <= 3.2:
                        # Center button
                        b_dist = (dx*dx + dy*dy)**0.5
                        if b_dist <= 1.5:
                            # White button center
                            rows[y][x] = (255, 255, 255, 255) if (dx < 0.2 and dy < 0.2) else (203, 213, 225, 255)
                        elif b_dist <= 2.6:
                            # Inner silver ring
                            rows[y][x] = (148, 163, 184, 255)
                        else:
                            # Outer black ring
                            rows[y][x] = (30, 30, 36, 255)
                    else:
                        rows[y][x] = (30, 30, 36, 255)
                elif dy < -1.2:
                    # Top dome: Great Ball Cobalt Blue with Crimson Stripes
                    # Two red stripes on sides
                    is_red_stripe = (abs(dx - 4.5) <= 1.5 or abs(dx + 4.5) <= 1.5) and (dy < -2.0)
                    if is_red_stripe:
                        if diff > 0.8:
                            rows[y][x] = (239, 68, 68, 255)
                        elif diff > 0.4:
                            rows[y][x] = (220, 38, 38, 255)
                        else:
                            rows[y][x] = (185, 28, 28, 255)
                    else:
                        # Blue dome
                        if diff > 0.9:
                            rows[y][x] = (96, 165, 250, 255)
                        elif diff > 0.6:
                            rows[y][x] = (37, 99, 235, 255)
                        elif diff > 0.3:
                            rows[y][x] = (29, 78, 216, 255)
                        else:
                            rows[y][x] = (30, 58, 138, 255)
                else:
                    # Bottom dome: Pure white with cool gray shading
                    if diff > 0.7:
                        rows[y][x] = (255, 255, 255, 255)
                    elif diff > 0.4:
                        rows[y][x] = (226, 232, 240, 255)
                    elif diff > 0.2:
                        rows[y][x] = (203, 213, 225, 255)
                    else:
                        rows[y][x] = (148, 163, 184, 255)
                # Outer perimeter edge
                if dist >= r - 0.7:
                    rows[y][x] = (30, 30, 36, 255)
                    
    return w, h, rows

def generate_decor_mobile():
    """Generates 32x32 nursery mobile with mini Pokéball, Great Ball, Staryu, Togepi."""
    w, h = 32, 32
    rows = [[(0, 0, 0, 0) for _ in range(w)] for _ in range(h)]
    
    # Top hanger cord
    for y in range(0, 7):
        rows[y][15] = (148, 163, 184, 255)
        rows[y][16] = (100, 116, 139, 255)
        
    # Main arch / crossbars
    for x in range(4, 28):
        rows[7][x] = (203, 213, 225, 255)
        rows[8][x] = (100, 116, 139, 255)
        
    # Vertical hanging strings to charms
    # String 1 to Pokéball (x=6, y=9..15)
    for y in range(9, 16):
        rows[y][6] = (148, 163, 184, 255)
    # String 2 to Staryu (x=12, y=9..19)
    for y in range(9, 20):
        rows[y][12] = (148, 163, 184, 255)
    # String 3 to Togepi (x=19, y=9..14)
    for y in range(9, 15):
        rows[y][19] = (148, 163, 184, 255)
    # String 4 to Great Ball (x=25, y=9..18)
    for y in range(9, 19):
        rows[y][25] = (148, 163, 184, 255)
        
    # Charm 1: Mini Pokéball at x=4..8, y=16..20
    ball1 = [
        " DDD ",
        "DHRRD",
        "DDWDD",
        "DWWSD",
        " DDD "
    ]
    pal1 = {
        ' ': (0,0,0,0),
        'D': (30,30,36,255),
        'R': (238,21,21,255),
        'H': (255,164,164,255),
        'W': (255,255,255,255),
        's': (203,213,225,255),
        'S': (148,163,184,255),
    }
    for py, l in enumerate(ball1):
        for px, ch in enumerate(l):
            if ch != ' ':
                rows[16+py][4+px] = pal1[ch]
                
    # Charm 2: Staryu Star at x=10..15, y=20..25
    star = [
        "  GG  ",
        " GDDG ",
        "GGMRGG",
        " GDDG ",
        " G  G "
    ]
    pal2 = {
        ' ': (0,0,0,0),
        'G': (250,204,21,255),  # Gold
        'D': (202,138,4,255),   # Dark gold
        'M': (255,255,255,255), # Ruby shine
        'R': (220,38,38,255),   # Red core
    }
    for py, l in enumerate(star):
        for px, ch in enumerate(l):
            if ch != ' ':
                rows[20+py][10+px] = pal2[ch]
                
    # Charm 3: Togepi charm at x=17..22, y=15..20
    togepi = [
        "  CC  ",
        " CWWbC",
        " CRWBC",
        " CWWWC",
        "  CC  "
    ]
    pal3 = {
        ' ': (0,0,0,0),
        'C': (217,119,6,255),   # Border
        'W': (254,243,199,255), # Cream
        'R': (239,68,68,255),   # Red triangle
        'B': (37,99,235,255),   # Blue triangle
        'b': (59,130,246,255),  # Light blue
    }
    for py, l in enumerate(togepi):
        for px, ch in enumerate(l):
            if ch != ' ':
                rows[15+py][17+px] = pal3[ch]
                
    # Charm 4: Great Ball at x=23..27, y=19..23
    ball2 = [
        " DDD ",
        "DBRBD",
        "DDWDD",
        "DWWSD",
        " DDD "
    ]
    pal4 = {
        ' ': (0,0,0,0),
        'D': (30,30,36,255),
        'B': (37,99,235,255),   # Cobalt blue
        'R': (220,38,38,255),   # Crimson stripe
        'W': (255,255,255,255),
        's': (203,213,225,255),
        'S': (148,163,184,255),
    }
    for py, l in enumerate(ball2):
        for px, ch in enumerate(l):
            if ch != ' ':
                rows[19+py][23+px] = pal4[ch]
                
    return w, h, rows

def generate_decor_lamp():
    """
    Generates 64x64 incubator heat lamp.
    Preserves exact beam opening edge at [1, 13, 14, 25] and illuminates columns [1, 13, 14, 25].
    Features amber incubator hood, steel articulated arm, slate base, glowing radiant bulb.
    """
    w, h = 64, 64
    rows = [[(0, 0, 0, 0) for _ in range(w)] for _ in range(h)]
    
    # 1. Base on shelf at y=56..63, x=12..35
    for y in range(56, 64):
        for x in range(12, 35):
            if y == 56:
                rows[y][x] = (71, 85, 105, 255) # Top highlight
            elif y == 63 or x in (12, 34):
                rows[y][x] = (15, 23, 42, 255)  # Shadow edge
            else:
                rows[y][x] = (30, 41, 59, 255)  # Heavy slate base
    # Power switch and indicator on base
    rows[58][15] = (239, 68, 68, 255) # Red power switch
    rows[59][15] = (239, 68, 68, 255)
    rows[58][18] = (34, 197, 94, 255) # Green heat LED
    
    # 2. Articulated Steel Arm (Lower arm and Upper arm)
    # Lower arm going up from (x=24, y=55) to elbow at (x=29, y=26)
    for y in range(26, 56):
        t = (y - 26) / 30.0
        x_mid = 29.0 - 5.0 * t
        xi = int(round(x_mid))
        rows[y][xi-1] = (100, 116, 139, 255)
        rows[y][xi] = (148, 163, 184, 255)
        rows[y][xi+1] = (51, 65, 85, 255)
        
    # Elbow joint at (x=27..31, y=23..27)
    for y in range(23, 28):
        for x in range(27, 32):
            rows[y][x] = (71, 85, 105, 255)
    rows[25][29] = (203, 213, 225, 255)
    
    # Upper arm reaching from elbow (x=28, y=24) up-left to hood socket (x=19, y=6)
    for y in range(6, 25):
        t = (y - 6) / 18.0
        x_mid = 19.0 + 9.0 * t
        xi = int(round(x_mid))
        rows[y][xi-1] = (148, 163, 184, 255)
        rows[y][xi] = (71, 85, 105, 255)
        
    # Socket pivot at (x=17..21, y=4..7)
    for y in range(4, 8):
        for x in range(17, 22):
            rows[y][x] = (100, 116, 139, 255)
            
    # 3. Incubator Hood / Shade
    # Must preserve shade opening diagonal from (x1=1, y1=13) to (x2=14, y2=25)!
    # Fill the hood polygon and shade interior
    for y in range(3, 27):
        for x in range(0, 24):
            # Check if point is inside hood volume
            # Opening line: from (1, 13) to (14, 25)
            # Line equation: (y - 13) = (12/13) * (x - 1)  => x_edge = 1 + (13/12)*(y - 13)
            # Top curve from (1, 10) to (19, 4)
            # Right edge from (19, 4) down to (14, 25)
            if y >= 12 and y <= 26:
                x_rim = 1.0 + (13.0 / 12.0) * (y - 13.0)
                if abs(x - x_rim) <= 1.2:
                    rows[y][x] = (180, 83, 9, 255) # Hood outer bronze rim
                elif x > x_rim and x <= 22:
                    # Inside the hood opening or bulb reflection
                    dy_bulb = y - 16.0
                    dx_bulb = x - 8.0
                    if dx_bulb*dx_bulb + dy_bulb*dy_bulb <= 9.0:
                        rows[y][x] = (255, 255, 255, 255) # Radiant bulb center
                    elif dx_bulb*dx_bulb + dy_bulb*dy_bulb <= 20.0:
                        rows[y][x] = (254, 240, 138, 255) # Bulb glow
                    else:
                        rows[y][x] = (245, 158, 11, 255) # Amber reflector
            elif y >= 8 and y < 12:
                # Top dome of hood
                if x >= 0 and x <= 20:
                    if x == 0 or x == 20 or y == 8:
                        rows[y][x] = (120, 53, 15, 255) # Outline
                    elif y <= 9:
                        rows[y][x] = (251, 191, 36, 255) # Highlight
                    else:
                        rows[y][x] = (217, 119, 6, 255)  # Amber metal
            elif y >= 4 and y < 8:
                if x >= 12 and x <= 19:
                    rows[y][x] = (180, 83, 9, 255)
                    
    # Ensure exact beam opening pixels at (1, 13) and (14, 25) are non-transparent!
    rows[13][1] = (180, 83, 9, 255)
    rows[25][14] = (180, 83, 9, 255)
    # Ensure columns 1, 13, 14, 25 all have non-transparent pixels
    assert rows[13][1][3] > 0
    assert any(rows[y][13][3] > 0 for y in range(h))
    assert any(rows[y][14][3] > 0 for y in range(h))
    assert any(rows[y][25][3] > 0 for y in range(h))
    
    return w, h, rows

def generate_decor_poster():
    """Generates 96x48 Kanto Championship wall poster with Pikachu silhouette and lightning."""
    w, h = 96, 48
    rows = [[(0, 0, 0, 0) for _ in range(w)] for _ in range(h)]
    
    # 1. Gold poster frame (x=2..93, y=2..45)
    for y in range(2, 46):
        for x in range(2, 94):
            if y in (2, 45) or x in (2, 93):
                rows[y][x] = (180, 83, 9, 255)   # Outer dark gold border
            elif y in (3, 44) or x in (3, 92):
                rows[y][x] = (250, 204, 21, 255)  # Bright gold inner frame
            else:
                # Arena navy background
                rows[y][x] = (15, 23, 42, 255)
                
    # 2. Header banner at y=5..11: "KANTO CHAMPIONSHIP"
    # Stylized banner ribbon
    for y in range(5, 12):
        for x in range(12, 84):
            if y in (5, 11):
                rows[y][x] = (202, 138, 4, 255)
            else:
                rows[y][x] = (30, 41, 59, 255)
    # Header gold lettering blocks
    for x in range(16, 80, 3):
        rows[7][x] = (250, 204, 21, 255)
        rows[8][x] = (250, 204, 21, 255)
        rows[9][x] = (250, 204, 21, 255)
        
    # 3. Dramatic Lightning Bolts cutting through arena
    lightning_coords = [
        (20, 14), (22, 16), (21, 18), (25, 22), (24, 24), (27, 28),
        (75, 14), (73, 17), (76, 20), (72, 25), (74, 29),
        (35, 15), (37, 18), (34, 21), (39, 26)
    ]
    for lx, ly in lightning_coords:
        for ox in (-1, 0, 1):
            if 0 <= lx+ox < w:
                rows[ly][lx+ox] = (254, 240, 138, 255) # Light yellow
        rows[ly][lx] = (255, 255, 255, 255)          # White core
        
    # 4. Center Pikachu Running Silhouette (x=40..60, y=16..34)
    # Head & Body
    for y in range(18, 32):
        for x in range(42, 56):
            dx = (x - 49.0) / 6.0
            dy = (y - 25.0) / 6.0
            if dx*dx + dy*dy <= 1.0:
                rows[y][x] = (250, 204, 21, 255) # Golden yellow body
    # Black ear tips
    rows[14][43] = (30, 30, 36, 255)
    rows[15][44] = (30, 30, 36, 255)
    rows[16][45] = (250, 204, 21, 255)
    rows[14][55] = (30, 30, 36, 255)
    rows[15][54] = (30, 30, 36, 255)
    rows[16][53] = (250, 204, 21, 255)
    # Red cheek
    rows[25][44] = (239, 68, 68, 255)
    rows[26][44] = (239, 68, 68, 255)
    rows[25][54] = (239, 68, 68, 255)
    rows[26][54] = (239, 68, 68, 255)
    # White eye
    rows[23][46] = (255, 255, 255, 255)
    rows[23][52] = (255, 255, 255, 255)
    # Lightning Tail
    tail_pts = [(56, 26), (58, 24), (57, 22), (61, 20), (63, 17), (62, 15), (66, 13)]
    for tx, ty in tail_pts:
        rows[ty][tx] = (250, 204, 21, 255)
        rows[ty][tx+1] = (254, 240, 138, 255)
        
    # 5. Kanto Gym Badges row at y=37..41
    badge_colors = [
        (148, 163, 184, 255), # Boulder (Gray)
        (56, 189, 248, 255),  # Cascade (Blue)
        (234, 179, 8, 255),   # Thunder (Gold)
        (34, 197, 94, 255),   # Rainbow (Green)
        (236, 72, 153, 255),  # Soul (Pink)
        (249, 115, 22, 255),  # Marsh (Orange)
        (239, 68, 68, 255),   # Volcano (Red)
        (21, 128, 61, 255),   # Earth (Dark Green)
    ]
    for idx, col in enumerate(badge_colors):
        bx = 18 + idx * 8
        for by in range(37, 42):
            for bdx in range(4):
                if by in (37, 41) and bdx in (0, 3):
                    continue
                rows[by][bx + bdx] = col
                
    return w, h, rows

def generate_decor_plant_ace():
    """Generates 32x32 Sitrus/Tamato berry bonsai tree in porcelain planter."""
    w, h = 32, 32
    rows = [[(0, 0, 0, 0) for _ in range(w)] for _ in range(h)]
    
    # 1. Porcelain planter at y=23..30, x=6..25
    for y in range(23, 31):
        for x in range(6, 26):
            if y == 23:
                # Gold planter rim
                rows[y][x] = (245, 158, 11, 255)
            elif y in (24, 29) or x in (6, 25):
                rows[y][x] = (203, 213, 225, 255) # Planter shadow edge
            elif y == 30:
                # Planter feet at x=8..10 and x=21..23
                if x in (8, 9, 10, 21, 22, 23):
                    rows[y][x] = (100, 116, 139, 255)
            else:
                # White porcelain with cobalt blue wave design
                if (x + y) % 4 == 0:
                    rows[y][x] = (37, 99, 235, 255) # Cobalt pattern
                else:
                    rows[y][x] = (248, 250, 252, 255) # White porcelain
    # Potting soil
    for x in range(8, 24):
        rows[22][x] = (69, 26, 3, 255)
        
    # 2. Gnarled bonsai trunk and branches
    # Main trunk
    for y in range(15, 23):
        rows[y][14] = (120, 53, 15, 255)
        rows[y][15] = (69, 26, 3, 255)
        rows[y][16] = (120, 53, 15, 255)
    # Left branch reaching to (8, 11)
    for t in range(7):
        bx = 14 - t
        by = 17 - int(t * 0.8)
        rows[by][bx] = (120, 53, 15, 255)
        rows[by+1][bx] = (69, 26, 3, 255)
    # Right branch reaching to (22, 10)
    for t in range(7):
        bx = 16 + t
        by = 16 - int(t * 0.9)
        rows[by][bx] = (120, 53, 15, 255)
        rows[by+1][bx] = (69, 26, 3, 255)
        
    # 3. Dense foliage canopies (left and right)
    # Left canopy centered at (8, 8), r=6
    for y in range(2, 14):
        for x in range(2, 15):
            dx = (x - 8.0) / 5.5
            dy = (y - 7.5) / 4.5
            if dx*dx + dy*dy <= 1.0:
                if dy < -0.3:
                    rows[y][x] = (34, 197, 94, 255)  # Light leaf green
                elif dy < 0.3:
                    rows[y][x] = (21, 128, 61, 255)  # Mid leaf green
                else:
                    rows[y][x] = (20, 83, 45, 255)   # Shadow green
                    
    # Right canopy centered at (22, 7), r=6.5
    for y in range(2, 14):
        for x in range(15, 29):
            dx = (x - 22.0) / 6.0
            dy = (y - 7.0) / 4.5
            if dx*dx + dy*dy <= 1.0:
                if dy < -0.3:
                    rows[y][x] = (34, 197, 94, 255)
                elif dy < 0.3:
                    rows[y][x] = (21, 128, 61, 255)
                else:
                    rows[y][x] = (20, 83, 45, 255)
                    
    # 4. Berries hanging from canopies
    # Golden Sitrus berries (Yellow)
    sitrus_pts = [(6, 10), (10, 12), (24, 10), (19, 8)]
    for sx, sy in sitrus_pts:
        rows[sy][sx] = (250, 204, 21, 255)
        rows[sy+1][sx] = (202, 138, 4, 255)
    # Crimson Tamato berries (Red)
    tamato_pts = [(8, 5), (21, 12), (26, 7)]
    for tx, ty in tamato_pts:
        rows[ty][tx] = (239, 68, 68, 255)
        rows[ty+1][tx] = (185, 28, 28, 255)
        
    return w, h, rows

DECOR_SPRITES = {
    "decor_controller.png": lambda: (16, 16, [
        [DECOR_CONTROLLER_PALETTE[ch] for ch in line.strip()]
        for line in CONTROLLER_ASCII.strip().split('\n') if line.strip()
    ]),
    "decor_sock.png": lambda: (16, 16, [
        [DECOR_SOCK_PALETTE[ch] for ch in line.strip()]
        for line in SOCK_ASCII.strip().split('\n') if line.strip()
    ]),
    "decor_plant_gremlin.png": lambda: (16, 16, [
        [DECOR_PLANT_GREMLIN_PALETTE[ch] for ch in line.strip()]
        for line in PLANT_GREMLIN_ASCII.strip().split('\n') if line.strip()
    ]),
    "decor_plant_ok.png": lambda: (16, 16, [
        [DECOR_PLANT_OK_PALETTE[ch] for ch in line.strip()]
        for line in PLANT_OK_ASCII.strip().split('\n') if line.strip()
    ]),
    "decor_ball.png": generate_decor_ball,
    "decor_mobile.png": generate_decor_mobile,
    "decor_lamp.png": generate_decor_lamp,
    "decor_poster.png": generate_decor_poster,
    "decor_plant_ace.png": generate_decor_plant_ace,
}
