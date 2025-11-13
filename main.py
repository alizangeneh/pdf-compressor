"""
PDF Compressor
--------------
Cross-platform PDF compression tool for Windows, macOS, and Linux.

Author: Ali Zangeneh
GitHub: https://github.com/alizangeneh
License: MIT
Version: 1.0.0
"""

import sys
import os
import fitz  # PyMuPDF
from tkinter import Tk, filedialog, messagebox
from PIL import Image
from src.pdf_compressor import PDFCompressor


def main():
    app = PDFCompressor()
    app.run()


if __name__ == "__main__":
    # جلوگیری از باز شدن پنجره‌ی سیاه CMD در ویندوز
    if sys.platform.startswith("win"):
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    main()
