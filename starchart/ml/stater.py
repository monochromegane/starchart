#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from starchart.ml import jobs

def state(args):
    context = Context(args)

    jobs_, _ = jobs.list(context, fields='jobs(jobId,state)')
    for job in jobs_:
        if context.model_name in job['jobId']:
            print('jobId: {} ({})'.format(job['jobId'], job['state']))

class Context(object):
    def __init__(self, args):
        self.args = args

        self.setup_dir, _ = os.path.split(os.path.abspath(args.package_path))
        _, self.model_name = os.path.split(self.setup_dir)
