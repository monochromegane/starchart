#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

def dump(context, created_version, job, is_default):
    file_name = '{}.json'.format(context.model_name)
    created_version.update({'job': job, 'isDefault': is_default})
    version = {'version': created_version}

    if not os.path.isfile(file_name):
        content = {
                'model': context.model_name,
                'versions': [version],
                }
        with open(file_name, mode='w') as f:
            json.dump(content, f, indent=2)
    else:
        with open(file_name) as f:
            content = json.load(f)
            content['versions'].append(version)
        with open(file_name, mode='w') as f:
            json.dump(content, f, indent=2)
