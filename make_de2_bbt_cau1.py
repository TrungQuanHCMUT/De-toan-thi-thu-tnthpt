import os
os.environ['MPLCONFIGDIR'] = os.path.abspath('assets/.mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# BBT Câu 1 Phần I (Đề 2): Bảng biến thiên hàm số bậc ba
fig, ax = plt.subplots(figsize=(7.5, 2.2), dpi=300)
ax.axis('off')

# Kẻ các đường khung
ax.plot([0, 10], [1.5, 1.5], 'k-', lw=1.2)
ax.plot([0, 10], [0.95, 0.95], 'k-', lw=1.2)
ax.plot([1.4, 1.4], [0, 2.1], 'k-', lw=1.2)
ax.plot([0, 10], [2.1, 2.1], 'k-', lw=1.2)
ax.plot([0, 10], [0, 0], 'k-', lw=1.2)
ax.plot([0, 0], [0, 2.1], 'k-', lw=1.2)
ax.plot([10, 10], [0, 2.1], 'k-', lw=1.2)

# Cột tiêu đề
ax.text(0.7, 1.78, r'$x$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(0.7, 1.22, r"$f'(x)$", ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(0.7, 0.48, r'$f(x)$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')

# Hàng x
ax.text(2.0, 1.78, r'$-\infty$', ha='center', va='center', fontsize=13, fontweight='bold', family='serif')
ax.text(4.4, 1.78, r'$-2$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(7.2, 1.78, r'$0$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(9.4, 1.78, r'$+\infty$', ha='center', va='center', fontsize=13, fontweight='bold', family='serif')

# Hàng f'(x)
ax.text(3.2, 1.22, r'$+$', ha='center', va='center', fontsize=15, fontweight='bold', family='serif')
ax.text(4.4, 1.22, r'$0$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(5.8, 1.22, r'$-$', ha='center', va='center', fontsize=15, fontweight='bold', family='serif')
ax.text(7.2, 1.22, r'$0$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(8.3, 1.22, r'$+$', ha='center', va='center', fontsize=15, fontweight='bold', family='serif')

# Hàng f(x)
ax.text(2.0, 0.16, r'$-\infty$', ha='center', va='center', fontsize=12, fontweight='bold', family='serif')
ax.text(4.4, 0.78, r'$3$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(7.2, 0.16, r'$-1$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(9.4, 0.78, r'$+\infty$', ha='center', va='center', fontsize=12, fontweight='bold', family='serif')

# Mũi tên biến thiên màu đỏ sắc nét
ax.annotate('', xy=(4.0, 0.72), xytext=(2.4, 0.22), arrowprops=dict(arrowstyle='->', lw=1.5, color='#c53030'))
ax.annotate('', xy=(6.8, 0.25), xytext=(4.8, 0.72), arrowprops=dict(arrowstyle='->', lw=1.5, color='#c53030'))
ax.annotate('', xy=(9.0, 0.72), xytext=(7.6, 0.25), arrowprops=dict(arrowstyle='->', lw=1.5, color='#c53030'))

ax.set_xlim(-0.1, 10.1)
ax.set_ylim(-0.1, 2.2)
plt.savefig('assets/de2_khao_sat_bbt_cau1.png', bbox_inches='tight', pad_inches=0.02)
plt.close()
print("Saved assets/de2_khao_sat_bbt_cau1.png")
