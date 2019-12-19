#!/usr/bin/env python
import setuptools
from setuptools import find_packages
from numpy.distutils.core import setup
from numpy.distutils.core import Extension
from numpy.distutils import log

packages = find_packages(exclude=('tests', 'doc'))
provides = ['taurex_fortran_plugin', ]


requires = []


install_requires = ['numpy',
                    'taurex']


def build_fortran(package_name, fortran_sources, extra_compile_args=['-O3']):
    print(fortran_sources)
    ext = Extension(name=f'taurex_fortran_plugin.external.{package_name}',
                    extra_compile_args=extra_compile_args,
                    sources=fortran_sources)

    return ext

def build_temperature():

    sources = ['taurex_fortran_plugin/external/temp_fort.pyf',
               'src/temp_fort/calc_temp.f90']

    return build_fortran('temp_fort', sources)


entry_points = {'taurex.plugins': 'fortran_example = taurex_fortran_plugin'}


extensions = [build_temperature(), ]
setup(name='taurex_fortran_plugin',
      author='Ahmed Faris Al-Refaie',
      author_email='ahmed.al-refaie.12@ucl.ac.uk',
      license="BSD",
      description='TauREx 3 retrieval framework',
      packages=packages,
      include_package_data=True,
      entry_points=entry_points,
      provides=provides,
      requires=requires,
      install_requires=install_requires,
      ext_modules=extensions
      )