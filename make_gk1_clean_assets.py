import os
os.environ['MPLCONFIGDIR'] = os.path.abspath('assets/.mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def make_bbt_cau1():
    fig, ax = plt.subplots(figsize=(6.5, 1.8), dpi=300)
    ax.axis('off')
    # Khung và vạch ngăn
    ax.plot([0, 10], [2.1, 2.1], 'k-', lw=1.2)   # Viền trên
    ax.plot([0, 10], [1.5, 1.5], 'k-', lw=1.2)   # Phân cách x và f'(x)
    ax.plot([0, 10], [0.95, 0.95], 'k-', lw=1.2) # Phân cách f'(x) và f(x)
    ax.plot([0, 10], [0, 0], 'k-', lw=1.2)       # Viền dưới
    ax.plot([0, 0], [0, 2.1], 'k-', lw=1.2)      # Viền trái
    ax.plot([10, 10], [0, 2.1], 'k-', lw=1.2)    # Viền phải
    ax.plot([1.4, 1.4], [0, 2.1], 'k-', lw=1.2)  # Ngăn cột nhãn

    # Nhãn
    ax.text(0.7, 1.78, r'$x$', ha='center', va='center', fontsize=12, fontweight='bold', family='serif')
    ax.text(0.7, 1.22, r"$f'(x)$", ha='center', va='center', fontsize=12, fontweight='bold', family='serif')
    ax.text(0.7, 0.48, r'$f(x)$', ha='center', va='center', fontsize=12, fontweight='bold', family='serif')

    # Hàng x
    ax.text(2.0, 1.78, r'$-\infty$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(4.4, 1.78, r'$-2$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(7.0, 1.78, r'$2$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(9.3, 1.78, r'$+\infty$', ha='center', va='center', fontsize=11, family='serif')

    # Hàng f'(x)
    ax.text(3.2, 1.22, r'$+$', ha='center', va='center', fontsize=13, family='serif')
    ax.text(4.4, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(5.7, 1.22, r'$-$', ha='center', va='center', fontsize=13, family='serif')
    ax.text(7.0, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(8.2, 1.22, r'$+$', ha='center', va='center', fontsize=13, family='serif')

    # Hàng f(x)
    ax.text(2.0, 0.16, r'$-\infty$', ha='center', va='center', fontsize=10, family='serif')
    ax.text(4.4, 0.78, r'$4$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(7.0, 0.16, r'$-3$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(9.3, 0.78, r'$+\infty$', ha='center', va='center', fontsize=10, family='serif')

    # Mũi tên biến thiên
    ax.annotate('', xy=(4.1, 0.72), xytext=(2.4, 0.22),
                arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
    ax.annotate('', xy=(6.7, 0.22), xytext=(4.7, 0.72),
                arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
    ax.annotate('', xy=(9.0, 0.72), xytext=(7.3, 0.22),
                arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

    ax.set_xlim(-0.1, 10.1)
    ax.set_ylim(-0.1, 2.2)
    plt.savefig('assets/gk1_clean_bbt_cau1.png', bbox_inches='tight', pad_inches=0.02)
    plt.close()
    print("Saved assets/gk1_clean_bbt_cau1.png")

def make_bxd_cau2():
    # Bảng xét dấu f'(x)
    fig, ax = plt.subplots(figsize=(6.5, 1.15), dpi=300)
    ax.axis('off')
    # Khung và vạch ngăn
    ax.plot([0, 10], [1.35, 1.35], 'k-', lw=1.2) # Viền trên
    ax.plot([0, 10], [0.7, 0.7], 'k-', lw=1.2)   # Phân cách x và f'(x)
    ax.plot([0, 10], [0, 0], 'k-', lw=1.2)       # Viền dưới
    ax.plot([0, 0], [0, 1.35], 'k-', lw=1.2)     # Viền trái
    ax.plot([10, 10], [0, 1.35], 'k-', lw=1.2)   # Viền phải
    ax.plot([1.4, 1.4], [0, 1.35], 'k-', lw=1.2) # Ngăn cột nhãn

    # Nhãn
    ax.text(0.7, 1.02, r'$x$', ha='center', va='center', fontsize=12, fontweight='bold', family='serif')
    ax.text(0.7, 0.35, r"$f'(x)$", ha='center', va='center', fontsize=12, fontweight='bold', family='serif')

    # Hàng x: -inf, -1, 1, 3, +inf
    ax.text(1.9, 1.02, r'$-\infty$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(3.7, 1.02, r'$-1$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(5.5, 1.02, r'$1$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(7.3, 1.02, r'$3$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(9.3, 1.02, r'$+\infty$', ha='center', va='center', fontsize=11, family='serif')

    # Hàng f'(x): +, 0, -, 0, +, 0, -
    ax.text(2.8, 0.35, r'$+$', ha='center', va='center', fontsize=13, family='serif')
    ax.text(3.7, 0.35, r'$0$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(4.6, 0.35, r'$-$', ha='center', va='center', fontsize=13, family='serif')
    ax.text(5.5, 0.35, r'$0$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(6.4, 0.35, r'$+$', ha='center', va='center', fontsize=13, family='serif')
    ax.text(7.3, 0.35, r'$0$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(8.3, 0.35, r'$-$', ha='center', va='center', fontsize=13, family='serif')

    ax.set_xlim(-0.1, 10.1)
    ax.set_ylim(-0.1, 1.45)
    plt.savefig('assets/gk1_clean_bxd_cau2.png', bbox_inches='tight', pad_inches=0.02)
    plt.close()
    print("Saved assets/gk1_clean_bxd_cau2.png")

def make_bbt_cau11():
    # BBT Câu 11: trùng phương, 3 cực trị (-1, 0, 1)
    fig, ax = plt.subplots(figsize=(6.5, 1.8), dpi=300)
    ax.axis('off')
    ax.plot([0, 10], [2.1, 2.1], 'k-', lw=1.2)   # Viền trên
    ax.plot([0, 10], [1.5, 1.5], 'k-', lw=1.2)   # Phân cách x và y'
    ax.plot([0, 10], [0.95, 0.95], 'k-', lw=1.2) # Phân cách y' và y
    ax.plot([0, 10], [0, 0], 'k-', lw=1.2)       # Viền dưới
    ax.plot([0, 0], [0, 2.1], 'k-', lw=1.2)      # Viền trái
    ax.plot([10, 10], [0, 2.1], 'k-', lw=1.2)    # Viền phải
    ax.plot([1.4, 1.4], [0, 2.1], 'k-', lw=1.2)  # Ngăn cột nhãn

    # Nhãn
    ax.text(0.7, 1.78, r'$x$', ha='center', va='center', fontsize=12, fontweight='bold', family='serif')
    ax.text(0.7, 1.22, r"$y'$", ha='center', va='center', fontsize=12, fontweight='bold', family='serif')
    ax.text(0.7, 0.48, r'$y$', ha='center', va='center', fontsize=12, fontweight='bold', family='serif')

    # Hàng x: -inf, -1, 0, 1, +inf
    ax.text(1.9, 1.78, r'$-\infty$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(3.7, 1.78, r'$-1$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(5.5, 1.78, r'$0$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(7.3, 1.78, r'$1$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(9.3, 1.78, r'$+\infty$', ha='center', va='center', fontsize=11, family='serif')

    # Hàng y': -, 0, +, 0, -, 0, +
    ax.text(2.8, 1.22, r'$-$', ha='center', va='center', fontsize=13, family='serif')
    ax.text(3.7, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(4.6, 1.22, r'$+$', ha='center', va='center', fontsize=13, family='serif')
    ax.text(5.5, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(6.4, 1.22, r'$-$', ha='center', va='center', fontsize=13, family='serif')
    ax.text(7.3, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(8.3, 1.22, r'$+$', ha='center', va='center', fontsize=13, family='serif')

    # Hàng y: +inf giảm về -2, tăng lên 3, giảm về -2, tăng lên +inf
    ax.text(1.9, 0.78, r'$+\infty$', ha='center', va='center', fontsize=10, family='serif')
    ax.text(3.7, 0.16, r'$-2$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(5.5, 0.78, r'$3$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(7.3, 0.16, r'$-2$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(9.3, 0.78, r'$+\infty$', ha='center', va='center', fontsize=10, family='serif')

    # Mũi tên biến thiên
    ax.annotate('', xy=(3.4, 0.22), xytext=(2.2, 0.72),
                arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
    ax.annotate('', xy=(5.2, 0.72), xytext=(4.0, 0.22),
                arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
    ax.annotate('', xy=(7.0, 0.22), xytext=(5.8, 0.72),
                arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
    ax.annotate('', xy=(9.0, 0.72), xytext=(7.6, 0.22),
                arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

    ax.set_xlim(-0.1, 10.1)
    ax.set_ylim(-0.1, 2.2)
    plt.savefig('assets/gk1_clean_bbt_cau11.png', bbox_inches='tight', pad_inches=0.02)
    plt.close()
    print("Saved assets/gk1_clean_bbt_cau11.png")

def make_bbt_p2_cau1():
    # BBT Phần II Câu 1: hàm bậc 3 cực đại tại -1 (y=3), cực tiểu tại 1 (y=-5)
    fig, ax = plt.subplots(figsize=(6.5, 1.8), dpi=300)
    ax.axis('off')
    ax.plot([0, 10], [2.1, 2.1], 'k-', lw=1.2)
    ax.plot([0, 10], [1.5, 1.5], 'k-', lw=1.2)
    ax.plot([0, 10], [0.95, 0.95], 'k-', lw=1.2)
    ax.plot([0, 0], [0, 2.1], 'k-', lw=1.2)
    ax.plot([10, 10], [0, 2.1], 'k-', lw=1.2)
    ax.plot([0, 10], [0, 0], 'k-', lw=1.2)
    ax.plot([1.4, 1.4], [0, 2.1], 'k-', lw=1.2)

    ax.text(0.7, 1.78, r'$x$', ha='center', va='center', fontsize=12, fontweight='bold', family='serif')
    ax.text(0.7, 1.22, r"$f'(x)$", ha='center', va='center', fontsize=12, fontweight='bold', family='serif')
    ax.text(0.7, 0.48, r'$f(x)$', ha='center', va='center', fontsize=12, fontweight='bold', family='serif')

    ax.text(2.0, 1.78, r'$-\infty$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(4.4, 1.78, r'$-1$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(7.0, 1.78, r'$1$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(9.3, 1.78, r'$+\infty$', ha='center', va='center', fontsize=11, family='serif')

    ax.text(3.2, 1.22, r'$+$', ha='center', va='center', fontsize=13, family='serif')
    ax.text(4.4, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(5.7, 1.22, r'$-$', ha='center', va='center', fontsize=13, family='serif')
    ax.text(7.0, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(8.2, 1.22, r'$+$', ha='center', va='center', fontsize=13, family='serif')

    ax.text(2.0, 0.16, r'$-\infty$', ha='center', va='center', fontsize=10, family='serif')
    ax.text(4.4, 0.78, r'$3$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(7.0, 0.16, r'$-5$', ha='center', va='center', fontsize=11, family='serif')
    ax.text(9.3, 0.78, r'$+\infty$', ha='center', va='center', fontsize=10, family='serif')

    ax.annotate('', xy=(4.1, 0.72), xytext=(2.4, 0.22),
                arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
    ax.annotate('', xy=(6.7, 0.22), xytext=(4.7, 0.72),
                arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
    ax.annotate('', xy=(9.0, 0.72), xytext=(7.3, 0.22),
                arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

    ax.set_xlim(-0.1, 10.1)
    ax.set_ylim(-0.1, 2.2)
    plt.savefig('assets/gk1_clean_bbt_p2_cau1.png', bbox_inches='tight', pad_inches=0.02)
    plt.close()
    print("Saved assets/gk1_clean_bbt_p2_cau1.png")

if __name__ == '__main__':
    make_bbt_cau1()
    make_bxd_cau2()
    make_bbt_cau11()
    make_bbt_p2_cau1()
