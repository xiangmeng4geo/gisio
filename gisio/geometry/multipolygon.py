#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

author:     meng.xiang
date:       2019-05-08
description:
"""
from shapely.geometry import MultiPolygon as ShpMultiPolygon

__all__ = ['MultiPolygon']


class MultiPolygon(ShpMultiPolygon):
    """A collection of one or more polygons

    If component polygons overlap the collection is `invalid` and some
    operations on it may fail.

    Attributes
    ----------
    geoms : sequence
        A sequence of `Polygon` instances
    """

    def __init__(self, polygons=None, context_type='polygons'):
        """
        Parameters
        ----------
        polygons : sequence
            A sequence of (shell, holes) tuples where shell is the sequence
            representation of a linear ring (see linearring.py) and holes is
            a sequence of such linear rings

        Example
        -------
        Construct a collection from a sequence of coordinate tuples

          >>> ob = MultiPolygon( [
          ...     (
          ...     ((0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0)),
          ...     [((0.1,0.1), (0.1,0.2), (0.2,0.2), (0.2,0.1))]
          ...     )
          ... ] )
          >>> len(ob.geoms)
          1
          >>> type(ob.geoms[0]) == Polygon
          True
        """
        MultiPolygon.__init__(self, polygons, context_type)
