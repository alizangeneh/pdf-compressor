from setuptools import setup

APP = ['main.py']  # فایل اصلی پروژه
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['fitz', 'PIL', 'tkinterdnd2', 'ghostscript'],  # fitz نام داخلی PyMuPDF است
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
