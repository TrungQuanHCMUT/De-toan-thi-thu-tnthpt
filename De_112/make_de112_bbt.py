import os
os.environ['MPLCONFIGDIR'] = os.path.abspath('assets/.mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['svg.fonttype'] = 'path'

def generate_bbt(base_name, x_vals, fprime_vals, f_points, arrows, title_col=(r'$x$', r"$f'(x)$", r'$f(x)$')):
    fig, ax = plt.subplots(figsize=(6.0, 1.55), dpi=300)
    ax.axis('off')
    
    lw = 0.95
    # Outer box and horizontal dividing lines
    ax.plot([0, 10], [2.1, 2.1], 'k-', lw=lw)   # Viền trên
    ax.plot([0, 10], [1.44, 1.44], 'k-', lw=lw) # Dưới hàng x
    ax.plot([0, 10], [0.90, 0.90], 'k-', lw=lw) # Dưới hàng f'(x)
    ax.plot([0, 10], [0, 0], 'k-', lw=lw)       # Viền dưới
    
    ax.plot([0, 0], [0, 2.1], 'k-', lw=lw)      # Viền trái
    ax.plot([10, 10], [0, 2.1], 'k-', lw=lw)    # Viền phải
    ax.plot([1.25, 1.25], [0, 2.1], 'k-', lw=lw) # Vạch ngăn cột tiêu đề
    
    # Tiêu đề cột
    ax.text(0.62, 1.77, title_col[0], ha='center', va='center', fontsize=12)
    ax.text(0.62, 1.17, title_col[1], ha='center', va='center', fontsize=12)
    ax.text(0.62, 0.45, title_col[2], ha='center', va='center', fontsize=12)
    
    # Hàng x
    for x_c, txt in x_vals:
        ax.text(x_c, 1.77, txt, ha='center', va='center', fontsize=11)
        
    # Hàng f'(x)
    for x_c, txt in fprime_vals:
        fs = 13 if txt in [r'$+$', r'$-$'] else 11.5
        ax.text(x_c, 1.17, txt, ha='center', va='center', fontsize=fs)
        
    # Hàng f(x)
    for x_c, y_c, txt in f_points:
        ax.text(x_c, y_c, txt, ha='center', va='center', fontsize=11.5)
        
    # Mũi tên biến thiên
    for xs, ys, xe, ye in arrows:
        ax.annotate('', xy=(xe, ye), xytext=(xs, ys),
                    arrowprops=dict(arrowstyle='->', lw=1.0, color='black', shrinkA=0, shrinkB=0))
        
    ax.set_xlim(-0.03, 10.03)
    ax.set_ylim(-0.03, 2.13)
    plt.tight_layout()
    plt.savefig(f'assets/{base_name}.png', bbox_inches='tight', pad_inches=0.01)
    plt.savefig(f'assets/{base_name}.svg', bbox_inches='tight', pad_inches=0.01)
    plt.close()
    print(f"Generated assets/{base_name}.png and .svg")

# Câu 1: x in {-\infty, -1, 3, +\infty}, f'(x) in {+, 0, -, 0, +}, f(x) in {-\infty, 4, -2, +\infty}
generate_bbt(
    'de112_bbt_cau1',
    x_vals=[(1.85, r'$-\infty$'), (4.3, r'$-1$'), (6.9, r'$3$'), (9.35, r'$+\infty$')],
    fprime_vals=[(3.05, r'$+$'), (4.3, r'$0$'), (5.6, r'$-$'), (6.9, r'$0$'), (8.1, r'$+$')],
    f_points=[(1.85, 0.16, r'$-\infty$'), (4.3, 0.73, r'$4$'), (6.9, 0.16, r'$-2$'), (9.35, 0.73, r'$+\infty$')],
    arrows=[(2.28, 0.22, 3.98, 0.67), (4.62, 0.67, 6.55, 0.22), (7.25, 0.22, 8.95, 0.67)]
)

# Câu 7: x in {-\infty, -2, 1, +\infty}, f'(x) in {+, 0, -, 0, +}, f(x) in {-\infty, 3, -2, +\infty}
generate_bbt(
    'de112_bbt_cau7',
    x_vals=[(1.85, r'$-\infty$'), (4.3, r'$-2$'), (6.9, r'$1$'), (9.35, r'$+\infty$')],
    fprime_vals=[(3.05, r'$+$'), (4.3, r'$0$'), (5.6, r'$-$'), (6.9, r'$0$'), (8.1, r'$+$')],
    f_points=[(1.85, 0.16, r'$-\infty$'), (4.3, 0.73, r'$3$'), (6.9, 0.16, r'$-2$'), (9.35, 0.73, r'$+\infty$')],
    arrows=[(2.28, 0.22, 3.98, 0.67), (4.62, 0.67, 6.55, 0.22), (7.25, 0.22, 8.95, 0.67)]
)
