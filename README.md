# CS Quest - Coding Adventures 🚀

An interactive Quarto website featuring 12 engaging computer science mini-lessons for beginning students. Each quest is a 5-minute adventure designed to teach fundamental programming concepts through interactive Python demonstrations.

## 📚 Quest Collection

The website includes 12 complete interactive lessons:

1. **Variables - Your Coding Backpack** - Store and use data
2. **Data Types - Shapes of Information** - Integers, strings, booleans, floats
3. **Conditionals - Choose Your Path** - If/else statements and decision making
4. **Loops - The Power of Repetition** - For and while loops
5. **Lists - Collecting Treasures** - Arrays and collections
6. **Functions - Magic Spells** - Reusable code blocks
7. **Dictionaries - The Key Keeper** - Key-value pairs
8. **Fibonacci - The Golden Sequence** - Mathematical patterns in nature
9. **Sorting - Organizing Chaos** - Bubble sort and selection sort
10. **Number Game - Can You Guess It?** - Build an interactive game
11. **Recursion - The Echo Chamber** - Functions calling themselves
12. **Big O - Speed Matters** - Algorithm complexity and efficiency

## 🎯 Features

- ✨ **Interactive Python Code**: Multiple ways to run code:
  - **In-page execution**: Code runs directly on lesson pages using Pyodide
  - **JupyterLite**: Full Jupyter environment in the browser (no installation needed!)
  - **Downloadable notebooks**: Use in local Jupyter or Google Colab
- 🎨 **Consistent Theme**: Beautiful, cohesive design across all lessons
- 📱 **Mobile-Friendly**: Responsive design optimized for phone access via QR codes
- 🎮 **Engaging Format**: Each lesson includes:
  - Introduction with engaging story
  - Clear explanations with examples
  - Interactive coding challenges
  - Puzzles with solutions
  - Key takeaways and next steps
- 🔍 **Searchable**: Built-in search functionality
- 🎓 **Beginner-Friendly**: Friendly, encouraging tone perfect for new coders

## 🚀 Quick Start

### Prerequisites

