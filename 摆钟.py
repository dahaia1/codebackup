import tkinter as tk
import math
import time
import winsound

class MechanicalClock:
    def __init__(self, master):
        self.master = master
        self.master.title("机械摆钟")
        self.canvas = tk.Canvas(master, width=600, height=800, bg='white')
        self.canvas.pack()

        # 初始化参数
        self.clock_radius = 250
        self.center_x = 300
        self.center_y = 300
        self.pendulum_pivot_y = self.center_y + self.clock_radius + 50
        self.last_hour = -1
        self.pendulum_angle = 0
        self.pendulum_direction = 1
        self.swing_speed = 0.6
        self.max_angle = 20
        self.damping = 0.998

        self.setup_face()
        self.setup_hands()  # 确保包含指针初始化方法
        self.setup_pendulum()
        self.update_clock()

    def setup_face(self):
        """创建表盘和刻度"""
        # 表盘外圆
        self.canvas.create_oval(
            self.center_x - self.clock_radius,
            self.center_y - self.clock_radius,
            self.center_x + self.clock_radius,
            self.center_y + self.clock_radius,
            width=4
        )
        
        # 小时刻度和数字
        for i in range(12):
            angle = math.radians(i * 30)
            inner = self.clock_radius - 20
            outer = self.clock_radius - 10
            x_inner = self.center_x + inner * math.sin(angle)
            y_inner = self.center_y - inner * math.cos(angle)
            x_outer = self.center_x + outer * math.sin(angle)
            y_outer = self.center_y - outer * math.cos(angle)
            self.canvas.create_line(x_inner, y_inner, x_outer, y_outer, width=3)
            
            # 添加水平数字
            num_radius = self.clock_radius - 50
            x = self.center_x + num_radius * math.sin(angle)
            y = self.center_y - num_radius * math.cos(angle)
            self.canvas.create_text(x, y, 
                text=str(12 if i == 0 else i),
                font=('Arial', 14, 'bold'))

        # 分钟刻度
        for i in range(60):
            angle = math.radians(i * 6)
            inner = self.clock_radius - 15
            outer = self.clock_radius - 10
            x_inner = self.center_x + inner * math.sin(angle)
            y_inner = self.center_y - inner * math.cos(angle)
            x_outer = self.center_x + outer * math.sin(angle)
            y_outer = self.center_y - outer * math.cos(angle)
            self.canvas.create_line(x_inner, y_inner, x_outer, y_outer)

    def setup_hands(self):
        """初始化时钟指针"""
        self.hands = {
            'hour': self.create_hand(100, 6, 'black'),
            'minute': self.create_hand(160, 4, 'blue'),
            'second': self.create_hand(180, 2, 'red')
        }

    def create_hand(self, length, width, color):
        """创建单个指针"""
        return self.canvas.create_line(
            self.center_x, self.center_y,
            self.center_x, self.center_y - length,
            width=width, fill=color, arrow=tk.LAST
        )

    def setup_pendulum(self):
        """初始化钟摆系统"""
        # 悬挂支架
        self.canvas.create_rectangle(
            self.center_x - 30, self.pendulum_pivot_y - 10,
            self.center_x + 30, self.pendulum_pivot_y,
            fill='#666', outline='black'
        )
        # 摆杆和摆锤
        self.pendulum_rod = self.canvas.create_line(
            self.center_x, self.pendulum_pivot_y,
            self.center_x, self.pendulum_pivot_y + 200,
            width=3
        )
        self.pendulum_bob = self.canvas.create_oval(
            self.center_x - 25, self.pendulum_pivot_y + 180,
            self.center_x + 25, self.pendulum_pivot_y + 220,
            fill='#654321', outline='black'
        )

    def update_clock(self):
        """更新时钟状态"""
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec
        
        # 更新指针
        self.update_hand('hour', hours * 30 + minutes * 0.5)
        self.update_hand('minute', minutes * 6 + seconds * 0.1)
        self.update_hand('second', seconds * 6)
        
        # 更新钟摆
        self.update_pendulum()
        
        # 整点报时
        if minutes == 0 and seconds == 0 and hours != self.last_hour:
            self.chime()
            self.last_hour = hours
        
        self.master.after(50, self.update_clock)

    def update_hand(self, hand_name, angle):
        """更新指针位置"""
        angle_rad = math.radians(angle - 90)
        hand = self.hands[hand_name]
        length = self.clock_radius - 20 if hand_name == 'hour' else self.clock_radius
        
        x = self.center_x + math.cos(angle_rad) * (length - 40 if hand_name == 'hour' else length)
        y = self.center_y + math.sin(angle_rad) * (length - 40 if hand_name == 'hour' else length)
        
        self.canvas.coords(hand, self.center_x, self.center_y, x, y)

    def update_pendulum(self):
        """改进后的钟摆物理模拟"""
        acceleration = -math.sin(math.radians(self.pendulum_angle)) * 0.8
        self.pendulum_angle += acceleration + self.swing_speed * self.pendulum_direction
        
        if abs(self.pendulum_angle) > self.max_angle:
            self.pendulum_direction *= -1
            self.pendulum_angle = math.copysign(self.max_angle, self.pendulum_angle)
        
        self.pendulum_angle *= self.damping

        angle_rad = math.radians(self.pendulum_angle)
        rod_length = 200
        x = self.center_x + math.sin(angle_rad) * rod_length
        y = self.pendulum_pivot_y + math.cos(angle_rad) * rod_length
        
        self.canvas.coords(self.pendulum_rod, 
            self.center_x, self.pendulum_pivot_y,
            x, y
        )
        self.canvas.coords(
            self.pendulum_bob,
            x - 25, y - 20,
            x + 25, y + 20
        )

    def chime(self):
        """整点报时"""
        for _ in range(3):
            winsound.Beep(800, 200)
            winsound.Beep(1200, 300)
            self.master.update()
            time.sleep(0.2)

if __name__ == "__main__":
    root = tk.Tk()
    clock = MechanicalClock(root)
    root.mainloop()
