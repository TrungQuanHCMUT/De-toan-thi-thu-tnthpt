import os
os.environ['MPLCONFIGDIR'] = os.path.abspath('assets/.mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_book_page():
    fig, ax = plt.subplots(figsize=(3.5, 4.2), dpi=300)
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-0.5, 8.5)
    ax.axis('off')

    # Trang sách ngoài ABCD
    # D: top-left (0.8, 7.8), C: top-right (5.2, 7.8), B: bottom-right (5.2, 0.8), A: bottom-left (0.8, 0.8)
    x0, y0 = 0.8, 0.8
    w, h = 4.4, 7.0
    rect_outer = patches.Rectangle((x0, y0), w, h, linewidth=1.5, edgecolor='black', facecolor='white')
    ax.add_patch(rect_outer)

    # Đỉnh ABCD
    ax.text(x0 - 0.25, y0, r'$A$', fontsize=13, fontstyle='italic', family='serif', va='center', ha='center')
    ax.text(x0 + w + 0.25, y0, r'$B$', fontsize=13, fontstyle='italic', family='serif', va='center', ha='center')
    ax.text(x0 + w + 0.25, y0 + h, r'$C$', fontsize=13, fontstyle='italic', family='serif', va='center', ha='center')
    ax.text(x0 - 0.25, y0 + h, r'$D$', fontsize=13, fontstyle='italic', family='serif', va='center', ha='center')

    # Phần trình bày MNPQ
    # lề trái 15, phải 16, trên 22, dưới 22
    # Tỉ lệ w = 4.4, lề trái = 0.7, lề phải = 0.75, lề dưới = 1.0, lề trên = 1.0
    mx = x0 + 0.7
    my = y0 + 1.0
    mw = w - (0.7 + 0.75)
    mh = h - 2.0
    rect_inner = patches.Rectangle((mx, my), mw, mh, linewidth=1.2, edgecolor='black', facecolor='#c94c7b')
    ax.add_patch(rect_inner)

    # Đỉnh MNPQ
    ax.text(mx - 0.25, my, r'$M$', fontsize=12, fontstyle='italic', family='serif', va='center', ha='center')
    ax.text(mx + mw + 0.25, my, r'$N$', fontsize=12, fontstyle='italic', family='serif', va='center', ha='center')
    ax.text(mx + mw + 0.25, my + mh, r'$P$', fontsize=12, fontstyle='italic', family='serif', va='center', ha='center')
    ax.text(mx - 0.25, my + mh, r'$Q$', fontsize=12, fontstyle='italic', family='serif', va='center', ha='center')

    # Đường gióng nét đứt
    # Lề trái trên
    ax.plot([x0, mx], [my + mh, my + mh], 'k--', lw=0.9)
    ax.text(x0 + 0.35, my + mh + 0.3, '15', fontsize=11, family='serif', ha='center', va='bottom')

    # Lề phải trên
    ax.plot([mx + mw, x0 + w], [my + mh, my + mh], 'k--', lw=0.9)
    ax.text(mx + mw + 0.37, my + mh + 0.3, '16', fontsize=11, family='serif', ha='center', va='bottom')

    # Lề dưới
    ax.plot([mx, mx], [y0, my], 'k--', lw=0.9)
    ax.text(mx + 0.4, y0 + 0.45, '22', fontsize=11, family='serif', ha='center', va='center')

    plt.tight_layout()
    plt.savefig('assets/hinh_trang_sach_cau4.png', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    print('Created assets/hinh_trang_sach_cau4.png')

def draw_water_ripples():
    fig, ax = plt.subplots(figsize=(3.4, 3.4), dpi=300)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.axis('off')

    # Vành ngoài cùng có màu hồng
    c_outer = patches.Circle((0, 0), 1.1, facecolor='#ffe0ec', edgecolor='#e60067', lw=1.5)
    ax.add_patch(c_outer)

    # Vòng tròn thứ 2 (biên trong của dải màu)
    c_mid = patches.Circle((0, 0), 0.85, facecolor='white', edgecolor='black', lw=1.2)
    ax.add_patch(c_mid)

    # Vòng tròn trong cùng
    c_in = patches.Circle((0, 0), 0.45, facecolor='none', edgecolor='black', lw=1.0)
    ax.add_patch(c_in)

    # Tâm O
    ax.plot(0, 0, 'ko', markersize=3.5)
    ax.text(-0.08, -0.15, r'$O$', fontsize=13, fontstyle='italic', family='serif', ha='right', va='top')

    # Vector bán kính r
    # Vẽ mũi tên hướng góc 35 độ
    import numpy as np
    theta = np.deg2rad(35)
    r_len = 1.25
    ax.annotate('', xy=(r_len*np.cos(theta), r_len*np.sin(theta)), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', lw=1.4, color='#e60067'))
    # Điểm cắt trên vòng tròn ngoài
    ax.plot(1.1*np.cos(theta), 1.1*np.sin(theta), 'o', color='#e60067', markersize=3.5)
    # Nhãn r
    ax.text(0.65*np.cos(theta) - 0.08, 0.65*np.sin(theta) + 0.1, r'$r$', fontsize=13, fontstyle='italic', family='serif')

    plt.tight_layout()
    plt.savefig('assets/hinh_gon_song_cau6.png', bbox_inches='tight', pad_inches=0.03)
    plt.close()
    print('Created assets/hinh_gon_song_cau6.png')

if __name__ == '__main__':
    draw_book_page()
    draw_water_ripples()
