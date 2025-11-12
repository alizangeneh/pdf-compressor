from setuptools import setup, find_packages

APP = ['main.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PIL', 'fitz', 'tkinterdnd2'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    name="pdf-compressor",
    version="1.0.0",
    author="Ali Zangeneh",
    description="Smart PDF compressor for image and vector PDFs",
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
)
