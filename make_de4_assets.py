import os
os.environ['MPLCONFIGDIR'] = '/tmp/matplotlib'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

os.makedirs('assets', exist_ok=True)

# 1. Đồ thị f'(x) cho Câu 2 Phần I (Parabol cắt Ox tại -1 và 3, bề lõm hướng lên)
fig, ax = plt.subplots(figsize=(3.6, 2.8), dpi=300)
x = np.linspace(-2.2, 4.2, 300)
y = (x + 1) * (x - 3) / 1.5 # f'(x)

ax.plot(x, y, 'b-', lw=1.8, label=r"$y = f'(x)$")
ax.axhline(0, color='black', lw=1.0)
ax.axvline(0, color='black', lw=1.0)

# Points
ax.plot([-1, 3], [0, 0], 'ro', markersize=4)
ax.plot([0, 1], [-2/1.5, -4/1.5], 'k.', markersize=3)
ax.plot([1, 1], [0, -4/1.5], 'k--', lw=0.8)
ax.plot([0, 1], [-4/1.5, -4/1.5], 'k--', lw=0.8)

# Labels
ax.text(4.2, 0.15, r'$x$', fontsize=10, family='serif')
ax.text(0.15, 3.2, r'$y$', fontsize=10, family='serif')
ax.text(-0.25, -0.3, r'$O$', fontsize=9.5, family='serif')
ax.text(-1, 0.25, r'$-1$', ha='center', fontsize=9, family='serif')
ax.text(3, 0.25, r'$3$', ha='center', fontsize=9, family='serif')
ax.text(1, 0.25, r'$1$', ha='center', fontsize=9, family='serif')
ax.text(-0.35, -4/1.5, r'$-2$', va='center', fontsize=9, family='serif')

ax.set_xlim(-2.2, 4.5)
ax.set_ylim(-3.2, 3.5)
ax.axis('off')
# arrow heads
ax.annotate('', xy=(4.5, 0), xytext=(4.3, 0), arrowprops=dict(arrowstyle="->", color="black", lw=1.0))
ax.annotate('', xy=(0, 3.5), xytext=(0, 3.3), arrowprops=dict(arrowstyle="->", color="black", lw=1.0))

plt.tight_layout()
plt.savefig('assets/de4_dothi_fprime_cau2.png', dpi=300)
plt.close()
print("Saved assets/de4_dothi_fprime_cau2.png")

# 2. Đồ thị hàm phân thức bậc 2 trên bậc 1 cho Câu 7 Phần I: y = (x^2 - x + 1)/(x - 1) = x + 1/(x - 1)
# TCĐ x = 1, TCX y = x. Cực đại (0; -1), cực tiểu (2; 3)
fig, ax = plt.subplots(figsize=(3.6, 3.2), dpi=300)
x1 = np.linspace(-3.5, 0.85, 250)
x2 = np.linspace(1.15, 5.0, 250)
y1 = (x1**2 - x1 + 1) / (x1 - 1)
y2 = (x2**2 - x2 + 1) / (x2 - 1)

ax.plot(x1, y1, 'b-', lw=1.8)
ax.plot(x2, y2, 'b-', lw=1.8)

# Asymptotes
ax.axvline(1, color='red', linestyle='--', lw=1.0)
x_line = np.linspace(-3.5, 5.0, 100)
ax.plot(x_line, x_line, 'g--', lw=1.0)

# Axes
ax.axhline(0, color='black', lw=1.0)
ax.axvline(0, color='black', lw=1.0)

# Extremum points
ax.plot([0, 2], [-1, 3], 'ro', markersize=4)
ax.plot([2, 2], [0, 3], 'k--', lw=0.8)
ax.plot([0, 2], [3, 3], 'k--', lw=0.8)

ax.text(5.0, 0.2, r'$x$', fontsize=10, family='serif')
ax.text(0.15, 6.0, r'$y$', fontsize=10, family='serif')
ax.text(-0.35, -0.35, r'$O$', fontsize=9.5, family='serif')
ax.text(1.1, 5.2, r'$x=1$', color='red', fontsize=8.5, family='serif')
ax.text(3.8, 4.4, r'$y=x$', color='green', fontsize=8.5, family='serif')
ax.text(2, -0.4, r'$2$', ha='center', fontsize=9, family='serif')
ax.text(-0.35, 3, r'$3$', va='center', fontsize=9, family='serif')
ax.text(-0.35, -1, r'$-1$', va='center', fontsize=9, family='serif')

