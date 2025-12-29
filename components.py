import customtkinter as ctk
import tkinter as tk

# คลาสสเกลบาร์แบบใส (วาดลง Canvas โดยตรงไม่ได้ แต่ใช้ Canvas ซ้อนได้)
# ในเวอร์ชัน Modular นี้ เราจะปรับให้มันดูแลง่ายขึ้น
class TransparentScaleBar(ctk.CTkCanvas):
    """แถบสเกลระยะทางแบบโปร่งใส วางซ้อนบนแผนที่และวาดกราฟิกด้วย Canvas"""
    def __init__(self, master, **kwargs):
        """กำหนดค่าเริ่มต้นของ Canvas และตั้งสีพื้นหลังให้กลมกลืนกับธีม"""
        super().__init__(master, highlightthickness=0, **kwargs)
        # พยายามดึงสีพื้นหลัง parent มาใช้ (หรือใช้สีเทาเข้มเป็นค่าเริ่มต้น)
        try:
            bg_color = master._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
            self.configure(bg=bg_color)
        except:
            self.configure(bg="gray20")

    def update_scale(self, label_text, pixel_width):
        """วาดข้อความระยะทางและเส้นสเกลตามความกว้างพิกเซลที่คำนวณได้"""
        self.delete("all") 
        w = self.winfo_width()
        h = self.winfo_height()
        
        if w <= 1: return 

        center_x = w / 2
        text_y = h - 25 
        line_y = h - 8 
        half_w = pixel_width / 2
        
        # วาด Text แบบมีขอบ
        for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1), (0,1), (0,-1), (1,0), (-1,0)]:
            self.create_text(center_x+dx, text_y+dy, text=label_text, font=("Arial", 12, "bold"), fill="black", anchor="s")
        self.create_text(center_x, text_y, text=label_text, font=("Arial", 12, "bold"), fill="white", anchor="s")

        # วาดเส้นสเกล
        self.create_line(center_x - half_w, line_y, center_x + half_w, line_y, fill="white", width=2)
        self.create_line(center_x - half_w, line_y, center_x - half_w, line_y - 8, fill="white", width=2)
        self.create_line(center_x + half_w, line_y, center_x + half_w, line_y - 8, fill="white", width=2)
