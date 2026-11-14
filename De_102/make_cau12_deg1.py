import os
os.environ['MPLCONFIGDIR'] = os.path.abspath('assets/.mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Đồ thị hàm số phân thức bậc 1 / bậc 1: y = (x - 2)/(x - 1) = 1 - 1/(x - 1)
fig, ax = plt.subplots(figsize=(4.4, 4.2), dpi=300)

x1 = np.linspace(-3.2, 0.82, 300)
y1 = (x1 - 2) / (x1 - 1)

x2 = np.linspace(1.18, 5.2, 300)
y2 = (x2 - 2) / (x2 - 1)

# Vẽ 2 nhánh đồ thị
ax.plot(x1, y1, color='#c53030', lw=2.2)
ax.plot(x2, y2, color='#c53030', lw=2.2)

# Trục Ox, Oy
ax.axhline(0, color='black', lw=1.2)
ax.axvline(0, color='black', lw=1.2)

# Tiệm cận đứng x = 1, tiệm cận ngang y = 1
ax.axvline(1, color='#1e3a8a', ls='--', lw=1.5)
ax.axhline(1, color='#1e3a8a', ls='--', lw=1.5)

# Mũi tên trục
ax.annotate('', xy=(5.5, 0), xytext=(5.0, 0), arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
ax.annotate('', xy=(0, 4.8), xytext=(0, 4.3), arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

# Nhãn trục
ax.text(5.4, -0.45, r'$x$', fontsize=15, fontweight='bold', family='serif')
ax.text(-0.45, 4.6, r'$y$', fontsize=15, fontweight='bold', family='serif')
ax.text(-0.35, -0.45, r'$O$', fontsize=14, fontweight='bold', family='serif')

# Nhãn tiệm cận
ax.text(1.1, 4.0, r'$x=1$', fontsize=13, fontweight='bold', family='serif', color='#1e3a8a',
        bbox=dict(boxstyle='square,pad=0.15', facecolor='white', edgecolor='#1e3a8a', lw=0.8))
ax.text(4.0, 1.25, r'$y=1$', fontsize=13, fontweight='bold', family='serif', color='#1e3a8a',
        bbox=dict(boxstyle='square,pad=0.15', facecolor='white', edgecolor='#1e3a8a', lw=0.8))

# Các giao điểm: Cắt Oy tại (0; 2), Cắt Ox tại (2; 0)
ax.plot([0, 2], [2, 0], 'ko', ms=5.5)
ax.text(-0.45, 2.0, r'$2$', fontsize=14, fontweight='bold', va='center', family='serif')
ax.text(2.0, -0.45, r'$2$', fontsize=14, fontweight='bold', ha='center', family='serif')

# Số 1 trên trục Ox và Oy của tiệm cận
ax.plot([1, 0], [0, 1], 'bo', ms=4)
ax.text(1.15, -0.45, r'$1$', fontsize=14, fontweight='bold', family='serif', color='#1e3a8a')
ax.text(-0.45, 1.0, r'$1$', fontsize=14, fontweight='bold', va='center', family='serif', color='#1e3a8a')

# Tâm đối xứng I(1; 1)
ax.plot([1], [1], 'bo', ms=5)
ax.text(0.65, 1.25, r'$I$', fontsize=14, fontweight='bold', family='serif', color='#1e3a8a')

ax.set_xlim(-3.4, 5.6)
ax.set_ylim(-3.2, 5.0)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de2_khao_sat_dothi_cau12.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de2_khao_sat_dothi_cau12.png with degree 1/1 function!")