ax.set_xlim(-3.5, 5.2)
ax.set_ylim(-4.5, 6.2)
ax.axis('off')
ax.annotate('', xy=(5.2, 0), xytext=(5.0, 0), arrowprops=dict(arrowstyle="->", color="black", lw=1.0))
ax.annotate('', xy=(0, 6.2), xytext=(0, 6.0), arrowprops=dict(arrowstyle="->", color="black", lw=1.0))

plt.tight_layout()
plt.savefig('assets/de4_dothi_cau7.png', dpi=300)
plt.close()
print("Saved assets/de4_dothi_cau7.png")

# 3. Hình vẽ tấm tôn cắt 4 góc làm hộp không nắp cho Câu 4 Phần II
fig, ax = plt.subplots(figsize=(6.0, 3.4), dpi=300)
ax.set_xlim(-5, 95)
ax.set_ylim(-8, 62)
ax.axis('off')

# Outer rectangle 80 x 50
ax.plot([0, 80, 80, 0, 0], [0, 0, 50, 50, 0], 'k-', lw=1.5)

# Cutout squares at 4 corners of size x=12
x_c = 12
for cx, cy in [(0, 0), (80-x_c, 0), (0, 50-x_c), (80-x_c, 50-x_c)]:
    rect = matplotlib.patches.Rectangle((cx, cy), x_c, x_c, facecolor='lightgray', edgecolor='red', hatch='//', lw=1.2)
    ax.add_patch(rect)

# Fold lines (dashed)
ax.plot([x_c, 80-x_c], [x_c, x_c], 'b--', lw=1.2)
ax.plot([x_c, 80-x_c], [50-x_c, 50-x_c], 'b--', lw=1.2)
ax.plot([x_c, x_c], [x_c, 50-x_c], 'b--', lw=1.2)
ax.plot([80-x_c, 80-x_c], [x_c, 50-x_c], 'b--', lw=1.2)

# Text labels
ax.text(40, 25, 'Đáy hộp', ha='center', va='center', fontsize=11, fontweight='bold', family='serif', color='navy')
ax.text(x_c/2, x_c/2, r'$x$', ha='center', va='center', fontsize=10, color='red', family='serif')
ax.text(80 - x_c/2, x_c/2, r'$x$', ha='center', va='center', fontsize=10, color='red', family='serif')
ax.text(x_c/2, 50 - x_c/2, r'$x$', ha='center', va='center', fontsize=10, color='red', family='serif')
ax.text(80 - x_c/2, 50 - x_c/2, r'$x$', ha='center', va='center', fontsize=10, color='red', family='serif')

# Dimensions
ax.annotate('', xy=(80, -4), xytext=(0, -4), arrowprops=dict(arrowstyle='<->', lw=1.0, color='black'))
ax.text(40, -7, '80 cm', ha='center', va='center', fontsize=10, family='serif')

ax.annotate('', xy=(-3, 50), xytext=(-3, 0), arrowprops=dict(arrowstyle='<->', lw=1.0, color='black'))
ax.text(-5, 25, '50 cm', ha='right', va='center', fontsize=10, family='serif', rotation=90)

plt.tight_layout()
plt.savefig('assets/de4_hop_ton_cau4.png', dpi=300)
plt.close()
print("Saved assets/de4_hop_ton_cau4.png")

# 4. Hình vẽ bồn chứa nước hình nón cho Câu 3 Phần III
fig, ax = plt.subplots(figsize=(5.5, 4.0), dpi=300)
ax.set_xlim(-4, 4)
ax.set_ylim(-1.5, 6.5)
ax.axis('off')

# Outer cone
R = 2.5
H = 5.0
# Ellipse at top
theta = np.linspace(0, 2*np.pi, 200)
ax.plot(R * np.cos(theta), H + 0.35 * np.sin(theta), 'k-', lw=1.5)
ax.plot([-R, 0], [H, 0], 'k-', lw=1.5)
ax.plot([R, 0], [H, 0], 'k-', lw=1.5)

# Water level at h = 2.0 (h/H = 2/5 -> r = 1.0)
h_w = 2.0
r_w = R * (h_w / H)
ax.plot(r_w * np.cos(theta), h_w + 0.2 * np.sin(theta), color='royalblue', lw=1.5)
# Water fill
x_fill = np.linspace(-r_w, r_w, 100)
ax.fill_between(x_fill, h_w - 0.2*np.sqrt(np.maximum(0, 1 - (x_fill/r_w)**2)), (h_w/r_w)*np.abs(x_fill), color='skyblue', alpha=0.5)

