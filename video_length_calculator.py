import os
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog, messagebox

def calculate_total_duration(folder_path):
    total_duration = 0

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".mp4"):  # Add more extensions if needed
                video_path = os.path.join(root, filename)
                try:
                    with VideoFileClip(video_path) as video:
                        total_duration += video.duration
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

    return total_duration

def convert_seconds_to_hms(total_seconds):
    total_minutes, total_seconds = divmod(total_seconds, 60)
    total_hours, total_minutes = divmod(total_minutes, 60)
    return int(total_hours), int(total_minutes), int(total_seconds)

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        total_seconds = calculate_total_duration(folder_path)
        hours, minutes, seconds = convert_seconds_to_hms(total_seconds)
        messagebox.showinfo("Total Video Length", f"Total video length: {hours}h {minutes}m {seconds}s")

def main():
    root = tk.Tk()
    root.title("Video Length Calculator")

    select_button = tk.Button(root, text="Select Folder", command=select_folder)
    select_button.pack(pady=20)

    root.geometry("300x150")
    root.mainloop()

if __name__ == "__main__":
    main()
