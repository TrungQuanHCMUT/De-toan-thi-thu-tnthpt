import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Serif'
plt.rcParams['mathtext.fontset'] = 'cm'

# =========================================================
# 1. Phần III - Câu 1: Ellipsoid bead with cylindrical hole (minimal annotations)
# =========================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.4, 2.55), dpi=220, gridspec_kw={'width_ratios': [1.02, 1.15]})

x_full = np.linspace(-5, 5, 300)
y_ell = 3 * np.sqrt(np.maximum(0, 1 - x_full**2 / 25))
x_kept = np.linspace(-4, 4, 250)
y_kept = 3 * np.sqrt(1 - x_kept**2 / 25)

# Left panel: 3D cutaway bead schematic
ax1.fill_between(x_kept, 1.8, y_kept, color='#d97706', alpha=0.28)
ax1.fill_between(x_kept, -y_kept, -1.8, color='#d97706', alpha=0.28)
ax1.plot(x_kept, y_kept, color='#78350f', lw=1.8)
ax1.plot(x_kept, -y_kept, color='#78350f', lw=1.8)

x_cap_l = np.linspace(-5, -4, 60)
x_cap_r = np.linspace(4, 5, 60)
ax1.plot(x_cap_l, 3*np.sqrt(1 - x_cap_l**2/25), color='#9ca3af', lw=1.1, ls='--')
ax1.plot(x_cap_l, -3*np.sqrt(1 - x_cap_l**2/25), color='#9ca3af', lw=1.1, ls='--')
ax1.plot(x_cap_r, 3*np.sqrt(1 - x_cap_r**2/25), color='#9ca3af', lw=1.1, ls='--')
ax1.plot(x_cap_r, -3*np.sqrt(1 - x_cap_r**2/25), color='#9ca3af', lw=1.1, ls='--')

ax1.plot([-4, 4], [1.8, 1.8], color='#b45309', lw=1.2, ls='--')
ax1.plot([-4, 4], [-1.8, -1.8], color='#b45309', lw=1.2, ls='--')

th = np.linspace(0, 2*np.pi, 120)
ax1.plot(-4 + 0.35*np.cos(th), 1.8*np.sin(th), color='#78350f', lw=1.5)
th_front = np.linspace(-np.pi/2, np.pi/2, 80)
th_back = np.linspace(np.pi/2, 3*np.pi/2, 80)
ax1.plot(4 + 0.35*np.cos(th_front), 1.8*np.sin(th_front), color='#78350f', lw=1.5)
ax1.plot(4 + 0.35*np.cos(th_back), 1.8*np.sin(th_back), color='#78350f', lw=1.0, ls='--')

ax1.plot([-5.4, 5.4], [0, 0], color='k', lw=0.8, ls='-.')
ax1.set_xlim(-5.6, 5.6)
ax1.set_ylim(-3.3, 3.3)
ax1.set_aspect('equal')
ax1.axis('off')

# Right panel: 2D Oxy cross-section (O, x, y only, no numeric ticks)
ax2.fill_between(x_kept, 1.8, y_kept, color='#fbbf24', alpha=0.4)
ax2.fill_between(x_kept, -y_kept, -1.8, color='#fbbf24', alpha=0.4)
ax2.plot(x_full, y_ell, color='#1d4ed8', lw=1.8)
ax2.plot(x_full, -y_ell, color='#1d4ed8', lw=1.8)
ax2.plot([-4, 4], [1.8, 1.8], color='#dc2626', lw=1.5)
ax2.plot([-4, 4], [-1.8, -1.8], color='#dc2626', lw=1.5)
ax2.plot([-4, -4], [-1.8, 1.8], color='gray', lw=1.0, ls=':')
ax2.plot([4, 4], [-1.8, 1.8], color='gray', lw=1.0, ls=':')

ax2.annotate('', xy=(5.9, 0), xytext=(-5.9, 0), arrowprops=dict(arrowstyle='->', lw=1.0))
ax2.annotate('', xy=(0, 3.85), xytext=(0, -3.7), arrowprops=dict(arrowstyle='->', lw=1.0))
ax2.text(5.8, -0.45, '$x$', fontsize=10)
ax2.text(0.22, 3.55, '$y$', fontsize=10)
ax2.text(-0.48, -0.48, '$O$', fontsize=9.5)

ax2.set_xlim(-6.2, 6.3)
ax2.set_ylim(-3.9, 4.1)
ax2.set_aspect('equal')
ax2.axis('off')

