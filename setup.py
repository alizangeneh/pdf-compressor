from setuptools import setup, find_packages

# ----------------------------
# Main script for macOS py2app
APP = ["main.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "packages": ["fitz", "PIL", "tkinterdnd2", "io", "subprocess", "threading", "tkinter", "webbrowser"],
}

# ----------------------------
setup(
    name="pdf-compressor",
    version="1.0.0",
    author="Ali Zangeneh",
    author_email="engineer.zangeneh@gmail.com",  # Optional
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
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.9",
    # For macOS py2app
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
)
