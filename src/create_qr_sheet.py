"""
Create a printable PDF sheet with all CS Quest QR codes.
This script generates a single PDF with all lesson QR codes arranged in a grid.

Requirements:
    pip install reportlab qrcode[pil] pillow

Usage:
    1. Update the BASE_URL variable with your deployed website URL
    2. Run: python create_qr_sheet.py
    3. PDF will be saved as 'CS_Quest_QR_Codes.pdf'
"""

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor
except ImportError:
    print("❌ Error: reportlab not installed")
    print("Install with: pip install reportlab qrcode[pil] pillow")
    exit(1)

import qrcode
from io import BytesIO

# ⚠️ UPDATE THIS URL TO YOUR DEPLOYED WEBSITE
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
    ("12-complexity", "Quest 12: Big O"),
]

def create_qr_sheet(output_filename="CS_Quest_QR_Codes.pdf"):
    """Create PDF with all QR codes in a grid layout"""
    
    print("=" * 60)
    print("CS QUEST QR CODE SHEET GENERATOR")
    print("=" * 60)
    print(f"\nBase URL: {BASE_URL}")
    print(f"Output file: {output_filename}")
    print(f"Creating PDF with {len(quests)} QR codes...\n")
    
    # Create PDF canvas
    c = canvas.Canvas(output_filename, pagesize=letter)
    width, height = letter
    
    # Header
    c.setFillColor(HexColor("#6366f1"))
    c.rect(0, height - 1.5*inch, width, 1.5*inch, fill=True, stroke=False)
    
    c.setFillColor(HexColor("#ffffff"))
    c.setFont("Helvetica-Bold", 28)
    c.drawString(0.75*inch, height - 1*inch, "🚀 CS Quest - Coding Adventures")
    
    c.setFont("Helvetica", 14)
    c.drawString(0.75*inch, height - 1.3*inch, "Scan any QR code to start your coding journey!")
    
    # Layout: 3 columns x 4 rows
    x_positions = [0.75*inch, 3.25*inch, 5.75*inch]
    y_start = height - 2.25*inch
    y_spacing = 2.3*inch
    
    for idx, (lesson_id, title) in enumerate(quests):
        row = idx // 3
        col = idx % 3
        
        x = x_positions[col]
        y = y_start - (row * y_spacing)
        
        # Generate QR code
        url = f"{BASE_URL}/lessons/{lesson_id}.html"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=8,
            border=2
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert to suitable format for reportlab
        img_buffer = BytesIO()
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        
        # Draw QR code
        qr_size = 1.5*inch
        c.drawImage(img_buffer, x, y - qr_size, width=qr_size, height=qr_size)
        
        # Draw title
        c.setFillColor(HexColor("#1e293b"))
        c.setFont("Helvetica-Bold", 9)
        c.drawString(x, y - qr_size - 0.15*inch, title)
        
        # Draw quest number badge
        c.setFillColor(HexColor("#6366f1"))
        quest_num = idx + 1
        c.circle(x + qr_size - 0.2*inch, y - 0.2*inch, 0.15*inch, fill=True)
        c.setFillColor(HexColor("#ffffff"))
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(x + qr_size - 0.2*inch, y - 0.25*inch, str(quest_num))
        
        print(f"✅ Added {title}")
    
    # Footer
    c.setFillColor(HexColor("#64748b"))
    c.setFont("Helvetica", 8)
    footer_text = f"Generated for: {BASE_URL} | Print this sheet and distribute to students"
    c.drawCentredString(width/2, 0.5*inch, footer_text)
    
    # Save PDF
    c.save()
    
    print("\n" + "=" * 60)
    print(f"✨ SUCCESS! QR code sheet created!")
    print(f"📄 File: {output_filename}")
    print("=" * 60)
    print("\n📌 Next steps:")
    print("1. Open the PDF and review")
    print("2. Print on standard letter-size paper")
    print("3. Cut out individual QR codes or post the full sheet")
    print("4. Test with a phone to ensure URLs work correctly")

def main():
    """Main entry point"""
    
    # Check if BASE_URL has been updated
    if "your-website.com" in BASE_URL:
        print("\n⚠️  WARNING: Please update BASE_URL in this script!")
        print("   Set it to your deployed website URL before generating the PDF.\n")
        response = input("Continue anyway with placeholder URL? (y/n): ")
        if response.lower() != 'y':
            print("\nAborted. Please update BASE_URL and try again.")
            return
        print()
    
    create_qr_sheet()

if __name__ == "__main__":
    main()
