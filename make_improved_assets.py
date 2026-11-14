import os
os.environ['MPLCONFIGDIR'] = os.path.abspath('assets/.mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 1. assets/de2_hinh_ngoinha.png
fig, ax = plt.subplots(figsize=(5.2, 4.4), dpi=300)
ax.axis('off')

B = np.array([0.0, 0.0])
C = np.array([4.0, 0.0])
A = np.array([2.0, 2.0 * np.sqrt(3)])
D = np.array([0.0, 4.0 / np.sqrt(3)])
M = np.array([4.0 / 3.0, 0.0])

# Draw triangle ABC
ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=1.4)
ax.plot([B[0], A[0]], [B[1], A[1]], 'k-', lw=1.4)
ax.plot([A[0], C[0]], [A[1], C[1]], 'k-', lw=1.4)

# Draw D and connections DA, DB
ax.plot([D[0], A[0]], [D[1], A[1]], 'k-', lw=1.4)
ax.plot([D[0], B[0]], [D[1], B[1]], 'k-', lw=1.4)

# Draw road CM and MD in prominent magenta
ax.plot([C[0], M[0]], [C[1], M[1]], color='#d63384', lw=2.6)
ax.plot([M[0], D[0]], [M[1], D[1]], color='#d63384', lw=2.6)

# House icons
def draw_house(ax, pos, offset=(0, 0.22)):
    x, y = pos[0] + offset[0], pos[1] + offset[1]
    w, h = 0.24, 0.22
    # Base
    ax.plot([x - w/2, x + w/2, x + w/2, x - w/2, x - w/2],
            [y - h/2, y - h/2, y + h/2, y + h/2, y - h/2], 'k-', lw=1.1)
    # Roof
    ax.plot([x - w*0.7, x, x + w*0.7], [y + h/2, y + h*1.1, y + h/2], 'k-', lw=1.1)
    # Door
    ax.plot([x - w*0.2, x + w*0.2, x + w*0.2, x - w*0.2],
            [y - h/2, y - h/2, y + h*0.1, y + h*0.1], 'k-', lw=0.9)

draw_house(ax, A, offset=(0.26, 0.15))
draw_house(ax, B, offset=(-0.30, 0.15))
draw_house(ax, C, offset=(0.28, 0.15))
draw_house(ax, D, offset=(-0.30, 0.15))

# Markers for points
for pt in [A, B, C, D]:
    ax.plot(pt[0], pt[1], 'ko', ms=4.5)
ax.plot(M[0], M[1], 'o', color='#d63384', ms=5.5)

# Clear, large, bold labels
ax.text(A[0] - 0.15, A[1] + 0.15, 'A', fontsize=14, fontweight='bold', family='sans-serif', ha='right', va='bottom')
ax.text(B[0] - 0.22, B[1] - 0.25, 'B', fontsize=14, fontweight='bold', family='sans-serif', ha='right', va='top')
ax.text(C[0] + 0.18, C[1] - 0.25, 'C', fontsize=14, fontweight='bold', family='sans-serif', ha='left', va='top')
ax.text(D[0] - 0.22, D[1] - 0.18, 'D', fontsize=14, fontweight='bold', family='sans-serif', ha='right', va='top')
ax.text(M[0], M[1] - 0.28, 'M', fontsize=14, fontweight='bold', color='#d63384', family='sans-serif', ha='center', va='top')

# Tick marks for DA = DB
mid_DA = (D + A) / 2
mid_DB = (D + B) / 2
dir_DA = (A - D) / np.linalg.norm(A - D)
norm_DA = np.array([-dir_DA[1], dir_DA[0]])
ax.plot([mid_DA[0] - 0.09*norm_DA[0], mid_DA[0] + 0.09*norm_DA[0]],
        [mid_DA[1] - 0.09*norm_DA[1], mid_DA[1] + 0.09*norm_DA[1]], 'k-', lw=1.3)

dir_DB = (B - D) / np.linalg.norm(B - D)
norm_DB = np.array([-dir_DB[1], dir_DB[0]])
ax.plot([mid_DB[0] - 0.09*norm_DB[0], mid_DB[0] + 0.09*norm_DB[0]],
        [mid_DB[1] - 0.09*norm_DB[1], mid_DB[1] + 0.09*norm_DB[1]], 'k-', lw=1.3)

# Angle arc at D (120 deg)
theta_B = -np.pi/2
theta_A = np.arctan2(A[1] - D[1], A[0] - D[0])
arc_angles = np.linspace(theta_B, theta_A, 50)
r_arc = 0.36
ax.plot(D[0] + r_arc * np.cos(arc_angles), D[1] + r_arc * np.sin(arc_angles), 'k-', lw=1.1)

