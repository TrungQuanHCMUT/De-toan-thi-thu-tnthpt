import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Rectangle, Arc, Wedge

# Set global styles
plt.rcParams['font.sans-serif'] = 'Helvetica'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 1.0

# 1. Đồ thị Câu 1 Phần I: Hàm số bậc ba y = f(x) = x^3 - 3x + 1
fig, ax = plt.subplots(figsize=(3.6, 3.2), dpi=300)
x = np.linspace(-2.2, 2.2, 400)
y = x**3 - 3*x + 1

ax.plot(x, y, color='#dc2626', lw=2.2)
ax.axhline(0, color='black', lw=1.2)
ax.axvline(0, color='black', lw=1.2)

# Cực trị (-1, 3) và (1, -1)
ax.plot([-1, -1], [0, 3], 'k--', lw=1.0)
ax.plot([0, -1], [3, 3], 'k--', lw=1.0)
ax.plot([-1], [3], 'ko', ms=4.5)

ax.plot([1, 1], [0, -1], 'k--', lw=1.0)
ax.plot([0, 1], [-1, -1], 'k--', lw=1.0)
ax.plot([1], [-1], 'ko', ms=4.5)

ax.text(2.2, -0.4, r'$x$', fontsize=13, fontweight='bold', family='serif')
ax.text(-0.35, 3.7, r'$y$', fontsize=13, fontweight='bold', family='serif')
ax.text(-0.3, -0.35, r'$O$', fontsize=12, fontweight='bold', family='serif')

ax.text(-1.15, -0.4, r'$-1$', fontsize=11, fontweight='bold', family='serif')
ax.text(0.95, 0.15, r'$1$', fontsize=11, fontweight='bold', family='serif')
ax.text(0.12, 2.9, r'$3$', fontsize=11, fontweight='bold', family='serif')
ax.text(0.12, -1.1, r'$-1$', fontsize=11, fontweight='bold', family='serif')

ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-2.2, 4.0)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de3_khao_sat_dothi_cau1.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de3_khao_sat_dothi_cau1.png")

# 2. Đồ thị Câu 5 Phần I: Đồ thị hàm đạo hàm y = f'(x) cắt Ox tại -2, 0, 3
fig, ax = plt.subplots(figsize=(3.8, 3.0), dpi=300)
x = np.linspace(-2.7, 3.7, 400)
# f'(x) = -0.3 * (x + 2) * x * (x - 3)
y = -0.3 * (x + 2) * x * (x - 3)

ax.plot(x, y, color='#2563eb', lw=2.2)
ax.axhline(0, color='black', lw=1.2)
ax.axvline(0, color='black', lw=1.2)

ax.plot([-2, 0, 3], [0, 0, 0], 'ko', ms=5)

ax.text(3.7, -0.4, r'$x$', fontsize=13, fontweight='bold', family='serif')
ax.text(-0.35, 2.7, r'$y$', fontsize=13, fontweight='bold', family='serif')
ax.text(-0.35, -0.4, r'$O$', fontsize=12, fontweight='bold', family='serif')

ax.text(-2.3, 0.2, r'$-2$', fontsize=12, fontweight='bold', family='serif')
ax.text(2.9, 0.2, r'$3$', fontsize=12, fontweight='bold', family='serif')
ax.text(1.2, 1.8, r'$y = f\'(x)$', fontsize=12, fontweight='bold', color='#2563eb', family='serif')

ax.set_xlim(-2.9, 4.0)
ax.set_ylim(-2.0, 3.0)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de3_khao_sat_dothi_cau5.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de3_khao_sat_dothi_cau5.png")

# 3. Đồ thị Câu 7 Phần I: Hàm trùng phương y = -x^4 + 2x^2 + 1
fig, ax = plt.subplots(figsize=(3.6, 3.2), dpi=300)
x = np.linspace(-1.9, 1.9, 400)
y = -x**4 + 2*x**2 + 1

ax.plot(x, y, color='#dc2626', lw=2.2)
ax.axhline(0, color='black', lw=1.2)
ax.axvline(0, color='black', lw=1.2)

