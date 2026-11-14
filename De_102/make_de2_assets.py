import os
os.environ['MPLCONFIGDIR'] = os.path.abspath('assets/.mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 1. BBT Câu 1 Phần I (de 2)
fig, ax = plt.subplots(figsize=(6.5, 1.8), dpi=300)
ax.axis('off')
ax.plot([0, 10], [1.5, 1.5], 'k-', lw=1.2)
ax.plot([0, 10], [0.95, 0.95], 'k-', lw=1.2)
ax.plot([1.3, 1.3], [0, 2.1], 'k-', lw=1.2)
ax.plot([0, 10], [2.1, 2.1], 'k-', lw=1.2)
ax.plot([0, 10], [0, 0], 'k-', lw=1.2)
ax.plot([0, 0], [0, 2.1], 'k-', lw=1.2)
ax.plot([10, 10], [0, 2.1], 'k-', lw=1.2)

ax.text(0.65, 1.78, r'$x$', ha='center', va='center', fontsize=12, family='serif')
ax.text(0.65, 1.22, r"$f'(x)$", ha='center', va='center', fontsize=12, family='serif')
ax.text(0.65, 0.48, r'$f(x)$', ha='center', va='center', fontsize=12, family='serif')

ax.text(1.9, 1.78, r'$-\infty$', ha='center', va='center', fontsize=11, family='serif')
ax.text(4.4, 1.78, r'$-2$', ha='center', va='center', fontsize=11, family='serif')
ax.text(7.2, 1.78, r'$0$', ha='center', va='center', fontsize=11, family='serif')
ax.text(9.4, 1.78, r'$+\infty$', ha='center', va='center', fontsize=11, family='serif')

ax.text(3.15, 1.22, r'$+$', ha='center', va='center', fontsize=12, family='serif')
ax.text(4.4, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
ax.text(5.8, 1.22, r'$-$', ha='center', va='center', fontsize=12, family='serif')
ax.text(7.2, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
ax.text(8.3, 1.22, r'$+$', ha='center', va='center', fontsize=12, family='serif')

ax.text(1.9, 0.15, r'$-\infty$', ha='center', va='center', fontsize=10, family='serif')
ax.text(4.4, 0.78, r'$3$', ha='center', va='center', fontsize=11, family='serif')
ax.text(7.2, 0.15, r'$-1$', ha='center', va='center', fontsize=11, family='serif')
ax.text(9.4, 0.78, r'$+\infty$', ha='center', va='center', fontsize=10, family='serif')

ax.annotate('', xy=(4.0, 0.7), xytext=(2.3, 0.2), arrowprops=dict(arrowstyle='->', lw=1.2, color='#c53030'))
ax.annotate('', xy=(6.8, 0.25), xytext=(4.8, 0.72), arrowprops=dict(arrowstyle='->', lw=1.2, color='#c53030'))
ax.annotate('', xy=(9.0, 0.7), xytext=(7.6, 0.25), arrowprops=dict(arrowstyle='->', lw=1.2, color='#c53030'))

ax.set_xlim(-0.1, 10.1)
ax.set_ylim(-0.1, 2.2)
plt.savefig('assets/de2_bbt_cau1.png', bbox_inches='tight', pad_inches=0.02)
plt.close()

# 2. Đồ thị Câu 5 Phần I (de 2): y = x^3 - 3x + 1
fig, ax = plt.subplots(figsize=(3.4, 3.2), dpi=300)
x = np.linspace(-2.1, 2.1, 300)
y = x**3 - 3*x + 1
ax.plot(x, y, color='#c53030', lw=1.6)
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)
ax.annotate('', xy=(2.3, 0), xytext=(2.0, 0), arrowprops=dict(arrowstyle='->', lw=1, color='black'))
ax.annotate('', xy=(0, 4.2), xytext=(0, 3.8), arrowprops=dict(arrowstyle='->', lw=1, color='black'))
ax.text(2.25, -0.38, r'$x$', fontsize=11, ha='center', family='serif')
ax.text(-0.25, 4.05, r'$y$', fontsize=11, va='center', family='serif')
ax.text(0.18, -0.3, r'$O$', fontsize=11, ha='center', family='serif')

ax.plot([-1, -1, 0], [0, 3, 3], 'k--', lw=0.9)
ax.plot([1, 1, 0], [0, -1, -1], 'k--', lw=0.9)
ax.text(-1, -0.4, r'$-1$', fontsize=10, ha='center', family='serif')
ax.text(1, 0.18, r'$1$', fontsize=10, ha='center', family='serif')
ax.text(0.2, 3, r'$3$', fontsize=10, va='center', family='serif')
ax.text(0.25, 1, r'$1$', fontsize=10, va='center', family='serif')
ax.text(-0.35, -1, r'$-1$', fontsize=10, va='center', family='serif')
ax.set_xlim(-2.3, 2.4)
ax.set_ylim(-2.5, 4.3)
ax.axis('off')
plt.savefig('assets/de2_dothi_cau5.png', bbox_inches='tight', pad_inches=0.03)
plt.close()

# 3. Hình minh họa Cà phê Newton Câu 2 Phần II
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.2, 2.6), dpi=300, gridspec_kw={'width_ratios': [1, 1.4]})

