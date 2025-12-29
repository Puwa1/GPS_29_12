import customtkinter as ctk

# ตั้งค่า Theme หลัก
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# รวมสีที่ใช้ในโปรแกรม
COLORS = {
    "primary": "#3b82f6",       # สีน้ำเงินหลัก
    "success": "#10b981",       # สีเขียว (Running/Start)
    "warning": "#facc15",       # สีเหลือง (Idle)
    "danger": "#ef4444",        # สีแดง (Stop/End)
    "text_white": "white",
    "text_gray": "gray",
    "bg_dark": "#212121",
    "bg_gray": "gray15"
}

# ตั้งค่าทั่วไป
APP_TITLE = "GPS Tracking Version 1.0"
DEFAULT_WINDOW_SIZE = "1600x900"
MAX_LOG_DISPLAY = 100
ALL_DAYS_OPTION = "--- ดูข้อมูลทั้งหมด (All Days) ---"
