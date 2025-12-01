import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 设置参数
frames = 100
t = np.linspace(0, 2*np.pi, frames)

# 模拟气泡半径变化 (Rayleigh-Plesset方程的简化拟合)
# 快速膨胀，然后震荡衰减
radius = 5 * np.exp(-0.2*t) * np.sin(3*t) + 1
radius[radius < 0.5] = 0.5 # 保持最小半径

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_facecolor('#001f3f') # 深海蓝背景

bubble = plt.Circle((0, 0), 0.1, color='white', alpha=0.7)
ax.add_patch(bubble)

title = ax.text(0, 8, "Gemini Airgun Bubble Oscillation", ha='center', color='white')

def animate(i):
    r = radius[i]
    # 模拟气泡大小变化
    bubble.set_radius(r)
    # 模拟震荡时的透明度变化
    bubble.set_alpha(0.4 + 0.3 * np.sin(i/5))
    
    if i < 10:
        title.set_text("Phase: Firing (Release)")
    elif 10 <= i < 40:
         title.set_text("Phase: Expansion (Low Freq Generation)")
    else:
         title.set_text("Phase: Collapse & Damping")
    return bubble, title

ani = animation.FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)

# 保存为gif (需要安装imagemagick或ffmpeg)
# ani.save('airgun_demo.gif', writer='imagemagick')
plt.show()