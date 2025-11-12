PDF Compressor

A smart and simple Python tool to compress both image-based and vector-based PDF files. Built with a clean drag-and-drop GUI and DPI control for precise compression results.

------------------------------------------------------------

Features:
- Compress scanned (image) PDFs by reducing DPI
- Optimize vector PDFs using Ghostscript
- Simple Tkinter-based interface
- Saves output files to a “Compressed PDFs” folder automatically
- Fast, lightweight, and completely open-source

------------------------------------------------------------

Installation:

1. Clone this repository:
   git clone https://github.com/alizangeneh/pdf-compressor.git
   cd pdf-compressor

2. Install dependencies:
   pip install -r requirements.txt

3. Install Ghostscript for vector PDF optimization:
   https://www.ghostscript.com/download.html

4. Make sure the Ghostscript path (for example C:\Program Files\gs\gs9.xx\bin\) is added to your system PATH.

------------------------------------------------------------

Usage:

Run the application:
   python main.py

Steps:
1. Drag and drop your PDF files into the app or use the Browse button.
2. Choose a compression level (DPI value).
3. Click Process to start compression.
4. The compressed PDFs will be saved inside a new folder called Compressed_PDFs.

------------------------------------------------------------

Requirements:
- Python 3.9 or higher
- PyMuPDF (fitz)
- Pillow
- tkinterdnd2
- Ghostscript (for vector PDFs)

Manual install:
   pip install PyMuPDF Pillow tkinterdnd2

------------------------------------------------------------

License:
This project is licensed under the MIT License – see the LICENSE file for details.

------------------------------------------------------------

Author:
Developed with ❤️ by Ali Zangeneh
GitHub: https://github.com/alizangeneh
