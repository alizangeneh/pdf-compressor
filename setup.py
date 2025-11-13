from setuptools import setup

APP = ['main.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['fitz', 'PIL', 'tkinterdnd2', 'ghostscript'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
