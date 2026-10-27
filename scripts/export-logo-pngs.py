#!/usr/bin/env python3
"""Regenerate TriNKY PNG exports from the approved SVG logo assets."""
from pathlib import Path
import io
import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "TriNKY_Final_Identity"

def render(svg_name, out_name, width, background=None):
    source = (ASSETS / svg_name).read_bytes()
    png = cairosvg.svg2png(bytestring=source, output_width=width)
    if background:
        image = Image.open(io.BytesIO(png)).convert("RGBA")
        canvas = Image.new("RGBA", image.size, background)
        canvas.alpha_composite(image)
        image = canvas.convert("RGB")
        image.save(ASSETS / out_name, format="PNG", optimize=True)
    else:
        image = Image.open(io.BytesIO(png)).convert("RGBA")
        image.save(ASSETS / out_name, format="PNG", optimize=True)

render("TriNKY_Master.svg", "TriNKY_Master_Transparent_2400.png", 2400)
render("TriNKY_Master.svg", "TriNKY_Master_Transparent_4800.png", 4800)
render("TriNKY_Reversed.svg", "TriNKY_Reversed_Transparent_2400.png", 2400)
render("TriNKY_Symbol.svg", "TriNKY_Symbol_Transparent_1400.png", 1400)
render("TriNKY_Symbol_Reversed.svg", "TriNKY_Symbol_Reversed_Transparent_1400.png", 1400)
render("TriNKY_Master.svg", "TriNKY_Master_On_Chalk.png", 1800, "#F3F2EE")
render("TriNKY_Reversed.svg", "TriNKY_Reversed_On_Plum.png", 1800, "#21112F")
