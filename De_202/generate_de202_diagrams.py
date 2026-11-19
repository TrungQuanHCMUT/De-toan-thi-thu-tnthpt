#!/usr/bin/env python3
"""Generate clean, minimal high-DPI diagrams for De_202 Part III (Questions 1 & 2)."""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams["font.family"] = "DejaVu Serif"
plt.rcParams["mathtext.fontset"] = "cm"

ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)


def draw_p3_c1_parabola_circle():
    """Circle (R = 5) with inscribed parabolic arc ACB and shaded upper cap/goblet."""
    fig, ax = plt.subplots(figsize=(4.4, 4.4), dpi=300)
    ax.set_aspect("equal")
    ax.axis("off")

    R = 5.0
    theta = np.linspace(0, 2 * np.pi, 600)
    ax.plot(R * np.cos(theta), R * np.sin(theta), color="#1a365d", lw=2.0, zorder=4)

    # Shaded region between y = x^2 - 5 and upper circle arc sqrt(25 - x^2) on [-3, 3]
    xs = np.linspace(-3.0, 3.0, 400)
    y_low = xs**2 - 5.0
    y_high = np.sqrt(R**2 - xs**2)
    ax.fill_between(xs, y_low, y_high, color="#bae6fd", alpha=0.82, zorder=2)
    ax.fill_between(xs, y_low, y_high, facecolor="none", edgecolor="#0284c7", hatch="///", lw=0.0, alpha=0.35, zorder=2)

    # Draw full parabola slightly past A, B for visual clarity, clipped inside [-3.4, 3.4]
    xp_ext = np.linspace(-3.3, 3.3, 300)
    ax.plot(xp_ext, xp_ext**2 - 5.0, color="#0369a1", lw=2.0, zorder=5)

    # Symmetry dashed vertical line & horizontal chord AB
    ax.plot([0, 0], [-5.5, 5.5], color="#64748b", lw=1.0, ls="--", zorder=3)
    ax.plot([-3, 3], [4, 4], color="#1e293b", lw=1.3, ls="--", zorder=4)

    # Points O, A, B, C (large clear markers & labels)
    pts = {"O": (0, 0), "A": (-3, 4), "B": (3, 4), "C": (0, -5)}
    for label, (px, py) in pts.items():
        ax.scatter([px], [py], color="#0f172a", s=56, zorder=6)

    ax.text(0.32, -0.50, r"$O$", fontsize=17.5, fontweight="bold")
    ax.text(-3.98, 4.15, r"$A$", fontsize=17.5, fontweight="bold")
    ax.text(3.32, 4.15, r"$B$", fontsize=17.5, fontweight="bold")
    ax.text(0.32, -5.80, r"$C$", fontsize=17.5, fontweight="bold")

    # Radius segment OA
    ax.plot([0, -3], [0, 4], color="#334155", lw=1.15, ls=":", zorder=4)
    ax.text(2.45, -1.75, r"$(P)$", fontsize=14, color="#0369a1", fontweight="bold")

    ax.set_xlim(-5.9, 5.9)
    ax.set_ylim(-6.2, 5.8)
    fig.tight_layout(pad=0.15)
    out = os.path.join(ASSETS_DIR, "de202_p3_c1_parabola_circle.png")
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)


def draw_p3_c2_corridor():
    """Minimal L-shaped corridor of widths 2,7 m and 6,4 m with a turning beam."""
    fig, ax = plt.subplots(figsize=(5.4, 3.8), dpi=300)
    ax.set_aspect("equal")
    ax.axis("off")

    a = 2.7   # height of horizontal corridor (bottom outer wall y=0, inner corner y=a)
    b = 4.2   # scaled visual width for 6,4 m vertical corridor (left wall x=0, inner wall x=b)
    X_max = 11.2
    Y_max = 7.7

    # Inner building corner block (open on top/right, bold walls only along the corridor)
    inner_block = patches.Rectangle((b, a), X_max - b, Y_max - a, facecolor="#e2e8f0", edgecolor="none", zorder=2)
    ax.add_patch(inner_block)
    ax.plot([b, b, X_max], [Y_max, a, a], color="#0f172a", lw=2.5, zorder=4)

    # Outer boundary lines: bottom wall y=0 (x from 0 to X_max) and left wall x=0 (y from 0 to Y_max)
    ax.plot([0, X_max], [0, 0], color="#0f172a", lw=2.5, zorder=4)
    ax.plot([0, 0], [0, Y_max], color="#0f172a", lw=2.5, zorder=4)

    # Rigid rod tangent at inner corner (b, a) reaching outer walls (0, y0) and (x0, 0)
    m = -0.62
    x0 = b - a / m
    y0 = a - m * b
    ax.plot([0, x0], [y0, 0], color="#dc2626", lw=3.2, solid_capstyle="round", zorder=5)
    ax.scatter([b, 0, x0], [a, y0, 0], color="#dc2626", s=32, zorder=6)

    # Inner right-angle marker at (0,0)
    ax.plot([0.35, 0.35, 0], [0, 0.35, 0.35], color="#334155", lw=1.0)

    # Dimension arrows: large uniform 2,7 m (vertical width on right) and 6,4 m (horizontal width near top)
    dim_x = 9.05
    ax.annotate("", xy=(dim_x, a), xytext=(dim_x, 0),
                arrowprops=dict(arrowstyle="<->", color="#0f172a", lw=1.4))
    ax.text(dim_x + 0.24, a / 2, r"$2{,}7\ \mathrm{m}$", va="center", ha="left", fontsize=17.5, color="#0f172a")

    dim_y = 6.50
    ax.annotate("", xy=(b, dim_y), xytext=(0, dim_y),
                arrowprops=dict(arrowstyle="<->", color="#0f172a", lw=1.4))
    ax.text(b / 2, dim_y + 0.25, r"$6{,}4\ \mathrm{m}$", va="bottom", ha="center", fontsize=17.5, color="#0f172a")

    ax.set_xlim(-0.6, X_max + 0.4)
    ax.set_ylim(-0.6, Y_max + 0.2)
    fig.tight_layout(pad=0.15)
    out = os.path.join(ASSETS_DIR, "de202_p3_c2_corridor.png")
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    draw_p3_c1_parabola_circle()
    draw_p3_c2_corridor()
    print("Diagrams generated successfully.")
