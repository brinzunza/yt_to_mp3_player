import tkinter as tk
from tkinter import messagebox
import pygame
import os
from main import download_and_convert

pygame.mixer.init()

class MP3Player:
    def __init__(self, root):
        self.root = root
        self.root.title("MP3 Player")
        
        self.current_file = None
        
        self.create_widgets()
    
    def create_widgets(self):
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.pack(pady=10)
        
        self.download_button = tk.Button(self.root, text="Download and Convert", command=self.download_and_convert)
        self.download_button.pack(pady=5)
        
        self.play_button = tk.Button(self.root, text="Play", state=tk.DISABLED, command=self.play_music)
        self.play_button.pack(pady=5)
        
        self.pause_button = tk.Button(self.root, text="Pause", state=tk.DISABLED, command=self.pause_music)
        self.pause_button.pack(pady=5)
        
        self.stop_button = tk.Button(self.root, text="Stop", state=tk.DISABLED, command=self.stop_music)
        self.stop_button.pack(pady=5)
    
    def download_and_convert(self):
        url = self.url_entry.get()
        if url:
            try:
                download_and_convert(url)
                self.current_file = "output_audio.mp3"
                self.play_button.config(state=tk.NORMAL)
                messagebox.showinfo("Success", "Download and conversion complete.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please enter a YouTube URL.")
    
    def play_music(self):
        if self.current_file and os.path.exists(self.current_file):
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.play()
            self.pause_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
        else:
            messagebox.showwarning("File Error", "No MP3 file to play.")
    
    def pause_music(self):
        pygame.mixer.music.pause()
    
    def stop_music(self):
        pygame.mixer.music.stop()
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MP3Player(root)
    root.mainloop()
