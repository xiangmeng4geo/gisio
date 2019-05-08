#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

author:     meng.xiang
date:       2019-05-08
description:
"""
from shapely.geometry import GeometryCollection as ShpGeometryCollection


class GeometryCollection(ShpGeometryCollection):
    """A heterogenous collection of geometries

    Attributes
    ----------
    geoms : sequence
        A sequence of Shapely geometry instances
    """

    def __init__(self, geoms=None):
        """
        Parameters
        ----------
        geoms : list
            A list of shapely geometry instances, which may be heterogenous.

        Example
        -------
        Create a GeometryCollection with a Point and a LineString

          >>> p = Point(51, -1)
          >>> l = LineString([(52, -1), (49, 2)])
          >>> gc = GeometryCollection([p, l])
        """
        ShpGeometryCollection.__init__(self, geoms)
