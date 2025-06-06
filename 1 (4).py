import tkinter as tk
from tkinter import ttk
import time
import datetime
import calendar
from lunarcalendar import Converter, Solar, Lunar
import math
import random
import jieba
import pypinyin
# 示例中文文本
sample_text = "自然语言处理是人工智能的重要分支，深度学习技术推动了其快速发展"
random_words = list(jieba.cut(sample_text))

# 创建主窗口
root = tk.Tk()
root.title("数字时钟和月历日历（含农历）")

# 创建左侧框架
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

# 创建LED容器
led_container = tk.Frame(left_frame)
led_container.pack(pady=5)

# 创建两列LED
led_columns = [tk.Frame(led_container) for _ in range(2)]
for col in led_columns:
    col.pack(side=tk.LEFT, padx=10)

# 添加交通灯Canvas
traffic_light_canvas = tk.Canvas(led_container, width=80, height=180)
traffic_light_canvas.pack(side=tk.LEFT, padx=20)

# 添加方形灯Canvas
square_light_canvas = tk.Canvas(led_container, width=80, height=180)
square_light_canvas.pack(side=tk.LEFT, padx=20)
square_light = square_light_canvas.create_rectangle(20, 60, 60, 100, fill='#333333')
# 绘制交通灯框架
traffic_light_canvas.create_rectangle(20, 10, 60, 170, fill='#333333')
# 初始化三色灯
traffic_lights = [
    traffic_light_canvas.create_oval(25, 20, 55, 50, fill='#330000'),  # 红灯
    traffic_light_canvas.create_oval(25, 70, 55, 100, fill='#333300'), # 黄灯
    traffic_light_canvas.create_oval(25, 120, 55, 150, fill='#003300') # 绿灯
]
traffic_light_state = 0
color_history = set()
current_minute = time.localtime().tm_min

# 初始化LED
leds = []
colors = ['#330000'] * 8
def create_leds():
    for i in range(8):
        col_idx = i // 4
        canvas = tk.Canvas(led_columns[col_idx], width=30, height=30)
        canvas.pack(pady=5)
        led = canvas.create_oval(5,5,25,25, fill=colors[i])
        leds.append((canvas, led))
create_leds()

# 创建时钟标签
clock_label = tk.Label(left_frame, font=("Arial", 24))
clock_label.pack(pady=10)

# 创建日期标签
lunar_label = tk.Label(left_frame, font=("Arial", 18))
lunar_label.pack(pady=5)
unix_label = tk.Label(left_frame, font=("Arial", 12))
unix_label.pack()
quarter_label = tk.Label(left_frame, font=("Arial", 12))
quarter_label.pack()
week_label = tk.Label(left_frame, font=("Arial", 12))
week_label.pack()

