#!/usr/bin/env python3
"""
Facebook Bulk Video Downloader
A user-friendly GUI tool for downloading multiple Facebook videos at once
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import subprocess
import threading
import os
import sys
from pathlib import Path

class FacebookVideoDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Facebook Bulk Video Downloader")
        self.root.geometry("800x600")
        
        # Variables
        self.download_folder = tk.StringVar(value=str(Path.home() / "Downloads" / "Facebook_Videos"))
        self.is_downloading = False
        
        self.setup_ui()
        self.check_ytdlp()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="Facebook Bulk Video Downloader", 
            font=("Arial", 16, "bold"),
            pady=10
        )
        title_label.pack()
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Paste Facebook video URLs below (one per line). Videos will be saved with their captions as filenames.",
            font=("Arial", 10),
            fg="gray"
        )
        instructions.pack()
        
        # URL Input Frame
        input_frame = tk.LabelFrame(self.root, text="Video URLs", padx=10, pady=10)
        input_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.url_text = scrolledtext.ScrolledText(
            input_frame,
            height=10,
            font=("Courier", 10),
            wrap=tk.WORD
        )
        self.url_text.pack(fill="both", expand=True)
        self.url_text.insert("1.0", "# Paste your Facebook video URLs here, one per line\n# Example:\n# https://www.facebook.com/watch/?v=123456789\n# https://fb.watch/xyz123/\n")
        
        # Folder Selection Frame
        folder_frame = tk.Frame(self.root, padx=20)
        folder_frame.pack(fill="x", pady=5)
        
        tk.Label(folder_frame, text="Download Folder:", font=("Arial", 10)).pack(side="left")
        
        folder_entry = tk.Entry(
            folder_frame,
            textvariable=self.download_folder,
            font=("Arial", 9),
            state="readonly"
        )
        folder_entry.pack(side="left", fill="x", expand=True, padx=10)
        
        browse_btn = tk.Button(
            folder_frame,
            text="Browse",
            command=self.browse_folder,
            bg="#4CAF50",
            fg="white",
            padx=10
        )
        browse_btn.pack(side="right")
        
        # Progress Frame
        progress_frame = tk.LabelFrame(self.root, text="Progress", padx=10, pady=10)
        progress_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.progress_text = scrolledtext.ScrolledText(
            progress_frame,
            height=8,
            font=("Courier", 9),
            bg="#f5f5f5",
            state="disabled"
        )
        self.progress_text.pack(fill="both", expand=True)
        
        # Download Button
        self.download_btn = tk.Button(
            self.root,
            text="Download Videos",
            command=self.start_download,
            bg="#2196F3",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10
        )
        self.download_btn.pack(pady=10)
        
        # Status Bar
        self.status_label = tk.Label(
            self.root,
            text="Ready",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            font=("Arial", 9)
        )
        self.status_label.pack(side="bottom", fill="x")
        
    def browse_folder(self):
        folder = filedialog.askdirectory(initialdir=self.download_folder.get())
        if folder:
            self.download_folder.set(folder)
            
    def log_message(self, message, tag="info"):
        self.progress_text.config(state="normal")
        if tag == "error":
            self.progress_text.insert("end", f"❌ {message}\n", "error")
            self.progress_text.tag_config("error", foreground="red")
        elif tag == "success":
            self.progress_text.insert("end", f"✅ {message}\n", "success")
            self.progress_text.tag_config("success", foreground="green")
        else:
            self.progress_text.insert("end", f"ℹ️  {message}\n")
        
        self.progress_text.see("end")
        self.progress_text.config(state="disabled")
        self.root.update()
        
    def check_ytdlp(self):
        """Check if yt-dlp is installed"""
        try:
            subprocess.run(
                ["yt-dlp", "--version"],
                capture_output=True,
                check=True
            )
            self.log_message("yt-dlp is installed and ready!", "success")
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.log_message("yt-dlp not found. Installing...", "info")
            self.install_ytdlp()
            
    def install_ytdlp(self):
        """Install yt-dlp using pip"""
        try:
            self.log_message("Installing yt-dlp... This may take a moment.", "info")
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "--break-system-packages", "yt-dlp"],
                capture_output=True,
                check=True
            )
            self.log_message("yt-dlp installed successfully!", "success")
        except subprocess.CalledProcessError as e:
            self.log_message(f"Failed to install yt-dlp: {e}", "error")
            messagebox.showerror(
                "Installation Error",
                "Could not install yt-dlp. Please install it manually:\npip install yt-dlp"
            )
            
    def get_urls(self):
        """Extract valid URLs from the text box"""
        text = self.url_text.get("1.0", "end-1c")
        urls = []
        for line in text.split("\n"):
            line = line.strip()
            # Skip comments and empty lines
            if line and not line.startswith("#"):
                if "facebook.com" in line or "fb.watch" in line:
                    urls.append(line)
        return urls
        
    def start_download(self):
        """Start the download process in a separate thread"""
        if self.is_downloading:
            messagebox.showwarning("Download in Progress", "Please wait for the current download to complete.")
            return
            
        urls = self.get_urls()
        
        if not urls:
            messagebox.showwarning("No URLs", "Please enter at least one Facebook video URL.")
            return
            
        # Clear progress
        self.progress_text.config(state="normal")
        self.progress_text.delete("1.0", "end")
        self.progress_text.config(state="disabled")
        
        # Create download folder if it doesn't exist
        download_path = Path(self.download_folder.get())
        download_path.mkdir(parents=True, exist_ok=True)
        
        self.is_downloading = True
        self.download_btn.config(state="disabled", bg="gray")
        
        # Start download in a separate thread
        thread = threading.Thread(target=self.download_videos, args=(urls,))
        thread.daemon = True
        thread.start()
        
    def download_videos(self, urls):
        """Download videos using yt-dlp"""
        total = len(urls)
        successful = 0
        failed = 0
        
        self.log_message(f"Starting download of {total} video(s)...\n", "info")
        
        for i, url in enumerate(urls, 1):
            self.status_label.config(text=f"Downloading {i}/{total}: {url[:50]}...")
            self.log_message(f"[{i}/{total}] Processing: {url}")
            
            try:
                # yt-dlp command with options
                cmd = [
                    "yt-dlp",
                    url,
                    "-o", f"{self.download_folder.get()}/%(title)s.%(ext)s",  # Use title as filename
                    "--no-playlist",  # Don't download playlists
                    "--format", "best",  # Download best quality
                ]
                
                # Run yt-dlp
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=300  # 5 minute timeout per video
                )
                
                if result.returncode == 0:
                    self.log_message(f"[{i}/{total}] Successfully downloaded!", "success")
                    successful += 1
                else:
                    error_msg = result.stderr.split("\n")[0] if result.stderr else "Unknown error"
                    self.log_message(f"[{i}/{total}] Failed: {error_msg}", "error")
                    failed += 1
                    
            except subprocess.TimeoutExpired:
                self.log_message(f"[{i}/{total}] Timeout: Video took too long to download", "error")
                failed += 1
            except Exception as e:
                self.log_message(f"[{i}/{total}] Error: {str(e)}", "error")
                failed += 1
                
            self.log_message("")  # Empty line for readability
            
        # Final summary
        self.log_message("=" * 50)
        self.log_message(f"Download Complete!", "success")
        self.log_message(f"Total: {total} | Success: {successful} | Failed: {failed}")
        self.log_message(f"Files saved to: {self.download_folder.get()}")
        self.log_message("=" * 50)
        
        self.status_label.config(text=f"Complete! {successful}/{total} downloaded successfully")
        self.download_btn.config(state="normal", bg="#2196F3")
        self.is_downloading = False
        
        # Show completion message
        messagebox.showinfo(
            "Download Complete",
            f"Downloaded {successful} out of {total} videos.\n\nFiles saved to:\n{self.download_folder.get()}"
        )

def main():
    root = tk.Tk()
    app = FacebookVideoDownloader(root)
    root.mainloop()

if __name__ == "__main__":
    main()