# Water faucet at top
ax.plot([0, 0, -0.6], [6.2, 5.7, 5.7], 'k-', lw=3.0)
ax.plot([0, 0], [5.7, 5.4], 'gray', lw=2.5)
# Water drops
for dy in [5.1, 4.5, 3.9, 3.3, 2.7]:
    ax.plot([0, 0], [dy, dy-0.3], 'deepskyblue', lw=2.0)
ax.text(0.3, 5.9, r'Vòi nước ($40\pi\ \mathrm{cm^3/s}$)', fontsize=10, family='serif', color='navy')

# Dimension lines
# Radius R
ax.plot([0, R], [H, H], 'k--', lw=1.0)
ax.plot([0, 0], [0, H], 'k-.', lw=0.8)
ax.text(R/2, H + 0.2, r'$R = 60\ \mathrm{cm}$', ha='center', fontsize=9.5, family='serif')

# Total Height H
ax.annotate('', xy=(3.2, H), xytext=(3.2, 0), arrowprops=dict(arrowstyle='<->', lw=1.0, color='black'))
ax.text(3.35, H/2, r'$H = 120\ \mathrm{cm}$', va='center', fontsize=9.5, family='serif')

# Water height h
ax.annotate('', xy=(-2.2, h_w), xytext=(-2.2, 0), arrowprops=dict(arrowstyle='<->', lw=1.0, color='royalblue'))
ax.text(-2.35, h_w/2, r'$h = 40\ \mathrm{cm}$', ha='right', va='center', fontsize=9.5, family='serif', color='royalblue')

plt.tight_layout()
plt.savefig('assets/de4_bon_nuoc_cau3.png', dpi=300)
plt.close()
print("Saved assets/de4_bon_nuoc_cau3.png")

# 5. Sơ đồ cáp điện qua sông cho Câu 5 Phần III
fig, ax = plt.subplots(figsize=(6.2, 3.2), dpi=300)
ax.set_xlim(-1, 14)
ax.set_ylim(-1, 5.5)
ax.axis('off')

# River banks
ax.axhline(4, color='darkgreen', lw=2.0) # South bank
ax.axhline(0, color='darkgreen', lw=2.0) # North bank
ax.fill_between([-1, 14], 0, 4, color='powderblue', alpha=0.35)
ax.text(6.5, 2.0, 'SÔNG (rộng 4 km)', ha='center', va='center', fontsize=11, color='teal', style='italic', family='serif')

# Points
xA, yA = 0, 4
xB, yB = 0, 0
xC, yC = 12, 0
xM, yM = 3, 0

ax.plot([xA, xM], [yA, yM], 'r-', lw=2.2, label='Cáp ngầm dưới sông (AM)')
ax.plot([xM, xC], [yM, yC], 'darkorange', lw=3.0, label='Cáp trên bờ (MC)')
ax.plot([xA, xB], [yA, yB], 'k--', lw=1.2)

for pt, name, pos in [((xA, yA), 'A (Trạm điện)', (xA-0.2, yA+0.3)),
                      ((xB, yB), 'B', (xB-0.2, yB-0.4)),
                      ((xM, yM), 'M', (xM, yM-0.45)),
                      ((xC, yC), 'C (Nhà máy)', (xC, yC-0.45))]:
    ax.plot(pt[0], pt[1], 'ko', markersize=5)
    ax.text(pos[0], pos[1], name, fontsize=10, fontweight='bold', family='serif')

# Dimensions
# AB = 4km
ax.annotate('', xy=(-0.4, 4), xytext=(-0.4, 0), arrowprops=dict(arrowstyle='<->', lw=1.0, color='black'))
ax.text(-0.6, 2, '4 km', ha='right', va='center', fontsize=9.5, family='serif')

# BM = x
ax.annotate('', xy=(xM, 0.4), xytext=(0, 0.4), arrowprops=dict(arrowstyle='<->', lw=1.0, color='black'))
ax.text(xM/2, 0.65, r'$x$', ha='center', va='center', fontsize=10, fontweight='bold', family='serif')

# BC = 12 km
ax.annotate('', xy=(12, -0.7), xytext=(0, -0.7), arrowprops=dict(arrowstyle='<->', lw=1.0, color='black'))
ax.text(6, -0.95, '12 km', ha='center', va='center', fontsize=9.5, family='serif')

plt.tight_layout()
plt.savefig('assets/de4_cap_dien_cau5.png', dpi=300)
plt.close()
print("Saved assets/de4_cap_dien_cau5.png")

