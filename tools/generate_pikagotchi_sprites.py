#!/usr/bin/env python3
"""
generate_pikagotchi_sprites.py
Pure-Python, zero-dependency pixel-art generator for Pikagotchi (hihry.pikagotchi).
Generates all 68 authentic full-color pet sprites (16x16) and 9 Pokémon room decor props,
conforming to RGBA, palette, grounding, and animation specifications.
Also builds an upscaled nearest-neighbor contact sheet (assets/contact_sheet.png).
"""

import os
import sys
import zlib
import struct
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PLUGIN_DIR = os.path.dirname(SCRIPT_DIR)
SPRITES_DIR = os.path.join(PLUGIN_DIR, "assets", "sprites")
ASSETS_DIR = os.path.join(PLUGIN_DIR, "assets")

os.makedirs(SPRITES_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

# ==============================================================================
# PNG ENCODER (Pure Python RGBA / PNG32)
# ==============================================================================

def make_png_rgba(width, height, pixel_rows):
    """
    Encodes a list of rows (each containing width (r, g, b, a) tuples)
    into a spec-compliant 32-bit RGBA PNG with binary alpha purity.
    """
    raw_idat = bytearray()
    for row in pixel_rows:
        raw_idat.append(0)  # Filter type 0: None
        for r, g, b, a in row:
            # Enforce binary alpha purity (0 or 255)
            alpha = 255 if a > 0 else 0
            raw_idat.extend((r, g, b, alpha))
    
    compressed = zlib.compress(bytes(raw_idat), 9)
    
    def png_chunk(tag, data):
        crc = zlib.crc32(tag + data) & 0xffffffff
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', crc)
    
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0) # 8-bit RGBA
    png_bytes = (
        b'\x89PNG\r\n\x1a\n' +
        png_chunk(b'IHDR', ihdr) +
        png_chunk(b'IDAT', compressed) +
        png_chunk(b'IEND', b'')
    )
    return png_bytes

def parse_ascii_grid(ascii_art, palette):
    """
    Parses a multiline ASCII string into a 2D list of (r, g, b, a) tuples.
    """
    lines = [line.strip() for line in ascii_art.strip().split('\n') if line.strip()]
    rows = []
    for line in lines:
        row = [palette[char] for char in line]
        rows.append(row)
    return len(rows[0]), len(rows), rows

# ==============================================================================
# COLOR PALETTES
# ==============================================================================

# Pokéball Egg Palette
# Required: has_red (r>160, g<100, b<100), has_white (r>200, g>200, b>200), has_dark (r<80, g<80, b<80)
EGG_PALETTE = {
    '.': (0, 0, 0, 0),             # Transparent
    'D': (30, 30, 36, 255),        # Dark band/outline (#1E1E24)
    'R': (238, 21, 21, 255),       # Classic Pokéball red (#EE1515)
    'r': (186, 12, 12, 255),       # Deep red shadow (#BA0C0C)
    'H': (255, 164, 164, 255),     # Specular red highlight (#FFA4A4)
    'W': (255, 255, 255, 255),     # Pure white bottom hemisphere (#FFFFFF)
    's': (203, 213, 225, 255),     # White hemisphere shadow (#CBD5E1)
    'S': (148, 163, 184, 255),     # Deep button/base shadow (#94A3B8)
}

# Baby & Child Pichu Palette
# Required: has_yellow (r>180, g>160, b<160), has_pink (r>180, g<160, b>100), has_dark (r<80, g<80, b<80)
PICHU_PALETTE = {
    '.': (0, 0, 0, 0),             # Transparent
    'Y': (255, 245, 102, 255),     # Pale yellow Pichu body (#FFF566)
    'y': (230, 194, 0, 255),       # Pichu body shadow (#E6C200)
    'P': (255, 140, 160, 255),     # Rosy pink cheek pouches (#FF8CA0)
    'D': (32, 32, 40, 255),        # Charcoal black ears, collar, tail (#202028)
    'W': (255, 255, 255, 255),     # White eye sparkle (#FFFFFF)
    'M': (225, 29, 72, 255),       # Cheerful red mouth (#E11D48)
    'B': (59, 130, 246, 255),      # Oran berry blue (#3B82F6)
    'b': (29, 78, 216, 255),       # Oran berry shadow (#1D4ED8)
    'G': (34, 197, 94, 255),       # Berry leaf green (#22C55E)
}

