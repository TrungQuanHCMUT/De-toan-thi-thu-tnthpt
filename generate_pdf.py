import os
import matplotlib
matplotlib.use('Agg')
os.environ['MPLCONFIGDIR'] = '/tmp/matplotlib'
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

# --- 1. GENERATE FIGURES ---
# BBT for Question 1
fig, ax = plt.subplots(figsize=(7, 1.8), dpi=300)
ax.axis('off')

# Lines
ax.plot([0, 10], [1.5, 1.5], 'k-', lw=1.2)
ax.plot([0, 10], [0.95, 0.95], 'k-', lw=1.2)
ax.plot([1.3, 1.3], [0, 2.1], 'k-', lw=1.2)
ax.plot([0, 10], [2.1, 2.1], 'k-', lw=1.2)
ax.plot([0, 10], [0, 0], 'k-', lw=1.2)
ax.plot([0, 0], [0, 2.1], 'k-', lw=1.2)
ax.plot([10, 10], [0, 2.1], 'k-', lw=1.2)

# Labels
ax.text(0.65, 1.78, r'$x$', ha='center', va='center', fontsize=12, family='serif')
ax.text(0.65, 1.22, r"$f'(x)$", ha='center', va='center', fontsize=12, family='serif')
ax.text(0.65, 0.48, r'$f(x)$', ha='center', va='center', fontsize=12, family='serif')

# Values x
ax.text(1.9, 1.78, r'$-\infty$', ha='center', va='center', fontsize=11, family='serif')
ax.text(4.4, 1.78, r'$-1$', ha='center', va='center', fontsize=11, family='serif')
ax.text(7.2, 1.78, r'$2$', ha='center', va='center', fontsize=11, family='serif')
ax.text(9.4, 1.78, r'$+\infty$', ha='center', va='center', fontsize=11, family='serif')

# Values f'(x)
ax.text(3.15, 1.22, r'$+$', ha='center', va='center', fontsize=12, family='serif')
ax.text(4.4, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
ax.text(5.8, 1.22, r'$-$', ha='center', va='center', fontsize=12, family='serif')
ax.text(7.2, 1.22, r'$0$', ha='center', va='center', fontsize=11, family='serif')
ax.text(8.3, 1.22, r'$+$', ha='center', va='center', fontsize=12, family='serif')

# Arrows & Values f(x)
ax.text(1.9, 0.15, r'$-\infty$', ha='center', va='center', fontsize=10, family='serif')
ax.text(4.4, 0.78, r'$3$', ha='center', va='center', fontsize=11, family='serif')
ax.text(7.2, 0.15, r'$-1$', ha='center', va='center', fontsize=11, family='serif')
ax.text(9.4, 0.78, r'$+\infty$', ha='center', va='center', fontsize=10, family='serif')

ax.annotate('', xy=(4.0, 0.7), xytext=(2.3, 0.2), arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
ax.annotate('', xy=(6.8, 0.25), xytext=(4.8, 0.72), arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))
ax.annotate('', xy=(9.0, 0.7), xytext=(7.6, 0.25), arrowprops=dict(arrowstyle='->', lw=1.2, color='black'))

ax.set_xlim(-0.1, 10.1)
ax.set_ylim(-0.1, 2.2)
plt.savefig('/tmp/bbt_cau1.png', bbox_inches='tight', pad_inches=0.02)
plt.close()

# Graph for Question 5
fig, ax = plt.subplots(figsize=(3.4, 3.2), dpi=300)
x = np.linspace(-2.2, 2.2, 300)
y = x**3 - 3*x

ax.plot(x, y, 'k-', lw=1.6)

# Axes
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)

ax.annotate('', xy=(2.4, 0), xytext=(2.1, 0), arrowprops=dict(arrowstyle='->', lw=1, color='black'))
ax.annotate('', xy=(0, 3.8), xytext=(0, 3.4), arrowprops=dict(arrowstyle='->', lw=1, color='black'))

ax.text(2.35, -0.35, r'$x$', fontsize=11, ha='center', family='serif')
ax.text(-0.25, 3.65, r'$y$', fontsize=11, va='center', family='serif')
ax.text(-0.25, -0.3, r'$O$', fontsize=11, ha='center', family='serif')

# Dashed lines
ax.plot([-1, -1, 0], [0, 2, 2], 'k--', lw=0.9)
ax.plot([1, 1, 0], [0, -2, -2], 'k--', lw=0.9)

ax.text(-1, -0.38, r'$-1$', fontsize=10, ha='center', family='serif')
ax.text(1, 0.18, r'$1$', fontsize=10, ha='center', family='serif')
ax.text(0.2, 2, r'$2$', fontsize=10, va='center', family='serif')
ax.text(-0.35, -2, r'$-2$', fontsize=10, va='center', family='serif')

ax.set_xlim(-2.4, 2.5)
ax.set_ylim(-3.5, 3.9)
ax.axis('off')
plt.savefig('/tmp/dothi_cau5.png', bbox_inches='tight', pad_inches=0.05)
plt.close()
print("Figures created successfully.")
