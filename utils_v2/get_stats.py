#!/usr/bin/env python3

# Copyright 2020 Lam Nguyen

import sys
import json
import numpy as np

def get_stats(data, var="unknown", depth=0):

    stats = {}
    stats['var'] = var
    stats['size'] = str(sys.getsizeof(data)/1024) + " KB"
    stats['type'] = str(type(data))

    if type(data) is list:
        stats['len'] = str(len(data))
        stats['1st item'] = get_stats(data[0], var=var+'[0]', depth=depth+1)

    if type(data) is dict:
        stats['key_count'] = str(len(data.keys()))
        stats['1st item'] = get_stats(data[list(data.keys())[0]], var=var+'[' + list(data.keys())[0] +']', depth=depth+1)

    if type(data) is np.ndarray:
        stats['shape'] = str(data.shape)
        stats['dtype'] = str(data.dtype)

    if type(data) is np.lib.npyio.NpzFile:
        stats['files'] = str(data.files)
        for f in data.files:
            stats[var+'['+f+']'] = get_stats(data[f], var=var+'['+f+']', depth=depth+1)

    return stats
