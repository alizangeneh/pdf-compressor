"""
PDF Compressor
--------------
A smart PDF compression tool for both image-based and vector-based PDF files.

Author: Ali Zangeneh
GitHub: https://github.com/alizangeneh
License: MIT
Version: 1.0.0
Year: 2025

Description:
    This tool reduces the size of PDF files using DPI-based compression for scanned (image)
    PDFs and Ghostscript optimization for vector PDFs. It features a simple drag-and-drop
    interface built with Tkinter.
"""

from src.pdf_compressor import PDFCompressorApp
from tkinterdnd2 import TkinterDnD
import tkinter as tk

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = PDFCompressorApp(root)
    root.mainloop()
