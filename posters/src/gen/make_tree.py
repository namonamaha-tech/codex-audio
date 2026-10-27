"""Procedurally draw the BG 2.41 metaphor as a black & white SVG.

Left: the irresolute mind, a bush of many branches with no trunk (bahu-shakha).
Right: the resolute mind, roots -> one strong trunk -> a crown of branches
(Velumani's sequence: resolve, focus on one thing, then diversify).

Writes posters/src/art/tree.svg. Deterministic (fixed seeds).
"""
import math
import random
from pathlib import Path

from opensimplex import OpenSimplex

W, H, GROUND = 1000, 600, 488
OUT = Path(__file__).resolve().parent.parent / "art" / "tree.svg"
noise = OpenSimplex(seed=41)
parts = []


def seg(x1, y1, x2, y2, w, color="#000"):
    parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{w:.2f}" stroke-linecap="round"/>')


def halftone(cx, cy, r, step=13, rmax=4.6):
    """True variable-radius halftone disc (dots shrink towards the edge)."""
    out = []
    for gy in range(int(cy - r), int(cy + r) + 1, step):
        for gx in range(int(cx - r), int(cx + r) + 1, step):
            d = math.hypot(gx - cx, gy - cy) / r
            if d < 1 and gy < GROUND - 4:
                rad = rmax * (1 - d) ** 0.8
                if rad > .45:
                    out.append(f'<circle cx="{gx}" cy="{gy}" r="{rad:.2f}"/>')
    return '<g fill="#000" opacity=".5">' + "".join(out) + "</g>"


# --- resolute tree -------------------------------------------------------
rng = random.Random(241)
TX = 560
leaves = []


def crown(x, y, ang, length, width, depth):
    jitter = noise.noise2(x * .01, y * .01) * .12
    a = ang + jitter
    x2, y2 = x + length * math.cos(a), y - length * math.sin(a)
    seg(x, y, x2, y2, width)
    if depth == 0:
        leaves.append((x2, y2))
        return
    spread = math.radians(rng.uniform(24, 36))
    kids = 3 if depth in (6, 4) and rng.random() < .35 else 2
    angles = [a - spread, a + spread] if kids == 2 else [a - spread * 1.2, a + rng.uniform(-.1, .1), a + spread * 1.2]
    for na in angles:
        crown(x2, y2, na, length * rng.uniform(.72, .8), max(width * .66, 1.1), depth - 1)


def roots(x, y, ang, length, width, depth):
    a = ang + noise.noise2(x * .02, y * .02) * .3
    x2, y2 = x + length * math.cos(a), y - length * math.sin(a)
    y2 = max(y2, GROUND + 6)
    seg(x, y, x2, y2, width)
    if depth == 0:
        return
    for s in (-1, 1):
        roots(x2, y2, a + s * math.radians(rng.uniform(22, 38)), length * .7, max(width * .6, .9), depth - 1)


# halo behind the crown
parts.append(halftone(TX, 170, 215))

# trunk: a tapered, gently swaying polygon
TOP = 262
left, right = [], []
for i in range(21):
    t = i / 20
    y = GROUND - (GROUND - TOP) * t
    sway = noise.noise2(t * 2.2, 3.1) * 6
    half = 30 - 16 * t + (6 * (1 - t) ** 6)  # flare at the base
    left.append((TX + sway - half, y))
    right.append((TX + sway + half, y))
pts = left + right[::-1]
parts.append('<path d="M' + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + ' Z" fill="#000"/>')
# bark lines (white) give the trunk volume
for off, h in ((-9, 70), (3, 120), (12, 54)):
    parts.append(f'<path d="M{TX+off} {GROUND-10} Q {TX+off-3} {GROUND-h*.6} {TX+off*0.7} {GROUND-h}" stroke="#fff" stroke-width="1.8" fill="none" stroke-linecap="round"/>')

top_x = TX + noise.noise2(2.2, 3.1) * 6
crown(top_x, TOP + 10, math.radians(90), 70, 26, 8)
for lx, ly in leaves[::2]:
    r = rng.uniform(2.6, 4.4)
    parts.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="{r:.1f}" fill="#000"/>')

# roots below ground
for a in (-70, -90, -110, -55, -125):
    roots(TX, GROUND + 4, math.radians(a), 34, 9, 4)

# --- irresolute bush ------------------------------------------------------
rng2 = random.Random(7)
BX = 150
tips = []


def twig(x, y, ang, length, width, depth):
    a = ang + rng2.uniform(-.35, .35)
    x2, y2 = x + length * math.cos(a), min(y - length * math.sin(a), GROUND - 2)
    seg(x, y, x2, y2, width)
    if depth == 0 or y2 < 300:
        tips.append((x2, y2))
        return
    for _ in range(rng2.choice((2, 2, 3))):
        twig(x2, y2, a + rng2.uniform(-.9, .9), length * rng2.uniform(.55, .85), max(width * .7, .9), depth - 1)


for i in range(15):
    ang = math.radians(28 + 124 * i / 14 + rng2.uniform(-6, 6))
    twig(BX + rng2.uniform(-18, 18), GROUND, ang, rng2.uniform(26, 44), 3.4, 4)
for x, y in tips[::2]:
    parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="#fff" stroke="#000" stroke-width="1.6"/>')

# --- ground ------------------------------------------------------------
parts.insert(0, f'<rect x="0" y="{GROUND}" width="{W}" height="{H-GROUND}" fill="#fff"/>')
ground = [f'<line x1="0" y1="{GROUND}" x2="{W}" y2="{GROUND}" stroke="#000" stroke-width="3.5"/>']
for i in range(0, W, 9):  # soil hatching
    ground.append(f'<line x1="{i}" y1="{GROUND+9}" x2="{i-7}" y2="{GROUND+16}" stroke="#000" stroke-width="1.1" opacity=".55"/>')
parts.extend(ground)

svg = f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' + "".join(parts) + "</svg>"
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(svg)
print("wrote", OUT, f"{len(svg)//1024} KB, {len(leaves)} leaves, {len(tips)} bush tips")
