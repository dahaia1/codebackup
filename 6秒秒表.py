import tkinter as tk
import math
import time

class MechanicalStopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("机械秒表")
        self.running = False
        self.start_time = 0
        self.elapsed = 0
        
        # 布局参数调整
        self.main_center = (200, 230)  # 主表盘中心
        self.sub_center = (200, 180)    # 小表盘下移后的中心
        
        self.canvas = tk.Canvas(root, width=400, height=450, bg="#f0f0f0")
        self.canvas.pack()
        
        # 调整后的绘制顺序
        self.draw_sub_dial()    # 先绘制小表盘
        self.draw_main_dial()   # 后绘制主表盘
        self.draw_decorations()
        self.draw_brand()
        
        # 指针系统
        self.main_hand = self.create_hand(self.main_center, 90, "red")
        self.sub_hand = self.create_hand(self.sub_center, 40, "blue")
        
        self.create_controls()

    def draw_main_dial(self):
        """主表盘（6秒刻度）"""
        cx, cy = self.main_center
        # 外圈刻度（每0.5秒一个长刻度）
        for i in range(60):
            angle = math.radians(90 - i*6)
            if i%5 == 0:
                self.draw_tick(cx, cy, 150, 135, angle, width=2)
            else:
                self.draw_tick(cx, cy, 150, 142, angle, width=1)
        
        # 主表盘数字（1-6）
        for i in range(6):
            angle = math.radians(90 - i*60)
            x = cx + 120 * math.cos(angle)
            y = cy - 120 * math.sin(angle)
            self.canvas.create_text(x, y, text=str(i+1), 
                                  font=("Arial", 14, "bold"))

    def draw_sub_dial(self):
        """下移后的小表盘（显示0/15/30/45）"""
        cx, cy = self.sub_center
        
        # 刻度系统
        for i in range(60):
            angle = math.radians(90 - i*6)
            if i%15 == 0:  # 每15秒一个长刻度
                self.draw_tick(cx, cy, 45, 35, angle, width=1.5)
            else:
                self.draw_tick(cx, cy, 45, 40, angle, width=0.5)
        
        # 数字布局调整
        number_config = {
            0: (0, -30, 12),    # 顶部
            15: (30, 0, 10),    # 右侧
            30: (0, 30, 12),    # 底部
            45: (-30, 0, 10)    # 左侧
        }
        for num, (dx, dy, fs) in number_config.items():
            self.canvas.create_text(cx+dx, cy+dy, text=str(num),
                                  font=("Arial", fs), fill="#333333")

    def draw_tick(self, cx, cy, r1, r2, angle, width=1):
        """通用刻度绘制方法"""
        x1 = cx + r1 * math.cos(angle)
        y1 = cy - r1 * math.sin(angle)
        x2 = cx + r2 * math.cos(angle)
        y2 = cy - r2 * math.sin(angle)
        self.canvas.create_line(x1, y1, x2, y2, width=width)

    def draw_decorations(self):
        """装饰元素"""
        # 主中心点
        cx, cy = self.main_center
        self.canvas.create_oval(cx-5, cy-5, cx+5, cy+5,
                              fill="black", outline="")
        # 小表盘中心点
        sx, sy = self.sub_center
        self.canvas.create_oval(sx-3, sy-3, sx+3, sy+3,
                              fill="black", outline="")
        # 装饰环
        self.canvas.create_oval(cx-155, cy-155, cx+155, cy+155,
                              outline="#999999", width=1)

    def draw_brand(self):
        """品牌标识"""
        self.canvas.create_text(200, 400, text="6秒秒表模拟器",
                              font=("宋体", 12), fill="#444444")

    def create_hand(self, center, length, color):
        """创建带箭头的指针"""
        cx, cy = center
        return self.canvas.create_line(cx, cy, cx, cy-length,
                                     width=2, fill=color,
                                     arrow=tk.LAST, arrowshape=(6,8,3))

    def create_controls(self):
        """控制按钮面板"""
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=10)
        
        controls = [
            ("启动", "#4CAF50", self.start),
            ("停止", "#F44336", self.stop),
            ("复位", "#2196F3", self.reset)
        ]
        
        for text, color, cmd in controls:
            btn = tk.Button(btn_frame, text=text, command=cmd,
                          width=8, bg=color, fg="white",
                          font=("微软雅黑", 10), relief="flat")
            btn.pack(side=tk.LEFT, padx=8)
            btn.bind("<Enter>", lambda e: e.widget.config(relief="groove"))
            btn.bind("<Leave>", lambda e: e.widget.config(relief="flat"))

    def update_hands(self):
        if self.running:
            current_time = time.time() - self.start_time + self.elapsed
            
            # 主指针（6秒/圈）
            main_angle = math.radians(90 - (current_time % 6) * 60)
            self.rotate_hand(self.main_hand, self.main_center, 90, main_angle)
            
            # 小表盘指针（60秒/圈）
            sub_angle = math.radians(90 - (current_time % 60) * 6)
            self.rotate_hand(self.sub_hand, self.sub_center, 40, sub_angle)
            
            self.root.after(20, self.update_hands)

    def rotate_hand(self, hand, center, length, angle):
        """旋转指针"""
        cx, cy = center
        x = cx + length * math.cos(angle)
        y = cy - length * math.sin(angle)
        self.canvas.coords(hand, cx, cy, x, y)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.update_hands()

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed += time.time() - self.start_time

    def reset(self):
        self.running = False
        self.elapsed = 0
        self.rotate_hand(self.main_hand, self.main_center, 90, math.radians(90))
        self.rotate_hand(self.sub_hand, self.sub_center, 40, math.radians(90))

if __name__ == "__main__":
    root = tk.Tk()
    app = MechanicalStopwatch(root)
    root.mainloop()
