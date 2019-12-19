from setuptools import find_packages
from distutils.core import setup

packages = find_packages(exclude=('tests', 'doc'))
provides = ['taurex_example_plugin', ]

requires = []

install_requires = ['taurex', ]

entry_points = {'taurex.plugins': 'example = taurex_example_plugin'}

setup(name='taurex_example_plugin',
      author="Ahmed Faris Al-Refaie",
      author_email="ahmed.al-refaie.12@ucl.ac.uk",
      license="BSD",
      description='A Taurex3 plugin example',
      packages=packages,
      entry_points=entry_points,
      provides=provides,
      requires=requires,
      install_requires=install_requires)