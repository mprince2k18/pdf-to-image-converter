The program first opens the PDF file and then iterates over all of its pages starting from the 6th page. For each page, it retrieves a pixel map of the page and then saves the page as a JPEG image. Finally, it closes the PDF.

* 1.  import fitz: This line imports the fitz library which provides the tools to process and render PDF documents. 
* 2. pdf_path = "2021.pdf": This line specifies the path of the PDF document. 
* 3. fitz.open(pdf_path): This line opens the PDF document. 
* 4. for i, page in enumerate(pdf): This line iterates over the pages of the PDF document starting from the 6th page. 
* 5. pix = page.get_pixmap(alpha=False): This line renders the page as a JPEG image. 
* 6. pix.writeJPG(f"page_{i+1}.jpg"): This line saves each page in the PDF document as an image file. 
* 7. pdf.close(): This line closes the PDF document. 
* 8. print("Successful"): This line prints a success message
