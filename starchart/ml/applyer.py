#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
from starchart.ml import versions

def apply(args):
    context = Context(args)
    file_name = '{}.json'.format(context.model_name)
    with open(file_name) as f:
        content = json.load(f)
        for name in [version['version']['name'] for version in content['versions'] if version['version']['isDefault']]:
            versions.set_default(name)

class Context(object):
    def __init__(self, args):
        self.args = args

        self.setup_dir, _ = os.path.split(os.path.abspath(args.package_path))
        _, self.model_name = os.path.split(self.setup_dir)
