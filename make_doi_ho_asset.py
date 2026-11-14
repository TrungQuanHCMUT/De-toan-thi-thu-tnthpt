import os
os.environ['MPLCONFIGDIR'] = os.path.abspath('assets/.mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def draw_coastal_profile():
    fig, ax = plt.subplots(figsize=(6.2, 2.6), dpi=300)
    
    # Range of x
    x = np.linspace(-0.3, 3.5, 500)
    # Cubic function: f(x) = k * x * (x - 2) * (x - 3)
    # Let k = 0.55 / f(x_peak) so that the hill peak is around 0.55 in scale,
    # but for drawing visually, we can set k = 1 so the height is visually clear
    k = 1.0
    y = k * x * (x - 2) * (x - 3)
    
    # Plot curve
    ax.plot(x, y, color='#d91414', lw=2.0)
    
    # Axes
    ax.axhline(0, color='black', lw=1.0)
    ax.axvline(0, color='black', lw=1.0)
    
    # Shading
    # Đồi: from 0 to 2, y >= 0
    x_doi = np.linspace(0, 2, 200)
    y_doi = k * x_doi * (x_doi - 2) * (x_doi - 3)
    ax.fill_between(x_doi, 0, y_doi, color='#e0e0e0', hatch='..', alpha=0.5)
    
    # Hồ: from 2 to 3, y <= 0
    x_ho = np.linspace(2, 3, 200)
    y_ho = k * x_ho * (x_ho - 2) * (x_ho - 3)
    ax.fill_between(x_ho, 0, y_ho, color='#adc6ff', alpha=0.8)
    
    # Núi: from 3 to 3.4, y >= 0
    x_nui = np.linspace(3, 3.4, 100)
    y_nui = k * x_nui * (x_nui - 2) * (x_nui - 3)
    ax.fill_between(x_nui, 0, y_nui, color='#e0e0e0', hatch='..', alpha=0.5)
    
    # Text labels
    ax.text(0.1, -0.28, r'$O$', fontsize=12, fontweight='bold', fontstyle='italic', family='serif')
    ax.text(2.0, 0.12, r'$A$', fontsize=12, fontstyle='italic', family='serif', ha='center')
    ax.text(2.88, 0.12, r'$B$', fontsize=12, fontstyle='italic', family='serif', ha='center')
    
    # Region names
    ax.text(-0.35, -0.05, 'Biển', fontsize=11, family='serif', fontweight='bold', ha='right', va='center')
    ax.text(0.9, 1.25, 'Đồi', fontsize=11, family='serif', fontweight='bold', ha='center')
    ax.text(2.5, -0.42, 'Hồ', fontsize=11, family='serif', fontweight='bold', color='#002387', ha='center')
    
    # Núi box
    ax.text(3.18, 0.9, 'Núi', fontsize=11, family='serif', fontweight='bold', ha='center',
            bbox=dict(boxstyle='square,pad=0.25', facecolor='#e6e6e6', edgecolor='none'))
    
    # Axis arrows and labels
    ax.annotate('', xy=(3.6, 0), xytext=(3.45, 0), arrowprops=dict(arrowstyle='->', lw=1.0, color='black'))
    ax.text(3.62, -0.05, r'$x$', fontsize=11, fontstyle='italic', family='serif', va='center')
    
    ax.annotate('', xy=(0, 2.3), xytext=(0, 2.15), arrowprops=dict(arrowstyle='->', lw=1.0, color='black'))
    ax.text(0.08, 2.25, r'$y$', fontsize=11, fontstyle='italic', family='serif', va='center')
    
    ax.set_xlim(-0.6, 3.75)
    ax.set_ylim(-0.8, 2.35)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('assets/hinh_cat_doi_ho_cau2.png', bbox_inches='tight', pad_inches=0.02)
    plt.close()
    print('Created assets/hinh_cat_doi_ho_cau2.png')

if __name__ == '__main__':
    draw_coastal_profile()
