# Facebook Bulk Video Downloader

A user-friendly tool for downloading multiple Facebook videos at once using yt-dlp.

## 🎯 Two Versions Available

### 1. 🖥️ Desktop App (`fb_video_downloader.py`)
- GUI application for Windows/Mac/Linux
- Run on your own computer
- Downloads directly to your computer

### 2. 🌐 Web App (`streamlit_app.py`)
- Host online for free
- Share with friends via URL
- Works on any device with a browser
- **See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for hosting instructions**

## Features

✨ **Easy to Use** - Simple interface, no command line needed!
📦 **Batch Download** - Download as many videos as you want at once
📝 **Smart Naming** - Automatically saves files with the video caption/title as filename
🎯 **Best Quality** - Downloads videos in the best available quality
📊 **Progress Tracking** - See real-time progress for each download

---

## 🖥️ Desktop App - Quick Start

### Installation

### Step 1: Install Python
Make sure you have Python 3.7 or higher installed:
- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **Mac**: Already installed, or use `brew install python3`
- **Linux**: Use your package manager: `sudo apt install python3`

### Step 2: Install yt-dlp
The app will try to install yt-dlp automatically on first run, but you can also install it manually:

```bash
pip install yt-dlp
```

Or on Linux:
```bash
pip install yt-dlp --break-system-packages
```

## How to Use

### Method 1: Double-click (Easiest)
1. Just double-click `fb_video_downloader.py`
2. If it asks, open with Python

### Method 2: Command Line
```bash
python3 fb_video_downloader.py
```

### Using the App

1. **Paste URLs**: Copy and paste Facebook video URLs into the text box (one per line)
   - Works with: `https://www.facebook.com/watch/?v=...`
   - Works with: `https://fb.watch/...`
   - Works with: Full Facebook post URLs

2. **Choose Folder**: Click "Browse" to select where you want videos saved
   - Default: `Downloads/Facebook_Videos`

3. **Click Download**: Hit the "Download Videos" button and wait!

4. **Check Progress**: Watch the progress window to see each video being downloaded

## Example URLs

```
https://www.facebook.com/watch/?v=123456789
https://fb.watch/xyz123/
https://www.facebook.com/username/videos/987654321/
```

## Tips

💡 **Remove comments**: Lines starting with `#` are ignored, so you can add notes
💡 **Multiple downloads**: You can download 10, 50, 100+ videos at once!
💡 **Check your internet**: Downloading many videos takes time and bandwidth
💡 **Filenames**: Videos are saved with their Facebook title/caption as the filename

## Troubleshooting

### "yt-dlp not found"
- The app will try to install it automatically
- If that fails, manually run: `pip install yt-dlp`

### "Download failed"
- Check if the URL is correct and the video is public
- Some private videos may not work
- Try the URL in a browser first to make sure it works

### "Permission denied"
- Make sure you have write access to the download folder
- Try selecting a different folder (like Desktop or Documents)

### Windows: "Python is not recognized"
- Make sure you checked "Add Python to PATH" during installation
- Reinstall Python and check that option

## Requirements

- Python 3.7+
- yt-dlp (auto-installed)
- tkinter (usually comes with Python)
- Internet connection

## Legal Notice

⚠️ **Important**: Only download videos you have permission to download. Respect copyright and privacy:
- Don't download copyrighted content without permission
- Don't download private videos without authorization
- Use this tool responsibly and legally

---

## 🌐 Web App - Host for Free

Want to share this tool with friends? Host it online for free!

### Quick Setup (5 minutes)

1. **Create GitHub account** at [github.com](https://github.com)
2. **Upload these files** to a new repository:
   - `streamlit_app.py`
   - `requirements.txt`
3. **Deploy on Streamlit Cloud**:
   - Go to [streamlit.io/cloud](https://streamlit.io/cloud)
   - Connect your GitHub
   - Deploy your app!

**Your app will be live at:** `https://your-app-name.streamlit.app`

📚 **Full deployment guide:** See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions!

### Features of Web Version:
- 🌍 Access from anywhere
- 📱 Works on phone, tablet, computer
- 👥 Share with friends via URL
- 💯 100% Free hosting
- 📊 Built-in analytics

---

## 📂 Project Files

- `fb_video_downloader.py` - Desktop GUI application
- `streamlit_app.py` - Web application
- `requirements.txt` - Python dependencies
- `README.md` - This file
- `DEPLOYMENT_GUIDE.md` - How to host online for free
- `.gitignore` - Git ignore file

## Support

If you encounter any issues:
1. Make sure Python and yt-dlp are installed correctly
2. Check that the Facebook URLs are valid
3. Ensure you have internet connection
4. Try downloading just one video first to test

## License

Free to use for personal purposes. Use responsibly!

---

Made with ❤️ for easy Facebook video downloading
