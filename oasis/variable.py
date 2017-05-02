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

from .f import oasis as foasis
from .f import types
import numpy as np

class Variable(object):
    """
    Oasis' view of a model variable

    Should be registered with the Oasis singleton before calling Oasis.enddef()
    """

    def __init__(self, name, partition, shape, type, inout):
        """
        Create a variable

        Must call `Oasis.register()` on the variable for Oasis to know about it
        """
        self.name = name
        self.partition = partition
        self.shape = shape
        self.type = type
        self.inout = inout
        self.id = None

    def _register(self):
        nodims = [len(self.shape), 1]
        bounds = np.array([[1,x] for x in self.shape]).flatten()

        self.id, err = foasis.def_var(self.name, self.partition.id, 
                nodims, self.inout, bounds, self.type)

        if err != foasis.ok:
            raise Exception()

        if self.id < 0:
            raise Exception("Variable <%s> not present in namcouple"%self.name)

    def put(self, date, array):
        """
        Send data to the coupler. If there is no coupling at this date
        according to the namcouple file this function will be a no-op.

        :param int date: Date at the start of the timestep, in seconds since the model start
        :param numpy.Array array: Data array to send (1 or 2D)
        """
        if (len(self.shape) == 1 and self.type == types.real):
            func = foasis.put_14
        elif (len(self.shape) == 1 and self.type == types.double):
            func = foasis.put_18
        elif (len(self.shape) == 2 and self.type == types.real):
            func = foasis.put_24
        elif (len(self.shape) == 2 and self.type == types.double):
            func = foasis.put_28
        else:
            raise Exception

        info = func(var_id=self.id, date=date, fld1=array)
        return info

    def get(self, date, array):
        """
        Get data from the coupler. If there is no coupling at this date
        according to the namcouple file this function will be a no-op.

        :param int date: Date at the start of the timestep, in seconds since the model start
        :param numpy.Array array: Data array to send (1 or 2D)
        """
        if (len(self.shape) == 1 and self.type == types.real):
            func = foasis.get_14
        elif (len(self.shape) == 1 and self.type == types.double):
            func = foasis.get_18
        elif (len(self.shape) == 2 and self.type == types.real):
            func = foasis.get_24
        elif (len(self.shape) == 2 and self.type == types.double):
            func = foasis.get_28
        else:
            raise Exception

        info = func(var_id=self.id, date=date, fld1=array)
        return info
