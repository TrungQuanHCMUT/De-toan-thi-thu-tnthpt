import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Figure 1: Christmas cone only (clean, with full base visible)
fig, ax = plt.subplots(figsize=(3.8, 4.0), dpi=200)

# Base ellipse
t_front = np.linspace(np.pi, 2*np.pi, 100)
t_back = np.linspace(0, np.pi, 100)
rx = 1.6
ry = 0.45
h_cone = 3.8
y_base = 0.8  # elevated base so bottom of ellipse y = 0.8 - 0.45 = 0.35 is well inside axes

# Draw ellipse base
ax.plot(rx*np.cos(t_front), y_base + ry*np.sin(t_front), 'forestgreen', lw=2)
ax.plot(rx*np.cos(t_back), y_base + ry*np.sin(t_back), 'forestgreen', lw=1.2, linestyle='--')

# Outline of cone
ax.plot([-rx, 0, rx], [y_base, y_base + h_cone, y_base], 'forestgreen', lw=2)

# Axis SO and radius OA
ax.plot([0, 0], [y_base, y_base + h_cone], 'k--', lw=1.2)
ax.plot([0, rx], [y_base, y_base], 'k--', lw=1.2)
ax.plot(0, y_base, 'ko', markersize=3.5)
ax.text(-0.16, y_base - 0.16, 'O', fontsize=11, fontweight='bold')

# Right angle symbol at O
ra_size = 0.16
ax.plot([0, ra_size, ra_size], [y_base + ra_size, y_base + ra_size, y_base], 'k-', lw=0.9)

# Points S, A, M
y_apex = y_base + h_cone
ax.plot(0, y_apex, 'ko', markersize=4)
ax.text(0, y_apex + 0.18, 'S', fontsize=11, fontweight='bold', ha='center')

# Point A at bottom right
ax.plot(rx, y_base, 'ro', markersize=4.5)
ax.text(rx + 0.14, y_base - 0.05, 'A', fontsize=11, fontweight='bold', color='red')

# Point M at midpoint of SA
x_m = rx / 2
y_m = (y_base + y_apex) / 2
ax.plot(x_m, y_m, 'bo', markersize=4.5)
ax.text(x_m + 0.14, y_m + 0.05, 'M', fontsize=11, fontweight='bold', color='blue')

# Spiral ribbon wrapped 1 full turn around cone from A to M
th_spiral = np.linspace(0, 2*np.pi, 200)
z_spiral = np.linspace(y_base, y_m, 200)
r_factor = 1.0 - (z_spiral - y_base) / h_cone
x_spiral = rx * r_factor * np.cos(th_spiral)
y_spiral = z_spiral + ry * r_factor * np.sin(th_spiral)

# Draw spiral with dashed line on back and solid line on front
for i in range(len(th_spiral)-1):
    if np.sin(th_spiral[i]) < 0 or np.sin(th_spiral[i+1]) < 0:
        ax.plot(x_spiral[i:i+2], y_spiral[i:i+2], 'crimson', lw=2.2, linestyle='-')
    else:
        ax.plot(x_spiral[i:i+2], y_spiral[i:i+2], 'crimson', lw=1.4, linestyle='--')

# Set limits with generous padding so bottom of ellipse (0.35) is well within [0.0, 5.2]
ax.set_xlim(-2.2, 2.4)
ax.set_ylim(0.0, 5.2)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('assets/de115_cau1_cone.png', bbox_inches='tight', dpi=200)
plt.close()
print("Regenerated assets/de115_cau1_cone.png successfully with full base!")