# Cực trị (-1, 2), (1, 2), (0, 1)
ax.plot([-1, -1], [0, 2], 'k--', lw=1.0)
ax.plot([1, 1], [0, 2], 'k--', lw=1.0)
ax.plot([-1, 1], [2, 2], 'k--', lw=1.0)
ax.plot([-1, 0, 1], [2, 1, 2], 'ko', ms=4.5)

ax.text(1.9, -0.3, r'$x$', fontsize=13, fontweight='bold', family='serif')
ax.text(-0.3, 2.5, r'$y$', fontsize=13, fontweight='bold', family='serif')
ax.text(-0.25, -0.28, r'$O$', fontsize=12, fontweight='bold', family='serif')

ax.text(-1.2, -0.3, r'$-1$', fontsize=11, fontweight='bold', family='serif')
ax.text(0.9, -0.3, r'$1$', fontsize=11, fontweight='bold', family='serif')
ax.text(0.12, 0.9, r'$1$', fontsize=11, fontweight='bold', family='serif')
ax.text(0.12, 1.9, r'$2$', fontsize=11, fontweight='bold', family='serif')

ax.set_xlim(-2.1, 2.1)
ax.set_ylim(-1.5, 2.7)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de3_khao_sat_dothi_cau7.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de3_khao_sat_dothi_cau7.png")

# 4. Đồ thị Câu 12 Phần I: Hàm bậc hai trên bậc nhất y = (x^2 - 2x + 2)/(x - 1) = x - 1 + 1/(x - 1)
fig, ax = plt.subplots(figsize=(3.8, 3.5), dpi=300)
x1 = np.linspace(-2.2, 0.85, 250)
x2 = np.linspace(1.15, 4.2, 250)
y1 = (x1**2 - 2*x1 + 2) / (x1 - 1)
y2 = (x2**2 - 2*x2 + 2) / (x2 - 1)

ax.plot(x1, y1, color='#dc2626', lw=2.2)
ax.plot(x2, y2, color='#dc2626', lw=2.2)

# Tiệm cận đứng x = 1, tiệm cận xiên y = x - 1
ax.axvline(1, color='#2563eb', lw=1.3, ls='--', label=r'$x=1$')
x_asy = np.linspace(-2.2, 4.2, 100)
ax.plot(x_asy, x_asy - 1, color='#2563eb', lw=1.3, ls='--', label=r'$y=x-1$')

ax.axhline(0, color='black', lw=1.2)
ax.axvline(0, color='black', lw=1.2)

# Cực trị: (0; -2) và (2; 2)
ax.plot([0], [-2], 'ko', ms=4.5)
ax.plot([2], [2], 'ko', ms=4.5)
ax.plot([2, 2], [0, 2], 'k--', lw=0.9)
ax.plot([0, 2], [2, 2], 'k--', lw=0.9)

# Nhãn
ax.text(4.2, -0.4, r'$x$', fontsize=13, fontweight='bold', family='serif')
ax.text(-0.35, 4.5, r'$y$', fontsize=13, fontweight='bold', family='serif')
ax.text(-0.3, -0.35, r'$O$', fontsize=12, fontweight='bold', family='serif')

ax.text(1.05, 3.8, r'$x = 1$', fontsize=11, fontweight='bold', color='#2563eb', family='serif')
ax.text(3.1, 2.5, r'$y = x - 1$', fontsize=11, fontweight='bold', color='#2563eb', family='serif')
ax.text(-0.45, -2.1, r'$-2$', fontsize=11, fontweight='bold', family='serif')
ax.text(1.9, -0.4, r'$2$', fontsize=11, fontweight='bold', family='serif')
ax.text(-0.35, 1.9, r'$2$', fontsize=11, fontweight='bold', family='serif')

ax.set_xlim(-2.3, 4.5)
ax.set_ylim(-4.5, 4.8)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de3_khao_sat_dothi_cau12.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de3_khao_sat_dothi_cau12.png")

# 5. Hình Câu 3 Phần II: Đồ thị hàm chi phí trung bình C_bar(x) = x + 20 + 400/x
fig, ax = plt.subplots(figsize=(4.6, 3.2), dpi=300)
x = np.linspace(4, 50, 400)
y = x + 20 + 400/x

