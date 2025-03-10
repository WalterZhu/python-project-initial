from copy import deepcopy

def deep_merge_dict(x: dict, y: dict) -> dict:
    """
    深合并字典
    :param x:
    :param y:
    :return:
    """
    z = deepcopy(x)
    z.update(y)
    for k, v in z.items():
        if k in x and k in y:
            if isinstance(x[k], dict) and isinstance(y[k], dict):
                z[k] = deep_merge_dict(x[k], y[k])
    return z

def str_to_bool(s, default):
    if s == 'True':
        return True
    elif s == 'False':
        return False
    else:
        return default
