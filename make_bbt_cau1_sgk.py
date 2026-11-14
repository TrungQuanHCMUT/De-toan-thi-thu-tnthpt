import os
os.environ['MPLCONFIGDIR'] = os.path.abspath('assets/.mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def make_bbt_cau1_sgk():
    fig, ax = plt.subplots(figsize=(6.4, 1.7), dpi=300)
    ax.axis('off')
    
    # Kích thước khung
    # X từ 0 đến 10, Y từ 0 đến 2.1
    # Đường ngang
    ax.plot([0, 10], [2.1, 2.1], 'k-', lw=1.1)   # Viền trên
    ax.plot([0, 10], [1.5, 1.5], 'k-', lw=1.1)   # Dưới hàng x
    ax.plot([0, 10], [0.95, 0.95], 'k-', lw=1.1) # Dưới hàng f'(x)
    ax.plot([0, 10], [0, 0], 'k-', lw=1.1)       # Viền dưới
    
    # Đường dọc duy nhất: viền ngoài và vạch ngăn cột nhãn
    ax.plot([0, 0], [0, 2.1], 'k-', lw=1.1)      # Viền trái
    ax.plot([10, 10], [0, 2.1], 'k-', lw=1.1)    # Viền phải
    ax.plot([1.3, 1.3], [0, 2.1], 'k-', lw=1.1)  # Vạch ngăn cột nhãn x, f', f (Duy nhất một vạch dọc này!)

    # Nhãn cột đầu
    ax.text(0.65, 1.78, r'$x$', ha='center', va='center', fontsize=11.5, family='serif')
    ax.text(0.65, 1.22, r"$f'(x)$", ha='center', va='center', fontsize=11.5, family='serif')
    ax.text(0.65, 0.48, r'$f(x)$', ha='center', va='center', fontsize=11.5, family='serif')

    # Hàng x: -\infty, -1, 2, +\infty
    ax.text(1.9, 1.78, r'$-\infty$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(4.4, 1.78, r'$-1$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(6.9, 1.78, r'$2$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(9.3, 1.78, r'$+\infty$', ha='center', va='center', fontsize=11, family='serif')

    # Hàng f'(x): +, 0, -, 0, +
    ax.text(3.15, 1.22, r'$+$', ha='center', va='center', fontsize=13, family='serif')
    ax.text(4.4, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(5.65, 1.22, r'$-$', ha='center', va='center', fontsize=13, family='serif')
    ax.text(6.9, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(8.15, 1.22, r'$+$', ha='center', va='center', fontsize=13, family='serif')

    # Hàng f(x):
    # -\infty ở thấp, lên 3 ở cao, xuống -1 ở thấp, lên +\infty ở cao
    ax.text(1.9, 0.16, r'$-\infty$', ha='center', va='center', fontsize=10.5, family='serif')
    ax.text(4.4, 0.78, r'$3$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(6.9, 0.16, r'$-1$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(9.3, 0.78, r'$+\infty$', ha='center', va='center', fontsize=10.5, family='serif')

    # Mũi tên biến thiên
    ax.annotate('', xy=(4.1, 0.72), xytext=(2.3, 0.22),
                arrowprops=dict(arrowstyle='->', lw=1.1, color='black'))
    ax.annotate('', xy=(6.6, 0.22), xytext=(4.7, 0.72),
                arrowprops=dict(arrowstyle='->', lw=1.1, color='black'))
    ax.annotate('', xy=(9.0, 0.72), xytext=(7.2, 0.22),
                arrowprops=dict(arrowstyle='->', lw=1.1, color='black'))

    plt.tight_layout()
    plt.savefig('assets/bbt_cau1_sgk.png', bbox_inches='tight', pad_inches=0.02)
    plt.close()
    print('Created assets/bbt_cau1_sgk.png')

if __name__ == '__main__':
    make_bbt_cau1_sgk()
