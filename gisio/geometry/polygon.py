#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

author:     meng.xiang
date:       2019-05-08
description:
"""

from shapely.geometry.polygon import LinearRing as ShpLinearRing, Polygon as ShpPolygon


class LinearRing(ShpLinearRing):
    def __init__(self, coordinates):
        """
        Parameters
        ----------
        coordinates : sequence
            A sequence of (x, y [,z]) numeric coordinate pairs or triples

        Rings are implicitly closed. There is no need to specific a final
        coordinate pair identical to the first.

        Example
        -------
        Construct a square ring.

          >>> ring = LinearRing( ((0, 0), (0, 1), (1 ,1 ), (1 , 0)) )
          >>> ring.is_closed
          True
          >>> ring.length
          4.0
        """
        ShpLinearRing.__init__(self, coordinates)


class Polygon(ShpPolygon):
    """
    A two-dimensional figure bounded by a linear ring

    A polygon has a non-zero area. It may have one or more negative-space
    "holes" which are also bounded by linear rings. If any rings cross each
    other, the feature is invalid and operations on it may fail.

    Attributes
    ----------
    exterior : LinearRing
        The ring which bounds the positive space of the polygon.
    interiors : sequence
        A sequence of rings which bound all existing holes.
    """

    def __init__(self, shell=None, holes=None):
        ShpPolygon.__init__(self, shell, holes)
