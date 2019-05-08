#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

author:     meng.xiang
date:       2019-05-08
description:
"""
from shapely.geometry import MultiPoint as ShpMultiPoint

__all__ = ['MultiPoint']


class MultiPoint(ShpMultiPoint):
    """A collection of one or more points

    A MultiPoint has zero area and zero length.

    Attributes
    ----------
    geoms : sequence
        A sequence of Points
    """

    def __init__(self, points=None):
        """
        Parameters
        ----------
        points : sequence
            A sequence of (x, y [,z]) numeric coordinate pairs or triples or a
            sequence of objects that implement the numpy array interface,
            including instaces of Point.

        Example
        -------
        Construct a 2 point collection

          >>> ob = MultiPoint([[0.0, 0.0], [1.0, 2.0]])
          >>> len(ob.geoms)
          2
          >>> type(ob.geoms[0]) == Point
          True
        """
        MultiPoint.__init__(self, points)