# ax1: Coffee cup & room temp sign
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')

# Table
ax1.plot([0, 10], [3, 3], 'k-', lw=1.5)
ax1.plot([2, 2], [0, 3], 'k-', lw=1.2)
ax1.plot([8, 8], [0, 3], 'k-', lw=1.2)

# Cup
cup_x = [3.2, 3.5, 5.5, 5.8]
cup_y = [7.5, 3.5, 3.5, 7.5]
ax1.plot(cup_x, cup_y, 'k-', lw=1.5)
# Saucer
ax1.plot([2.8, 6.2], [3.3, 3.3], 'k-', lw=2)
# Coffee surface
ax1.plot([3.5, 5.5], [6.5, 6.5], color='#c53030', lw=2)
# Handle
theta = np.linspace(-np.pi/2, np.pi/2, 50)
hx = 5.65 + 0.8 * np.cos(theta)
hy = 5.5 + 1.0 * np.sin(theta)
ax1.plot(hx, hy, 'k-', lw=1.5)
# Steam
ax1.plot([4.0, 3.8, 4.2], [7.8, 8.5, 9.2], 'k-', lw=0.9, alpha=0.7)
ax1.plot([4.8, 5.0, 4.7], [7.8, 8.6, 9.3], 'k-', lw=0.9, alpha=0.7)
# Sign: Nhiệt độ phòng 25°C
ax1.add_patch(plt.Rectangle((7.0, 4.5), 2.8, 3.5, fill=True, color='#f7fafc', ec='black', lw=1.2))
ax1.plot([8.4, 8.4], [3, 4.5], 'k-', lw=1.2)
ax1.text(8.4, 6.7, 'Nhiệt độ\nphòng\n25°C', fontsize=8.5, ha='center', va='center', weight='bold', family='serif')

# ax2: Decay curve
t = np.linspace(0, 45, 200)
T = 25 + 70 * (0.5**(t/10))
ax2.plot(t, T, color='#c53030', lw=2)
ax2.axhline(25, color='black', lw=0.8, ls='--')
ax2.axvline(0, color='black', lw=1)
ax2.axhline(0, color='black', lw=1)

# Annotate points
ax2.plot(0, 95, 'ko', ms=4)
ax2.plot(10, 60, 'ko', ms=4)
ax2.plot([10, 10], [0, 60], 'k--', lw=0.8)
ax2.plot([0, 10], [60, 60], 'k--', lw=0.8)

ax2.annotate('', xy=(48, 0), xytext=(44, 0), arrowprops=dict(arrowstyle='->', lw=1, color='black'))
ax2.annotate('', xy=(0, 105), xytext=(0, 98), arrowprops=dict(arrowstyle='->', lw=1, color='black'))

ax2.text(47, -7, r'$t$', fontsize=10, family='serif')
ax2.text(-3, 102, r'$T$', fontsize=10, family='serif')
ax2.text(-1, -7, r'$O$', fontsize=9.5, family='serif')
ax2.text(-5, 95, '95', fontsize=9.5, family='serif', va='center')
ax2.text(-5, 60, '60', fontsize=9.5, family='serif', va='center')
ax2.text(-5, 25, '25', fontsize=9.5, family='serif', va='center')
ax2.text(10, -7, '10', fontsize=9.5, family='serif', ha='center')
ax2.text(40, -7, '40', fontsize=9.5, family='serif', ha='center')
ax2.text(35, 30, r'$T = 25$', fontsize=9, style='italic', family='serif')

ax2.set_xlim(-6, 50)
ax2.set_ylim(-12, 108)
ax2.axis('off')

plt.tight_layout()
plt.savefig('assets/de2_hinh_cafe.png', bbox_inches='tight', pad_inches=0.02)
plt.close()

# 4. Hình minh họa Ao nuôi vịt Bài 32 Câu 6 Phần III
fig, ax = plt.subplots(figsize=(6.5, 2.8), dpi=300)
ax.set_aspect('equal')
ax.axis('off')

