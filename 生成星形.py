import matplotlib.pyplot as plt
import numpy as np
import math
import os

# 全局配置参数
BASE_SCALE = 50.0       # 基础缩放比例
FIG_SIZE = (8, 8)       # 图像物理尺寸
LINE_WIDTH = 0.3        # 基础线宽
ALPHA = 0.15            # 对角线透明度

def valid_steps(n):
    """计算有效星形生成步长"""
    steps = []
    for m in range(2, n//2 + 1):
        if math.gcd(n, m) == 1:
            steps.append(m)
    return steps

def setup_axes(ax, scale):
    """统一坐标轴设置"""
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-scale*1.1, scale*1.1)
    ax.set_ylim(-scale*1.1, scale*1.1)

def generate_polygon(n, scale):
    """生成基础多边形"""
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta) * scale
    y = np.sin(theta) * scale
    
    fig = plt.figure(figsize=FIG_SIZE)
    ax = fig.add_subplot(111)
    
    for i in range(n):
        next_i = (i+1) % n
        ax.plot([x[i], x[next_i]], [y[i], y[next_i]], 
               color='black', lw=LINE_WIDTH)
    
    setup_axes(ax, scale)
    plt.savefig(f"polygons/polygon_{n}.svg", bbox_inches='tight', pad_inches=0)
    plt.close()

def generate_diagonal_polygon(n, scale):
    """生成带对角线的多边形"""
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta) * scale
    y = np.sin(theta) * scale
    
    fig = plt.figure(figsize=FIG_SIZE)
    ax = fig.add_subplot(111)
    
    # 绘制边
    for i in range(n):
        next_i = (i+1) % n
        ax.plot([x[i], x[next_i]], [y[i], y[next_i]], 
               color='black', lw=LINE_WIDTH)
    
    # 绘制对角线
    for i in range(n):
        for j in range(i+2, n):
            ax.plot([x[i], x[j]], [y[i], y[j]], 
                   color='black', lw=LINE_WIDTH*0.6, alpha=ALPHA)
    
    setup_axes(ax, scale)
    plt.savefig(f"polygons_with_diagonals/polygon_diag_{n}.svg", bbox_inches='tight', pad_inches=0)
    plt.close()

def generate_rotated_star(n, scale):
    """生成复合旋转星形（最终正确版）"""
    fig = plt.figure(figsize=FIG_SIZE)
    ax = fig.add_subplot(111)
    
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta) * scale
    y = np.sin(theta) * scale
    
    # 根据边数类型选择生成方式
    if n % 2 == 0:
        # 偶数边数生成双交叉星
        step = n//2 - 1
        for offset in [0, 1]:
            indexes = [(i*step + offset) % n for i in range(n)]
            for i in range(n):
                start = indexes[i]
                end = indexes[(i+1) % n]
                ax.plot([x[start], x[end]], [y[start], y[end]], 
                       color='black', lw=LINE_WIDTH)
    elif n % 3 == 0:
        # 3的倍数生成三交叉星
        step = n//3 + 1
        for offset in [0, 1, 2]:
            indexes = [(i*step + offset) % n for i in range(n)]
            for i in range(n):
                start = indexes[i]
                end = indexes[(i+1) % n]
                ax.plot([x[start], x[end]], [y[start], y[end]], 
                       color='black', lw=LINE_WIDTH)
    else:
        # 其他情况生成全对角线
        for i in range(n):
            for j in range(i+2, n):
                ax.plot([x[i], x[j]], [y[i], y[j]], 
                       color='black', lw=LINE_WIDTH*0.6, alpha=ALPHA)
    
    setup_axes(ax, scale)
    plt.savefig(f"stars/star_comp_{n}.svg", bbox_inches='tight', pad_inches=0)
    plt.close()

def generate_star(n, m, scale):
    """生成传统星形"""
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta) * scale
    y = np.sin(theta) * scale
    
    fig = plt.figure(figsize=FIG_SIZE)
    ax = fig.add_subplot(111)
    
    for i in range(n):
        next_i = (i + m) % n
        ax.plot([x[i], x[next_i]], [y[i], y[next_i]], 
               color='black', lw=LINE_WIDTH)
    
    setup_axes(ax, scale)
    plt.savefig(f"stars/star_{n}_{m}.svg", bbox_inches='tight', pad_inches=0)
    plt.close()

def generate_all_stars(n, scale):
    """生成所有可能的星形"""
    steps = valid_steps(n)
    if steps:
        for m in steps:
            generate_star(n, m, scale)
    else:
        generate_rotated_star(n, scale)

def generate_shapes():
    """主生成函数"""
    os.makedirs("stars", exist_ok=True)
    os.makedirs("polygons", exist_ok=True)
    os.makedirs("polygons_with_diagonals", exist_ok=True)
    
    for n in range(3, 101):
        dynamic_scale = BASE_SCALE * math.log(n + 1)
        generate_polygon(n, dynamic_scale)
        generate_diagonal_polygon(n, dynamic_scale)
        generate_all_stars(n, dynamic_scale)

if __name__ == "__main__":
    generate_shapes()
