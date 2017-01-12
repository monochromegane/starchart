#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from starchart.ml import contexts, versions

def apply(args):
    context = contexts.Context(args)
    file_name = '{}.json'.format(context.model_name)
    with open(file_name) as f:
        content = json.load(f)
        for name in [version['version']['name'] for version in content['versions'] if version['version']['isDefault']]:
            versions.set_default(name)