plt.tight_layout()
plt.savefig('assets/de200_p3_c1_ellipsoid.png', bbox_inches='tight', dpi=220)
plt.close()

# =========================================================
# 2. Phần III - Câu 2: Paper folding (no 'Nếp gấp' or '12 cm')
# =========================================================
fig, ax = plt.subplots(figsize=(4.6, 2.55), dpi=220)
W_rect, H_rect = 20.0, 12.0
xm, ym = 0.0, 9.0
xe, ye = 6 * np.sqrt(2), 12.0
xn, yn = 9 * np.sqrt(2), 0.0

ax.plot([0, W_rect, W_rect, 0, 0], [0, 0, H_rect, H_rect, 0], 'k-', lw=1.2)
ax.plot([0, 0], [0, ym], color='white', lw=2.2)
ax.plot([0, xn], [0, 0], color='white', lw=2.2)
ax.plot([0, 0], [0, ym], color='#6b7280', lw=1.2, ls='--')
ax.plot([0, xn], [0, 0], color='#6b7280', lw=1.2, ls='--')

tri = patches.Polygon([[xm, ym], [xe, ye], [xn, yn]], closed=True, facecolor='#bfdbfe', edgecolor='#1d4ed8', lw=1.8, alpha=0.7)
ax.add_patch(tri)
ax.plot([xm, xn], [ym, yn], color='#dc2626', lw=2.2)

ax.scatter([0, 0, W_rect, W_rect, xm, xn, xe], [H_rect, 0, 0, H_rect, ym, yn, ye], color='k', s=16, zorder=6)
ax.text(-0.95, H_rect + 0.3, '$A$', fontsize=10, fontweight='bold')
ax.text(-0.95, -0.75, '$B$', fontsize=10, color='#6b7280')
ax.text(W_rect + 0.35, -0.75, '$C$', fontsize=10, fontweight='bold')
ax.text(W_rect + 0.35, H_rect + 0.3, '$D$', fontsize=10, fontweight='bold')
ax.text(-1.15, ym, '$M$', fontsize=10, fontweight='bold', color='#1d4ed8')
ax.text(xn - 0.3, -1.35, '$N$', fontsize=10, fontweight='bold', color='#1d4ed8')
ax.text(xe - 0.2, ye + 0.55, '$E$', fontsize=10, fontweight='bold', color='#1d4ed8')

ax.set_xlim(-2.2, W_rect + 1.8)
ax.set_ylim(-2.0, H_rect + 1.8)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/de200_p3_c2_fold.png', bbox_inches='tight', dpi=220)
plt.close()

# =========================================================
# 3. Phần III - Câu 3: Regular square frustum ABCD.A'B'C'D' (geometry only, no meter labels)
# =========================================================
fig, ax = plt.subplots(figsize=(4.1, 3.0), dpi=220)

def proj(x, y, z):
    px = x + 0.44 * y
    py = z + 0.34 * y
    return px, py

pts3d = {
    'A': (-4, -4, 0), 'B': (4, -4, 0), 'C': (4, 4, 0), 'D': (-4, 4, 0),
    'Ap': (-1.5, -1.5, 4.8), 'Bp': (1.5, -1.5, 4.8), 'Cp': (1.5, 1.5, 4.8), 'Dp': (-1.5, 1.5, 4.8),
    'O': (0, 0, 0), 'Op': (0, 0, 4.8)
}
P = {k: proj(*v) for k, v in pts3d.items()}

for u, v in [('A', 'D'), ('D', 'C'), ('D', 'Dp'), ('O', 'Op'), ('A', 'C'), ('B', 'D')]:
    ax.plot([P[u][0], P[v][0]], [P[u][1], P[v][1]], color='#4b5563', lw=1.1, ls='--')

for u, v in [('A', 'B'), ('B', 'C'), ('A', 'Ap'), ('B', 'Bp'), ('C', 'Cp'),
             ('Ap', 'Bp'), ('Bp', 'Cp'), ('Cp', 'Dp'), ('Dp', 'Ap')]:
    ax.plot([P[u][0], P[v][0]], [P[u][1], P[v][1]], color='#111827', lw=1.7)

