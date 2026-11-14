import os
os.environ['MPLCONFIGDIR'] = os.path.abspath('assets/.mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# BBT Câu 1 Phần I (Đề 3): Bảng biến thiên chuẩn SGK Toán 12
fig, ax = plt.subplots(figsize=(6.5, 1.8), dpi=300)
ax.axis('off')

# Khung viền ngoài và các đường phân cách ngang/dọc chuẩn SGK
# Bề rộng bảng từ 0 đến 10, chiều cao từ 0 đến 2.1
ax.plot([0, 10], [2.1, 2.1], 'k-', lw=1.2)   # Viền trên
ax.plot([0, 10], [1.5, 1.5], 'k-', lw=1.2)   # Phân cách hàng x và f'(x)
ax.plot([0, 10], [0.95, 0.95], 'k-', lw=1.2) # Phân cách hàng f'(x) và f(x)
ax.plot([0, 10], [0, 0], 'k-', lw=1.2)       # Viền dưới
ax.plot([0, 0], [0, 2.1], 'k-', lw=1.2)       # Viền trái
ax.plot([10, 10], [0, 2.1], 'k-', lw=1.2)    # Viền phải
ax.plot([1.4, 1.4], [0, 2.1], 'k-', lw=1.2)  # Đường dọc duy nhất ngăn cách cột nhãn với vùng dữ liệu

# Cột tiêu đề (nhãn)
ax.text(0.7, 1.78, r'$x$', ha='center', va='center', fontsize=12, fontweight='bold', family='serif')
ax.text(0.7, 1.22, r"$f'(x)$", ha='center', va='center', fontsize=12, fontweight='bold', family='serif')
ax.text(0.7, 0.48, r'$f(x)$', ha='center', va='center', fontsize=12, fontweight='bold', family='serif')

# Hàng x
ax.text(2.0, 1.78, r'$-\infty$', ha='center', va='center', fontsize=11, family='serif')
ax.text(4.4, 1.78, r'$-1$', ha='center', va='center', fontsize=11, family='serif')
ax.text(7.0, 1.78, r'$1$', ha='center', va='center', fontsize=11, family='serif')
ax.text(9.3, 1.78, r'$+\infty$', ha='center', va='center', fontsize=11, family='serif')

# Hàng f'(x)
ax.text(3.2, 1.22, r'$+$', ha='center', va='center', fontsize=13, family='serif')
ax.text(4.4, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
ax.text(5.7, 1.22, r'$-$', ha='center', va='center', fontsize=13, family='serif')
ax.text(7.0, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
ax.text(8.2, 1.22, r'$+$', ha='center', va='center', fontsize=13, family='serif')

# Hàng f(x)
ax.text(2.0, 0.16, r'$-\infty$', ha='center', va='center', fontsize=10, family='serif')
ax.text(4.4, 0.78, r'$3$', ha='center', va='center', fontsize=11, family='serif')
ax.text(7.0, 0.16, r'$-1$', ha='center', va='center', fontsize=11, family='serif')
ax.text(9.3, 0.78, r'$+\infty$', ha='center', va='center', fontsize=10, family='serif')

# Mũi tên biến thiên (chuẩn SGK toán 12)
ax.annotate('', xy=(4.0, 0.72), xytext=(2.4, 0.22),
            arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
ax.annotate('', xy=(6.6, 0.22), xytext=(4.8, 0.72),
            arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
ax.annotate('', xy=(8.9, 0.72), xytext=(7.4, 0.22),
            arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

ax.set_xlim(-0.1, 10.1)
ax.set_ylim(-0.1, 2.2)
plt.savefig('assets/de3_khao_sat_bbt_cau1.png', bbox_inches='tight', pad_inches=0.02)
plt.close()
print("Saved assets/de3_khao_sat_bbt_cau1.png")
