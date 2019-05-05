import time
from arcgis.geometry import Point as arcPoint
from shapely.geometry import Point as shpPoint
from gisio.geometry import Point as gisPoint


def timeit(call_time):
    # call_time = 5000

    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            cost_time_list = []
            c = 0
            while True:
                c += 1
                if c > call_time:
                    break
                start_time = time.time()
                func(*args, **kwargs)
                end_time = time.time()
                cost_time_list.append(end_time - start_time)
            print("%s call %s time ,max cost (%02f ms),avg cost (%02f ms)" % (
                func.__name__, call_time, max(cost_time_list) * 1000, sum(cost_time_list) * 1000 / len(cost_time_list)))

        return inner_wrapper

    return wrapper


point_call_time = 100000


@timeit(call_time=point_call_time)
def arcgis_api_point():
    point = arcPoint({"x": 0.01, "y": 0.01})
    point.buffer()


@timeit(call_time=point_call_time)
def shapely_point():
    point = shpPoint(0.01, 0.01)


@timeit(call_time=point_call_time)
def gisio_point():
    point = gisPoint(0.01, 0.01)


if __name__ == '__main__':
    arcgis_api_point()
    shapely_point()
    gisio_point()
