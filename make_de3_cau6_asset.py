import os
os.environ['MPLCONFIGDIR'] = '/tmp/matplotlib'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 4.0), dpi=300)
ax.set_xlim(-0.5, 5.5)
ax.set_ylim(-0.5, 6.4)
ax.axis('off')

# Ground
ax.plot([-0.2, 5.2], [0, 0], 'k-', lw=1.5)
for x in np.arange(0, 5.2, 0.3):
    ax.plot([x, x-0.15], [0, -0.2], 'gray', lw=0.8)
ax.text(2.5, -0.4, 'Mặt sàn', ha='center', va='center', fontsize=10.5, family='serif')

# Wall
ax.plot([4.5, 4.5], [0, 6.2], 'k-', lw=2.5)

# Painting on wall AB
ax.plot([4.5, 4.5], [2.6, 5.6], color='darkred', lw=6, solid_capstyle='butt')
ax.plot([4.35, 4.65], [5.6, 5.6], 'k-', lw=1.5)
ax.plot([4.35, 4.65], [2.6, 2.6], 'k-', lw=1.5)
ax.text(4.7, 5.6, 'A (mép trên)', ha='left', va='center', fontsize=10.5, fontweight='bold', family='serif')
ax.text(4.7, 2.6, 'B (mép dưới)', ha='left', va='center', fontsize=10.5, fontweight='bold', family='serif')
ax.text(4.7, 4.1, 'Bức tranh (3 m)', ha='left', va='center', fontsize=10, color='darkred', family='serif', rotation=-90)

# Person at x = 1.8
xp = 1.8
# Body
ax.plot([xp, xp], [0, 1.6], 'k-', lw=1.5)
# Head
circle = plt.Circle((xp, 1.7), 0.12, color='black', fill=False, lw=1.2)
ax.add_patch(circle)
ax.plot([xp-0.2, xp+0.2], [0, 0], 'k-', lw=2) # feet
ax.text(xp, 1.95, 'Mắt người (M)', ha='center', va='center', fontsize=10.5, fontweight='bold', family='serif')

# Eye level line MO
ax.plot([xp, 4.5], [1.6, 1.6], 'k--', lw=1)
ax.text(4.65, 1.6, 'O', ha='left', va='center', fontsize=10.5, family='serif')

# Sight lines MA and MB
ax.plot([xp, 4.5], [1.6, 5.6], 'b-', lw=1.3)
ax.plot([xp, 4.5], [1.6, 2.6], 'b-', lw=1.3)

# Angle theta arc
angle_arc = matplotlib.patches.Arc((xp, 1.6), 1.2, 1.2, angle=0, theta1=np.degrees(np.arctan2(1.0, 2.7)), theta2=np.degrees(np.arctan2(4.0, 2.7)), color='red', lw=1.8)
ax.add_patch(angle_arc)
ax.text(xp + 0.8, 2.15, r'$\theta$', fontsize=13, fontweight='bold', color='red', family='serif')

# Distance x dimension
ax.annotate('', xy=(4.5, 0.4), xytext=(xp, 0.4), arrowprops=dict(arrowstyle='<->', lw=1.2, color='black'))
ax.text((xp+4.5)/2, 0.65, r'$x$', ha='center', va='center', fontsize=12, fontweight='bold', family='serif')

# Height dimensions
# Eye height 1.6m
ax.annotate('', xy=(xp-0.35, 1.6), xytext=(xp-0.35, 0), arrowprops=dict(arrowstyle='<->', lw=1, color='black'))
ax.text(xp-0.45, 0.8, '1,6 m', ha='right', va='center', fontsize=10, family='serif')

# Bottom of painting 2.6m
ax.annotate('', xy=(3.8, 2.6), xytext=(3.8, 0), arrowprops=dict(arrowstyle='<->', lw=1, color='black'))
ax.text(3.65, 1.3, '2,6 m', ha='right', va='center', fontsize=10, family='serif')

# Painting height 3m
ax.annotate('', xy=(3.8, 5.6), xytext=(3.8, 2.6), arrowprops=dict(arrowstyle='<->', lw=1, color='darkred'))
ax.text(3.65, 4.1, '3 m', ha='right', va='center', fontsize=10, color='darkred', family='serif')

plt.tight_layout()
plt.savefig('assets/de3_ngam_tranh_cau6.png', dpi=300)
print('SUCCESS')
