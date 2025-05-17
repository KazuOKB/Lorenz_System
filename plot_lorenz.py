#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 3Dプロット用

# データ読み込み
data = np.loadtxt('lorentz_data.txt')
t, x, y, z = data[:,0], data[:,1], data[:,2], data[:,3]

# —– 3D アトラクタ —–
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z, linewidth=0.5, alpha=0.85)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('Lorenz atractor')
plt.tight_layout()
plt.savefig('lorenz_attractor.png', dpi=300, bbox_inches='tight', pad_inches=0.02)
plt.show()
