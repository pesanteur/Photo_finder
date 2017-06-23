from setuptools import setup
from __init__ import __version__, __email__, __author__

__version__ = __version__
__author__  = __author__

requirements = [
        'facial_recognition'
        ]

description = "Finds photos in folder with people"

setup(
        name        = 'photo_finder_py',
        version     = __version__,
        author      = __author__,

        )