offsets = {
    'A': (-0.65, -0.45), 'B': (0.25, -0.45), 'C': (0.35, 0.0), 'D': (-0.7, 0.05),
    'Ap': (-0.7, 0.05), 'Bp': (0.25, -0.1), 'Cp': (0.35, 0.2), 'Dp': (-0.7, 0.25),
    'O': (0.15, -0.42), 'Op': (0.18, -0.05)
}
names = {'A': '$A$', 'B': '$B$', 'C': '$C$', 'D': '$D$',
         'Ap': "$A'$", 'Bp': "$B'$", 'Cp': "$C'$", 'Dp': "$D'$",
         'O': '$O$', 'Op': "$O'$"}
for k, (dx, dy) in offsets.items():
    ax.scatter(*P[k], color='k', s=12, zorder=5)
    ax.text(P[k][0] + dx, P[k][1] + dy, names[k], fontsize=9.8, fontweight='bold')

ax.set_xlim(-6.5, 6.8)
ax.set_ylim(-2.1, 6.2)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/de200_p3_c3_frustum.png', bbox_inches='tight', dpi=220)
plt.close()

# =========================================================
# 4. Phần III - Câu 5: 4x4 Grid (no axis tick numbers, simple point labels)
# =========================================================
fig, ax = plt.subplots(figsize=(2.7, 2.6), dpi=220)
for i in range(5):
    ax.plot([0, 4], [i, i], color='#cbd5e1', lw=1.0)
    ax.plot([i, i], [0, 4], color='#cbd5e1', lw=1.0)

ax.annotate('', xy=(4.55, 0), xytext=(-0.2, 0), arrowprops=dict(arrowstyle='->', lw=1.1, color='k'))
ax.annotate('', xy=(0, 4.55), xytext=(0, -0.2), arrowprops=dict(arrowstyle='->', lw=1.1, color='k'))
ax.text(4.5, -0.35, '$x$', fontsize=9.5)
ax.text(-0.35, 4.45, '$y$', fontsize=9.5)

ax.scatter([0, 4], [0, 4], color='#1d4ed8', s=34, zorder=6)
ax.scatter([1], [2], color='#dc2626', marker='X', s=65, zorder=7)
ax.scatter([3], [3], color='#15803d', s=42, zorder=7)

ax.text(-0.42, -0.38, '$O$', fontsize=9.5, fontweight='bold')
ax.text(4.14, 4.02, '$A$', fontsize=9.5, fontweight='bold', color='#1d4ed8')
ax.text(1.14, 2.12, '$M$', fontsize=9.5, fontweight='bold', color='#dc2626')
ax.text(3.14, 2.75, '$N$', fontsize=9.5, fontweight='bold', color='#15803d')

ax.set_xlim(-0.7, 4.9)
ax.set_ylim(-0.7, 4.9)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/de200_p3_c5_grid.png', bbox_inches='tight', dpi=220)
plt.close()

# =========================================================
# 5. Phần III - Câu 6: Infinite tangent circles in angle xOy (minimal labels)
# =========================================================
fig, ax = plt.subplots(figsize=(3.4, 2.2), dpi=220)
L = 14.2
ax.plot([0, L*np.cos(np.pi/6)], [0, L*np.sin(np.pi/6)], 'k-', lw=1.4)
ax.plot([0, L*np.cos(np.pi/6)], [0, -L*np.sin(np.pi/6)], 'k-', lw=1.4)
ax.plot([0, L*0.92], [0, 0], color='gray', lw=0.8, ls='-.')

R = 4.0
labels = ['$(C_1)$', '$(C_2)$', '', '']
colors = ['#dbeafe', '#bfdbfe', '#93c5fd', '#60a5fa']
for idx in range(4):
    cx = 2 * R
    circ = patches.Circle((cx, 0), R, facecolor=colors[idx], edgecolor='#1d4ed8', lw=1.3, alpha=0.85)
    ax.add_patch(circ)
    if labels[idx]:
        ax.text(cx, 0, labels[idx], ha='center', va='center',
                fontsize=9.2 if idx==0 else 7.8, fontweight='bold')
    R /= 3.0

ax.text(-0.92, -0.28, '$O$', fontsize=9.5, fontweight='bold')
ax.text(L*np.cos(np.pi/6)+0.2, L*np.sin(np.pi/6), '$x$', fontsize=9.5)
ax.text(L*np.cos(np.pi/6)+0.2, -L*np.sin(np.pi/6)-0.25, '$y$', fontsize=9.5)

ax.set_xlim(-1.45, 13.4)
ax.set_ylim(-6.4, 6.4)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/de200_p3_c6_circles.png', bbox_inches='tight', dpi=220)
plt.close()

print("All 5 minimal Ma De 200 diagrams generated successfully!")
