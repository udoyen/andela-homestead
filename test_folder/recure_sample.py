

def replicate_iter(times, data):
    if isinstance(times, int) and (isinstance(data, str) or isinstance(data, int)):
        if not times <= 0:
            for i in range(0, times):
                return [data] * times
        else:
            return []
    else:
        raise ValueError()


def replicate_recur(times, data):
    if isinstance(times, int) and (isinstance(data, str) or isinstance(data, int)):
        if not times <= 0:
            if times == 1:
                return [data]
            else:
                replicate_recur(times - 1, data)
                return [data] * times
        else:
            return []
    else:
        raise ValueError()


print(replicate_iter(-1, []))
