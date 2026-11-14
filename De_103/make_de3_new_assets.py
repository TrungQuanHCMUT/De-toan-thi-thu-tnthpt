import os
os.environ['MPLCONFIGDIR'] = os.path.abspath('assets/.mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 1. Đồ thị công suất P(R) = 144R / (R + 2)^2 cho Câu 2 Phần II
fig, ax = plt.subplots(figsize=(4.6, 2.4), dpi=300)
R = np.linspace(0, 12, 300)
P = (144 * R) / (R + 2)**2
ax.plot(R, P, color='#c53030', lw=1.8)
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)

ax.annotate('', xy=(12.5, 0), xytext=(12.0, 0), arrowprops=dict(arrowstyle='->', lw=1, color='black'))
ax.annotate('', xy=(0, 21), xytext=(0, 19.5), arrowprops=dict(arrowstyle='->', lw=1, color='black'))
ax.text(12.3, -1.8, r'$R\,(\Omega)$', fontsize=10, family='serif')
ax.text(-0.5, 20.2, r'$P\text{ (W)}$', fontsize=10, family='serif')
ax.text(-0.4, -1.5, r'$O$', fontsize=9.5, family='serif')

# Peak at R = 2, P = 18
ax.plot([2, 2, 0], [0, 18, 18], 'k--', lw=0.9)
ax.plot(2, 18, 'ro', ms=4)
ax.text(2, -1.7, r'$2$', fontsize=9.5, ha='center', family='serif')
ax.text(-0.4, 18, r'$18$', fontsize=9.5, ha='right', family='serif')

# Value P = 16 at R = 1 and R = 4
ax.plot([1, 1, 0], [0, 16, 16], 'k:', lw=0.8)
ax.plot([4, 4, 0], [0, 16, 16], 'k:', lw=0.8)
ax.text(1, -1.7, r'$1$', fontsize=9, ha='center', family='serif')
ax.text(4, -1.7, r'$4$', fontsize=9, ha='center', family='serif')
ax.text(-0.4, 15.8, r'$16$', fontsize=9, ha='right', family='serif')

ax.set_xlim(-0.8, 13)
ax.set_ylim(-2.5, 22)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de3_mach_dien_cau2.png', bbox_inches='tight', pad_inches=0.02)
plt.close()

# 2. Hình vẽ tam giác ABC và đường gấp khúc CBDEFGH... cho Câu 3 Phần II (từ Image 1)
fig, ax = plt.subplots(figsize=(3.4, 3.4), dpi=300)
ax.axis('off')

# Triangle ABC: AC = 2*AB, BC = 10
# Let A be at top: A = (0, 6)
# B = (-1.8, 2.0)
# C = (1.5, 0.0)
A = np.array([0.0, 5.5])
B = np.array([-1.5, 1.8])
C = np.array([1.2, 0.0])

# D on AC: AD = 1/4 AC => D = A + 0.25*(C - A)
D = A + 0.25 * (C - A)
# E on AB: AE = 1/4 AB => E = A + 0.25*(B - A)
E = A + 0.25 * (B - A)
# F on AD: AF = 1/4 AD => F = A + 0.25*(D - A)
F = A + 0.25 * (D - A)
# G on AE: AG = 1/4 AE => G = A + 0.25*(E - A)
G = A + 0.25 * (E - A)

# Triangle ABC outline
ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', lw=1.2)
ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=1.2)
ax.plot([C[0], A[0]], [C[1], A[1]], 'k-', lw=1.2)

# Zigzag fold line: C -> B -> D -> E -> F -> G
ax.plot([C[0], B[0]], [C[1], B[1]], 'k-', lw=1.2)
ax.plot([B[0], D[0]], [B[1], D[1]], 'k-', lw=1.2)
ax.plot([D[0], E[0]], [D[1], E[1]], 'k-', lw=1.2)
ax.plot([E[0], F[0]], [E[1], F[1]], 'k-', lw=1.2)
ax.plot([F[0], G[0]], [F[1], G[1]], 'k-', lw=1.2)

# Points
pts = [(A, 'A', (0, 0.18)),
       (B, 'B', (-0.22, -0.05)),
       (C, 'C', (0.18, -0.05)),
       (D, 'D', (0.18, 0)),
       (E, 'E', (-0.2, 0)),
       (F, 'F', (0.16, 0.05))]

