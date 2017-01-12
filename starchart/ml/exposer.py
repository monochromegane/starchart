#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from starchart.ml import models, jobs, versions, files

def expose(args):
    context = Context(args)

    # create model
    is_default = False
    model, _ = models.get(context)
    if not model:
        models.create(context)
        is_default = True

    # create versions
    jobs_, _ = jobs.list(context, filter='state=SUCCEEDED')
    for job in jobs_:
        timestamp = job['jobId'].split('_')[-1]
        version, _ = versions.get(context, timestamp)
        if not version:
            created, _ = versions.create(context, timestamp)
            files.dump(context, created['metadata']['version'], job, is_default)
            is_default = False

class Context(object):
    def __init__(self, args):
        self.args = args
        self.bucket_name = '{}-ml'.format(args.project_id)

        self.setup_dir, _ = os.path.split(os.path.abspath(args.package_path))
        _, self.model_name = os.path.split(self.setup_dir)

    def deployment_uri(self, version):
        return '/'.join(['gs:/', self.bucket_name, self.model_name, version, 'model'])