# Pikachu Palette (teen_neat, teen_scruffy, adult_ok, adult_gremlin)
# Required: has_yellow (r>200, g>170, b<80), has_red (r>170, g<80, b<80), has_dark (r<80, g<80, b<80)
PIKACHU_PALETTE = {
    '.': (0, 0, 0, 0),             # Transparent
    'Y': (255, 222, 0, 255),       # Bright golden yellow (#FFDE00)
    'y': (224, 184, 0, 255),       # Warm yellow shadow (#E0B800)
    'R': (238, 21, 21, 255),       # Red electric cheeks (#EE1515)
    'D': (31, 31, 36, 255),        # Charcoal black ear tips / eyes (#1F1F24)
    'B': (146, 64, 14, 255),       # Brown back stripes & tail base (#92400E)
    'W': (255, 255, 255, 255),     # White eye reflection (#FFFFFF)
    'M': (251, 113, 133, 255),     # Pink inner mouth (#FB7185)
    'm': (225, 29, 72, 255),       # Dark red mouth (#E11D48)
    'K': (255, 255, 153, 255),     # Electric spark crackle (#FFFF99)
    'A': (239, 68, 68, 255),       # Snack apple / berry red (#EF4444)
    'a': (185, 28, 28, 255),       # Snack shadow (#B91C1C)
}

# Raichu Adult Ace Palette
# Required: has_orange (r>180, 80<g<180, b<90), has_cream_or_yellow (r>180, g>170), has_dark (r<100, g<80, b<80)
RAICHU_PALETTE = {
    '.': (0, 0, 0, 0),             # Transparent
    'O': (255, 153, 36, 255),      # Rich warm orange body (#FF9924)
    'o': (217, 115, 0, 255),       # Orange flank shadow (#D97300)
    'C': (255, 240, 208, 255),     # Cream belly (#FFF0D0)
    'c': (245, 218, 175, 255),     # Cream shadow (#F5DAAF)
    'G': (255, 222, 38, 255),      # Golden curled ear spiral & tail blade (#FFDE26)
    'g': (234, 179, 8, 255),       # Golden blade shadow (#EAB308)
    'D': (74, 40, 16, 255),        # Dark chocolate paws and ears (#4A2810)
    'T': (59, 30, 8, 255),         # Slender tail cord brown (#3B1E08)
    'W': (255, 255, 255, 255),     # White eye sparkle (#FFFFFF)
    'M': (225, 29, 72, 255),       # Happy mouth red (#E11D48)
    'B': (59, 130, 246, 255),      # Berry blue (#3B82F6)
}

# ==============================================================================
# MAIN GENERATION PROCESS
# ==============================================================================

def generate_all_sprites():
    # Import sprite modules
    from sprites_egg import EGG_SPRITES
    from sprites_pichu import PICHU_SPRITES
    from sprites_pikachu import PIKACHU_SPRITES
    from sprites_raichu import RAICHU_SPRITES
    from sprites_decor import DECOR_SPRITES

    pet_sprites = {}
    pet_sprites.update(EGG_SPRITES)
    pet_sprites.update(PICHU_SPRITES)
    pet_sprites.update(PIKACHU_SPRITES)
    pet_sprites.update(RAICHU_SPRITES)

    print(f"Generating {len(pet_sprites)} pet sprites...")
    for filename, (ascii_art, palette) in pet_sprites.items():
        w, h, rows = parse_ascii_grid(ascii_art, palette)
        png_bytes = make_png_rgba(w, h, rows)
        out_path = os.path.join(SPRITES_DIR, filename)
        with open(out_path, 'wb') as f:
            f.write(png_bytes)
        # print(f"  Wrote {filename} ({w}x{h}, {len(png_bytes)} bytes)")

    print(f"Generating {len(DECOR_SPRITES)} decor sprites...")
    for filename, gen_fn in DECOR_SPRITES.items():
        w, h, rows = gen_fn()
        png_bytes = make_png_rgba(w, h, rows)
        out_path = os.path.join(SPRITES_DIR, filename)
        with open(out_path, 'wb') as f:
            f.write(png_bytes)
        # print(f"  Wrote {filename} ({w}x{h}, {len(png_bytes)} bytes)")

    print("All sprites generated successfully.")