ax.plot(x, y, color='#dc2626', lw=2.2)
ax.axhline(0, color='black', lw=1.2)
ax.axvline(0, color='black', lw=1.2)

# Cực tiểu tại x = 20, y = 60
ax.plot([20, 20], [0, 60], 'k--', lw=1.1)
ax.plot([0, 20], [60, 60], 'k--', lw=1.1)
ax.plot([20], [60], 'ro', ms=6)

ax.text(51, -4, r'$x\text{ (sản phẩm)}$', fontsize=11, fontweight='bold', family='serif')
ax.text(-3, 135, r'$\bar{C}(x)\text{ (nghìn đồng)}$', fontsize=11, fontweight='bold', family='serif')
ax.text(-2, -5, r'$O$', fontsize=12, fontweight='bold', family='serif')

ax.text(18.5, -6, r'$20$', fontsize=12, fontweight='bold', family='serif')
ax.text(-4, 58, r'$60$', fontsize=12, fontweight='bold', family='serif')
ax.text(26, 75, r'$\bar{C}(x) = x + 20 + \frac{400}{x}$', fontsize=11, color='#dc2626', fontweight='bold', family='serif')

ax.set_xlim(-5, 55)
ax.set_ylim(-8, 140)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de3_khao_sat_chi_phi_cau3.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de3_khao_sat_chi_phi_cau3.png")

# 6. Hình Câu 4 Phần II: Máng nước hình thang cân
fig, ax = plt.subplots(figsize=(4.6, 3.2), dpi=300)
# Đáy nhỏ 20 cm, hai cạnh bên 20 cm, góc alpha = 60 độ
# Đáy dưới: (-10, 0) đến (10, 0)
# Cạnh bên trái: từ (-10, 0) lên (-10 - 20*cos(60), 20*sin(60)) = (-20, 17.32)
# Cạnh bên phải: từ (10, 0) lên (10 + 20*cos(60), 20*sin(60)) = (20, 17.32)
A = np.array([-20.0, 17.32])
B = np.array([-10.0, 0.0])
C = np.array([10.0, 0.0])
D = np.array([20.0, 17.32])

# Máng chứa nước: tô màu xanh nhạt
poly_trap = Polygon([A, B, C, D], closed=True, facecolor='#bfdbfe', edgecolor='#1e3a8a', lw=2.5)
ax.add_patch(poly_trap)

# Đường nét đứt đáy kéo dài để thể hiện góc alpha
ax.plot([-24, -10], [0, 0], 'k--', lw=1.2)
ax.plot([10, 24], [0, 0], 'k--', lw=1.2)

# Cung góc alpha
arc_left = Arc((-10, 0), 10, 10, angle=0, theta1=120, theta2=180, color='#dc2626', lw=1.5)
ax.add_patch(arc_left)
ax.text(-14, 2.5, r'$\alpha$', fontsize=13, fontweight='bold', color='#dc2626', family='serif')

ax.set_xlim(-26, 26)
ax.set_ylim(-5, 23)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de3_khao_sat_mang_nuoc_cau4.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de3_khao_sat_mang_nuoc_cau4.png")

# 7. Hình Câu 3 Phần III: Lon nước ngọt hình trụ
fig, ax = plt.subplots(figsize=(4.0, 3.4), dpi=300)
# Vẽ hình trụ 3D đơn giản
center_top = (0, 3.5)
center_bot = (0, -0.5)
R = 2.0
H = 4.0

# Nắp trên
wedge_top = matplotlib.patches.Ellipse(center_top, 2*R, 0.8, facecolor='#e2e8f0', edgecolor='black', lw=1.8)
ax.add_patch(wedge_top)

# Đáy dưới
wedge_bot = matplotlib.patches.Ellipse(center_bot, 2*R, 0.8, facecolor='#cbd5e1', edgecolor='black', lw=1.8)
ax.add_patch(wedge_bot)

