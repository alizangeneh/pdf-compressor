from setuptools import setup

setup(
    app=['main.py'],  # فایل اصلی پروژه
    setup_requires=['py2app'],
    install_requires=[
        "PyMuPDF==1.26.6",
        "Pillow==11.0.0",
        "tkinterdnd2==0.4.3",
        "ghostscript==0.7"
    ],
    options={
        'py2app': {
            'argv_emulation': True,
            'packages': ['fitz', 'PIL', 'tkinterdnd2']
        }
    },
)
