import tkinter as tk
from math import sin, cos, radians, pi
from datetime import datetime

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("完整版指针时钟")
        
        # 创建双倍尺寸画布
        self.canvas = tk.Canvas(root, width=800, height=800, bg="white")
        self.canvas.pack()
        
        # 表盘参数
        self.center_x = 400  # 双倍中心坐标
        self.center_y = 400
        self.radius = 300    # 双倍半径
        
        # 预定义时钟数字（确保12在顶部）
        self.hour_numbers = ["12", "1", "2", "3", "4", "5", 
                           "6", "7", "8", "9", "10", "11"]
        
        # 初始化组件
        self.init_components()
        
        # 启动平滑动画
        self.update_time(smooth_update=True)

    def init_components(self):
        """初始化所有视觉组件"""
        self.draw_face()
        self.create_digital_display()
        self.hand_ids = []  # 存储指针ID

    def draw_face(self):
        """绘制完整表盘"""
        # 绘制外圆
        self.canvas.create_oval(
            self.center_x - self.radius,
            self.center_y - self.radius,
            self.center_x + self.radius,
            self.center_y + self.radius,
            width=8,
            outline="black"
        )
        
        # 绘制小时刻度
        for hour in range(12):
            # 计算角度（从顶部开始顺时针排列）
            angle = radians(hour * 30 - 90)
            
            # 主刻度线
            inner_length = self.radius - 40
            outer_length = self.radius - 20
            x1 = self.center_x + cos(angle) * inner_length
            y1 = self.center_y + sin(angle) * inner_length
            x2 = self.center_x + cos(angle) * outer_length
            y2 = self.center_y + sin(angle) * outer_length
            self.canvas.create_line(x1, y1, x2, y2, width=4, fill="black")
            
            # 绘制小时数字
            text_radius = self.radius - 70
            x_text = self.center_x + cos(angle) * text_radius
            y_text = self.center_y + sin(angle) * text_radius
            self.canvas.create_text(x_text, y_text,
                                  text=self.hour_numbers[hour],
                                  font=("Arial", 28, "bold"),
                                  fill="black")

        # 添加中心点
        self.canvas.create_oval(
            self.center_x - 8,
            self.center_y - 8,
            self.center_x + 8,
            self.center_y + 8,
            fill="red"
        )

    def create_digital_display(self):
        """创建数字时钟显示"""
        self.digital_clock = self.canvas.create_text(
            self.center_x,
            self.center_y + 250,  # 底部显示位置
            text="00:00:00",
            font=('Arial', 32, 'bold'),
            fill='darkblue'
        )

    def update_time(self, smooth_update=False):
        """带平滑动画的时间更新"""
        now = datetime.now()
        
        # 获取精确时间
        if smooth_update:
            current_time = datetime.now()
            total_seconds = current_time.second + current_time.microsecond / 1e6
            total_minutes = current_time.minute + total_seconds / 60
            total_hours = current_time.hour % 12 + total_minutes / 60
        else:
            total_seconds = now.second
            total_minutes = now.minute
            total_hours = now.hour % 12

        # 计算指针角度（弧度制）
        second_angle = radians(total_seconds * 6 - 90)
        minute_angle = radians(total_minutes * 6 - 90)
        hour_angle = radians(total_hours * 30 - 90)

        # 绘制指针（带箭头效果）
        self.draw_hand(hour_angle, 120, 12, "black")   # 时针
        self.draw_hand(minute_angle, 180, 8, "blue")   # 分针
        self.draw_hand(second_angle, 220, 4, "red")    # 秒针

        # 更新数字显示
        time_str = f"{now.hour % 12:02}:{now.minute:02}:{now.second:02}"
        self.canvas.itemconfig(self.digital_clock, text=time_str)

        # 设置50ms刷新实现平滑动画
        self.root.after(50, lambda: self.update_time(smooth_update=True))

    def draw_hand(self, angle, length, width, color):
        """绘制带箭头的时钟指针"""
        # 计算端点坐标
        end_x = self.center_x + cos(angle) * length
        end_y = self.center_y + sin(angle) * length
        
        # 创建指针
        hand = self.canvas.create_line(
            self.center_x, self.center_y,
            end_x, end_y,
            width=width,
            fill=color,
            arrow=tk.LAST,
            arrowshape=(16, 20, 8)
        )
        
        # 管理指针对象（保留最近3个）
        self.hand_ids.append(hand)
        if len(self.hand_ids) > 3:
            old_hand = self.hand_ids.pop(0)
            self.canvas.delete(old_hand)

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalogClock(root)
    root.mainloop()