# Shoreline
ax.plot([-0.5, 5.5], [0, 0], 'k-', lw=1.4)
ax.text(0.3, -0.4, 'bờ kênh', fontsize=9.5, family='serif')

# House at A, H
H = np.array([0.5, 0])
A = np.array([0.5, 1.4])
ax.plot([A[0], H[0]], [A[1], H[1]], 'k-', lw=1.2)
# Right angle at H
ax.plot([H[0], H[0]+0.15, H[0]+0.15], [H[1]+0.15, H[1]+0.15, H[1]], 'k-', lw=0.9)

# House icon
ax.plot([0.3, 0.5, 0.7, 0.7, 0.3, 0.3], [1.4, 1.7, 1.4, 1.2, 1.2, 1.4], 'k-', lw=1.2)
ax.text(0.5, 1.85, 'Nhà', fontsize=9.5, ha='center', weight='bold', family='serif')

# Points M, I, C
M = np.array([2.0, 0])
C = np.array([4.4, 0])
I = (M + C) / 2
R = (C[0] - M[0]) / 2

# Circle
theta = np.linspace(0, 2*np.pi, 200)
cx = I[0] + R * np.cos(theta)
cy = I[1] + R * np.sin(theta)
# Lower half dashed, upper half dashed
ax.plot(cx[cy < 0], cy[cy < 0], 'k--', lw=1)
ax.plot(cx[cy >= 0], cy[cy >= 0], 'k--', lw=1)

# Point D on circle such that angle AMD = 120 deg
# Vector MA = A - M = (-1.5, 1.4)
# Angle of MA relative to positive x: arctan2(1.4, -1.5) = 137 deg
# Then angle AMD = 120 deg => vector MD has direction around 17 deg
angle_DMC = np.radians(25) # acute
D = np.array([M[0] + 2*R*np.cos(angle_DMC)*np.cos(angle_DMC), 2*R*np.cos(angle_DMC)*np.sin(angle_DMC)])

# Pink paths: A -> M -> D -> arc DC -> C
ax.plot([A[0], M[0]], [A[1], M[1]], color='#c53030', lw=2.2) # Bridge 1
ax.plot([M[0], D[0]], [M[1], D[1]], color='#c53030', lw=2.2) # Bridge 2

# Arc DC
theta_D = np.arctan2(D[1] - I[1], D[0] - I[0])
theta_arc = np.linspace(theta_D, 0, 100)
ax.plot(I[0] + R*np.cos(theta_arc), I[1] + R*np.sin(theta_arc), color='#c53030', lw=2.5)

# Arrows on path
ax.annotate('', xy=(1.3, 0.65), xytext=(1.0, 0.95), arrowprops=dict(arrowstyle='->', lw=1.5, color='#c53030'))
ax.annotate('', xy=(2.7, 0.4), xytext=(2.3, 0.2), arrowprops=dict(arrowstyle='->', lw=1.5, color='#c53030'))

# Points markers and labels
for pt, name in [(A, 'A'), (H, 'H'), (M, 'M'), (C, 'C'), (D, 'D'), (I, 'I')]:
    ax.plot(pt[0], pt[1], 'ko', ms=4)
ax.text(A[0]-0.15, A[1], 'A', fontsize=10, weight='bold', ha='right', family='serif')
ax.text(H[0]-0.15, H[1]-0.15, 'H', fontsize=10, weight='bold', ha='right', family='serif')
ax.text(M[0], M[1]-0.3, 'M', fontsize=10, weight='bold', ha='center', color='#c53030', family='serif')
ax.text(C[0], C[1]-0.3, 'C', fontsize=10, weight='bold', ha='center', family='serif')
ax.text(D[0]+0.1, D[1]+0.15, 'D', fontsize=10, weight='bold', family='serif')
ax.text(I[0], I[1]-0.3, 'I', fontsize=10, style='italic', ha='center', family='serif')

# Duck coop icon at C
ax.plot([4.6, 4.8, 5.0, 5.0, 4.6, 4.6], [0.3, 0.5, 0.3, 0, 0, 0.3], 'k-', lw=1.2)
ax.text(4.8, -0.4, 'chuồng\nvịt', fontsize=9.5, ha='center', family='serif')

ax.set_xlim(-0.7, 5.7)
ax.set_ylim(-1.4, 2.0)

plt.tight_layout()
plt.savefig('assets/de2_hinh_ao_vit.png', bbox_inches='tight', pad_inches=0.02)
plt.close()

print("All De 2 assets generated successfully!")