for p, name, offset in pts:
    ax.plot(p[0], p[1], 'ko', ms=3.5)
    ax.text(p[0] + offset[0], p[1] + offset[1], name, fontsize=10.5, family='serif', style='italic', ha='center', va='center')

ax.set_xlim(-2.0, 2.0)
ax.set_ylim(-0.3, 6.0)
ax.set_aspect('equal')
plt.tight_layout()
plt.savefig('assets/de3_tam_giac_gapkhuc.png', bbox_inches='tight', pad_inches=0.02)
plt.close()

# 3. Hình vẽ bài toán chèo thuyền qua sông cho Câu 6 Phần III
fig, ax = plt.subplots(figsize=(5.6, 2.6), dpi=300)
ax.axis('off')

# River banks: two parallel horizontal lines at y = 0 and y = 2.4
ax.plot([-0.5, 7.5], [0, 0], color='#2b6cb0', lw=2)
ax.plot([-0.5, 7.5], [2.4, 2.4], color='#2b6cb0', lw=2)
ax.fill_between([-0.5, 7.5], 0, 2.4, color='#ebf8ff', alpha=0.7)

# River text
ax.text(4.0, 1.2, 'dòng sông (rộng 3 km)', fontsize=10, color='#2b6cb0', style='italic', ha='center', va='center', family='serif')

# Points: A = (0.5, 0), B = (0.5, 2.4), C = (6.5, 2.4), M = (2.3, 2.4)
A = np.array([0.5, 0.0])
B = np.array([0.5, 2.4])
M = np.array([2.5, 2.4])
C = np.array([6.5, 2.4])

# Perpendicular line AB
ax.plot([A[0], B[0]], [A[1], B[1]], 'k--', lw=1)
# Right angle symbol at B
ax.plot([B[0], B[0]+0.2, B[0]+0.2], [B[1]-0.2, B[1]-0.2, B[1]], 'k-', lw=0.8)

# Path: A -> M (rowing) in red, M -> C (running) in red
ax.plot([A[0], M[0]], [A[1], M[1]], color='#c53030', lw=2.4)
ax.plot([M[0], C[0]], [M[1], C[1]], color='#c53030', lw=2.4)

# Arrows
ax.annotate('', xy=(1.5, 1.2), xytext=(1.2, 0.84), arrowprops=dict(arrowstyle='->', lw=1.6, color='#c53030'))
ax.annotate('', xy=(4.6, 2.4), xytext=(4.2, 2.4), arrowprops=dict(arrowstyle='->', lw=1.6, color='#c53030'))

# Labels on path
ax.text(1.2, 1.45, 'chèo thuyền (6 km/h)', fontsize=9, color='#c53030', ha='center', rotation=43, family='serif')
ax.text(4.5, 2.65, 'chạy bộ (10 km/h)', fontsize=9, color='#c53030', ha='center', family='serif')

# Markers and labels
for pt, name, offset in [
    (A, 'A', (0, -0.3)),
    (B, 'B', (0, 0.25)),
    (M, 'M', (0, 0.25)),
    (C, 'C', (0, 0.25))
]:
    ax.plot(pt[0], pt[1], 'ko', ms=4)
    if name == 'M':
        ax.text(pt[0] + offset[0], pt[1] + offset[1], name, fontsize=11, fontweight='bold', color='#c53030', ha='center', family='serif')
    else:
        ax.text(pt[0] + offset[0], pt[1] + offset[1], name, fontsize=11, fontweight='bold', ha='center', family='serif')

# Dimensions labels
ax.text(0.1, 1.2, r'$3\text{ km}$', fontsize=9.5, ha='right', va='center', family='serif')
ax.text((B[0]+C[0])/2, 2.9, r'$BC = 8\text{ km}$', fontsize=9.5, ha='center', family='serif')

# Dimension arrow for BC
ax.annotate('', xy=(C[0], 2.8), xytext=(B[0], 2.8),
            arrowprops=dict(arrowstyle='<->', lw=0.9, color='black'))

ax.set_xlim(-0.6, 7.6)
ax.set_ylim(-0.6, 3.2)
plt.tight_layout()
plt.savefig('assets/de3_cheo_thuyen_cau6.png', bbox_inches='tight', pad_inches=0.02)
plt.close()

print("All new De 3 assets generated successfully!")
