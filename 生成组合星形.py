import matplotlib
matplotlib.use('Agg')  # 使用非GUI后端
import matplotlib.pyplot as plt
import numpy as np
import math

# 优化配置参数
BASE_SCALE = 25.0       # 缩小基础比例
CELL_SIZE = 4           # 单元格物理尺寸（英寸）
DPI = 96                # 输出分辨率
LINE_WIDTH = 0.3
ALPHA = 0.15
BATCH_SIZE = 20         # 每批处理20个边数

def valid_steps(n):
    """计算有效星形步长"""
    return [m for m in range(2, n//2+1) if math.gcd(n, m) == 1]

def setup_axes(ax, scale):
    """统一坐标轴设置"""
    ax.set_xlim(-scale*1.1, scale*1.1)
    ax.set_ylim(-scale*1.1, scale*1.1)
    ax.set_aspect('equal')
    ax.axis('off')

def draw_polygon(n, scale, ax):
    """绘制基础多边形"""
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta) * scale
    y = np.sin(theta) * scale
    ax.plot(np.append(x, x[0]), np.append(y, y[0]), color='black', lw=LINE_WIDTH)
    setup_axes(ax, scale)

def draw_diagonal_polygon(n, scale, ax):
    """绘制带对角线多边形"""
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta) * scale
    y = np.sin(theta) * scale
    
    # 绘制边
    ax.plot(np.append(x, x[0]), np.append(y, y[0]), color='black', lw=LINE_WIDTH)
    
    # 绘制对角线
    for i in range(n):
        for j in range(i+2, n):
            ax.plot([x[i], x[j]], [y[i], y[j]], color='black', lw=LINE_WIDTH*0.6, alpha=ALPHA)
    setup_axes(ax, scale)

def draw_compound_star(n, scale, ax):
    """绘制复合星形（优化内存版）"""
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta) * scale
    y = np.sin(theta) * scale
    
    if n % 2 == 0:
        # 偶数边数双星
        step = n//2 - 1
        for offset in [0, 1]:
            idx = [(i*step + offset) % n for i in range(n)]
            ax.plot(x[idx], y[idx], color='black', lw=LINE_WIDTH)
    elif n % 3 == 0:
        # 3倍数三星
        step = n//3 + 1
        for offset in [0, 1, 2]:
            idx = [(i*step + offset) % n for i in range(n)]
            ax.plot(x[idx], y[idx], color='black', lw=LINE_WIDTH)
    else:
        # 全对角线
        for i in range(n):
            for j in range(i+2, n):
                ax.plot([x[i], x[j]], [y[i], y[j]], color='black', lw=LINE_WIDTH*0.6, alpha=ALPHA)
    setup_axes(ax, scale)

def draw_star(n, m, scale, ax):
    """绘制步长星形"""
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta) * scale
    y = np.sin(theta) * scale
    idx = [(i*m) % n for i in range(n)]
    ax.plot(np.append(x[idx], x[0]), np.append(y[idx], y[0]), color='black', lw=LINE_WIDTH)
    setup_axes(ax, scale)

def generate_batch(start_n, end_n):
    """生成指定范围内的组合图形"""
    # 计算布局参数
    layout = []
    max_cols = 0
    for n in range(start_n, end_n+1):
        steps = valid_steps(n)
        cols = 3 + len(steps)  # 基础+对角线+复合星形+步长星形
        layout.append((n, steps, cols))
        max_cols = max(max_cols, cols)
    
    total_rows = len(layout)
    if total_rows == 0:
        return
    
    # 创建图形
    fig = plt.figure(
        figsize=(max_cols*CELL_SIZE, total_rows*CELL_SIZE),
        dpi=DPI,
        tight_layout=True
    )
    
    # 绘制每个图形
    for row_idx, (n, steps, cols) in enumerate(layout):
        scale = BASE_SCALE * math.log(n + 1)
        
        # 基础多边形
        ax = fig.add_subplot(total_rows, max_cols, row_idx*max_cols + 1)
        draw_polygon(n, scale, ax)
        
        # 带对角线多边形
        ax = fig.add_subplot(total_rows, max_cols, row_idx*max_cols + 2)
        draw_diagonal_polygon(n, scale, ax)
        
        # 复合星形
        ax = fig.add_subplot(total_rows, max_cols, row_idx*max_cols + 3)
        draw_compound_star(n, scale, ax)
        
        # 步长星形
        for step_idx, m in enumerate(steps, start=4):
            ax = fig.add_subplot(total_rows, max_cols, row_idx*max_cols + step_idx)
            draw_star(n, m, scale, ax)
    
    # 保存并清理内存
    plt.savefig(f"combined_{start_n}-{end_n}.svg", bbox_inches='tight')
    plt.close(fig)

def generate_all():
    """分批次生成全部图形"""
    for start in range(3, 101, BATCH_SIZE):
        end = min(start + BATCH_SIZE - 1, 100)
        print(f"Generating {start}-{end}...")
        generate_batch(start, end)

if __name__ == "__main__":
    generate_all()
