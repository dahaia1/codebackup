import tkinter as tk
from math import sin, cos, radians
from datetime import datetime

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("完整功能指针时钟")
        
        # 创建画布
        self.canvas = tk.Canvas(root, width=800, height=800, bg="white")
        self.canvas.pack()
        
        # 表盘参数
        self.center_x = 400
        self.center_y = 400
        self.radius = 300
        
        # 预定义组件参数
        self.hour_numbers = ["12", "1", "2", "3", "4", "5", 
                           "6", "7", "8", "9", "10", "11"]
        self.week_days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
        
        # 初始化组件
        self.init_components()
        self.update_time(smooth_update=True)

    def init_components(self):
        """初始化所有视觉组件"""
        self.draw_face()
        self.create_digital_display()
        self.create_calendar_window()
        self.create_am_pm_indicator()
        self.hand_ids = []

    def draw_face(self):
        """绘制表盘基础元素（已修复数字显示）"""
        # 外圆
        self.canvas.create_oval(
            self.center_x - self.radius,
            self.center_y - self.radius,
            self.center_x + self.radius,
            self.center_y + self.radius,
            width=8,
            outline="black"
        )
        
        # 小时刻度和数字
        for hour in range(12):
            angle = radians(hour * 30 - 90)
            
            # 刻度线设置（3点位置缩短）
            inner = self.radius - 40 if hour != 3 else self.radius - 70
            x1 = self.center_x + cos(angle) * inner
            y1 = self.center_y + sin(angle) * inner
            x2 = self.center_x + cos(angle) * (self.radius - 20)
            y2 = self.center_y + sin(angle) * (self.radius - 20)
            self.canvas.create_line(x1, y1, x2, y2, width=4, fill="black")
            
            # 绘制小时数字（跳过3点位置）
            if hour != 3:  # 正确跳过数字3
                text_radius = self.radius - 70
                x_text = self.center_x + cos(angle) * text_radius
                y_text = self.center_y + sin(angle) * text_radius
                self.canvas.create_text(x_text, y_text,
                                      text=self.hour_numbers[hour],
                                      font=("Arial", 28, "bold"),
                                      fill="black")

        # 中心点
        self.canvas.create_oval(
            self.center_x - 8,
            self.center_y - 8,
            self.center_x + 8,
            self.center_y + 8,
            fill="red"
        )

    def create_calendar_window(self):
        """三点钟位置的日历星期窗口"""
        window_x = self.center_x + self.radius * 0.55
        window_y = self.center_y
        
        # 背景框
        self.canvas.create_rectangle(
            window_x - 70, window_y - 35,
            window_x + 70, window_y + 35,
            fill="white",
            outline="black",
            width=2
        )
        
        # 日期显示
        self.date_text = self.canvas.create_text(
            window_x - 25, window_y,
            text="01",
            font=("Arial", 24, "bold"),
            fill="black"
        )
        
        # 星期显示
        self.week_text = self.canvas.create_text(
            window_x + 30, window_y,
            text="MON",
            font=("Arial", 20, "bold"),
            fill="blue"
        )
        
        # 分隔线
        self.canvas.create_line(
            window_x, window_y - 25,
            window_x, window_y + 25,
            width=2
        )

    def create_am_pm_indicator(self):
        """创建AM/PM指示器"""
        am_pm_x = self.center_x + self.radius * 0.35
        am_pm_y = self.center_y - self.radius * 0.15
        
        self.am_pm_text = self.canvas.create_text(
            am_pm_x, am_pm_y,
            text="AM",
            font=("Arial", 20, "bold"),
            fill="darkgreen"
        )

    def create_digital_display(self):
        """创建底部数字时钟"""
        self.digital_clock = self.canvas.create_text(
            self.center_x,
            self.center_y + 250,
            text="00:00:00",
            font=('Arial', 32, 'bold'),
            fill='darkblue'
        )

    def update_time(self, smooth_update=False):
        """更新时间显示"""
        now = datetime.now()
        
        # 获取时间信息
        current_time = datetime.now()
        is_am = current_time.hour < 12
        weekday = current_time.weekday()
        
        # 更新指针
        self.update_hands(current_time, smooth_update)
        
        # 更新数字显示
        time_str = f"{current_time.hour % 12:02}:{current_time.minute:02}:{current_time.second:02}"
        self.canvas.itemconfig(self.digital_clock, text=time_str)
        
        # 更新日历和星期
        self.canvas.itemconfig(self.date_text, text=f"{current_time.day:02}")
        self.canvas.itemconfig(self.week_text, text=self.week_days[(weekday + 1) % 7])
        
        # 更新AM/PM
        self.canvas.itemconfig(self.am_pm_text, text="AM" if is_am else "PM")
        
        # 设置刷新率
        self.root.after(50, lambda: self.update_time(smooth_update=True))

    def update_hands(self, current_time, smooth_update):
        """更新指针位置"""
        if smooth_update:
            total_seconds = current_time.second + current_time.microsecond / 1e6
            total_minutes = current_time.minute + total_seconds / 60
            total_hours = current_time.hour % 12 + total_minutes / 60
        else:
            total_seconds = current_time.second
            total_minutes = current_time.minute
            total_hours = current_time.hour % 12

        # 计算角度
        second_angle = radians(total_seconds * 6 - 90)
        minute_angle = radians(total_minutes * 6 - 90)
        hour_angle = radians(total_hours * 30 - 90)

        # 绘制指针
        self.draw_hand(hour_angle, 120, 12, "black")
        self.draw_hand(minute_angle, 180, 8, "blue")
        self.draw_hand(second_angle, 220, 4, "red")

    def draw_hand(self, angle, length, width, color):
        """绘制指针"""
        end_x = self.center_x + cos(angle) * length
        end_y = self.center_y + sin(angle) * length
        
        hand = self.canvas.create_line(
            self.center_x, self.center_y,
            end_x, end_y,
            width=width,
            fill=color,
            arrow=tk.LAST,
            arrowshape=(16, 20, 8)
        )
        
        # 管理指针对象
        self.hand_ids.append(hand)
        if len(self.hand_ids) > 3:
            old_hand = self.hand_ids.pop(0)
            self.canvas.delete(old_hand)

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalogClock(root)
    root.mainloop()
