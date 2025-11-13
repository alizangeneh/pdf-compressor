from setuptools import setup, find_packages

setup(
    name="pdf-compressor",
    version="1.0.0",
    author="Ali Zangeneh",
    author_email="engineer.zangeneh@gmail.com",
    description="Smart cross-platform PDF compressor (Windows, macOS, Linux)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alizangeneh/pdf-compressor",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "PyMuPDF>=1.24.9",
        "Pillow>=10.0.0",
        "tkinterdnd2>=0.4.3",
        "ghostscript>=0.7"
    ],
    entry_points={
        "console_scripts": [
            "pdf-compressor=src.pdf_compressor:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Topic :: Utilities",
    ],
    python_requires=">=3.9",
)
