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
from oasis.oasis import Oasis
import oasis.partition as partition
from oasis.variable import Variable
from oasis.f import types, direction

import numpy as np

with Oasis('test') as o:
    shape = (5,5)

    part = partition.Serial('default', shape[0]*shape[1])
    o.register(part)

    var = Variable('foo', part, shape, types.real, direction.out)
    o.register(var)
    o.enddef()

    data = np.zeros(shape, order='F')
    var.put(0, data)