# 创建进度条
progress_bar = ttk.Progressbar(left_frame, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

# 更新时钟的函数
led_pos = 0
def update_traffic_lights():
    global traffic_light_state, color_history, current_minute
    colors = ['#ff0000', '#00ff00', '#ffff00', '#ff0000']
    
    # 熄灭所有交通灯
    for light in traffic_lights:
        traffic_light_canvas.itemconfig(light, fill='#330000')
    
    # 根据状态点亮当前灯
    current_light = traffic_light_state % 4
    light_index = [0, 2, 1, 0][current_light]
    traffic_light_canvas.itemconfig(traffic_lights[light_index], fill=colors[current_light])
    
    # 更新方形灯颜色
    current_time = time.localtime()
    if current_time.tm_min != current_minute:
        color_history = set()
        current_minute = current_time.tm_min
    
    while True:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        new_color = f'#{r:02x}{g:02x}{b:02x}'
        if new_color not in color_history:
            color_history.add(new_color)
            break
    
    square_light_canvas.itemconfig(square_light, fill=new_color)
    
    traffic_light_state += 1
    root.after(200, update_traffic_lights)


def update_leds():
    global led_pos, colors
    
    # 熄灭所有LED
    colors = ['#000000'] * 8
    
    # 生成随机颜色
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = f'#{r:02x}{g:02x}{b:02x}'
    
    # 设置当前LED颜色
    colors[led_pos] = random_color
    
    # 更新所有LED
    for i in range(8):
        leds[i][0].itemconfig(leds[i][1], fill=colors[i])
    
    led_pos = (led_pos + 1) % 8
    root.after(200, update_leds)
update_traffic_lights()  # 启动交通灯动画

def update_clock():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    clock_label.config(text=current_time)

    # 更新新标签内容
    unix_time = int(time.time())
    unix_label.config(text=f"UNIX时间戳: {unix_time}")
    
    current_month = datetime.datetime.now().month
    quarter = (current_month - 1) // 3 + 1
    iso_year, iso_week, iso_weekday = datetime.datetime.now().isocalendar()
    quarter_start_week = (quarter-1)*13
    quarter_week = iso_week - quarter_start_week
    
    quarter_label.config(text=f"第{quarter}季度 第{quarter_week}周")
    week_label.config(text=f"今年第{iso_week}周")
    
    # 更新新标签内容
    unix_time = int(time.time())
    unix_label.config(text=f"UNIX时间戳: {unix_time}")
    
    current_month = datetime.datetime.now().month
    quarter = (current_month - 1) // 3 + 1
    iso_year, iso_week, iso_weekday = datetime.datetime.now().isocalendar()
    quarter_start_week = (quarter-1)*13
    quarter_week = iso_week - quarter_start_week
    
    quarter_label.config(text=f"第{quarter}季度 第{quarter_week}周")
    week_label.config(text=f"今年第{iso_week}周")
    # 更新农历日期
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    current_day = datetime.datetime.now().day
    solar = Solar(current_year, current_month, current_day)
    lunar = Converter.Solar2Lunar(solar)
    lunar_str = f"农历 {lunar.year}年 {lunar.month}月 {lunar.day}日"
    lunar_label.config(text=lunar_str)

    # 更新进度条
    current_second = datetime.datetime.now().second
    progress_bar["value"] = (current_second / 60) * 100
    progress_bar.pack(pady=5)  # 调整进度条间距
    root.after(100, update_clock)

# 创建月历日历的文本框
calendar_text = tk.Text(left_frame, height=10, width=20)
calendar_text.pack(pady=10)

# 更新月历日历的函数
def update_calendar():
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    cal = calendar.month(current_year, current_month)
    calendar_text.delete(1.0, tk.END)
    calendar_text.insert(tk.END, cal)

# 创建右侧框架用于摆钟和秒表
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# 创建24小时制时钟画布（摆钟左侧）
clock_24h_canvas = tk.Canvas(right_frame, width=300, height=400)
clock_24h_canvas.pack(side=tk.LEFT)

# 创建画布用于绘制摆钟
clock_canvas = tk.Canvas(right_frame, width=300, height=400)
clock_canvas.pack(side=tk.LEFT)

# 绘制摆钟表盘
def draw_24h_clock_face():
    # 表盘中心
    center_x = 150
    center_y = 150
    radius = 120

    # 绘制外圈黑色圆环
    clock_24h_canvas.create_oval(center_x - radius, center_y - radius, 
                               center_x + radius, center_y + radius, 
                               width=2, outline='black')

    # 绘制24小时刻度
    for i in range(24):
        angle = math.radians(i * 15 - 90)
        start_radius = radius - 15
        end_radius = radius
        start_x = center_x + start_radius * math.cos(angle)
        start_y = center_y + start_radius * math.sin(angle)
        end_x = center_x + end_radius * math.cos(angle)
        end_y = center_y + end_radius * math.sin(angle)
        clock_24h_canvas.create_line(start_x, start_y, end_x, end_y, width=2)
        text_x = center_x + (radius - 30) * math.cos(angle)
        text_y = center_y + (radius - 30) * math.sin(angle)
        clock_24h_canvas.create_text(text_x, text_y, text=str(i), font=("Arial", 12))

    # 绘制分针刻度（60分钟）
    for i in range(60):
        angle = math.radians(i * 6 - 90)
        start_radius = radius - 8
        end_radius = radius
        start_x = center_x + start_radius * math.cos(angle)
        start_y = center_y + start_radius * math.sin(angle)
        end_x = center_x + end_radius * math.cos(angle)
        end_y = center_y + end_radius * math.sin(angle)
        if i % 5 == 0:
            clock_24h_canvas.create_line(start_x, start_y, end_x, end_y, width=2)


def draw_clock_face():
    # 表盘中心
    center_x = 150
    center_y = 150
    radius = 120

    # 绘制表盘
    clock_canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, width=2)

    # 绘制刻度
    for i in range(60):
        angle = math.radians(i * 6 - 90)
        # 长刻度（小时刻度）
        if i % 5 == 0:
            start_radius = radius - 15
            end_radius = radius
        # 短刻度（分钟刻度）
        else:
            start_radius = radius - 8
            end_radius = radius
        start_x = center_x + start_radius * math.cos(angle)
        start_y = center_y + start_radius * math.sin(angle)
        end_x = center_x + end_radius * math.cos(angle)
        end_y = center_y + end_radius * math.sin(angle)
        clock_canvas.create_line(start_x, start_y, end_x, end_y, width=2)

    # 绘制数字
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = center_x + (radius - 20) * math.cos(angle)
        y = center_y + (radius - 20) * math.sin(angle)
        clock_canvas.create_text(x, y, text=str(i), font=("Arial", 12))

    # 绘制钟摆
    pendulum_length = 200
    pendulum_x = center_x
    pendulum_y = center_y + 20
    clock_canvas.create_line(pendulum_x, pendulum_y, pendulum_x, pendulum_y + pendulum_length, width=2, tags="pendulum")

    # 绘制摆锤
    pendulum_end_x = pendulum_x
    pendulum_end_y = pendulum_y + pendulum_length
    pendulum_ball_radius = 10
    clock_canvas.create_oval(
        pendulum_end_x - pendulum_ball_radius,
        pendulum_end_y - pendulum_ball_radius,
        pendulum_end_x + pendulum_ball_radius,
        pendulum_end_y + pendulum_ball_radius,
        fill="red",
        tags="pendulum_ball"
    )