# Hai đường sinh hai bên
ax.plot([-R, -R], [center_bot[1], center_top[1]], 'k-', lw=1.8)
ax.plot([R, R], [center_bot[1], center_top[1]], 'k-', lw=1.8)

# Trục và bán kính
ax.plot([0, 0], [center_bot[1], center_top[1]], 'k--', lw=1.0)
ax.plot([0, R], [center_top[1], center_top[1]], 'r-', lw=1.6)
ax.plot([0], [center_top[1]], 'ko', ms=3)
ax.text(R/2, center_top[1]+0.3, r'$R$', fontsize=13, fontweight='bold', color='#dc2626', ha='center', family='serif')

# Chiều cao h
ax.annotate('', xy=(R+0.6, center_bot[1]), xytext=(R+0.6, center_top[1]),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.2))
ax.text(R+0.9, (center_top[1]+center_bot[1])/2, r'$h$', fontsize=13, fontweight='bold', va='center', family='serif')

ax.set_xlim(-3.5, 4.0)
ax.set_ylim(-2.0, 5.0)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de3_khao_sat_lon_nuoc_cau3.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de3_khao_sat_lon_nuoc_cau3.png")

# 8. Hình Câu 4 Phần III: Đường ống dẫn dầu từ S đến bờ biển
fig, ax = plt.subplots(figsize=(4.8, 3.4), dpi=300)
# Biển ở trên, bờ ở dưới
# H tại (0, 0), T tại (8, 0)
# S tại (0, 3) -> SH = 6km (scale: y=3 tương ứng 6km, x=8 tương ứng 16km -> scale x=0.5km, y=2km)
# P tại (1.25, 0) -> x = 2.5km (scale 1.25)
S = np.array([0.0, 3.0])
H = np.array([0.0, 0.0])
T = np.array([8.0, 0.0])
P = np.array([1.25, 0.0])

# Vùng biển (màu xanh nhạt)
poly_sea = Polygon([(-1, 0), (9, 0), (9, 4), (-1, 4)], closed=True, facecolor='#e0f2fe', edgecolor='none')
ax.add_patch(poly_sea)

# Bờ biển: đường thẳng y = 0
ax.plot([-1, 9], [0, 0], 'k-', lw=2.2)

# Đường vuông góc SH
ax.plot([S[0], H[0]], [S[1], H[1]], 'k--', lw=1.2)
ax.plot([0, 0.4, 0.4, 0], [0.4, 0.4, 0, 0], 'k-', lw=0.9)

# Đường ống: SP (dưới biển, màu đỏ) và PT (trên bờ, màu cam)
ax.plot([S[0], P[0]], [S[1], P[1]], color='#dc2626', lw=2.5, ls='-', label='Dưới biển')
ax.plot([P[0], T[0]], [P[1], T[1]], color='#ea580c', lw=3.0, ls='-', label='Trên bờ')

# Điểm S, H, P, T
for pt, name in [(S, r'$S$'), (H, r'$H$'), (P, r'$P$'), (T, r'$T$')]:
    ax.plot(pt[0], pt[1], 'ko', ms=5)

ax.text(S[0]-0.4, S[1]+0.1, r'$S$', fontsize=13, fontweight='bold', family='serif')
ax.text(H[0]-0.4, H[1]-0.4, r'$H$', fontsize=13, fontweight='bold', family='serif')
ax.text(P[0]-0.1, P[1]-0.4, r'$P$', fontsize=13, fontweight='bold', family='serif')
ax.text(T[0]+0.1, T[1]-0.4, r'$T$', fontsize=13, fontweight='bold', family='serif')

# Khoảng cách
ax.text(-0.5, 1.5, r'$6\text{ km}$', fontsize=11, fontweight='bold', va='center', ha='right', family='serif')
ax.text(4.0, -0.6, r'$HT = 16\text{ km}$', fontsize=11, fontweight='bold', ha='center', family='serif')
ax.text(0.6, 0.15, r'$x$', fontsize=11, fontweight='bold', color='#dc2626', ha='center', family='serif')

ax.set_xlim(-1.5, 9.5)
ax.set_ylim(-1.0, 4.3)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de3_khao_sat_duong_ong_cau4.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de3_khao_sat_duong_ong_cau4.png")

