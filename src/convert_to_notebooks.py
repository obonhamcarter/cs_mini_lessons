"""
Convert CS Quest lessons from Quarto (.qmd) to Jupyter Notebooks (.ipynb)
This allows students to run the lessons in JupyterLite or download them.
"""

import json
import re
import os
import shutil

DOWNLOADS_DIR = "files/lessons"

def create_notebook_cell(cell_type, source):
    """Create a notebook cell"""
    return {
        "cell_type": cell_type,
        "metadata": {},
        "source": source if isinstance(source, list) else [source]
    }

def qmd_to_notebook(lesson_id, title, content_blocks):
    """Convert lesson content to Jupyter notebook format"""
    
    cells = []
    
    # Title cell
    cells.append(create_notebook_cell("markdown", [
        f"# {title}\n",
        "\n",
        "**CS Quest - Interactive Coding Adventures**\n",
        "\n",
        "Welcome to this interactive lesson! You can edit and run all the code cells below.\n"
    ]))
    
    # Add content blocks
    for block in content_blocks:
        if block["type"] == "markdown":
            cells.append(create_notebook_cell("markdown", block["content"]))
        elif block["type"] == "code":
            cell = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": block["content"]
            }
            cells.append(cell)
    
    # Create notebook structure
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
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

def save_notebook(notebook, filepath):
    """Save notebook to file"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    print(f"✅ Created: {filepath}")

    if filepath.startswith("jupyterlite/content/") and filepath.endswith(".ipynb"):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        download_path = os.path.join(DOWNLOADS_DIR, os.path.basename(filepath))
        shutil.copy2(filepath, download_path)
        print(f"📥 Synced download copy: {download_path}")

if __name__ == "__main__":
    print("Run create_all_notebooks.py to generate all lesson notebooks")
