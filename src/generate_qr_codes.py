"""
Generate QR codes for all CS Quest lessons.
This script creates individual QR code images for each lesson.

Requirements:
    pip install qrcode[pil]

Usage:
    1. Update the BASE_URL variable with your deployed website URL
    2. Run: python generate_qr_codes.py
    3. QR codes will be saved in the 'qr_codes/' directory
"""

import qrcode
import os

# ⚠️ UPDATE THIS URL TO YOUR DEPLOYED WEBSITE
BASE_URL = "https://your-website.com/cs_puzzles"

# Quest information - (lesson_id, title)
quests = [
    ("01-variables", "Quest 1: Variables - Your Coding Backpack"),
    ("02-data-types", "Quest 2: Data Types - Shapes of Information"),
    ("03-conditionals", "Quest 3: Conditionals - Choose Your Path"),
    ("04-loops", "Quest 4: Loops - The Power of Repetition"),
    ("05-lists", "Quest 5: Lists - Collecting Treasures"),
    ("06-functions", "Quest 6: Functions - Magic Spells"),
    ("07-dictionaries", "Quest 7: Dictionaries - The Key Keeper"),
    ("08-fibonacci", "Quest 8: Fibonacci - The Golden Sequence"),
    ("09-sorting", "Quest 9: Sorting - Organizing Chaos"),
    ("10-number-game", "Quest 10: Number Game - Can You Guess It?"),
    ("11-recursion", "Quest 11: Recursion - The Echo Chamber"),
    ("12-complexity", "Quest 12: Big O - Speed Matters"),
]

def generate_qr_codes():
    """Generate QR codes for all lessons"""
    
    # Create output directory
    output_dir = "qr_codes"
    os.makedirs(output_dir, exist_ok=True)
    
    print("=" * 60)
    print("CS QUEST QR CODE GENERATOR")
    print("=" * 60)
    print(f"\nBase URL: {BASE_URL}")
    print(f"Output directory: {output_dir}/")
    print(f"Generating {len(quests)} QR codes...\n")
    
    for lesson_id, title in quests:
        # Construct full URL
        url = f"{BASE_URL}/lessons/{lesson_id}.html"
        
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls size (1 is smallest)
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,  # Size of each box in pixels
            border=4,  # Border size in boxes
        )
        
        # Add data to QR code
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save with descriptive filename
        filename = f"{output_dir}/{lesson_id}.png"
        img.save(filename)
        
        print(f"✅ {title}")
        print(f"   URL: {url}")
        print(f"   File: {filename}\n")
    
    print("=" * 60)
    print(f"✨ SUCCESS! All {len(quests)} QR codes generated!")
    print(f"📁 Find them in: {output_dir}/")
    print("=" * 60)
    print("\n📌 Next steps:")
    print("1. Test the QR codes with your phone")
    print("2. Print them for distribution to students")
    print("3. Consider creating a PDF sheet (see create_qr_sheet.py)")

def main():
    """Main entry point"""
    
    # Check if BASE_URL has been updated
    if "your-website.com" in BASE_URL:
        print("\n⚠️  WARNING: Please update BASE_URL in this script!")
        print("   Set it to your deployed website URL before generating QR codes.\n")
        response = input("Continue anyway with placeholder URL? (y/n): ")
        if response.lower() != 'y':
            print("\nAborted. Please update BASE_URL and try again.")
            return
    
    generate_qr_codes()

if __name__ == "__main__":
    main()
