# -*- coding: utf-8 -*-
import sys

example_settings = {
  '-p': [9400, 'Server port', lambda x: int(x)],
}

def parse(settings):
    options = {k:settings[k][0] for k in settings}
    for k, v in enumerate(sys.argv):
        if v in settings and len(sys.argv) > k+1:
            options[v] = sys.argv[k+1]
            if settings[v][2]: options[v] = settings[v][2](options[v])
    return options
