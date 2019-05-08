#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

author:     meng.xiang
date:       2019-05-08
description:
"""
from shapely.geometry import MultiLineString as ShpMultiPolyline

__all__ = ['MultiPolyline']


class MultiPolyline(ShpMultiPolyline):
    """
    A collection of one or more line strings

    A MultiLineString has non-zero length and zero area.

    Attributes
    ----------
    geoms : sequence
        A sequence of LineStrings
    """

    def __init__(self, lines=None):
        """
        Parameters
        ----------
        lines : sequence
            A sequence of line-like coordinate sequences or objects that
            provide the numpy array interface, including instances of
            LineString.

        Example
        -------
        Construct a collection containing one line string.

          >>> lines = MultiPolyline( [[[0.0, 0.0], [1.0, 2.0]]] )
        """
        ShpMultiPolyline.__init__(self, lines)
