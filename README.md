# Convert PDF pages to JPEG images using Python and PyMuPDF

The program first opens the PDF file and then iterates over all of its pages starting from the 1st page. For each page, it retrieves a pixel map of the page and then saves the page as a JPEG image. Finally, it closes the PDF.

This Python script uses the PyMuPDF library to open a PDF file, iterate over its pages starting from the 1st page, render each page as a JPEG image, and save the image in the current directory.

## Prerequisites

* Python 3.x
* PyMuPDF library (pip install PyMuPDF)

## Usage

- Clone or download the script.
- Install the PyMuPDF library: pip install PyMuPDF.
- Change the pdf_path variable in the script to the path of the PDF file you want to convert.
- Run the script: python pdf2jpg.py.
- Check the current directory for the JPEG images of the PDF pages.

## Explanation

- import fitz: This line imports the fitz library which provides the tools to process and render PDF documents. 
- pdf_path = "yourpdf.pdf": This line specifies the path of the PDF document. 
- fitz.open(pdf_path): This line opens the PDF document. 
- for i, page in enumerate(pdf): This line iterates over the pages of the PDF document starting from the 6th page. 
- pix = page.get_pixmap(alpha=False): This line renders the page as a JPEG image. 
- pix.writeJPG(f"page_{i+1}.jpg"): This line saves each page in the PDF document as an image file. 
- pdf.close(): This line closes the PDF document. 
- print("Successful"): This line prints a success message
