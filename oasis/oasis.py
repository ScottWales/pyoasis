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

from mpi4py import MPI
from .f import oasis as foasis
from .partition import Partition
from .variable import Variable

class Oasis(object):
    """
    An Oasis coupled model connection

    May be used as a context manager to automatically terminate the coupling::

        with Oasis('atmos') as o:
            o.register(partition)
            o.register(grid)
            o.register(variable)

            variable.put(t, data)
            variable.get(t, data)
    """

    def __init__(self, name, coupled=True):
        """
        Create an Oasis session (singleton)
        """
        self.compid = foasis.init_comp(name)
        self.partition = {}
        self.variable = {}
        self._define_phase = True

    def terminate(self):
        """
        Terminate the Oasis session
        """
        foasis.terminate()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.terminate()

    def register(self, obj):
        """
        Register a partition, grid or variable with Oasis

        Must be called before `Oasis.enddef()`
        """
        if self._define_phase == False:
            raise Exception

        if isinstance(obj, Partition):
            self.partition[obj.name] = obj
        elif isinstance(obj, Variable):
            self.variable[obj.name] = obj

    def enddef(self):
        """
        End the definition phase

        Must be called before `Variable.put()` or `Variable.get()`
        """
        for p in self.partition.values():
            p._register()
        for v in self.variable.values():
            v._register()
        err = foasis.enddef()
        self._define_phase = False

