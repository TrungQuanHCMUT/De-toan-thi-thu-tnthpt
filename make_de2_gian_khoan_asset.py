import os
os.environ['MPLCONFIGDIR'] = os.path.abspath('assets/.mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

fig, ax = plt.subplots(figsize=(5.4, 3.2), dpi=300)
ax.set_xlim(-1, 12)
ax.set_ylim(-7.5, 2.5)
ax.axis('off')

# Biển (vùng y < 0) và Đất liền (vùng y >= 0)
poly_sea = Polygon([(-1, -7.5), (12, -7.5), (12, 0), (-1, 0)], closed=True,
                   facecolor='#e0f2fe', edgecolor='none', alpha=0.7)
ax.add_patch(poly_sea)

poly_land = Polygon([(-1, 0), (12, 0), (12, 2.5), (-1, 2.5)], closed=True,
                    facecolor='#fef3c7', edgecolor='none', alpha=0.6)
ax.add_patch(poly_land)

# Bờ biển: đường thẳng y = 0
ax.plot([-1, 12], [0, 0], color='#d97706', lw=2.2)
ax.text(11.5, 0.3, r'Bờ biển', fontsize=12, fontweight='bold', family='serif', color='#b45309', ha='right')
ax.text(11.5, -0.6, r'Biển', fontsize=12, fontweight='bold', family='serif', color='#0284c7', ha='right')

# Tọa độ các điểm:
# B = (0, 0)
# A = (0, -6) (giàn khoan ngoài biển)
# C = (10, 0) (nhà máy trên bờ)
# M = (4.5, 0) (điểm nối trên bờ)
B = np.array([0.0, 0.0])
A = np.array([0.0, -6.0])
C = np.array([10.0, 0.0])
M = np.array([4.5, 0.0])

# Đường ống ngầm AM dưới biển (nét màu xanh đậm / đỏ nổi bật)
ax.plot([A[0], M[0]], [A[1], M[1]], color='#dc2626', lw=2.2, ls='-', label='Đường ống ngầm')
# Đường ống trên bờ MC
ax.plot([M[0], C[0]], [M[1], C[1]], color='#ea580c', lw=3.0, ls='-', label='Đường ống trên bờ')

# Đoạn AB vuông góc bờ biển
ax.plot([A[0], B[0]], [A[1], B[1]], 'k--', lw=1.2)
# Ký hiệu góc vuông tại B
ax.plot([0, 0.6, 0.6], [-0.6, -0.6, 0], 'k-', lw=1.0)

# Điểm A, B, M, C
pts = [('A (Giàn khoan)', A, 'left', (-0.3, -6.5)),
       ('B', B, 'center', (0.0, 0.4)),
       ('M', M, 'center', (4.5, 0.4)),
       ('C (Nhà máy)', C, 'center', (10.0, 0.4))]

for name, pt, ha, text_pos in pts:
    ax.plot(pt[0], pt[1], 'ko', ms=6)
    ax.text(text_pos[0], text_pos[1], name, fontsize=12, fontweight='bold', family='serif')

# Kích thước:
# AB = 6 km
ax.text(-0.5, -3.0, r'$6\text{ km}$', fontsize=12, fontweight='bold', family='serif', ha='right', va='center')
# BM = x
ax.annotate('', xy=(M[0], -0.6), xytext=(B[0], -0.6), arrowprops=dict(arrowstyle='<->', lw=1.2, color='black'))
ax.text(2.25, -1.2, r'$x$', fontsize=13, fontweight='bold', family='serif', ha='center')
# BC = 10 km
ax.annotate('', xy=(C[0], 1.5), xytext=(B[0], 1.5), arrowprops=dict(arrowstyle='<->', lw=1.2, color='black'))
ax.text(5.0, 1.8, r'$10\text{ km}$', fontsize=12, fontweight='bold', family='serif', ha='center')

plt.tight_layout()
plt.savefig('assets/de2_khao_sat_gian_khoan_cau4.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de2_khao_sat_gian_khoan_cau4.png")
