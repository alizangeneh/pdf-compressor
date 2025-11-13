from setuptools import setup

APP = ['main.py']  # فایل اصلی برنامه
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyMuPDF', 'Pillow', 'tkinterdnd2', 'ghostscript'],
}

setup(
    app=APP,
    name='PDFCompressor',
    version='1.0',
    description='PDF Compressor with GUI',
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=[
        'PyMuPDF==1.26.6',
        'Pillow==11.0.0',
        'tkinterdnd2==0.4.3',
        'ghostscript==0.7'
    ],
)