# ==============================================================================
# CONTACT SHEET GENERATOR
# ==============================================================================

def generate_contact_sheet():
    """
    Builds a beautifully organized, upscaled (6x nearest-neighbor) contact sheet PNG
    containing all 68 pet sprites (organized by form & action) and all 9 decor props,
    with clear section headers, form names, and action labels.
    Uses ImageMagick's convert/montage commands.
    """
    contact_sheet_path = os.path.join(ASSETS_DIR, "contact_sheet.png")
    tmp_dir = os.path.join(SCRIPT_DIR, "contact_tmp")
    os.makedirs(tmp_dir, exist_ok=True)

    # Forms and actions catalog
    forms = [
        ("egg", "Pokéball Egg", ["idle"]),
        ("baby", "Pichu Baby", ["idle", "eat", "sleep"]),
        ("child", "Pichu Child", ["idle", "walk", "climb", "eat", "sleep"]),
        ("teen_neat", "Pikachu Teen (Neat)", ["idle", "walk", "climb", "eat", "sleep"]),
        ("teen_scruffy", "Pikachu Teen (Scruffy)", ["idle", "walk", "climb", "eat", "sleep"]),
        ("adult_ok", "Pikachu Adult (Classic)", ["idle", "walk", "climb", "eat", "sleep"]),
        ("adult_gremlin", "Pikachu Adult (Gremlin)", ["idle", "walk", "climb", "eat", "sleep"]),
        ("adult_ace", "Raichu Adult (Ace Champion)", ["idle", "walk", "climb", "eat", "sleep"]),
    ]

    # Standard 10 action slots for pet animation frames
    all_slots = [
        ("idle", "a"), ("idle", "b"),
        ("walk", "a"), ("walk", "b"),
        ("climb", "a"), ("climb", "b"),
        ("eat", "a"), ("eat", "b"),
        ("sleep", "a"), ("sleep", "b"),
    ]

    scale = 6  # 16x16 becomes 96x96
    
    # 0. Create empty slot card for unsupported actions
    empty_card_path = os.path.join(tmp_dir, "card_empty.png")
    cmd_empty = [
        "magick",
        "-size", "104x124", "xc:#14141A",
        "-bordercolor", "#252530", "-border", "2",
        "-fill", "#475569", "-font", "Adwaita-Sans-Bold", "-pointsize", "18",
        "-gravity", "center",
        "-annotate", "+0+0", "—",
        empty_card_path
    ]
    subprocess.run(cmd_empty, check=True)

    # 1. Create Column Header Row
    col_headers = []
    # Form title column header
    hdr_title = os.path.join(tmp_dir, "hdr_title.png")
    subprocess.run([
        "magick", "-size", "240x36", "xc:#0F172A",
        "-bordercolor", "#334155", "-border", "1",
        "-fill", "#94A3B8", "-font", "Adwaita-Sans-Bold", "-pointsize", "12",
        "-gravity", "center", "-annotate", "+0+0", "EVOLUTION FORM",
        hdr_title
    ], check=True)
    col_headers.append(hdr_title)

    for action, frame in all_slots:
        hdr_path = os.path.join(tmp_dir, f"hdr_{action}_{frame}.png")
        subprocess.run([
            "magick", "-size", "104x36", "xc:#0F172A",
            "-bordercolor", "#334155", "-border", "1",
            "-fill", "#38BDF8", "-font", "Adwaita-Sans-Bold", "-pointsize", "11",
            "-gravity", "center", "-annotate", "+0+0", f"{action}_{frame}",
            hdr_path
        ], check=True)
        col_headers.append(hdr_path)

    header_row_img = os.path.join(tmp_dir, "row_00_header.png")
    subprocess.run(["magick"] + col_headers + ["+append", header_row_img], check=True)

    # 2. Generate upscaled cards for each pet sprite with label
    row_images = [header_row_img]
    for form_id, form_title, actions in forms:
        sprite_cards = []
        for action, frame in all_slots:
            sname = f"{form_id}_{action}_{frame}.png"
            spath = os.path.join(SPRITES_DIR, sname)
            card_path = os.path.join(tmp_dir, f"card_{sname}")
            
            if action in actions and os.path.isfile(spath):
                # Checkered background to clearly showcase transparency
                cmd = [
                    "magick",
                    "-size", "104x104", "pattern:checkerboard",
                    "-fill", "#262626", "-colorize", "70%",
                    "(", spath, "-filter", "point", "-resize", f"{16*scale}x{16*scale}", ")",
                    "-gravity", "center", "-composite",
                    "-bordercolor", "#383838", "-border", "2",
                    "-background", "#181818",
                    "-fill", "#E5E5E5", "-font", "Adwaita-Sans-Bold", "-pointsize", "11",
                    "-gravity", "south", "-splice", "0x20",
                    "-annotate", "+0+4", f"{action}_{frame}",
                    card_path
                ]
                subprocess.run(cmd, check=True)
                sprite_cards.append(card_path)
            else:
                sprite_cards.append(empty_card_path)
                
        # Combine sprites in this row
        row_sprites_img = os.path.join(tmp_dir, f"row_{form_id}_sprites.png")
        subprocess.run(["magick"] + sprite_cards + ["+append", row_sprites_img], check=True)
        
        # Create form title header
        title_img = os.path.join(tmp_dir, f"title_{form_id}.png")
        # Count existing frames for this form
        frame_cnt = sum(1 for a, _ in all_slots if a in actions)
        cmd_title = [
            "magick",
            "-size", "240x124", "xc:#1A1A24",
            "-bordercolor", "#383838", "-border", "2",
            "-fill", "#FACC15", "-font", "Adwaita-Sans-Bold", "-pointsize", "14",
            "-gravity", "center",
            "-annotate", "+0-10", form_title,
            "-fill", "#94A3B8", "-font", "Adwaita-Sans", "-pointsize", "11",
            "-annotate", "+0+15", f"{frame_cnt} frames (16x16)",
            title_img
        ]
        subprocess.run(cmd_title, check=True)
        
        # Combine header and sprites into full row
        row_img = os.path.join(tmp_dir, f"row_{form_id}.png")
        subprocess.run(["magick", title_img, row_sprites_img, "+append", row_img], check=True)
        row_images.append(row_img)

    # 3. Decor Props Section
    decor_row1_items = [
        ("decor_controller.png", "Game Boy Color (16x16)", 4, 180, 150),
        ("decor_sock.png", "Pikachu Sock (16x16)", 4, 180, 150),
        ("decor_ball.png", "Great Ball Toy (32x32)", 3, 200, 150),
        ("decor_mobile.png", "Nursery Mobile (32x32)", 3, 200, 150),
        ("decor_poster.png", "Kanto Stadium Poster (96x48)", 2, 520, 150),
    ]
    decor_row2_items = [
        ("decor_plant_gremlin.png", "Cacnea Pot (16x16)", 4, 220, 180),
        ("decor_plant_ok.png", "Oran Berry Pot (16x16)", 4, 220, 180),
        ("decor_plant_ace.png", "Berry Bonsai Tree (32x32)", 3, 380, 180),
        ("decor_lamp.png", "Incubator Heat Lamp (64x64)", 2, 460, 180),
    ]

    def render_decor_row(items, row_name):
        cards = []
        for dname, dlabel, dscale, cwidth, cheight in items:
            dpath = os.path.join(SPRITES_DIR, dname)
            card_path = os.path.join(tmp_dir, f"card_{dname}")
            cmd = [
                "magick",
                "-size", f"{cwidth}x{cheight}", "pattern:checkerboard",
                "-fill", "#262626", "-colorize", "70%",
                "(", dpath, "-filter", "point", "-resize", f"{dscale*100}%", ")",
                "-gravity", "center", "-composite",
                "-bordercolor", "#383838", "-border", "2",
                "-background", "#14141E",
                "-fill", "#E5E5E5", "-font", "Adwaita-Sans-Bold", "-pointsize", "11",
                "-gravity", "south", "-splice", "0x24",
                "-annotate", "+0+5", dlabel,
                card_path
            ]
            subprocess.run(cmd, check=True)
            cards.append(card_path)
        out_row = os.path.join(tmp_dir, f"{row_name}.png")
        subprocess.run(["magick"] + cards + ["+append", out_row], check=True)
        return out_row

    row_d1 = render_decor_row(decor_row1_items, "decor_row1")
    row_d2 = render_decor_row(decor_row2_items, "decor_row2")

    # Center decor rows to 1280 width
    sheet_width = 1280
    row_d1_centered = os.path.join(tmp_dir, "row_d1_c.png")
    subprocess.run(["magick", row_d1, "-gravity", "center", "-background", "#0F0F14", "-extent", f"{sheet_width}x174", row_d1_centered], check=True)
    row_d2_centered = os.path.join(tmp_dir, "row_d2_c.png")
    subprocess.run(["magick", row_d2, "-gravity", "center", "-background", "#0F0F14", "-extent", f"{sheet_width}x204", row_d2_centered], check=True)

    decor_combined = os.path.join(tmp_dir, "decor_combined.png")
    subprocess.run(["magick", row_d1_centered, "-splice", "0x12", row_d2_centered, "-append", decor_combined], check=True)

    # Decor title header
    decor_title_img = os.path.join(tmp_dir, "title_decor.png")
    cmd_dtitle = [
        "magick",
        "-size", f"{sheet_width}x46", "xc:#1A1A24",
        "-bordercolor", "#383838", "-border", "2",
        "-fill", "#FACC15", "-font", "Adwaita-Sans-Bold", "-pointsize", "15",
        "-gravity", "center",
        "-annotate", "+0+0", "Pokémon Room Decor Props (9 Authentic Full-Color Multi-Layer Furnishings)",
        decor_title_img
    ]
    subprocess.run(cmd_dtitle, check=True)

    # Main contact sheet banner
    banner_img = os.path.join(tmp_dir, "banner.png")
    cmd_banner = [
        "magick",
        "-size", f"{sheet_width}x76", "xc:#0F172A",
        "-bordercolor", "#FACC15", "-border", "2",
        "-fill", "#FACC15", "-font", "Adwaita-Sans-Bold", "-pointsize", "20",
        "-gravity", "center",
        "-annotate", "+0-10", "Pikagotchi Sprite Suite & Decor Contact Sheet",
        "-fill", "#94A3B8", "-font", "Adwaita-Sans", "-pointsize", "12",
        "-annotate", "+0+16", "hihry.pikagotchi (Pokéball → Pichu → Pikachu → Raichu Evolution Chart | 68 Pet Sprites + 9 Decor Props)",
        banner_img
    ]
    subprocess.run(cmd_banner, check=True)

    # Combine everything vertically
    print("Assembling final contact sheet...")
    final_components = [banner_img]
    for r in row_images:
        final_components.extend(["-splice", "0x8", r])
    final_components.extend(["-splice", "0x14", decor_title_img, "-splice", "0x10", decor_combined])
    
    cmd_final = [
        "magick",
        "-background", "#0F0F14",
    ] + final_components + [
        "-background", "#0F0F14",
        "-append",
        "-bordercolor", "#1E1E24", "-border", "16",
        contact_sheet_path
    ]
    subprocess.run(cmd_final, check=True)
    print(f"Contact sheet saved to: {contact_sheet_path}")

    # Clean up tmp files
    for f in os.listdir(tmp_dir):
        os.remove(os.path.join(tmp_dir, f))
    os.rmdir(tmp_dir)

if __name__ == '__main__':
    generate_all_sprites()
    generate_contact_sheet()
