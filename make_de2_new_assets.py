import os
os.environ['MPLCONFIGDIR'] = os.path.abspath('assets/.mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Wedge, Arc, Rectangle

# 1. Bảng xét dấu đạo hàm f'(x) cho Câu 1 Phần I mới
fig, ax = plt.subplots(figsize=(7.2, 1.6), dpi=300)
ax.axis('off')

# Kẻ bảng 2 dòng
ax.plot([0, 10], [1.1, 1.1], 'k-', lw=1.2)
ax.plot([0, 10], [0, 0], 'k-', lw=1.2)
ax.plot([0, 10], [2.2, 2.2], 'k-', lw=1.2)
ax.plot([1.5, 1.5], [0, 2.2], 'k-', lw=1.2)
ax.plot([0, 0], [0, 2.2], 'k-', lw=1.2)
ax.plot([10, 10], [0, 2.2], 'k-', lw=1.2)

ax.text(0.75, 1.65, r'$x$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(0.75, 0.55, r"$f'(x)$", ha='center', va='center', fontsize=14, fontweight='bold', family='serif')

ax.text(2.1, 1.65, r'$-\infty$', ha='center', va='center', fontsize=13, fontweight='bold', family='serif')
ax.text(4.2, 1.65, r'$-1$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(6.3, 1.65, r'$2$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(8.2, 1.65, r'$4$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(9.4, 1.65, r'$+\infty$', ha='center', va='center', fontsize=13, fontweight='bold', family='serif')

ax.text(3.15, 0.55, r'$+$', ha='center', va='center', fontsize=16, fontweight='bold', family='serif')
ax.text(4.2, 0.55, r'$0$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(5.25, 0.55, r'$-$', ha='center', va='center', fontsize=16, fontweight='bold', family='serif')
ax.text(6.3, 0.55, r'$0$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(7.25, 0.55, r'$+$', ha='center', va='center', fontsize=16, fontweight='bold', family='serif')
ax.text(8.2, 0.55, r'$0$', ha='center', va='center', fontsize=14, fontweight='bold', family='serif')
ax.text(9.0, 0.55, r'$-$', ha='center', va='center', fontsize=16, fontweight='bold', family='serif')

ax.set_xlim(-0.1, 10.1)
ax.set_ylim(-0.1, 2.3)
plt.savefig('assets/de2_khao_sat_bxd_cau1.png', bbox_inches='tight', pad_inches=0.02)
plt.close()
print("Saved assets/de2_khao_sat_bxd_cau1.png")

# 2. Hình Câu 3 Phần III: Gấp tấm bìa vuông thành hình chóp tứ giác đều
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 3.5), dpi=300)

# ax1: Tấm bìa hình vuông phẳng ABCD
ax1.set_xlim(-6.2, 6.2)
ax1.set_ylim(-6.2, 6.2)
ax1.axis('off')
ax1.set_aspect('equal')

# Hình vuông ABCD: cạnh 10 -> toạ độ (-5,-5) đến (5,5)
sq = Rectangle((-5, -5), 10, 10, fill=None, edgecolor='black', lw=1.8)
ax1.add_patch(sq)

# Tâm O
ax1.plot(0, 0, 'ko', ms=3)
ax1.text(0.3, -0.6, r'$O$', fontsize=12, fontweight='bold', family='serif')

# Đường chéo nét đứt
ax1.plot([-5, 5], [-5, 5], 'k--', lw=0.9, alpha=0.6)
ax1.plot([-5, 5], [5, -5], 'k--', lw=0.9, alpha=0.6)

# Các điểm E, F, G, H trên các trục (với x = 3)
x_val = 2.8
E = np.array([-x_val, 0])
F = np.array([0, -x_val])
G = np.array([x_val, 0])
H = np.array([0, x_val])

# Tam giác cắt bỏ: AEB, BFC, CGD, DHA
A = np.array([-5.0, 5.0])
B = np.array([-5.0, -5.0])
C = np.array([5.0, -5.0])
D = np.array([5.0, 5.0])

ax1.plot([A[0], E[0], B[0]], [A[1], E[1], B[1]], 'k-', lw=1.4)
ax1.plot([B[0], F[0], C[0]], [B[1], F[1], C[1]], 'k-', lw=1.4)
ax1.plot([C[0], G[0], D[0]], [C[1], G[1], D[1]], 'k-', lw=1.4)
ax1.plot([D[0], H[0], A[0]], [D[1], H[1], A[1]], 'k-', lw=1.4)

# Nếp gấp: hình vuông EFGH nét đứt
ax1.plot([E[0], F[0], G[0], H[0], E[0]], [E[1], F[1], G[1], H[1], E[1]], color='#1e3a8a', ls='--', lw=1.5)

# Điểm M trung điểm HG
M = (H + G) / 2
ax1.plot([0, M[0]], [0, M[1]], 'k:', lw=1)
ax1.plot(M[0], M[1], 'ko', ms=3.5)
ax1.text(M[0]+0.2, M[1]+0.2, r'$M$', fontsize=11, fontweight='bold', family='serif')

# Tên các đỉnh
ax1.text(A[0]-0.4, A[1]+0.2, r'$A$', fontsize=13, fontweight='bold', family='serif')
ax1.text(B[0]-0.4, B[1]-0.5, r'$B$', fontsize=13, fontweight='bold', family='serif')
ax1.text(C[0]+0.2, C[1]-0.5, r'$C$', fontsize=13, fontweight='bold', family='serif')
ax1.text(D[0]+0.2, D[1]+0.2, r'$D$', fontsize=13, fontweight='bold', family='serif')

ax1.text(E[0]-0.5, E[1]-0.2, r'$E$', fontsize=12, fontweight='bold', family='serif')
ax1.text(F[0]-0.2, F[1]-0.6, r'$F$', fontsize=12, fontweight='bold', family='serif')
ax1.text(G[0]+0.3, G[1]-0.2, r'$G$', fontsize=12, fontweight='bold', family='serif')
ax1.text(H[0]-0.2, H[1]+0.3, r'$H$', fontsize=12, fontweight='bold', family='serif')

# Kích thước cạnh 10 cm
ax1.annotate('', xy=(5, -5.6), xytext=(-5, -5.6), arrowprops=dict(arrowstyle='<->', lw=1.2, color='black'))
ax1.text(0, -6.1, r'$10\text{ cm}$', fontsize=11, fontweight='bold', ha='center', family='serif')

# ax2: Hình chóp tứ giác đều S.EFGH (đỉnh S trùng A, B, C, D)
ax2.set_xlim(-4.5, 4.5)
ax2.set_ylim(-1.5, 6.2)
ax2.axis('off')

# Tọa độ 3D biểu diễn phẳng:
# Đáy EFGH hình bình hành
# F = (-2.8, 0), G = (1.6, -0.4), H = (3.2, 1.4), E = (-1.2, 1.8)
F_3d = np.array([-2.8, 0.0])
G_3d = np.array([1.6, -0.4])
H_3d = np.array([3.0, 1.4])
E_3d = np.array([-1.4, 1.8])
O_3d = (F_3d + H_3d) / 2
S_3d = np.array([O_3d[0], 5.0]) # Đỉnh S (chính là A trùng B, C, D)

# Đáy nét liền và nét đứt
ax2.plot([F_3d[0], G_3d[0]], [F_3d[1], G_3d[1]], 'k-', lw=1.5)
ax2.plot([G_3d[0], H_3d[0]], [G_3d[1], H_3d[1]], 'k-', lw=1.5)
ax2.plot([H_3d[0], E_3d[0]], [H_3d[1], E_3d[1]], 'k--', lw=1.2)
ax2.plot([E_3d[0], F_3d[0]], [E_3d[1], F_3d[1]], 'k--', lw=1.2)

# Đường chéo đáy nét đứt
ax2.plot([F_3d[0], H_3d[0]], [F_3d[1], H_3d[1]], 'k--', lw=0.9, alpha=0.6)
ax2.plot([E_3d[0], G_3d[0]], [E_3d[1], G_3d[1]], 'k--', lw=0.9, alpha=0.6)

# Chiều cao SO nét đứt
ax2.plot([S_3d[0], O_3d[0]], [S_3d[1], O_3d[1]], 'k--', lw=1.3)

# Các cạnh bên: SF, SG, SH nét liền; SE nét đứt
ax2.plot([S_3d[0], F_3d[0]], [S_3d[1], F_3d[1]], 'k-', lw=1.6)
ax2.plot([S_3d[0], G_3d[0]], [S_3d[1], G_3d[1]], 'k-', lw=1.6)
ax2.plot([S_3d[0], H_3d[0]], [S_3d[1], H_3d[1]], 'k-', lw=1.6)
ax2.plot([S_3d[0], E_3d[0]], [S_3d[1], E_3d[1]], 'k--', lw=1.2)

# Điểm M_3d trung điểm HG
M_3d = (G_3d + H_3d) / 2
ax2.plot([S_3d[0], M_3d[0]], [S_3d[1], M_3d[1]], 'k:', lw=1.2)
ax2.plot([O_3d[0], M_3d[0]], [O_3d[1], M_3d[1]], 'k:', lw=1.0)
ax2.plot(M_3d[0], M_3d[1], 'ko', ms=3)
ax2.text(M_3d[0]+0.2, M_3d[1]-0.3, r'$M$', fontsize=11, fontweight='bold', family='serif')

# Tên các đỉnh
ax2.text(S_3d[0]-0.2, S_3d[1]+0.2, r'$A$', fontsize=14, fontweight='bold', family='serif')
ax2.text(F_3d[0]-0.4, F_3d[1]-0.3, r'$F$', fontsize=12, fontweight='bold', family='serif')
ax2.text(G_3d[0]+0.1, G_3d[1]-0.4, r'$G$', fontsize=12, fontweight='bold', family='serif')
ax2.text(H_3d[0]+0.2, H_3d[1]+0.1, r'$H$', fontsize=12, fontweight='bold', family='serif')
ax2.text(E_3d[0]-0.4, E_3d[1]+0.1, r'$E$', fontsize=12, fontweight='bold', family='serif')
ax2.text(O_3d[0]+0.1, O_3d[1]-0.4, r'$O$', fontsize=12, fontweight='bold', family='serif')

plt.tight_layout()
plt.savefig('assets/de2_khao_sat_gap_bia_cau3.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de2_khao_sat_gap_bia_cau3.png")

# 3. Hình Câu 4 Phần III: Ao cá có cọc K và dây phao chắn góc
fig, ax = plt.subplots(figsize=(4.5, 3.6), dpi=300)
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 11)
ax.axis('off')

# Ao cá: hình chữ nhật góc tại A(0,0)
# Vẽ bờ AB (thẳng đứng), bờ AC (nằm ngang)
ax.plot([0, 0], [0, 10], 'k-', lw=2.2)
ax.plot([0, 12], [0, 0], 'k-', lw=2.2)
ax.plot([12, 12], [0, 10], 'k-', lw=1.2)
ax.plot([0, 12], [10, 10], 'k-', lw=1.2)

# Vùng nước ao cá màu xanh nhạt
poly_pond = Polygon([(0, 0), (12, 0), (12, 10), (0, 10)], closed=True,
                    facecolor='#f8fafc', edgecolor='none')
ax.add_patch(poly_pond)

# Góc ngăn nuôi cá ăn: tam giác AMN với M(0, 10), N(5, 0)
M_pt = np.array([0.0, 10.0])
N_pt = np.array([5.0, 0.0])
poly_feed = Polygon([(0, 0), (N_pt[0], 0), (0, M_pt[1])], closed=True,
                    facecolor='#93c5fd', edgecolor='none', alpha=0.7)
ax.add_patch(poly_feed)

# Dây phao: đoạn thẳng MN màu đỏ đậm
ax.plot([M_pt[0], N_pt[0]], [M_pt[1], N_pt[1]], color='#dc2626', lw=2.5, ls='-', label='Dây phao')

# Cọc K tại (1, 8)
K_pt = np.array([1.0, 8.0])
ax.plot([K_pt[0]], [K_pt[1]], 'ro', ms=6)
ax.text(K_pt[0]+0.3, K_pt[1]+0.2, r'$K$', fontsize=13, fontweight='bold', color='#dc2626', family='serif')

# Khoảng cách từ K đến AB là 1m (nét đứt)
ax.plot([0, K_pt[0]], [K_pt[1], K_pt[1]], 'k:', lw=1.2)
ax.text(0.5, K_pt[1]+0.3, r'$1\text{ m}$', fontsize=11, fontweight='bold', ha='center', family='serif')

# Khoảng cách từ K đến AC là 8m (nét đứt)
ax.plot([K_pt[0], K_pt[0]], [0, K_pt[1]], 'k:', lw=1.2)
ax.text(K_pt[0]+0.3, 4.0, r'$8\text{ m}$', fontsize=11, fontweight='bold', va='center', family='serif')

# Nhãn các đỉnh A, B, C
ax.text(-0.5, -0.5, r'$A$', fontsize=13, fontweight='bold', family='serif')
ax.text(-0.6, 10.0, r'$B$', fontsize=13, fontweight='bold', family='serif')
ax.text(12.2, -0.5, r'$C$', fontsize=13, fontweight='bold', family='serif')

plt.tight_layout()
plt.savefig('assets/de2_khao_sat_ao_ca_cau4.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de2_khao_sat_ao_ca_cau4.png")

# 4. Hình Câu 6 Phần III: Bờ hồ bán nguyệt
fig, ax = plt.subplots(figsize=(5.2, 3.2), dpi=300)
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-0.8, 2.6)
ax.axis('off')
ax.set_aspect('equal')

# Bán kính R = 2. Đường kính AB trên trục Ox: A(-2, 0), B(2, 0)
A_pos = np.array([-2.0, 0.0])
B_pos = np.array([2.0, 0.0])
O_pos = np.array([0.0, 0.0])

# Cung bán nguyệt y >= 0
theta = np.linspace(0, np.pi, 300)
x_arc = 2.0 * np.cos(theta)
y_arc = 2.0 * np.sin(theta)
ax.plot(x_arc, y_arc, color='#7c3aed', lw=2.2)

# Đường kính AB
ax.plot([A_pos[0], B_pos[0]], [A_pos[1], B_pos[1]], color='#1e3a8a', lw=2.2)

# Kẻ gạch chéo dưới đáy hồ AB tượng trưng cho bờ thẳng
for xx in np.linspace(-1.8, 1.8, 13):
    ax.plot([xx, xx-0.2], [0, -0.25], color='#64748b', lw=1.0)

# Điểm C trên nửa đường tròn: chọn góc 60 độ (phi = 30 độ)
angle_C = np.pi / 3 # 60 độ so với Ox dương
C_pos = np.array([2.0 * np.cos(angle_C), 2.0 * np.sin(angle_C)])

# Chèo thuyền: đoạn thẳng AC
ax.plot([A_pos[0], C_pos[0]], [A_pos[1], C_pos[1]], color='#2563eb', lw=2.0)
# Mũi tên trên đoạn AC
mid_AC = (A_pos + C_pos) / 2
ax.annotate('', xy=mid_AC + 0.1*(C_pos - A_pos)/np.linalg.norm(C_pos - A_pos),
            xytext=mid_AC - 0.1*(C_pos - A_pos)/np.linalg.norm(C_pos - A_pos),
            arrowprops=dict(arrowstyle='->', lw=2.0, color='#2563eb'))

# Chạy bộ: cung tròn CB tô đậm màu đen/tím
theta_CB = np.linspace(0, angle_C, 100)
x_CB = 2.0 * np.cos(theta_CB)
y_CB = 2.0 * np.sin(theta_CB)
ax.plot(x_CB, y_CB, color='black', lw=2.8)
# Mũi tên trên cung CB
mid_angle = angle_C / 2
ax.annotate('', xy=(2.0*np.cos(mid_angle-0.1), 2.0*np.sin(mid_angle-0.1)),
            xytext=(2.0*np.cos(mid_angle+0.1), 2.0*np.sin(mid_angle+0.1)),
            arrowprops=dict(arrowstyle='->', lw=2.0, color='black'))

# Dây cung BC nét đứt
ax.plot([C_pos[0], B_pos[0]], [C_pos[1], B_pos[1]], color='#3b82f6', ls='--', lw=1.2)

# Các điểm A, B, C, O
ax.plot([A_pos[0], B_pos[0], C_pos[0], O_pos[0]], [A_pos[1], B_pos[1], C_pos[1], O_pos[1]], 'ro', ms=5)
ax.text(A_pos[0]-0.25, A_pos[1]-0.1, r'$A$', fontsize=13, fontweight='bold', family='serif')
ax.text(B_pos[0]+0.1, B_pos[1]-0.1, r'$B$', fontsize=13, fontweight='bold', family='serif')
ax.text(C_pos[0]+0.05, C_pos[1]+0.15, r'$C$', fontsize=13, fontweight='bold', family='serif')
ax.text(O_pos[0], O_pos[1]-0.3, r'$O$', fontsize=12, fontweight='bold', ha='center', family='serif')

# Chú thích vận tốc
ax.text(-0.8, 1.1, r'$v_1 = 3\text{ km/h}$', fontsize=11, fontweight='bold', color='#1d4ed8', family='serif', rotation=25)
ax.text(1.7, 1.2, r'$v_2 = 6\text{ km/h}$', fontsize=11, fontweight='bold', color='black', family='serif')
ax.text(0, -0.6, r'$R = 2\text{ km}$', fontsize=11, fontweight='bold', color='#1e3a8a', ha='center', family='serif')

plt.tight_layout()
plt.savefig('assets/de2_khao_sat_ho_ban_nguyet_cau6.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de2_khao_sat_ho_ban_nguyet_cau6.png")
