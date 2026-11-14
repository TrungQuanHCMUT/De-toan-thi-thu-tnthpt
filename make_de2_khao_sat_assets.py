import os
os.environ['MPLCONFIGDIR'] = os.path.abspath('assets/.mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Wedge, Arc, Rectangle

# 1. Đồ thị Câu 7 Phần I: y = x^3 - 3x + 1
fig, ax = plt.subplots(figsize=(4.2, 4.0), dpi=300)
x = np.linspace(-2.25, 2.25, 400)
y = x**3 - 3*x + 1

ax.plot(x, y, color='#c53030', lw=2.2)
ax.axhline(0, color='black', lw=1.2)
ax.axvline(0, color='black', lw=1.2)

# Mũi tên trục
ax.annotate('', xy=(2.45, 0), xytext=(2.2, 0), arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
ax.annotate('', xy=(0, 4.3), xytext=(0, 3.9), arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

# Nhãn trục
ax.text(2.4, -0.45, r'$x$', fontsize=15, fontweight='bold', family='serif')
ax.text(-0.38, 4.15, r'$y$', fontsize=15, fontweight='bold', family='serif')
ax.text(0.12, -0.4, r'$O$', fontsize=14, fontweight='bold', family='serif')

# Các điểm đặc biệt: CĐ (-1; 3), CT (1; -1), Cắt Oy tại (0; 1)
ax.plot([-1, 1, 0], [3, -1, 1], 'ko', ms=5)

# Dóng toạ độ
ax.plot([-1, -1, 0], [0, 3, 3], 'k--', lw=1.1)
ax.plot([1, 1, 0], [0, -1, -1], 'k--', lw=1.1)

# Số trên trục phóng to cực rõ nét
ax.text(-1, -0.45, r'$-1$', fontsize=14, fontweight='bold', ha='center', family='serif')
ax.text(1, 0.25, r'$1$', fontsize=14, fontweight='bold', ha='center', family='serif')
ax.text(-0.35, 3.0, r'$3$', fontsize=14, fontweight='bold', va='center', family='serif')
ax.text(0.2, 1.15, r'$1$', fontsize=13, fontweight='bold', va='center', family='serif')
ax.text(-0.4, -1.0, r'$-1$', fontsize=14, fontweight='bold', va='center', family='serif')

ax.set_xlim(-2.4, 2.5)
ax.set_ylim(-3.2, 4.4)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de2_khao_sat_dothi_cau7.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de2_khao_sat_dothi_cau7.png")

# 2. Đồ thị Câu 12 Phần I: y = (x^2 - x + 1)/(x - 1) = x + 1/(x-1)
fig, ax = plt.subplots(figsize=(4.4, 4.2), dpi=300)
x1 = np.linspace(-2.5, 0.82, 300)
y1 = (x1**2 - x1 + 1) / (x1 - 1)
x2 = np.linspace(1.18, 4.5, 300)
y2 = (x2**2 - x2 + 1) / (x2 - 1)

ax.plot(x1, y1, color='#c53030', lw=2.2)
ax.plot(x2, y2, color='#c53030', lw=2.2)
ax.axhline(0, color='black', lw=1.2)
ax.axvline(0, color='black', lw=1.2)

# Tiệm cận đứng x = 1, tiệm cận xiên y = x
ax.axvline(1, color='#1e3a8a', ls='--', lw=1.5)
x_line = np.linspace(-2.5, 4.5, 100)
ax.plot(x_line, x_line, color='#1e3a8a', ls='--', lw=1.5)

# Mũi tên trục
ax.annotate('', xy=(4.7, 0), xytext=(4.3, 0), arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
ax.annotate('', xy=(0, 5.6), xytext=(0, 5.1), arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

ax.text(4.6, -0.5, r'$x$', fontsize=15, fontweight='bold', family='serif')
ax.text(-0.45, 5.4, r'$y$', fontsize=15, fontweight='bold', family='serif')
ax.text(-0.35, -0.45, r'$O$', fontsize=14, fontweight='bold', family='serif')

# Chú thích số tiệm cận và điểm
ax.text(1.15, -0.45, r'$1$', fontsize=14, fontweight='bold', family='serif', color='#1e3a8a')
ax.text(1.15, 4.6, r'$x=1$', fontsize=13, fontweight='bold', family='serif', color='#1e3a8a',
        bbox=dict(boxstyle='square,pad=0.15', facecolor='white', edgecolor='#1e3a8a', lw=0.8))
ax.text(3.5, 3.8, r'$y=x$', fontsize=13, fontweight='bold', family='serif', color='#1e3a8a',
        bbox=dict(boxstyle='square,pad=0.15', facecolor='white', edgecolor='#1e3a8a', lw=0.8))

# Các điểm cực trị (0; -1), (2; 3)
ax.plot([0, 2], [-1, 3], 'ko', ms=5)
ax.plot([2, 2, 0], [0, 3, 3], 'k--', lw=1.1)

ax.text(-0.45, -1.0, r'$-1$', fontsize=14, fontweight='bold', va='center', family='serif')
ax.text(2, -0.45, r'$2$', fontsize=14, fontweight='bold', ha='center', family='serif')
ax.text(-0.38, 3.0, r'$3$', fontsize=14, fontweight='bold', va='center', family='serif')

# Giao điểm 2 tiệm cận I(1; 1)
ax.plot([1], [1], 'bo', ms=5)
ax.text(0.65, 1.25, r'$I$', fontsize=14, fontweight='bold', family='serif', color='#1e3a8a')

ax.set_xlim(-2.6, 4.8)
ax.set_ylim(-3.5, 5.7)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de2_khao_sat_dothi_cau12.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de2_khao_sat_dothi_cau12.png")

# 3. Đồ thị Câu 4 Phần II: Công suất mạch điện P(R) = 144R / (R + 2)^2
fig, ax = plt.subplots(figsize=(4.6, 3.8), dpi=300)
R = np.linspace(0, 12, 400)
P = 144 * R / (R + 2)**2

ax.plot(R, P, color='#c53030', lw=2.2)
ax.axhline(0, color='black', lw=1.2)
ax.axvline(0, color='black', lw=1.2)

ax.annotate('', xy=(12.8, 0), xytext=(12.2, 0), arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
ax.annotate('', xy=(0, 21.0), xytext=(0, 19.5), arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

ax.text(12.5, -1.5, r'$R\,(\Omega)$', fontsize=14, fontweight='bold', family='serif')
ax.text(-1.4, 20.2, r'$P\,(\mathrm{W})$', fontsize=14, fontweight='bold', family='serif')
ax.text(-0.6, -1.3, r'$O$', fontsize=14, fontweight='bold', family='serif')

# Điểm cực đại R = 2, P = 18
ax.plot([2], [18], 'ko', ms=5)
ax.plot([2, 2, 0], [0, 18, 18], 'k--', lw=1.2)

ax.text(2, -1.4, r'$2$', fontsize=14, fontweight='bold', ha='center', family='serif')
ax.text(-1.1, 18, r'$18$', fontsize=14, fontweight='bold', va='center', family='serif')

# Tiệm cận ngang P -> 0 khi R -> +inf
ax.set_xlim(-1.2, 13.0)
ax.set_ylim(-2.2, 21.5)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/de2_khao_sat_mach_dien_cau4.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de2_khao_sat_mach_dien_cau4.png")

# 4. Hình Câu 5 Phần III: Bồn nước hình nón (xả nước, Related Rates)
fig, ax = plt.subplots(figsize=(4.4, 4.4), dpi=300)
ax.set_xlim(-40, 40)
ax.set_ylim(-15, 75)
ax.axis('off')

# Nón lớn: Đỉnh tại (0, 0), Miệng tại y = 60, R = 30
# Vẽ đường sinh
ax.plot([-30, 0], [60, 0], color='#2c3e50', lw=2)
ax.plot([30, 0], [60, 0], color='#2c3e50', lw=2)

# Miệng nón: elip bán trục 30 và 6
theta = np.linspace(0, 2*np.pi, 200)
x_rim = 30 * np.cos(theta)
y_rim = 60 + 6 * np.sin(theta)
ax.plot(x_rim, y_rim, color='#2c3e50', lw=2)

# Mực nước ở độ cao h = 20, khi đó r = 30 * (20/60) = 10
h_water = 20
r_water = 10
# Phần nón chứa nước
x_water_fill = np.array([-r_water, 0, r_water])
y_water_fill = np.array([h_water, 0, h_water])
poly_water = Polygon([(-r_water, h_water), (0, 0), (r_water, h_water)], closed=True,
                     facecolor='#93c5fd', edgecolor='#2563eb', alpha=0.6, lw=1.2)
ax.add_patch(poly_water)

# Bề mặt nước: elip bán trục 10 và 2.5
x_water_surface = r_water * np.cos(theta)
y_water_surface = h_water + 2.5 * np.sin(theta)
ax.plot(x_water_surface, y_water_surface, color='#1d4ed8', lw=1.5)
ax.fill(x_water_surface, y_water_surface, color='#60a5fa', alpha=0.7)

# Trục đối xứng thẳng đứng
ax.plot([0, 0], [0, 60], 'k-.', lw=1)

# Kích thước miệng: R = 30 cm
ax.plot([0, 30], [60, 60], 'k-', lw=1.2)
ax.plot([0, 0], [58, 62], 'k-', lw=1.2)
ax.plot([30, 30], [58, 62], 'k-', lw=1.2)
ax.text(15, 63, r'$R = 30\text{ cm}$', fontsize=12, fontweight='bold', ha='center', family='serif')

# Kích thước chiều cao H = 60 cm bên trái
ax.plot([-34, -34], [0, 60], 'k-', lw=1.2)
ax.plot([-36, -32], [0, 0], 'k-', lw=1.2)
ax.plot([-36, -32], [60, 60], 'k-', lw=1.2)
ax.text(-36, 30, r'$H = 60\text{ cm}$', fontsize=12, fontweight='bold', ha='right', va='center', family='serif')

# Mực nước h = 20 cm
ax.plot([14, 14], [0, 20], 'b-', lw=1.2)
ax.plot([12, 16], [0, 0], 'b-', lw=1.2)
ax.plot([12, 16], [20, 20], 'b-', lw=1.2)
ax.text(17, 10, r'$h = 20\text{ cm}$', fontsize=12, fontweight='bold', ha='left', va='center', family='serif', color='#1d4ed8')

# Vòi nước đổ vào bên trên
ax.plot([0, 0], [68, 63], color='#2563eb', lw=3)
ax.annotate('', xy=(0, 61), xytext=(0, 66), arrowprops=dict(arrowstyle='->', lw=2, color='#2563eb'))
ax.text(3, 69, r'$v_0 = 50\pi\text{ cm}^3/\text{s}$', fontsize=12, fontweight='bold', family='serif', color='#1e40af')

plt.tight_layout()
plt.savefig('assets/de2_khao_sat_bon_nuoc_cau5.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de2_khao_sat_bon_nuoc_cau5.png")

# 5. Hình Câu 6 Phần III: Ngắm tranh nghệ thuật (Regiomontanus)
fig, ax = plt.subplots(figsize=(5.0, 3.8), dpi=300)
ax.set_xlim(-0.8, 4.5)
ax.set_ylim(-0.4, 4.6)
ax.axis('off')

# Mặt sàn y = 0
ax.plot([-0.5, 4.2], [0, 0], 'k-', lw=1.5)
# Bức tường x = 3.2
ax.plot([3.2, 3.2], [0, 4.5], 'k-', lw=2.5)

# Bức tranh AB trên tường: Mép dưới B tại y = 2.6, mép trên A tại y = 2.6 + 3.0 = 5.6 -> ta co lại tỷ lệ một chút:
# A = (3.2, 4.2), B = (3.2, 2.2), chiều cao 2.0 (tượng trưng cho AB = 3m)
# Người đứng tại x = 1.0, tầm mắt E = (1.0, 1.4)
ax.plot([3.2, 3.2], [2.2, 4.2], color='#b91c1c', lw=6)
ax.text(3.4, 3.2, r'Tranh $AB = 3\text{ m}$', fontsize=12, fontweight='bold', color='#b91c1c', family='serif', va='center')
ax.text(3.35, 4.2, r'$A$', fontsize=13, fontweight='bold', family='serif')
ax.text(3.35, 2.2, r'$B$', fontsize=13, fontweight='bold', family='serif')

# Tầm mắt E tại (1.0, 1.4)
ax.plot([1.0], [1.4], 'ko', ms=5)
ax.text(0.7, 1.4, r'$E$', fontsize=13, fontweight='bold', family='serif')
# Người
ax.plot([1.0, 1.0], [0, 1.4], 'k-', lw=1.5)
ax.text(0.85, 0.7, r'$1,6\text{ m}$', fontsize=11, fontweight='bold', ha='right', family='serif')

# Đường nằm ngang từ tầm mắt đến tường E -> H = (3.2, 1.4)
ax.plot([1.0, 3.2], [1.4, 1.4], 'k--', lw=1)
ax.text(3.35, 1.4, r'$H$', fontsize=13, fontweight='bold', family='serif')

# Tia nhìn EA và EB
ax.plot([1.0, 3.2], [1.4, 4.2], color='#2563eb', lw=1.4)
ax.plot([1.0, 3.2], [1.4, 2.2], color='#2563eb', lw=1.4)

# Góc theta
arc_angle = Arc((1.0, 1.4), 1.2, 1.2, angle=0, theta1=20, theta2=52, color='#c53030', lw=1.5)
ax.add_patch(arc_angle)
ax.text(1.7, 1.85, r'$\theta$', fontsize=14, fontweight='bold', color='#c53030', family='serif')

# Kích thước x (khoảng cách từ người đến tường)
ax.annotate('', xy=(3.2, 0.4), xytext=(1.0, 0.4), arrowprops=dict(arrowstyle='<->', lw=1.2, color='black'))
ax.text(2.1, 0.55, r'$x$', fontsize=14, fontweight='bold', ha='center', family='serif')

# Kích thước mép dưới cách sàn: 2,6 m
ax.plot([3.0, 3.0], [0, 2.2], 'k:', lw=1.2)
ax.text(2.9, 1.1, r'$2,6\text{ m}$', fontsize=11, fontweight='bold', ha='right', family='serif')

plt.tight_layout()
plt.savefig('assets/de2_khao_sat_ngam_tranh_cau6.png', bbox_inches='tight', pad_inches=0.03)
plt.close()
print("Saved assets/de2_khao_sat_ngam_tranh_cau6.png")
