#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

author:     meng.xiang
date:       2019-05-08
description:
"""
from shapely.geometry.linestring import LineString


class Polyline(LineString):
    def __init__(self, coordinates=None):
        """
        Parameters
        ----------
        coordinates : sequence
            A sequence of (x, y [,z]) numeric coordinate pairs or triples or
            an object that provides the numpy array interface, including
            another instance of LineString.

        Example
        -------
        Create a line with two segments

          >>> a = Polyline([[0, 0], [1, 0], [1, 1]])
          >>> a.length
          2.0
        """
        LineString.__init__(self, coordinates)
