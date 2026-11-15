import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

os.makedirs('assets', exist_ok=True)
plt.rcParams['font.family'] = 'DejaVu Serif'
plt.rcParams['mathtext.fontset'] = 'cm'

# =========================================================
# 1. Phần III - Câu 1: Hai hình trụ giao vuông góc (tối giản, không chữ số)
# =========================================================
fig, ax = plt.subplots(figsize=(5.4, 3.0), dpi=220)

# Oblique 3D projection: x along right-down, y along right-up, z up
def p3(x, y, z):
    return 0.88 * x - 0.52 * y, z + 0.34 * x + 0.28 * y

R = 1.6
L = 3.4
th = np.linspace(0, 2 * np.pi, 200)

# Cylinder 1 axis along X (y^2 + z^2 = R^2, x in [-L, L])
for x0, ls, lw, col in [(-L, '-', 1.3, '#475569'), (L, '-', 1.3, '#475569')]:
    pts = np.array([p3(x0, R * np.cos(t), R * np.sin(t)) for t in th])
    ax.fill(pts[:, 0], pts[:, 1], color='#e2e8f0', alpha=0.45, zorder=1)
    ax.plot(pts[:, 0], pts[:, 1], color=col, lw=lw, ls=ls, zorder=2)

# Envelope generators for Cylinder 1 (along X, screen dir (0.88, 0.34))
ang1 = np.arctan2(0.88, 0.52 * 0.34 + 0.28 * 0.88)
for offset_pi in (0.0, np.pi):
    ang = ang1 + offset_pi
    y_e, z_e = R * np.cos(ang), R * np.sin(ang)
    pA, pB = p3(-L, y_e, z_e), p3(L, y_e, z_e)
    ax.plot([pA[0], pB[0]], [pA[1], pB[1]], color='#334155', lw=1.4, zorder=2)

# Cylinder 2 axis along Y (x^2 + z^2 = R^2, y in [-L, L])
for y0 in (-L, L):
    pts = np.array([p3(R * np.cos(t), y0, R * np.sin(t)) for t in th])
    ax.fill(pts[:, 0], pts[:, 1], color='#dbeafe', alpha=0.45, zorder=3)
    ax.plot(pts[:, 0], pts[:, 1], color='#1e40af', lw=1.3, zorder=4)

ang2 = np.arctan2(0.52, 0.88 * 0.28 + 0.34 * 0.52)
for offset_pi in (0.0, np.pi):
    ang = ang2 + offset_pi
    x_e, z_e = R * np.cos(ang), R * np.sin(ang)
    pA, pB = p3(x_e, -L, z_e), p3(x_e, L, z_e)
    ax.plot([pA[0], pB[0]], [pA[1], pB[1]], color='#1e40af', lw=1.4, zorder=4)

# Smooth Steinmetz intersection curves parameterized by phi in [0, pi]
phi = np.linspace(0, np.pi, 160)
ts = R * np.cos(phi)
zs = R * np.sin(phi)
for sx in (-1, 1):
    pts_top = np.array([p3(t, sx * t, z) for t, z in zip(ts, zs)])
    pts_bot = np.array([p3(t, sx * t, -z) for t, z in zip(ts, zs)])
    ax.plot(pts_top[:, 0], pts_top[:, 1], color='#dc2626', lw=2.0, zorder=6)
    ax.plot(pts_bot[:, 0], pts_bot[:, 1], color='#dc2626', lw=1.3, ls='--', zorder=5)

# Dashed axes
ax1_l, ax1_r = p3(-L - 0.55, 0, 0), p3(L + 0.55, 0, 0)
ax2_l, ax2_r = p3(0, -L - 0.55, 0), p3(0, L + 0.55, 0)
ax.plot([ax1_l[0], ax1_r[0]], [ax1_l[1], ax1_r[1]], color='#111827', lw=0.85, ls='-.', zorder=7)
ax.plot([ax2_l[0], ax2_r[0]], [ax2_l[1], ax2_r[1]], color='#111827', lw=0.85, ls='-.', zorder=7)

ax.set_aspect('equal')
ax.autoscale_view()
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de201_p3_c1_cylinders.png', bbox_inches='tight', dpi=220)
plt.close()