ax.set_xlim(-0.8, 4.8)
ax.set_ylim(-0.6, 4.2)
ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('assets/de2_hinh_ngoinha.png', bbox_inches='tight', pad_inches=0.03)
plt.close()

# 2. assets/de2_hinh_ao_vit.png - make labels clear and sharp
fig, ax = plt.subplots(figsize=(6.0, 2.8), dpi=300)
ax.axis('off')

# Bank line
ax.plot([-0.6, 5.4], [0, 0], color='#2b6cb0', lw=2.2)
ax.text(0.2, -0.42, 'bờ kênh', fontsize=10.5, family='sans-serif')

H = np.array([0.5, 0])
A = np.array([0.5, 1.4])
ax.plot([A[0], H[0]], [A[1], H[1]], 'k-', lw=1.3)
ax.plot([H[0], H[0]+0.15, H[0]+0.15], [H[1]+0.15, H[1]+0.15, H[1]], 'k-', lw=1.0)

# House at A
ax.plot([0.3, 0.5, 0.7, 0.7, 0.3, 0.3], [1.4, 1.7, 1.4, 1.18, 1.18, 1.4], 'k-', lw=1.3)
ax.text(0.5, 1.88, 'Nhà', fontsize=10.5, ha='center', weight='bold', family='sans-serif')

M = np.array([2.0, 0])
C = np.array([4.4, 0])
I = (M + C) / 2
R = (C[0] - M[0]) / 2

theta = np.linspace(0, 2*np.pi, 200)
cx = I[0] + R * np.cos(theta)
cy = I[1] + R * np.sin(theta)
ax.plot(cx[cy < 0], cy[cy < 0], 'k--', lw=1.1)
ax.plot(cx[cy >= 0], cy[cy >= 0], 'k--', lw=1.1)

angle_DMC = np.radians(25)
D = np.array([M[0] + 2*R*np.cos(angle_DMC)*np.cos(angle_DMC), 2*R*np.cos(angle_DMC)*np.sin(angle_DMC)])

# Pink paths: A -> M -> D -> arc DC -> C
ax.plot([A[0], M[0]], [A[1], M[1]], color='#c53030', lw=2.4)
ax.plot([M[0], D[0]], [M[1], D[1]], color='#c53030', lw=2.4)

theta_D = np.arctan2(D[1] - I[1], D[0] - I[0])
theta_arc = np.linspace(theta_D, 0, 100)
ax.plot(I[0] + R*np.cos(theta_arc), I[1] + R*np.sin(theta_arc), color='#c53030', lw=2.6)

# Arrows on path
ax.annotate('', xy=(1.3, 0.65), xytext=(1.0, 0.95), arrowprops=dict(arrowstyle='->', lw=1.6, color='#c53030'))
ax.annotate('', xy=(2.7, 0.4), xytext=(2.3, 0.2), arrowprops=dict(arrowstyle='->', lw=1.6, color='#c53030'))

# Points markers and labels
for pt, name, pos_offset in [
    (A, 'A', (-0.18, 0)),
    (H, 'H', (-0.18, -0.22)),
    (M, 'M', (0, -0.35)),
    (C, 'C', (0, -0.35)),
    (D, 'D', (0.12, 0.16)),
    (I, 'I', (0, -0.35))
]:
    ax.plot(pt[0], pt[1], 'ko', ms=4.5)
    if name == 'M':
        ax.text(pt[0] + pos_offset[0], pt[1] + pos_offset[1], name, fontsize=12, weight='bold', color='#c53030', ha='center', family='sans-serif')
    elif name == 'I':
        ax.text(pt[0] + pos_offset[0], pt[1] + pos_offset[1], name, fontsize=11, style='italic', ha='center', family='sans-serif')
    else:
        ax.text(pt[0] + pos_offset[0], pt[1] + pos_offset[1], name, fontsize=12, weight='bold', ha='center', family='sans-serif')

# Duck coop icon at C
ax.plot([4.6, 4.8, 5.0, 5.0, 4.6, 4.6], [0.3, 0.5, 0.3, 0, 0, 0.3], 'k-', lw=1.3)
ax.text(4.8, -0.42, 'chuồng\nvịt', fontsize=10, ha='center', family='sans-serif')

ax.set_xlim(-0.7, 5.6)
ax.set_ylim(-0.8, 2.1)

plt.tight_layout()
plt.savefig('assets/de2_hinh_ao_vit.png', bbox_inches='tight', pad_inches=0.03)
plt.close()

print("Assets generated successfully with sharp labels!")
