"""
Quick script to generate placeholder notebooks for all 12 CS Quest lessons.
These can be filled in with full content later or generated from the .qmd files.
"""

import json
import os
import shutil

# Lesson metadata
lessons = [
    (1, "variables", "Variables - Your Coding Backpack", "🎒"),
    (2, "data-types", "Data Types - Shapes of Information", "🔷"),
    (3, "conditionals", "Conditionals - Choose Your Path", "🛤️"),
    (4, "loops", "Loops - The Power of Repetition", "🔄"),
    (5, "lists", "Lists - Collecting Treasures", "📜"),
    (6, "functions", "Functions - Magic Spells", "✨"),
    (7, "dictionaries", "Dictionaries - The Key Keeper", "🗝️"),
    (8, "fibonacci", "Fibonacci - The Golden Sequence", "🌟"),
    (9, "sorting", "Sorting - Organizing Chaos", "📊"),
    (10, "number-game", "Number Game - Can You Guess It?", "🎲"),
    (11, "recursion", "Recursion - The Echo Chamber", "🔁"),
    (12, "complexity", "Big O - Speed Matters", "⚡"),
]

def create_basic_notebook(quest_num, slug, title, emoji):
    """Create a basic notebook structure"""
    
    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# Quest {quest_num}: {title} {emoji}\n",
                "\n",
                "**CS Quest - Interactive Coding Adventures**\n",
                "\n",
                "Welcome to this interactive lesson! Edit and run all code cells below.\n",
                "\n",
                "[View lesson on website →](../lessons/{quest_num:02d}-{slug}.qmd)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Getting Started\n",
                "\n",
                "This is an interactive Jupyter notebook. You can:\n",
                "\n",
                "- **Run cells**: Click a code cell and press `Shift+Enter`\n",
                "- **Edit code**: Click in any cell to modify it\n",
                "- **Add cells**: Use the `+` button in the toolbar\n",
                "- **Save work**: Download your notebook with File → Download\n",
                "\n",
                "Let's start coding!"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Welcome to Quest " + str(quest_num) + "!\n",
                "print(f\"🎉 Welcome to Quest {" + str(quest_num) + "}: {title}\")\n",
                "print(\"Let's learn about \" + title.split('-')[0].lower().strip() + \"!\")\n",
                "\n",
                "# Edit this code and run it with Shift+Enter"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 📚 Lesson Content\n",
                "\n",
                "The complete lesson with explanations, examples, and challenges is available on the website.\n",
                "\n",
                "This notebook provides an interactive coding environment where you can experiment with the concepts.\n",
                "\n",
                "### Try it yourself!\n",
                "\n",
                "Use the cells below to practice coding:"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Your practice code here\n",
                "\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# More practice code\n",
                "\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 🎯 Next Steps\n",
                "\n",
                f"Great work on Quest {quest_num}!\n",
                "\n",
                "- Continue to the next quest\n",
                "- Or return to [CS Quest Home](../index.qmd)\n",
                "\n",
                "Keep coding! 💻✨"
            ]
        }
    ]
    
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    return notebook


def sync_to_downloads(source_path, downloads_dir):
    """Copy a generated notebook into files/lessons for direct downloads."""
    os.makedirs(downloads_dir, exist_ok=True)
    destination_path = os.path.join(downloads_dir, os.path.basename(source_path))
    shutil.copy2(source_path, destination_path)
    return destination_path

def main():
    """Generate all notebook files"""
    
    output_dir = "jupyterlite/content"
    downloads_dir = "files/lessons"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(downloads_dir, exist_ok=True)
    
    print("=" * 60)
    print("CS QUEST - NOTEBOOK GENERATOR")
    print("=" * 60)
    print()
    
    for quest_num, slug, title, emoji in lessons:
        filename = f"{output_dir}/{quest_num:02d}-{slug}.ipynb"
        
        if os.path.exists(filename):
            print(f"⏭️  Skipping Quest {quest_num} (already exists): {filename}")
        else:
            notebook = create_basic_notebook(quest_num, slug, title, emoji)

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, indent=2, ensure_ascii=False)

            print(f"✅ Created Quest {quest_num}: {filename}")

        synced_file = sync_to_downloads(filename, downloads_dir)
        print(f"📥 Synced download copy: {synced_file}")
    
    print()
    print("=" * 60)
    print("✨ Notebook generation complete!")
    print("=" * 60)
    print()
    print(f"📁 Notebooks saved in: {output_dir}/")
    print(f"📁 Download copies saved in: {downloads_dir}/")
    print()
    print("Next steps:")
    print("1. Review and enhance notebooks with full lesson content")
    print("2. Build JupyterLite: cd jupyterlite && jupyter lite build --contents content")
    print("3. Or use the build.sh script to build everything")

if __name__ == "__main__":
    main()
