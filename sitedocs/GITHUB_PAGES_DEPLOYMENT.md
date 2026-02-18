# GitHub Pages Deployment Guide

## 📋 Checklist Before Deploying

- ✅ JupyterLite built locally (`_site/jupyterlite/lab/index.html` exists)
- ✅ Quarto site renders successfully (`quarto render`)
- ✅ `.github/workflows/deploy.yml` configured
- ✅ GitHub repository created
- ✅ Code committed and pushed to `main` branch

## 🚀 Step-by-Step Deployment

### 1. Create GitHub Repository

```bash
# If you haven't already created a repo
git init
git add .
git commit -m "Initial commit: CS Quest interactive lessons"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/cs_puzzles.git
git push -u origin main
```

### 2. Enable GitHub Pages in Repository Settings

1. Go to **Settings** → **Pages**
2. Under "Build and deployment":
   - Source: Change from "Deploy from a branch" to **"GitHub Actions"**
3. Save

### 3. Automatic Deployment

That's it! The workflow in `.github/workflows/deploy.yml` will:
1. Detect push to `main` branch
2. Automatically run the build process:
   - Install Quarto
   - Install Python dependencies
   - Install JupyterLite
   - Render Quarto site
   - Build JupyterLite
3. Deploy to GitHub Pages

### 4. Monitor the Build

1. Go to **Actions** tab in your repository
2. Watch the "Deploy CS Quest to GitHub Pages" workflow
3. When it shows a ✅ checkmark, your site is live!

### 5. Access Your Live Site

Your site will be available at:

```
https://YOUR-USERNAME.github.io/cs_puzzles/
```

(Replace `YOUR-USERNAME` with your actual GitHub username)

## 🔌 What the Workflow Does

The `.github/workflows/deploy.yml` automatically:

```yaml
# 1. Checkout your code
# 2. Install Python 3.11
# 3. Install dependencies:
#    - Quarto
#    - jupyterlite-core
#    - jupyterlite-pyodide-kernel
# 4. Render Quarto: quarto render
# 5. Build JupyterLite: jupyter-lite build --output-dir _site/jupyterlite
# 6. Upload _site folder to GitHub Pages
# 7. Deploy automatically
```

## 📝 Making Updates

After deployment, to update your lessons:

```bash
# Edit your lesson files
nano lessons/01-variables.qmd

# Commit and push
git add lessons/01-variables.qmd
git commit -m "Update lesson 1"
git push origin main
```

The workflow will automatically:
1. Rebuild the entire site
2. Rebuild JupyterLite
3. Redeploy to GitHub Pages

Your changes go live in 2-5 minutes!

## ✏️ Update Lesson Content

### To update a lesson:

```bash
# Edit lesson file
nano lessons/01-variables.qmd

# Preview locally (optional)
quarto preview

# Commit and push
git add lessons/01-variables.qmd
git commit -m "Update Quest 1: Variables"
git push origin main
```

### To add new lessons:

1. Create new file: `lessons/17-your-topic.qmd`
2. Add entry to `_quarto.yml` sidebar
3. Create notebook: `jupyterlite/content/17-your-topic.ipynb`
4. Update `index.qmd` and `all-quests.qmd`
5. Commit and push

The CI/CD pipeline handles the rest! 🎉

## 🔍 Troubleshooting

### Build fails in Actions?

1. Check the **Actions** tab for error messages
2. Common issues:
   - Missing files (check file paths match exactly)
   - Python version incompatibility (workflow uses Python 3.11)
   - Quarto syntax errors (validate locally first)

Fix locally and push:
```bash
quarto render  # Test locally
git push origin main  # Trigger rebuild
```

### Site doesn't update?

1. Check Actions tab - is workflow still running?
2. Clear browser cache (Ctrl+Shift+Del or Cmd+Shift+Del)
3. Check the correct URL: `https://YOUR-USERNAME.github.io/cs_puzzles/`

### JupyterLite not working?

- Workflow must successfully complete (look for ✅ in Actions)
- Check that `_site/jupyterlite/lab/index.html` was created (in Actions logs)
- Try accessing: `https://YOUR-USERNAME.github.io/cs_puzzles/jupyterlite/lab/index.html`

## 📊 GitHub Actions Features

Your workflow includes:

✨ **Caching**: Python packages cached between builds (faster rebuilds)
✨ **Permissions**: Automatically configured for GitHub Pages deployment
✨ **Concurrency**: Only one deploy at a time (prevents conflicts)
✨ **Conditional Deploy**: Only deploys on push to `main`/`master`, not on pull requests

## 🎓 Custom Domain (Optional)

To use your own domain (e.g., `csquest.myschool.edu`):

1. Go **Settings** → **Pages**
2. Under "Custom domain", enter your domain
3. Configure DNS records (instructions provided by GitHub)
4. Save

## 📱 QR Codes for Students

Once deployed, generate QR codes pointing to your live site:

```python
# Update generate_qr_codes.py with your GitHub Pages URL
BASE_URL = "https://your-username.github.io/cs_puzzles"
python3 generate_qr_codes.py
```

## ✅ Verification Checklist

After first deployment, verify everything works:

- [ ] Main page loads at `https://your-username.github.io/cs_puzzles/`
- [ ] All 16 lessons appear in sidebar
- [ ] Can navigate between lessons
- [ ] Code blocks with light background visible
- [ ] JupyterLite accessible at `...../jupyterlite/lab/index.html`
- [ ] Can create and run code in JupyterLite
- [ ] Notebooks download correctly

## 🎉 You're Done!

Your CS Quest website is now automatically deployed and updated with every push! 

Students can access it anytime at:
```
https://your-username.github.io/cs_puzzles/
```

Happy teaching! 📚✨
