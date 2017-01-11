#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from starchart.ml import models

def expose(args):
    context = Context(args)

    # create model
    model, _ = models.get(context)
    if not model:
        models.create(context)

class Context:
    def __init__(self, args):
        self.args = args
        self.bucket_name = '{}-ml'.format(args.project_id)

        self.setup_dir, _ = os.path.split(os.path.abspath(args.package_path))
        _, self.model_name = os.path.split(self.setup_dir)

    def deployment_uri(self, version):
        return '/'.join(['gs:/', self.bucket_name, self.model_name, version, 'model'])