# 9. Hình Câu 5 Phần III: Cửa sổ vòm Norman
fig, ax = plt.subplots(figsize=(4.0, 3.4), dpi=300)
# Chiều rộng x = 4, chiều cao chữ nhật h = 3
w = 2.0 # nửa chiều rộng
h = 2.5
# Khung chữ nhật
rect = Rectangle((-w, 0), 2*w, h, facecolor='#f8fafc', edgecolor='black', lw=2.0)
ax.add_patch(rect)

# Nửa đường tròn phía trên
arc_norman = Wedge((0, h), w, 0, 180, facecolor='#f1f5f9', edgecolor='black', lw=2.0)
ax.add_patch(arc_norman)

# Kích thước
ax.annotate('', xy=(-w, -0.3), xytext=(w, -0.3),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.2))
ax.text(0, -0.7, r'$x$', fontsize=13, fontweight='bold', ha='center', family='serif')

ax.annotate('', xy=(w+0.3, 0), xytext=(w+0.3, h),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.2))
ax.text(w+0.6, h/2, r'$h$', fontsize=13, fontweight='bold', va='center', family='serif')

ax.text(0, h/2, r'Chu vi $= 10\text{ m}$', fontsize=11, fontweight='bold', ha='center', color='#1e3a8a', family='serif')

ax.set_xlim(-3.0, 3.5)
ax.set_ylim(-1.2, 5.2)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de3_khao_sat_cua_so_cau5.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de3_khao_sat_cua_so_cau5.png")

# 10. Hình Câu 6 Phần III: Hải đăng và Ca nô
fig, ax = plt.subplots(figsize=(4.6, 3.2), dpi=300)
# A tại (0, 0), B tại (0, 4) -> AB = 40m
# M tại (3, 0) -> AM = 30m
A = np.array([0.0, 0.0])
B = np.array([0.0, 3.5])
M = np.array([3.0, 0.0])

# Mặt biển
ax.plot([-0.5, 4.0], [0, 0], 'k-', lw=1.5)

# Tháp hải đăng AB
ax.plot([0, 0], [0, 3.5], color='#1e293b', lw=4.0)
# Đèn hải đăng B
ax.plot([0], [3.5], 'yo', ms=10, mec='orange', mew=2)

# Nối BM (đường tia nhìn / khoảng cách)
ax.plot([B[0], M[0]], [B[1], M[1]], color='#dc2626', lw=2.2, ls='-')

# Ca nô tại M
ax.plot([M[0]], [M[1]], 'bs', ms=8)
# Vector vận tốc ca nô hướng về A
ax.annotate('', xy=(M[0]-1.0, 0), xytext=(M[0], 0),
            arrowprops=dict(arrowstyle='->', color='#2563eb', lw=2.0))
ax.text(M[0]-0.5, 0.25, r'$v = 15\text{ m/s}$', fontsize=10, fontweight='bold', color='#2563eb', ha='center', family='serif')

# Góc vuông tại A
ax.plot([0, 0.3, 0.3, 0], [0.3, 0.3, 0, 0], 'k-', lw=0.9)

# Nhãn điểm
ax.text(-0.35, -0.3, r'$A$', fontsize=13, fontweight='bold', family='serif')
ax.text(-0.35, 3.6, r'$B$', fontsize=13, fontweight='bold', family='serif')
ax.text(M[0]+0.1, -0.3, r'$M$', fontsize=13, fontweight='bold', family='serif')

# Kích thước
ax.text(-0.6, 1.75, r'$40\text{ m}$', fontsize=11, fontweight='bold', ha='right', family='serif')
ax.text(1.5, -0.4, r'$30\text{ m}$', fontsize=11, fontweight='bold', ha='center', family='serif')
ax.text(1.7, 2.0, r'$y(t)$', fontsize=12, fontweight='bold', color='#dc2626', family='serif')

ax.set_xlim(-1.2, 4.5)
ax.set_ylim(-0.8, 4.2)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de3_khao_sat_hai_dang_cau6.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de3_khao_sat_hai_dang_cau6.png")

