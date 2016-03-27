from setuptools import setup
import os
import platform

req_file = None
if platform.system() == 'Darwin':
    req_file = 'osx-requirements.txt'

requires = []
if (req_file != None):
    with open(os.path.join(os.path.dirname(__file__), req_file)) as f:
        requires = list(f.readlines())

setup(name="guide",
      version='0.0.1',
      packages=['.'],
      author="Jake Waffle, Kyle Shoemaker, Gus Tropea",
      description=''.join("""
          Cross-platform IDE that is portable, customizable and supports any language!
      """.strip().split('\n')),
      install_requires=requires,
      entry_points=dict(console_scripts=['guide=guide:main'])
      )
