# Interactive Features Setup Guide

## ✨ What's New

Your CS Quest website now has **three ways** for students to run code interactively:

### 1. 📝 On Lesson Pages (Already Works!)
- Code blocks are already interactive with Pyodide
- Students can edit and run code directly on each lesson page
- No additional setup needed - it's built into Quarto!

### 2. 🚀 JupyterLite (New!)
- Full Jupyter Lab environment in the browser
- No installation required for students
- Requires one-time setup to build and deploy

### 3. 📥 Downloadable Notebooks (New!)
- Each lesson is now available as a `.ipynb` file
- Students can download and use in local Jupyter or Google Colab
- Files are in `files/lessons/`

## 🚀 Quick Start for Instructors

### Option A: Deploy with JupyterLite (Recommended)

**1. Install JupyterLite:**
```bash
pip install jupyterlite-core jupyterlite-pyodide-kernel
```

**2. Build everything:**
```bash
./build.sh
```

This script will:
- Build the JupyterLite site
- Build the Quarto website
- Copy JupyterLite into the final output

**3. Deploy the `_site` folder** to your web host (GitHub Pages, Netlify, etc.)

Students can then:
- Visit lesson pages and run code inline
- Click "Open in JupyterLite" for full Jupyter environment
- Download notebooks for local use

### Option B: Quarto Only (Simple)

If you don't want JupyterLite:

```bash
quarto render
```

Students can still:
- Run code on lesson pages (Pyodide still works!)
- Download notebook files from GitHub/your repository

The JupyterLite links won't work, but everything else will.

## 📁 Project Structure

```
cs_puzzles/
├── lessons/              # Quarto lesson pages (.qmd)
│   ├── 01-variables.qmd  # Now includes JupyterLite links
│   └── ...
├── jupyterlite/
│   ├── content/          # Jupyter notebooks (.ipynb)
│   │   ├── index.ipynb   # JupyterLite welcome page
│   │   ├── 01-variables.ipynb
│   │   ├── 02-data-types.ipynb
│   │   └── ... (all 12 lessons)
│   └── jupyter-lite.json # JupyterLite config
├── interactive.qmd       # Explains interactive options
├── build.sh              # Build script (Linux/Mac)
└── create_notebooks.py   # Generate notebooks
```

## 🔧 How It Works

### On Each Lesson Page

Updated lessons now show an interactive options box:

```markdown
::: {.tip-box}
**💻 Interactive Options:**
- 📓 Open in JupyterLite (full Jupyter environment)
- ▶️ Run code directly below (Pyodide on the page)
- 📥 Download Notebook (for local use)
:::
```

### JupyterLite Links

Links use this pattern:
```
jupyterlite/lab/index.html?path=01-variables.ipynb
```

This opens JupyterLite with the specific notebook loaded.

### Download Links

Direct links to `.ipynb` files:
```
files/lessons/01-variables.ipynb
```

Students can download and open in:
- Local Jupyter
- Google Colab (upload the file)
- VS Code with Jupyter extension

## 🌐 Deployment Examples

### GitHub Pages

```bash
# Build site
./build.sh

# Push _site folder to gh-pages branch
# Or configure GitHub Pages to serve from _site/
```

### Netlify

Add to `netlify.toml`:
```toml
[build]
  command = "./build.sh"
  publish = "_site"
```

### Manual Hosting

Just upload the `_site` folder to any web server.

## 🛠️ Customization

### Add More Notebooks

1. Create `.ipynb` file in `jupyterlite/content/`
2. Copy the lesson notebook to `files/lessons/` for direct download links
3. Rebuild JupyterLite: `./build.sh`
4. Link from lesson pages

### Update Existing Notebooks

1. Edit files in `jupyterlite/content/` and `files/lessons/` as needed
2. Rebuild: `./build.sh`
3. Changes appear in JupyterLite and download links

### Notebook Sync Helper

Use the helper script to generate and sync notebooks in one command:

```bash
python3 src/sync_notebooks.py
```

This updates both:
- `jupyterlite/content/` (for JupyterLite)
- `files/lessons/` (for direct downloads)

To sync and render in one run:

```bash
python3 src/sync_notebooks.py --render
```

### Change JupyterLite Theme

Edit `jupyterlite/jupyter-lite.json`:
```json
{
  "jupyter-config-data": {
    "settingsOverrides": {
      "@jupyterlab/apputils-extension:themes": {
        "theme": "JupyterLab Dark"
      }
    }
  }
}
```

## 📱 QR Codes for JupyterLite

Generate QR codes that link directly to JupyterLite notebooks:

```python
# In generate_qr_codes.py, update BASE_URL to include JupyterLite:
BASE_URL = "https://your-site.com/cs_puzzles"

# For JupyterLite-specific QR codes:
url = f"{BASE_URL}/jupyterlite/lab/index.html?path={lesson_id}.ipynb"
```

## 🎓 Student Instructions

Create a simple guide for students:

### To Use Interactive Code on Lesson Pages:
1. Scroll to any code block
2. Click the "Run" button or edit the code
3. See results appear below

### To Use JupyterLite:
1. Click "Open in JupyterLite" on any lesson
2. Wait for Jupyter to load (first time may take 30 seconds)
3. Edit and run cells with Shift+Enter
4. Download your work: File → Download

### To Use on Your Computer:
1. Click "Download Notebook" on any lesson
2. Open in Jupyter Lab/Notebook on your computer
3. Or upload to Google Colab

## 🐛 Troubleshooting

### JupyterLite Not Loading
- Check browser console for errors
- Ensure `_site/jupyterlite/` exists after build
- Try clearing browser cache
- Some older browsers may not support JupyterLite

### Code Not Running on Lesson Pages
- Quarto's Pyodide feature requires modern browsers
- Check that `{pyodide-python}` code blocks are used
- Verify Quarto is version 1.4+

### Notebooks Missing in JupyterLite
- Ensure files are in `jupyterlite/content/`
- Rebuild: `./build.sh`
- Check `jupyterlite_build/` was created

### Download Links Not Working
- Ensure files are in `files/lessons/`
- Run `quarto render` and verify `_site/files/lessons/` exists

## ✅ Testing Checklist

Before deploying:

- [ ] Build completes without errors: `./build.sh`
- [ ] Quarto site loads: `cd _site && python -m http.server 8000`
- [ ] JupyterLite loads: Visit `http://localhost:8000/jupyterlite/lab/index.html`
- [ ] Can open a notebook in JupyterLite
- [ ] Can run code in a JupyterLite notebook
- [ ] Can download a notebook file
- [ ] Code runs on lesson pages
- [ ] All links work
- [ ] QR codes point to correct URLs

## 📊 Benefits Summary

**For Students:**
- Multiple ways to learn and practice
- No software installation required
- Can work on any device
- Take work home as downloadable notebooks

**For Instructors:**
- More engagement with hands-on coding
- Students can experiment safely
- Easy to share via QR codes
- Progress can be saved and downloaded

## 🎯 Next Steps

1. **Build and test locally**: `./build.sh` then preview
2. **Update lesson pages**: Add interactive tip boxes to remaining lessons
3. **Deploy**: Push to your web hosting
4. **Generate QR codes**: Update URLs and create QR codes
5. **Test with students**: Get feedback on the interactive features

---

**Questions or issues?** Check the main README.md or Quarto documentation.

Happy teaching! 🎓✨
