from gisio.geometry import MultiPolygon, Polygon

if __name__ == '__main__':
    ob = MultiPolygon([
        (
            ((0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0)),
            [((0.1, 0.1), (0.1, 0.2), (0.2, 0.2), (0.2, 0.1))]
        )
    ])
    len(ob.geoms)
    assert type(ob.geoms[0]) == Polygon
