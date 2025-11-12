from setuptools import setup, find_packages

setup(
    name="pdf-compressor",
    version="1.0.0",
    author="Ali Zangeneh",
    author_email="your_email@example.com",  # اختیاری
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
        "Operating System :: Microsoft :: Windows",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.9",
)
