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

class Partition(object):
    def __init__(self, name, global_size = 0, partition = [0]):
        self.name = name
        self.global_size = global_size
        self.partition = partition

    def _register(self):
        self.id, err = foasis.def_partition(self.partition, self.global_size, self.name)

        if err != foasis.ok:
            raise Exception()

    def local_size(self):
        return self.partition[2]

class Serial(Partition):
    def __init__(self, name, global_size):
        """
        Serial partition (entire grid on one MPI rank)

        Must call `Oasis.register()` on the partition for Oasis to know about it

        :param str name: Partition name
        :param int global_size: Total number of grid points
        """
        partition = [0, 0, global_size]
        super(Serial, self).__init__(name, global_size, partition)

class Apple(Partition):
    def __init__(self, name, global_size, local_size, offset):
        """
        Apple partition (each MPI rank has a continuous memory slice)

        Must call `Oasis.register()` on the partition for Oasis to know about it

        :param str name: Partition name
        :param int global_size: Total number of grid points
        :param int local_size: Local number of grid points for this rank
        :param int offset: Starting offset for this rank's data
        """
        partition = [1, offset, local_size]
        super(Apple, self).__init__(name, global_size, partition)
