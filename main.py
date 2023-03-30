import fitz
# specify the path of the PDF file
pdf_path = "2021.pdf"
# Open the PDF
try:
    pdf = fitz.open(pdf_path)
except FileNotFoundError:
    print("File not found")
# Iterate over the pages starting from the 1st page
for i, page in enumerate(pdf):
    try:
        # Render the page as a JPEG image
        pix = page.get_pixmap(alpha=False)
        # Save the image
        pix.writeJPG(f"page_{i+1}.jpg")
    except Exception as e:
        print(e)
# Close the PDF
try:
    pdf.close()
    print("Successful")
except Exception as e:
    print(e)
