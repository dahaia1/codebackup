import matplotlib.pyplot as plt
import numpy as np
import math
import os

# 全局配置
BASE_SCALE = 50.0
LINE_WIDTH = 1
ALPHA = 1
CELL_SIZE = 8  # 每个单元格8x8英寸
DPI = 72       # 打印精度

def valid_steps(n):
    """计算有效星形步长"""
    return [m for m in range(2, n//2+1) if math.gcd(n, m) == 1]

def setup_axes(ax, scale):
    """设置坐标系"""
    ax.set_xlim(-scale*1.1, scale*1.1)
    ax.set_ylim(-scale*1.1, scale*1.1)
    ax.set_aspect('equal')
    ax.axis('off')

def draw_polygon(n, scale, ax):
    """绘制基础多边形"""
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta) * scale
    y = np.sin(theta) * scale
    
    for i in range(n):
        next_i = (i+1) % n
        ax.plot([x[i], x[next_i]], [y[i], y[next_i]], 
               color='black', lw=LINE_WIDTH)
    setup_axes(ax, scale)

def draw_diagonal_polygon(n, scale, ax):
    """绘制带对角线多边形"""
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta) * scale
    y = np.sin(theta) * scale
    
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

def draw_compound_star(n, scale, ax):
    """绘制复合星形"""
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta) * scale
    y = np.sin(theta) * scale
    
    if n % 2 == 0:
        # 偶数边数双星
        step = n//2 - 1
        for offset in [0, 1]:
            indexes = [(i*step + offset) % n for i in range(n)]
            for i in range(n):
                start = indexes[i]
                end = indexes[(i+1) % n]
                ax.plot([x[start], x[end]], [y[start], y[end]],
                       color='black', lw=LINE_WIDTH)
    elif n % 3 == 0:
        # 3倍数三星
        step = n//3 + 1
        for offset in [0, 1, 2]:
            indexes = [(i*step + offset) % n for i in range(n)]
            for i in range(n):
                start = indexes[i]
                end = indexes[(i+1) % n]
                ax.plot([x[start], x[end]], [y[start], y[end]],
                       color='black', lw=LINE_WIDTH)
    else:
        # 全对角线
        for i in range(n):
            for j in range(i+2, n):
                ax.plot([x[i], x[j]], [y[i], y[j]],
                       color='black', lw=LINE_WIDTH*0.6, alpha=ALPHA)
    setup_axes(ax, scale)

def draw_star(n, m, scale, ax):
    """绘制步长星形"""
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta) * scale
    y = np.sin(theta) * scale
    
    for i in range(n):
        next_i = (i + m) % n
        ax.plot([x[i], x[next_i]], [y[i], y[next_i]], 
               color='black', lw=LINE_WIDTH)
    setup_axes(ax, scale)

def generate_combined_svg():
    """生成组合SVG"""
    # 计算布局参数
    layout = []
    max_cols = 0
    for n in range(3, 24):
        steps = valid_steps(n)
        print(n)
        cols = 3 + len(steps)  # 基础+对角线+复合星形+步长星形
        layout.append((n, steps, cols))
        max_cols = max(max_cols, cols)
    
    total_rows = len(layout)
    fig = plt.figure(figsize=(max_cols*CELL_SIZE, total_rows*CELL_SIZE), dpi=DPI)
    
    # 绘制所有图形
    for row_idx, (n, steps, cols) in enumerate(layout):
        scale = BASE_SCALE * math.log(n + 1)
        row_height = 1.0 / total_rows
        y_pos = 1.0 - (row_idx + 1) * row_height
        
        # 基础多边形
        ax = fig.add_axes([0/max_cols, y_pos, 1/max_cols, row_height])
        draw_polygon(n, scale, ax)
        
        # 带对角线多边形
        ax = fig.add_axes([1/max_cols, y_pos, 1/max_cols, row_height])
        draw_diagonal_polygon(n, scale, ax)
        
        # 复合星形
        ax = fig.add_axes([2/max_cols, y_pos, 1/max_cols, row_height])
        draw_compound_star(n, scale, ax)
        
        # 步长星形
        for col_idx, m in enumerate(steps, start=3):
            ax = fig.add_axes([col_idx/max_cols, y_pos, 1/max_cols, row_height])
            draw_star(n, m, scale, ax)
    
    plt.savefig("combined_shapes.svg", bbox_inches='tight', pad_inches=0.1)
    plt.close()

if __name__ == "__main__":
    generate_combined_svg()
