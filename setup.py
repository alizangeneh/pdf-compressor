from setuptools import setup

APP = ['src/pdf_compressor.py']  # فایل اصلی برنامه (GUI و main loop)
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['Pillow', 'PyMuPDF', 'tkinterdnd2', 'ghostscript'],
    'includes': ['tkinter', 'os'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