# =========================================================
# 2. Phần III - Câu 2: Hình thang cân nội tiếp nửa đường tròn (tối giản)
# =========================================================
fig, ax = plt.subplots(figsize=(5.0, 2.7), dpi=220)
R2 = 6.0
th_arc = np.linspace(0, np.pi, 300)
ax.plot(R2 * np.cos(th_arc), R2 * np.sin(th_arc), color='#1e293b', lw=1.7)
ax.plot([-R2, R2], [0, 0], color='#1e293b', lw=1.7)

# Optimal angle theta = 60 deg
ang_B = 2 * np.pi / 3
ang_C = np.pi / 3
A_pt = (-R2, 0.0)
B_pt = (R2 * np.cos(ang_B), R2 * np.sin(ang_B))
C_pt = (R2 * np.cos(ang_C), R2 * np.sin(ang_C))
D_pt = (R2, 0.0)
O_pt = (0.0, 0.0)

trap = patches.Polygon([A_pt, B_pt, C_pt, D_pt], closed=True,
                       facecolor='#dbeafe', edgecolor='#1d4ed8', lw=1.9, alpha=0.65)
ax.add_patch(trap)

for pt in (A_pt, B_pt, C_pt, D_pt, O_pt):
    ax.scatter(pt[0], pt[1], color='#0f172a', s=18, zorder=6)

ax.text(A_pt[0] - 0.55, -0.55, '$A$', fontsize=10.5, fontweight='bold')
ax.text(D_pt[0] + 0.18, -0.55, '$D$', fontsize=10.5, fontweight='bold')
ax.text(O_pt[0] - 0.22, -0.65, '$O$', fontsize=10.0, fontweight='bold')
ax.text(B_pt[0] - 0.65, B_pt[1] + 0.25, '$B$', fontsize=10.5, fontweight='bold', color='#1d4ed8')
ax.text(C_pt[0] + 0.22, C_pt[1] + 0.25, '$C$', fontsize=10.5, fontweight='bold', color='#1d4ed8')

ax.set_xlim(-R2 - 1.1, R2 + 1.1)
ax.set_ylim(-1.0, R2 + 0.9)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de201_p3_c2_trapezoid.png', bbox_inches='tight', dpi=220)
plt.close()

# =========================================================
# 3. Phần III - Câu 6: Hai hộp đựng bi (Hộp I: 5 đỏ, 4 xanh; Hộp II: 6 đỏ, 3 xanh) - tối giản
# =========================================================
fig, ax = plt.subplots(figsize=(3.6, 2.15), dpi=220)

def draw_ball_box(ax, cx, cy, n_red, label):
    w, h = 1.95, 1.85
    box = patches.FancyBboxPatch(
        (cx - w / 2, cy - h / 2), w, h,
        boxstyle="round,pad=0.06,rounding_size=0.18",
        facecolor='#f8fafc', edgecolor='#1e293b', lw=1.6, zorder=1
    )
    ax.add_patch(box)
    ax.text(cx, cy + h / 2 + 0.30, label, ha='center', va='center',
            fontsize=11.5, fontweight='bold', color='#0f172a')
    # 3x3 grid inside the box
    xs = [cx - 0.56, cx, cx + 0.56]
    ys = [cy + 0.52, cy, cy - 0.52]
    idx = 0
    for yy in ys:
        for xx in xs:
            is_red = idx < n_red
            fc = '#ef4444' if is_red else '#3b82f6'
            ec = '#991b1b' if is_red else '#1e40af'
            ball = patches.Circle((xx, yy), radius=0.20, facecolor=fc, edgecolor=ec, lw=1.2, zorder=3)
            ax.add_patch(ball)
            # Subtle specular highlight on ball
            hl = patches.Circle((xx - 0.06, yy + 0.06), radius=0.055, facecolor='white', alpha=0.55, edgecolor='none', zorder=4)
            ax.add_patch(hl)
            idx += 1

draw_ball_box(ax, -1.65, -0.08, 5, 'I')
draw_ball_box(ax, 1.65, -0.08, 6, 'II')

arrow = patches.FancyArrowPatch(
    (-0.55, 0.35), (0.55, 0.35),
    connectionstyle="arc3,rad=-0.28",
    arrowstyle="-|>,head_length=6,head_width=4",
    color='#0f172a', lw=1.6, ls='--', zorder=5
)
ax.add_patch(arrow)

ax.set_xlim(-2.85, 2.85)
ax.set_ylim(-1.25, 1.38)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de201_p3_c6_boxes.png', bbox_inches='tight', dpi=220)
plt.close()

print("All 3 minimal Ma De 201 diagrams generated successfully!")
