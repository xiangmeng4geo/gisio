from .base import CAP_STYLE, JOIN_STYLE
from .collection import GeometryCollection
from .line import Polyline
from .multiline import MultiPolyline
from .multipoint import MultiPoint
from .multipolygon import MultiPolygon
from .point import Point
from .polygon import Polygon, LinearRing


def box(minx, miny, maxx, maxy, ccw=True):
    """Returns a rectangular polygon with configurable normal vector"""
    coords = [(maxx, miny), (maxx, maxy), (minx, maxy), (minx, miny)]
    if not ccw:
        coords = coords[::-1]
    return Polygon(coords)


def shape(context):
    """Returns a new, independent geometry with coordinates *copied* from the
    context.
    """
    if hasattr(context, "__geo_interface__"):
        ob = context.__geo_interface__
    else:
        ob = context
    geom_type = ob.get("type").lower()
    if geom_type == "point":
        return Point(ob["coordinates"])
    elif geom_type == "linestring":
        return Polyline(ob["coordinates"])
    elif geom_type == "polygon":
        return Polygon(ob["coordinates"][0], ob["coordinates"][1:])
    elif geom_type == "multipoint":
        return MultiPoint(ob["coordinates"])
    elif geom_type == "multilinestring":
        return MultiPolyline(ob["coordinates"])
    elif geom_type == "multipolygon":
        return MultiPolygon(ob["coordinates"], context_type='geojson')
    elif geom_type == "geometrycollection":
        geoms = [shape(g) for g in ob.get("geometries", [])]
        return GeometryCollection(geoms)
    else:
        raise ValueError("Unknown geometry type: %s" % geom_type)


def mapping(ob):
    """Returns a GeoJSON-like mapping"""
    return ob.__geo_interface__


__all__ = [
    'box', 'shape', 'Point', 'Polyline', 'Polygon', 'MultiPoint', 'MultiPolyline', 'MultiPolygon',
    'GeometryCollection', 'mapping', 'LinearRing', 'CAP_STYLE', 'JOIN_STYLE',
]


