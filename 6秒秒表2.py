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
        
        # 创建画布
        self.canvas = tk.Canvas(root, width=400, height=450, bg="#f0f0f0")
        self.canvas.pack()
        
        # 绘制表盘元素
        self.draw_outer_ring()
        self.draw_inner_ring()
        self.draw_center()
        self.draw_brand()
        
        # 创建指针
        self.outer_hand = self.canvas.create_line(200, 200, 200, 80, width=2, fill="red")
        self.inner_hand = self.canvas.create_line(200, 200, 200, 120, width=2, fill="blue")
        
        # 控制按钮
        self.create_buttons()
    
    def draw_outer_ring(self):
        # 外圈刻度（每0.1秒一个刻度）
        for i in range(60):
            angle = math.radians(90 - i*6)
            x1 = 200 + 170 * math.cos(angle)
            y1 = 200 - 170 * math.sin(angle)
            x2 = 200 + 160 * math.cos(angle)
            y2 = 200 - 160 * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, width=2 if i%10==0 else 1)
        
        # 外圈数字（0-6秒）
        for i in range(6):
            angle = math.radians(90 - i*60)
            x = 200 + 140 * math.cos(angle)
            y = 200 - 140 * math.sin(angle)
            self.canvas.create_text(x, y, text=str(i+1), font=("Arial", 12))

    def draw_inner_ring(self):
        # 内圈刻度（每1秒一个刻度）
        for i in range(60):
            angle = math.radians(90 - i*6)
            x1 = 200 + 120 * math.cos(angle)
            y1 = 200 - 120 * math.sin(angle)
            x2 = 200 + 110 * math.cos(angle)
            y2 = 200 - 110 * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, width=2 if i%5==0 else 1)
        
        # 内圈数字（0-60秒）
        for i in range(0, 60, 5):
            angle = math.radians(90 - i*6)
            x = 200 + 100 * math.cos(angle)
            y = 200 - 100 * math.sin(angle)
            self.canvas.create_text(x, y, text=str(i), font=("Arial", 10))

    def draw_center(self):
        # 中心装饰
        self.canvas.create_oval(195, 195, 205, 205, fill="black")
    
    def draw_brand(self):
        # 厂商文字
        self.canvas.create_text(200, 420, text="上海杉原厂", 
                              font=("宋体", 12), fill="#666666")

    def create_buttons(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="启动", command=self.start, 
                width=8, bg="#4CAF50").pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="停止", command=self.stop, 
                width=8, bg="#F44336").pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="复位", command=self.reset, 
                width=8, bg="#2196F3").pack(side=tk.LEFT, padx=5)

    def update_hands(self):
        if self.running:
            current_time = time.time() - self.start_time + self.elapsed
            
            # 更新外圈指针（6秒转一圈）
            outer_angle = math.radians(90 - (current_time % 6) * 60)
            x = 200 + 120 * math.cos(outer_angle)
            y = 200 - 120 * math.sin(outer_angle)
            self.canvas.coords(self.outer_hand, 200, 200, x, y)
            
            # 更新内圈指针（60秒转一圈）
            inner_angle = math.radians(90 - (current_time % 60) * 6)
            x = 200 + 80 * math.cos(inner_angle)
            y = 200 - 80 * math.sin(inner_angle)
            self.canvas.coords(self.inner_hand, 200, 200, x, y)
            
            self.root.after(50, self.update_hands)

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
        # 复位指针到初始位置
        self.canvas.coords(self.outer_hand, 200, 200, 200, 80)
        self.canvas.coords(self.inner_hand, 200, 200, 200, 120)

if __name__ == "__main__":
    root = tk.Tk()
    app = MechanicalStopwatch(root)
    root.mainloop()
