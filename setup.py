from setuptools import setup, find_packages
import sys

# تنظیمات macOS (py2app)
APP = ['main.py'] if sys.platform == 'darwin' else []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['fitz', 'PIL', 'tkinterdnd2'],
}

setup(
    name="pdf-compressor",
    version="1.0.0",
    author="Ali Zangeneh",
    author_email="engineer.zangeneh@gmail.com",
    description="Smart PDF compressor for both image and vector PDFs",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alizangeneh/pdf-compressor",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "PyMuPDF>=1.24.0",
        "Pillow>=10.0.0",
        "tkinterdnd2>=0.4.3"
    ],
    app=APP,
    options={'py2app': OPTIONS} if sys.platform == 'darwin' else {},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    python_requires=">=3.9",
)
