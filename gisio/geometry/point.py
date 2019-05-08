#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
new point geometry
author:     meng.xiang
date:       2019-05-08
description:
"""
from shapely.geometry.point import Point as ShpPoint


class Point(ShpPoint):
    def __init__(self, *args):
        ShpPoint.__init__(self, *args)


if __name__ == '__main__':
    p = Point(2, 3)
    print(p.x)
