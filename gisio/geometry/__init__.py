from shapely.geometry.base import CAP_STYLE, JOIN_STYLE
from shapely.geometry.geo import box, shape, asShape, mapping
from shapely.geometry.point import Point as shpPoint, asPoint
from shapely.geometry.linestring import LineString, asLineString
from shapely.geometry.polygon import Polygon, asPolygon, LinearRing, asLinearRing
from shapely.geometry.multipoint import MultiPoint, asMultiPoint
from shapely.geometry.multilinestring import MultiLineString, asMultiLineString
from shapely.geometry.multipolygon import MultiPolygon, asMultiPolygon
from shapely.geometry.collection import GeometryCollection

import numpy as np


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coor = np.array([x, y])
        pass


__all__ = [
    'box', 'shape', 'asShape', 'Point', 'asPoint', 'LineString',
    'asLineString', 'Polygon', 'asPolygon', 'MultiPoint', 'asMultiPoint',
    'MultiLineString', 'asMultiLineString', 'MultiPolygon', 'asMultiPolygon',
    'GeometryCollection', 'mapping', 'LinearRing', 'asLinearRing',
    'CAP_STYLE', 'JOIN_STYLE',
]
