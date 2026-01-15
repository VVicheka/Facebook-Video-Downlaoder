# 🚀 Free Hosting Guide for Facebook Video Downloader

You have **2 versions** of the tool:
1. **Desktop App** (`fb_video_downloader.py`) - GUI app for personal use
2. **Web App** (`streamlit_app.py`) - Host online for friends to use

## Option 1: Streamlit Cloud (Easiest & Best) ⭐

**100% FREE** with unlimited apps!

### Step 1: Create a GitHub Account
1. Go to [github.com](https://github.com)
2. Sign up for free

### Step 2: Create a New Repository
1. Click the `+` icon → "New repository"
2. Name it: `facebook-video-downloader`
3. Make it **Public**
4. Click "Create repository"

### Step 3: Upload Your Files
Upload these 3 files to your GitHub repo:
- `streamlit_app.py` (the web app)
- `requirements.txt` (dependencies)
- `README.md` (optional, for documentation)

You can upload by:
- Drag and drop on GitHub website
- Or use: `git push` if you know Git

### Step 4: Deploy to Streamlit Cloud
1. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
2. Sign in with your GitHub account
3. Click "New app"
4. Select:
   - Repository: `your-username/facebook-video-downloader`
   - Branch: `main`
   - Main file path: `streamlit_app.py`
5. Click "Deploy"!

**That's it!** Your app will be live in 2-3 minutes at:
`https://your-app-name.streamlit.app`

### Sharing with Friends
Just send them the URL! They can use it directly in their browser.

---

## Option 2: Hugging Face Spaces (Alternative)

Another free option with more resources:

### Steps:
1. Create account at [huggingface.co](https://huggingface.co)
2. Create a new "Space"
3. Choose "Streamlit" as SDK
4. Upload your files:
   - `streamlit_app.py` → rename to `app.py`
   - `requirements.txt`
5. Your app will be live!

URL: `https://huggingface.co/spaces/your-username/facebook-downloader`

---

## Option 3: Railway (Free Tier)

More powerful but limited free hours (500 hours/month):

### Steps:
1. Sign up at [railway.app](https://railway.app)
2. Create new project from GitHub repo
3. Add these files to your repo:
   - `streamlit_app.py`
   - `requirements.txt`
   - Create `Procfile` with content:
     ```
     web: streamlit run streamlit_app.py --server.port=$PORT
     ```
4. Deploy!

---

## Option 4: Share Desktop App (No Hosting)

If you don't want to host online, you can share the desktop app:

### Method A: Share Python Script
Send friends:
- `fb_video_downloader.py`
- `README.md`

They need Python installed and run:
```bash
pip install yt-dlp
python fb_video_downloader.py
```

### Method B: Create .EXE (Windows only)
Package as executable so they don't need Python:

```bash
# Install PyInstaller
pip install pyinstaller

# Create .exe
pyinstaller --onefile --windowed fb_video_downloader.py
```

Send them the `.exe` file from `dist/` folder!

---

## 🎯 Recommended Setup

For sharing with friends, I recommend:

**Best Option: Streamlit Cloud**
- ✅ 100% Free forever
- ✅ No credit card needed
- ✅ Easy to update
- ✅ Works on any device (phone, tablet, computer)
- ✅ Friends just need a web browser
- ✅ You can see usage stats

**Quick Comparison:**

| Platform | Free Tier | Ease | Best For |
|----------|-----------|------|----------|
| Streamlit Cloud | Unlimited | ⭐⭐⭐⭐⭐ | Most people |
| Hugging Face | Unlimited | ⭐⭐⭐⭐ | Tech-savvy users |
| Railway | 500 hrs/mo | ⭐⭐⭐ | Power users |
| Desktop .exe | N/A | ⭐⭐ | Windows users only |

---

## 📝 Quick Setup Script for GitHub

Create these files in a folder:

```bash
facebook-video-downloader/
├── streamlit_app.py      # Your web app
├── requirements.txt      # Dependencies
└── README.md            # Instructions (optional)
```

Then:
```bash
# Initialize git (one time)
git init
git add .
git commit -m "Initial commit"

# Connect to GitHub
git remote add origin https://github.com/YOUR-USERNAME/facebook-video-downloader.git
git push -u origin main
```

Now deploy on Streamlit Cloud!

---

## 🔧 Updating Your App

After deployment, to update:

**Streamlit Cloud:**
1. Edit files on GitHub
2. Commit changes
3. App auto-updates in ~1 minute!

**Or using Git:**
```bash
git add .
git commit -m "Updated features"
git push
```

---

## 💡 Pro Tips

1. **Add Authentication**: Prevent abuse by adding Streamlit password protection:
   ```python
   import streamlit as st
   
   password = st.text_input("Password", type="password")
   if password != "your-secret-password":
       st.stop()
   ```

2. **Limit Usage**: Add rate limiting to prevent server overload

3. **Analytics**: Streamlit Cloud shows visitor stats automatically

4. **Custom Domain**: Streamlit allows custom domains on paid plans

---

## 🆘 Troubleshooting

**"App is sleeping"**
- Free tier apps sleep after inactivity
- They wake up when someone visits (takes 10-30 seconds)

**"Resource limits exceeded"**
- Downloading huge videos may timeout
- Consider limiting video size or number

**"yt-dlp not installing"**
- Make sure `requirements.txt` is uploaded correctly
- Check Streamlit logs for errors

---

## 📊 Expected Costs

All recommended options are **100% FREE**:
- ✅ Streamlit Cloud: FREE forever
- ✅ Hugging Face: FREE forever
- ✅ GitHub: FREE forever
- ✅ Railway: FREE (500 hrs/month)

You won't pay anything unless you want premium features!

---

## Need Help?

If you get stuck:
1. Check Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)
2. Streamlit community forum: [discuss.streamlit.io](https://discuss.streamlit.io)
3. YouTube has great tutorials on "Deploy Streamlit app"

---

Happy sharing! 🎉