# 更新摆钟指针和钟摆
def update_24h_clock_face():
    current_time = time.time()
    local_time = time.localtime(current_time)
    hour = local_time.tm_hour
    minute = local_time.tm_min
    second = local_time.tm_sec
    millisecond = int((current_time - int(current_time)) * 1000)

    center_x = 150
    center_y = 150
    radius = 120

    # 计算指针角度（24小时制）
    hour_angle = math.radians((hour % 24) * 15 + (minute / 60) * 15 - 90)
    minute_angle = math.radians((minute + (second + millisecond / 1000) / 60) * 6 - 90)
    second_angle = math.radians((second + millisecond / 1000) * 6 - 90)

    # 绘制指针
    hour_x = center_x + (radius * 0.5) * math.cos(hour_angle)
    hour_y = center_y + (radius * 0.5) * math.sin(hour_angle)
    minute_x = center_x + (radius * 0.7) * math.cos(minute_angle)
    minute_y = center_y + (radius * 0.7) * math.sin(minute_angle)
    second_x = center_x + (radius * 0.8) * math.cos(second_angle)
    second_y = center_y + (radius * 0.8) * math.sin(second_angle)

    clock_24h_canvas.delete("24h_hour_hand", "24h_minute_hand", "24h_second_hand")
    clock_24h_canvas.create_line(center_x, center_y, hour_x, hour_y, width=6, fill="blue", tags="24h_hour_hand")
    clock_24h_canvas.create_line(center_x, center_y, minute_x, minute_y, width=4, fill="green", tags="24h_minute_hand")
    clock_24h_canvas.create_line(center_x, center_y, second_x, second_y, width=2, fill="red", tags="24h_second_hand")
    root.after(10, update_24h_clock_face)


