import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime, timedelta

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer - Made by Rehan Aslam")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")
        
        # Style configuration
        style = ttk.Style()
        style.configure("TButton", padding=5, font=("Helvetica", 10))
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TEntry", font=("Helvetica", 12))
        
        # Variables
        self.time_left = tk.StringVar()
        self.time_left.set("00:00:00")
        self.running = False
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Time input frame
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=0, column=0, pady=10)
        
        # Hours
        ttk.Label(input_frame, text="Hours:").grid(row=0, column=0, padx=5)
        self.hours = ttk.Entry(input_frame, width=5)
        self.hours.grid(row=0, column=1, padx=5)
        self.hours.insert(0, "0")
        
        # Minutes
        ttk.Label(input_frame, text="Minutes:").grid(row=0, column=2, padx=5)
        self.minutes = ttk.Entry(input_frame, width=5)
        self.minutes.grid(row=0, column=3, padx=5)
        self.minutes.insert(0, "0")
        
        # Seconds
        ttk.Label(input_frame, text="Seconds:").grid(row=0, column=4, padx=5)
        self.seconds = ttk.Entry(input_frame, width=5)
        self.seconds.grid(row=0, column=5, padx=5)
        self.seconds.insert(0, "0")
        
        # Timer display
        self.timer_label = ttk.Label(main_frame, textvariable=self.time_left, font=("Helvetica", 24))
        self.timer_label.grid(row=1, column=0, pady=20)
        
        # Control buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, pady=10)
        
        self.start_button = ttk.Button(button_frame, text="Start", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.stop_button = ttk.Button(button_frame, text="Stop", command=self.stop_timer)
        self.stop_button.grid(row=0, column=1, padx=5)
        
        self.reset_button = ttk.Button(button_frame, text="Reset", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=5)
        
    def start_timer(self):
        if not self.running:
            try:
                h = int(self.hours.get())
                m = int(self.minutes.get())
                s = int(self.seconds.get())
                
                if h < 0 or m < 0 or s < 0:
                    raise ValueError("Time values cannot be negative")
                
                self.total_seconds = h * 3600 + m * 60 + s
                if self.total_seconds <= 0:
                    raise ValueError("Please enter a time greater than 0")
                
                self.running = True
                self.update_timer()
            except ValueError as e:
                self.time_left.set("Invalid input")
                return
    
    def stop_timer(self):
        self.running = False
    
    def reset_timer(self):
        self.running = False
        self.time_left.set("00:00:00")
        self.hours.delete(0, tk.END)
        self.hours.insert(0, "0")
        self.minutes.delete(0, tk.END)
        self.minutes.insert(0, "0")
        self.seconds.delete(0, tk.END)
        self.seconds.insert(0, "0")
    
    def update_timer(self):
        if self.running and self.total_seconds > 0:
            hours = self.total_seconds // 3600
            minutes = (self.total_seconds % 3600) // 60
            seconds = self.total_seconds % 60
            
            time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.time_left.set(time_string)
            
            self.total_seconds -= 1
            self.root.after(1000, self.update_timer)
        elif self.total_seconds <= 0:
            self.running = False
            self.time_left.set("Time's up!")
            self.root.bell()  # Play a sound when timer ends

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
