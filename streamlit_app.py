import streamlit as st
import subprocess
import tempfile
import os
import zipfile
from pathlib import Path
import time

st.set_page_config(
    page_title="Facebook Video Downloader",
    page_icon="🎬",
    layout="wide"
)

# Title and description
st.title("🎬 Facebook Bulk Video Downloader")
st.markdown("""
Download multiple Facebook videos at once! Videos are saved with their captions as filenames.
""")

# Sidebar info
with st.sidebar:
    st.header("ℹ️ How to Use")
    st.markdown("""
    1. Paste Facebook video URLs (one per line)
    2. Click "Download Videos"
    3. Wait for processing
    4. Download your videos as a ZIP file
    
    **Supported URLs:**
    - `https://www.facebook.com/watch/?v=...`
    - `https://fb.watch/...`
    - Facebook post URLs with videos
    """)
    
    st.header("⚠️ Important")
    st.warning("Only download videos you have permission to use. Respect copyright and privacy!")

# Check if yt-dlp is installed
def check_ytdlp():
    try:
        result = subprocess.run(
            ["yt-dlp", "--version"],
            capture_output=True,
            text=True
        )
        return True
    except FileNotFoundError:
        return False

# Install yt-dlp if needed
if not check_ytdlp():
    with st.spinner("Installing yt-dlp... This will take a moment."):
        try:
            subprocess.run(
                ["pip", "install", "yt-dlp"],
                capture_output=True,
                check=True
            )
            st.success("✅ yt-dlp installed successfully!")
        except Exception as e:
            st.error(f"Failed to install yt-dlp: {e}")
            st.stop()

# URL input
st.subheader("📝 Enter Video URLs")
urls_text = st.text_area(
    "Paste Facebook video URLs here (one per line)",
    height=200,
    placeholder="https://www.facebook.com/watch/?v=123456789\nhttps://fb.watch/xyz123/\n..."
)

# Parse URLs
def get_urls(text):
    urls = []
    for line in text.split("\n"):
        line = line.strip()
        if line and not line.startswith("#"):
            if "facebook.com" in line or "fb.watch" in line:
                urls.append(line)
    return urls

urls = get_urls(urls_text)

# Display URL count
if urls:
    st.info(f"📊 Found {len(urls)} valid URL(s)")

# Download button
if st.button("⬇️ Download Videos", type="primary", disabled=not urls):
    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        log_container = st.container()
        
        successful = 0
        failed = 0
        total = len(urls)
        
        downloaded_files = []
        
        for i, url in enumerate(urls):
            progress = (i) / total
            progress_bar.progress(progress)
            status_text.text(f"Downloading {i+1}/{total}: {url[:50]}...")
            
            with log_container:
                with st.expander(f"Video {i+1}/{total}", expanded=(i == len(urls) - 1)):
                    st.write(f"🔗 URL: {url}")
                    
                    try:
                        # Download using yt-dlp
                        cmd = [
                            "yt-dlp",
                            url,
                            "-o", f"{temp_path}/%(title)s.%(ext)s",
                            "--no-playlist",
                            "--format", "best",
                        ]
                        
                        result = subprocess.run(
                            cmd,
                            capture_output=True,
                            text=True,
                            timeout=300
                        )
                        
                        if result.returncode == 0:
                            st.success("✅ Downloaded successfully!")
                            successful += 1
                            
                            # Find the downloaded file
                            for file in temp_path.glob("*"):
                                if file.is_file() and file not in downloaded_files:
                                    downloaded_files.append(file)
                        else:
                            error_msg = result.stderr.split("\n")[0] if result.stderr else "Unknown error"
                            st.error(f"❌ Failed: {error_msg}")
                            failed += 1
                            
                    except subprocess.TimeoutExpired:
                        st.error("❌ Timeout: Video took too long to download")
                        failed += 1
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                        failed += 1
        
        # Complete progress
        progress_bar.progress(1.0)
        status_text.text("Processing complete!")
        
        # Summary
        st.divider()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total", total)
        with col2:
            st.metric("Success", successful, delta=successful - failed if successful > failed else None)
        with col3:
            st.metric("Failed", failed)
        
        # Create ZIP file if there are downloaded files
        if downloaded_files:
            st.success(f"🎉 Successfully downloaded {successful} video(s)!")
            
            zip_path = temp_path / "facebook_videos.zip"
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file in downloaded_files:
                    zipf.write(file, file.name)
            
            # Provide download button
            with open(zip_path, 'rb') as f:
                st.download_button(
                    label="📦 Download All Videos (ZIP)",
                    data=f,
                    file_name=f"facebook_videos_{int(time.time())}.zip",
                    mime="application/zip",
                    type="primary"
                )
        else:
            st.error("❌ No videos were downloaded successfully.")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
    Made with ❤️ • Use responsibly • Respect copyright and privacy
</div>
""", unsafe_allow_html=True)