def update_clock_face():
    current_time = time.time()
    local_time = time.localtime(current_time)
    hour = local_time.tm_hour % 12
    minute = local_time.tm_min
    second = local_time.tm_sec
    millisecond = int((current_time - int(current_time)) * 1000)

    center_x = 150
    center_y = 150
    radius = 120

    # 计算指针角度
    hour_angle = math.radians((hour + (minute + (second + millisecond / 1000) / 60) / 60) * 30 - 90)
    minute_angle = math.radians((minute + (second + millisecond / 1000) / 60) * 6 - 90)
    second_angle = math.radians((second + millisecond / 1000) * 6 - 90)

    # 计算指针端点坐标
    hour_x = center_x + (radius * 0.5) * math.cos(hour_angle)
    hour_y = center_y + (radius * 0.5) * math.sin(hour_angle)
    minute_x = center_x + (radius * 0.7) * math.cos(minute_angle)
    minute_y = center_y + (radius * 0.7) * math.sin(minute_angle)
    second_x = center_x + (radius * 0.8) * math.cos(second_angle)
    second_y = center_y + (radius * 0.8) * math.sin(second_angle)

    # 更新指针
    clock_canvas.delete("hour_hand", "minute_hand", "second_hand")
    clock_canvas.create_line(center_x, center_y, hour_x, hour_y, width=6, fill="black", tags="hour_hand")
    clock_canvas.create_line(center_x, center_y, minute_x, minute_y, width=4, fill="black", tags="minute_hand")
    clock_canvas.create_line(center_x, center_y, second_x, second_y, width=2, fill="red", tags="second_hand")

    # 更新钟摆
    pendulum_length = 200
    pendulum_x = center_x
    pendulum_y = center_y + 20
    pendulum_angle = math.sin(current_time * 2) * 0.2  # 钟摆摆动角度
    pendulum_end_x = pendulum_x + pendulum_length * math.sin(pendulum_angle)
    pendulum_end_y = pendulum_y + pendulum_length * math.cos(pendulum_angle)
    clock_canvas.delete("pendulum", "pendulum_ball")
    clock_canvas.create_line(pendulum_x, pendulum_y, pendulum_end_x, pendulum_end_y, width=2, tags="pendulum")

    # 更新摆锤
    pendulum_ball_radius = 10
    clock_canvas.create_oval(
        pendulum_end_x - pendulum_ball_radius,
        pendulum_end_y - pendulum_ball_radius,
        pendulum_end_x + pendulum_ball_radius,
        pendulum_end_y + pendulum_ball_radius,
        fill="red",
        tags="pendulum_ball"
    )

    root.after(10, update_clock_face)

# 创建画布用于绘制第一个秒表
stopwatch_canvas_1 = tk.Canvas(right_frame, width=300, height=400)
stopwatch_canvas_1.pack(side=tk.LEFT)

# 绘制第一个秒表表盘（内圈 30 分钟，外圈 30 秒）
def draw_stopwatch_face_1():
    center_x = 150
    center_y = 150
    radius = 120

    # 绘制表盘
    stopwatch_canvas_1.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, width=2)

    # 绘制 30 分钟内圈刻度
    for i in range(30):
        angle = math.radians(i * 12 - 90)
        start_radius = radius - 15
        end_radius = radius
        start_x = center_x + start_radius * math.cos(angle)
        start_y = center_y + start_radius * math.sin(angle)
        end_x = center_x + end_radius * math.cos(angle)
        end_y = center_y + end_radius * math.sin(angle)
        stopwatch_canvas_1.create_line(start_x, start_y, end_x, end_y, width=2)
        if i % 5 == 0:
            text_x = center_x + (radius - 20) * math.cos(angle)
            text_y = center_y + (radius - 20) * math.sin(angle)
            stopwatch_canvas_1.create_text(text_x, text_y, text=str(i), font=("Arial", 12))

    # 绘制 30 秒外圈刻度
    for i in range(30):
        angle = math.radians(i * 12 - 90)
        start_radius = radius - 8
        end_radius = radius
        start_x = center_x + start_radius * math.cos(angle)
        start_y = center_y + start_radius * math.sin(angle)
        end_x = center_x + end_radius * math.cos(angle)
        end_y = center_y + end_radius * math.sin(angle)
        stopwatch_canvas_1.create_line(start_x, start_y, end_x, end_y, width=2)