# 6. Sơ đồ ngắm tranh cho Câu 6 Phần III
fig, ax = plt.subplots(figsize=(6, 3.8), dpi=300)
ax.set_xlim(-0.5, 5.5)
ax.set_ylim(-0.5, 6.0)
ax.axis('off')

# Ground
ax.plot([-0.2, 5.2], [0, 0], 'k-', lw=1.5)
for x_g in np.arange(0, 5.2, 0.3):
    ax.plot([x_g, x_g-0.15], [0, -0.2], 'gray', lw=0.8)
ax.text(2.5, -0.4, 'Mặt sàn', ha='center', va='center', fontsize=10.5, family='serif')

# Wall
ax.plot([4.5, 4.5], [0, 5.8], 'k-', lw=2.5)

# Painting on wall AB: B=2.4, A=5.1
ax.plot([4.5, 4.5], [2.4, 5.1], color='darkred', lw=6, solid_capstyle='butt')
ax.plot([4.35, 4.65], [5.1, 5.1], 'k-', lw=1.5)
ax.plot([4.35, 4.65], [2.4, 2.4], 'k-', lw=1.5)
ax.text(4.7, 5.1, 'A (mép trên)', ha='left', va='center', fontsize=10, fontweight='bold', family='serif')
ax.text(4.7, 2.4, 'B (mép dưới)', ha='left', va='center', fontsize=10, fontweight='bold', family='serif')
ax.text(4.7, 3.75, 'Bức tranh (2,7 m)', ha='left', va='center', fontsize=9.5, color='darkred', family='serif', rotation=-90)

# Person at x = 1.8 -> pos = 4.5 - 1.8 = 2.7
xp = 2.7
# Body
ax.plot([xp, xp], [0, 1.5], 'k-', lw=1.5)
# Head
circle = plt.Circle((xp, 1.6), 0.12, color='black', fill=False, lw=1.2)
ax.add_patch(circle)
ax.plot([xp-0.2, xp+0.2], [0, 0], 'k-', lw=2) # feet
ax.text(xp, 1.85, 'Mắt người (M)', ha='center', va='center', fontsize=10, fontweight='bold', family='serif')

# Eye level line MO
ax.plot([xp, 4.5], [1.5, 1.5], 'k--', lw=1)
ax.text(4.65, 1.5, 'O', ha='left', va='center', fontsize=10, family='serif')

# Sight lines MA and MB
ax.plot([xp, 4.5], [1.5, 5.1], 'b-', lw=1.3)
ax.plot([xp, 4.5], [1.5, 2.4], 'b-', lw=1.3)

# Angle theta arc
angle_arc = matplotlib.patches.Arc((xp, 1.5), 1.2, 1.2, angle=0, theta1=np.degrees(np.arctan2(0.9, 1.8)), theta2=np.degrees(np.arctan2(3.6, 1.8)), color='red', lw=1.8)
ax.add_patch(angle_arc)
ax.text(xp + 0.8, 2.05, r'$\theta$', fontsize=13, fontweight='bold', color='red', family='serif')

# Distance x dimension
ax.annotate('', xy=(4.5, 0.4), xytext=(xp, 0.4), arrowprops=dict(arrowstyle='<->', lw=1.2, color='black'))
ax.text((xp+4.5)/2, 0.65, r'$x$', ha='center', va='center', fontsize=12, fontweight='bold', family='serif')

# Height dimensions
# Eye height 1.5m
ax.annotate('', xy=(xp-0.35, 1.5), xytext=(xp-0.35, 0), arrowprops=dict(arrowstyle='<->', lw=1, color='black'))
ax.text(xp-0.45, 0.75, '1,5 m', ha='right', va='center', fontsize=9.5, family='serif')

# Bottom of painting 2.4m
ax.annotate('', xy=(3.8, 2.4), xytext=(3.8, 0), arrowprops=dict(arrowstyle='<->', lw=1, color='black'))
ax.text(3.65, 1.2, '2,4 m', ha='right', va='center', fontsize=9.5, family='serif')

# Painting height 2.7m
ax.annotate('', xy=(3.8, 5.1), xytext=(3.8, 2.4), arrowprops=dict(arrowstyle='<->', lw=1, color='darkred'))
ax.text(3.65, 3.75, '2,7 m', ha='right', va='center', fontsize=9.5, color='darkred', family='serif')

plt.tight_layout()
plt.savefig('assets/de4_ngam_tranh_cau6.png', dpi=300)
plt.close()
print("Saved assets/de4_ngam_tranh_cau6.png")
