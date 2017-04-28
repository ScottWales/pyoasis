#!/usr/bin/env python
"""
Copyright 2017 ARC Centre of Excellence for Climate Systems Science

author: Scott Wales <scott.wales@unimelb.edu.au>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from numpy.distutils.core import setup, Extension

oasisf = Extension('oasis.f', 
        sources=['oasis/oasis.f90'], 
        libraries=['psmile.MPI1', 'scrip', 'mct', 'mpeu'], 
        include_dirs=['/home/562/saw562/scratch/access10-kpp/oasis3-mct/install/include'],
        library_dirs=['/home/562/saw562/scratch/access10-kpp/oasis3-mct/install/lib'],
        extra_f90_compile_args=['-fPIC'])

setup(
        name = 'oasis',
        packages = ['oasis'],
        ext_modules = [oasisf],
        install_requires = ['numpy', 'mpi4py']
        )