# 更新第一个秒表指针
def update_stopwatch_face_1():
    current_time = time.time()
    local_time = time.localtime(current_time)
    minute = local_time.tm_min % 30
    second = local_time.tm_sec % 30
    millisecond = int((current_time - int(current_time)) * 1000)

    center_x = 150
    center_y = 150
    radius = 120

    # 计算指针角度
    minute_angle = math.radians((minute + (second + millisecond / 1000) / 60) * 12 - 90)
    second_angle = math.radians((second + millisecond / 1000) * 12 - 90)

    # 计算指针端点坐标
    minute_x = center_x + (radius * 0.7) * math.cos(minute_angle)
    minute_y = center_y + (radius * 0.7) * math.sin(minute_angle)
    second_x = center_x + (radius * 0.8) * math.cos(second_angle)
    second_y = center_y + (radius * 0.8) * math.sin(second_angle)

    # 更新指针
    stopwatch_canvas_1.delete("stopwatch_minute_hand_1", "stopwatch_second_hand_1")
    stopwatch_canvas_1.create_line(center_x, center_y, minute_x, minute_y, width=4, fill="black", tags="stopwatch_minute_hand_1")
    stopwatch_canvas_1.create_line(center_x, center_y, second_x, second_y, width=2, fill="red", tags="stopwatch_second_hand_1")

    root.after(10, update_stopwatch_face_1)

# 创建画布用于绘制第二个秒表
stopwatch_canvas_2 = tk.Canvas(right_frame, width=300, height=400)
stopwatch_canvas_2.pack(side=tk.LEFT)

# 绘制第二个秒表表盘（内圈 30 分钟，外圈 6 秒）
def draw_stopwatch_face_2():
    center_x = 150
    center_y = 150
    radius = 120

    # 绘制表盘
    stopwatch_canvas_2.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, width=2)

    # 绘制 30 分钟内圈刻度
    for i in range(30):
        angle = math.radians(i * 12 - 90)
        start_radius = radius - 15
        end_radius = radius
        start_x = center_x + start_radius * math.cos(angle)
        start_y = center_y + start_radius * math.sin(angle)
        end_x = center_x + end_radius * math.cos(angle)
        end_y = center_y + end_radius * math.sin(angle)
        stopwatch_canvas_2.create_line(start_x, start_y, end_x, end_y, width=2)
        # 去掉绘制 0 - 30 数字的代码
        # if i % 5 == 0:
        #     text_x = center_x + (radius - 20) * math.cos(angle)
        #     text_y = center_y + (radius - 20) * math.sin(angle)
        #     stopwatch_canvas_2.create_text(text_x, text_y, text=str(i), font=("Arial", 12))

    # 绘制 6 秒外圈刻度
    for i in range(7):  # 这里改为 7，因为要包含 0 到 6
        angle = math.radians(i * (360 / 6) - 90)  # 计算每个刻度的角度
        start_radius = radius - 8
        end_radius = radius
        start_x = center_x + start_radius * math.cos(angle)
        start_y = center_y + start_radius * math.sin(angle)
        end_x = center_x + end_radius * math.cos(angle)
        end_y = center_y + end_radius * math.sin(angle)
        stopwatch_canvas_2.create_line(start_x, start_y, end_x, end_y, width=2)
        text_x = center_x + (radius - 20) * math.cos(angle)
        text_y = center_y + (radius - 20) * math.sin(angle)
        stopwatch_canvas_2.create_text(text_x, text_y, text=str(i), font=("Arial", 12))