- [Quarto](https://quarto.org/) (version 1.4 or higher)
- Python 3.8+ (for local preview and JupyterLite)
- JupyterLite (for full notebook experience):
  ```bash
  pip install jupyterlite-core jupyterlite-pyodide-kernel
  ```

### Basic Setup (Quarto Only)

1. Navigate to the project directory:
```bash
cd /media/data/Dropbox/4_projects_current/cs_puzzles
```

2. Preview the website locally:
```bash
quarto preview
```

3. Build the website:
```bash
quarto render
```

The website will be generated in the `_site` directory.

### Full Setup (with JupyterLite)

For the complete interactive experience with Jupyter notebooks:

1. **Install JupyterLite:**
```bash
pip install jupyterlite-core jupyterlite-pyodide-kernel
```

2. **Build everything:**
```bash
./build.sh
```

Or manually:

```bash
# Build JupyterLite
cd jupyterlite
jupyter lite build --contents content --output-dir ../jupyterlite_build
cd ..

# Build Quarto site
quarto render

# Copy JupyterLite to output
mkdir -p _site/jupyterlite
cp -r jupyterlite_build/* _site/jupyterlite/
```

3. **Preview locally:**
```bash
cd _site
python -m http.server 8000
```

Then visit:
- Main site: `http://localhost:8000`
- JupyterLite: `http://localhost:8000/jupyterlite/lab/index.html`
## 🌐 Deploy to GitHub Pages

### Automatic Deployment with GitHub Actions

This project includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that automatically builds and deploys your site to GitHub Pages!

#### Setup Instructions

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add CS Quest lessons"
   git push origin main
   ```

2. **Enable GitHub Pages**
   - Go to your repository settings
   - Navigate to "Pages" section
   - Under "Build and deployment":
     - Select "GitHub Actions" as the source
     - Save

3. **Workflow Runs Automatically**
   - The `.github/workflows/deploy.yml` workflow triggers on push to `main` or `master`
   - It automatically:
     - Installs Quarto, Python dependencies, and JupyterLite
     - Renders the Quarto site
     - Builds JupyterLite
     - Deploys to GitHub Pages
   - Check the "Actions" tab in your repo to monitor build progress

#### What Gets Built

The workflow:
- ✅ Installs Quarto
- ✅ Installs Python 3.11
- ✅ Installs JupyterLite (`jupyterlite-core` and `jupyterlite-pyodide-kernel`)
- ✅ Renders all 16 lessons as HTML
- ✅ Builds JupyterLite lab environment
- ✅ Deploys combined `_site` folder to GitHub Pages

#### Your Site URL

After first successful deployment, your site will be available at:
```
https://your-username.github.io/repository-name
```

Or if using a custom domain, configure it in repository settings.

#### Rebuilding After Changes

Simply push to `main` (or `master`) and the workflow will:
1. Automatically trigger
2. Rebuild everything
3. Redeploy to GitHub Pages

#### View Deployment Status

- Actions tab: See build logs
- Deployments tab: See deployment history
- GitHub Pages settings: See current live site URL

### Manual Deployment Alternative

If you prefer manual deployment:

```bash
# Build everything
quarto render
jupyter-lite build --output-dir _site/jupyterlite

# Deploy _site folder to hosting service of choice
# (GitHub Pages, Netlify, Vercel, etc.)
```
## � Interactive Features

### Three Ways to Run Code

1. **On Lesson Pages (Easiest)**
   - All code blocks are editable and runnable
   - Uses Quarto's Pyodide integration
   - No setup required - works immediately
   - Click "Run Code" or edit and execute inline

2. **JupyterLite (Full Jupyter Experience)**
   - Complete Jupyter Lab environment in browser
   - File browser, multiple notebooks, extensions
   - Save and download your work
   - Access via: `yoursite.com/jupyterlite/lab/index.html`
   - Or use the "🚀 JupyterLite" link in the navbar

3. **Download & Use Locally**
   - Each lesson has a downloadable `.ipynb` file
   - Use in local Jupyter, VS Code, or Google Colab
   - Available in `jupyterlite/content/` directory

### Interactive Code on Lesson Pages

Every lesson now includes a tip box at the top with options:
- 📓 Open in JupyterLite (full notebook environment)
- ▶️ Run code directly on the page
- 📥 Download the notebook file

Example from a lesson page:
```markdown
::: {.tip-box}
**💻 Interactive Options:**
- 📓 **[Open in JupyterLite](../jupyterlite/lab/index.html?path=01-variables.ipynb)**
- ▶️ **Run code directly below**
- 📥 **[Download Notebook](../jupyterlite/content/01-variables.ipynb)**
:::
```

## �📱 QR Code Generation for Student Access

To create QR codes for each lesson (so students can scan and access individual quests):

### Method 1: Using Python with qrcode library

```bash
# Install required package
pip install qrcode[pil]
```

Create a Python script `generate_qr_codes.py`:

```python
import qrcode
import os

# Base URL (change this to your deployed website URL)
BASE_URL = "https://your-website.com/cs_puzzles"

# Quest information
quests = [
    ("01-variables", "Quest 1: Variables"),
    ("02-data-types", "Quest 2: Data Types"),
    ("03-conditionals", "Quest 3: Conditionals"),
    ("04-loops", "Quest 4: Loops"),
    ("05-lists", "Quest 5: Lists"),
    ("06-functions", "Quest 6: Functions"),
    ("07-dictionaries", "Quest 7: Dictionaries"),
    ("08-fibonacci", "Quest 8: Fibonacci"),
    ("09-sorting", "Quest 9: Sorting"),
    ("10-number-game", "Quest 10: Number Game"),
    ("11-recursion", "Quest 11: Recursion"),
    ("12-complexity", "Quest 12: Big O Complexity"),
]

# Create QR codes directory
os.makedirs("qr_codes", exist_ok=True)

# Generate QR codes
for lesson_id, title in quests:
    url = f"{BASE_URL}/lessons/{lesson_id}.html"
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save with descriptive filename
    filename = f"qr_codes/{lesson_id}.png"
    img.save(filename)
    
    print(f"✅ Created QR code for {title}: {filename}")

print("\n✨ All QR codes generated in 'qr_codes/' directory!")
```

Run the script:
```bash
python generate_qr_codes.py
```

### Method 2: Using Online QR Code Generators

For quick generation, use online tools like:

1. **QR Code Generator** (https://www.qr-code-generator.com/)
2. **QRStuff** (https://www.qrstuff.com/)
3. **GoQR** (https://goqr.me/)

Simply paste the URL of each lesson and download the QR code image.

### Method 3: Create a PDF Sheet with All QR Codes

Create `create_qr_sheet.py`:

```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import qrcode
from io import BytesIO
from PIL import Image

def create_qr_sheet(output_filename="CS_Quest_QR_Codes.pdf"):
    # Create PDF
    c = canvas.Canvas(output_filename, pagesize=letter)
    width, height = letter
    
    # Base URL (UPDATE THIS!)
    BASE_URL = "https://your-website.com/cs_puzzles"
    
    quests = [
        ("01-variables", "Quest 1: Variables"),
        ("02-data-types", "Quest 2: Data Types"),
        ("03-conditionals", "Quest 3: Conditionals"),
        ("04-loops", "Quest 4: Loops"),
        ("05-lists", "Quest 5: Lists"),
        ("06-functions", "Quest 6: Functions"),
        ("07-dictionaries", "Quest 7: Dictionaries"),
        ("08-fibonacci", "Quest 8: Fibonacci"),
        ("09-sorting", "Quest 9: Sorting"),
        ("10-number-game", "Quest 10: Number Game"),
        ("11-recursion", "Quest 11: Recursion"),
        ("12-complexity", "Quest 12: Big O"),
    ]
    
    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(1*inch, height - 1*inch, "CS Quest QR Codes")
    
    c.setFont("Helvetica", 12)
    c.drawString(1*inch, height - 1.4*inch, "Scan to access interactive coding lessons!")
    
    # Layout: 3 columns x 4 rows
    x_positions = [0.75*inch, 3.25*inch, 5.75*inch]
    y_start = height - 2.5*inch
    y_spacing = 2.25*inch
    
    for idx, (lesson_id, title) in enumerate(quests):
        row = idx // 3
        col = idx % 3
        
        x = x_positions[col]
        y = y_start - (row * y_spacing)
        
        # Generate QR code
        url = f"{BASE_URL}/lessons/{lesson_id}.html"
        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save to BytesIO
        img_buffer = BytesIO()
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        
        # Draw QR code
        c.drawImage(img_buffer, x, y - 1.5*inch, width=1.5*inch, height=1.5*inch)
        
        # Draw title
        c.setFont("Helvetica-Bold", 10)
        c.drawString(x, y - 1.7*inch, title)
    
    c.save()
    print(f"✅ QR code sheet created: {output_filename}")

if __name__ == "__main__":
    # Install: pip install reportlab qrcode[pil] pillow
    create_qr_sheet()
```

## 🌐 Deployment Options

### Option 1: GitHub Pages (Free)

1. Push your project to GitHub
2. Go to repository Settings → Pages
3. Select source branch and `/_site` folder
4. Your site will be available at `https://username.github.io/repository-name`

### Option 2: Netlify (Free)

1. Sign up at [netlify.com](https://www.netlify.com/)
2. Connect your GitHub repository
3. Set build command: `quarto render`
4. Set publish directory: `_site`
5. Deploy!

### Option 3: Quarto Pub (Free)

```bash
quarto publish quarto-pub
```

### Option 4: Local Server for Classroom

```bash
# Render once
quarto render

# Serve on local network
cd _site
python -m http.server 8000

# Students can access via: http://YOUR_IP:8000
```

## 🎨 Customization

### Modify Theme Colors

Edit `custom.scss`:

```scss
$primary: #6366f1;   // Change primary color
$secondary: #ec4899; // Change secondary color
```

### Add More Lessons

1. Create new lesson file in `lessons/` directory (e.g., `13-new-quest.qmd`)
2. Add entry to `_quarto.yml` under sidebar contents
3. Add to index.qmd and all-quests.qmd

### Modify Lesson Template

Each lesson follows this structure:

```markdown
---
title: "Quest Title"
subtitle: "Quest Subtitle"
---

::: {.quest-badge}
🎯 QUEST X | Difficulty: Level | Time: 5 minutes
:::

## 📖 Introduction
## 💡 Explanation
## 🎮 Activity
## 👨‍💻 Code Example
## 🧩 Puzzle Time!
## 🎯 Key Takeaways
```

## 📊 Analytics (Optional)

To track student engagement, add Google Analytics or Plausible:

In `_quarto.yml`, add:

```yaml
website:
  google-analytics: "G-XXXXXXXXXX"
```

## 🐛 Troubleshooting

### Code not running in browser?

Make sure you're using `{pyodide-python}` code blocks, not `{python}`.

### Website not rendering properly?

```bash
quarto check
```

### QR codes not working?

- Verify the base URL in your QR code generation script
- Test URLs in browser before generating QR codes
- Ensure website is deployed and accessible

## 📝 License

Feel free to use and modify these lessons for educational purposes!

## 🤝 Contributing

Suggestions for improvements:
- Additional interactive elements
- More lessons on advanced topics
- Translations to other languages
- Enhanced visualizations

## 🎓 Educational Use

Perfect for:
- Computer Science classrooms
- Coding clubs
- Self-paced learning
- Workshops and boot camps
- After-school programs

## 📞 Support

For questions or issues, please refer to the [Quarto documentation](https://quarto.org/docs/).

---

**Happy Coding! May your bugs be few and your solutions elegant!** ✨🐛✨
