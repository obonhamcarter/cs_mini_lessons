#!/usr/bin/env python3
"""
Generate Jupyter notebooks for lessons 13-16
"""
import json

def create_notebook(lesson_num, lesson_title, lesson_slug):
    """Create a notebook template for a lesson"""
    
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "id": f"#VSC-top-{lesson_num}",
                "metadata": {"language": "markdown"},
                "source": [
                    f"# Quest {lesson_num}: {lesson_title}",
                    "",
                    "**CS Quest - Interactive Coding Adventures**",
                    "",
                    f"Welcome to this interactive lesson! Edit and run all code cells below.",
                ]
            },
            {
                "cell_type": "markdown",
                "id": f"#VSC-intro-{lesson_num}",
                "metadata": {"language": "markdown"},
                "source": [
                    "## 📖 Introduction",
                    "",
                    "This lesson is available in two formats:",
                    "",
                    f"- **Full lesson with explanations**: [View on website](../lessons/{lesson_slug}.qmd)",
                    "- **Interactive practice**: Run code cells below to experiment!",
                ]
            },
            {
                "cell_type": "markdown",
                "id": f"#VSC-concept-{lesson_num}",
                "metadata": {"language": "markdown"},
                "source": [
                    "## 💡 Key Concepts",
                    "",
                    "Refer to the full lesson for detailed explanations.",
                    "",
                    "Try editing and running the code cells to practice!"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "id": f"#VSC-example1-{lesson_num}",
                "metadata": {"language": "python"},
                "outputs": [],
                "source": [
                    "# Example code cell - edit and run!",
                    f"print('Welcome to Quest {lesson_num}: {lesson_title}!')",
                    "",
                    "# Add your code below this line:"
                ]
            },
            {
                "cell_type": "markdown",
                "id": f"#VSC-challenge-{lesson_num}",
                "metadata": {"language": "markdown"},
                "source": [
                    "## 🧩 Challenge",
                    "",
                    "Try the challenge from the main lesson and test it here!",
                    "",
                    "Click the code cell below to edit and run your solution."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "id": f"#VSC-challenge-code-{lesson_num}",
                "metadata": {"language": "python"},
                "outputs": [],
                "source": [
                    "# Challenge code - write your solution below!",
                    "",
                    "# Hint: Check the full lesson for challenge details"
                ]
            },
            {
                "cell_type": "markdown",
                "id": f"#VSC-end-{lesson_num}",
                "metadata": {"language": "markdown"},
                "source": [
                    "## 🎓 What You Learned",
                    "",
                    "Great job! Review the main lesson for a summary of key concepts.",
                    "",
                    "## 🚀 What's Next?",
                    "",
                    "Ready for the next quest? Go back to the main website to continue your learning adventure!"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.11.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    return notebook

# Create notebooks for lessons 13-16
lessons_data = [
    (13, "Iterative Loops", "13-iterative-loops"),
    (14, "Functions Part 2: Non-Returning", "14-functions-non-returning"),
    (15, "Functions Part 3: Returning", "15-functions-returning"),
    (16, "Lambda Functions", "16-lambda-functions"),
]

for lesson_num, title, slug in lessons_data:
    notebook = create_notebook(lesson_num, title, slug)
    
    filename = f"jupyterlite/content/{slug}.ipynb"
    with open(filename, 'w') as f:
        json.dump(notebook, f, indent=2)
    
    print(f"✅ Created {filename}")

print("\n🎉 All notebooks created successfully!")