# 更新第二个秒表指针
def update_stopwatch_face_2():
    current_time = time.time()
    local_time = time.localtime(current_time)
    minute = local_time.tm_min % 30
    second = local_time.tm_sec % 6
    millisecond = int((current_time - int(current_time)) * 1000)

    center_x = 150
    center_y = 150
    radius = 120

    # 计算指针角度
    minute_angle = math.radians((minute + (second + millisecond / 1000) / 60) * 12 - 90)
    second_angle = math.radians((second + millisecond / 1000) * (360 / 6) - 90)  # 调整秒指针角度计算

    # 计算指针端点坐标
    minute_x = center_x + (radius * 0.7) * math.cos(minute_angle)
    minute_y = center_y + (radius * 0.7) * math.sin(minute_angle)
    second_x = center_x + (radius * 0.8) * math.cos(second_angle)
    second_y = center_y + (radius * 0.8) * math.sin(second_angle)

    # 更新指针
    stopwatch_canvas_2.delete("stopwatch_minute_hand_2", "stopwatch_second_hand_2")
    stopwatch_canvas_2.create_line(center_x, center_y, minute_x, minute_y, width=4, fill="black", tags="stopwatch_minute_hand_2")
    stopwatch_canvas_2.create_line(center_x, center_y, second_x, second_y, width=2, fill="red", tags="stopwatch_second_hand_2")

    root.after(10, update_stopwatch_face_2)

# 创建右侧装饰画布
decor_canvas = tk.Canvas(right_frame, width=300, height=400)
decor_canvas.pack(side=tk.RIGHT)

# 更新装饰图形的函数
def update_decor():
    current_time = time.localtime()
    second = current_time.tm_sec
    if second >= 3:
        decor_canvas.delete("decor_shape")
        center_x = 150
        center_y = 150
        radius = 100
        points = []
        for i in range(second):
            angle = 2 * math.pi * i / second
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.extend([x, y])
        decor_canvas.create_polygon(points, width=2, tags="decor_shape")
    root.after(1000, update_decor)

# 添加随机词语显示


# 拼音标签
text_label = tk.Label(root, text='')
text_label.pack(pady=5)
pinyin_label = tk.Label(root,text='')
pinyin_label.pack(pady=5)



def update_random_text():
    random_word = random.choice(random_words)
    # 生成带声调的拼音
    pinyin_list = pypinyin.lazy_pinyin(random_word, style=pypinyin.Style.TONE)
    pinyin_str = ' '.join(pinyin_list)
    print(pinyin_str)
    
    # 更新标签显示
    #pinyin_label.config(text=pinyin_str, font=('Arial', 12))
    text_label.config(text=random_word+pinyin_str, font=('Arial', 16, 'italic'), bd=0, relief='flat')
    root.after(1000, update_random_text)

# 创建文本标签
# 拼音标签


# 启动随机词语更新
update_random_text()

# 初始化24小时制表盘
draw_24h_clock_face()

# 初始化摆钟表盘
draw_clock_face()

# 初始化第一个秒表表盘
draw_stopwatch_face_1()

# 初始化第二个秒表表盘
draw_stopwatch_face_2()

# 初始化时钟和月历日历
update_clock()
update_calendar()
update_leds()

# 开始更新24小时制时钟
update_24h_clock_face()

# 开始更新摆钟
update_clock_face()

# 开始更新第一个秒表
update_stopwatch_face_1()

# 创建随机文字标签
text_label = tk.Label(left_frame, font=("Arial", 16))
text_label.pack(pady=5)

update_stopwatch_face_2()

# 开始更新装饰图形
update_decor()

# 运行主循环
root.mainloop()
