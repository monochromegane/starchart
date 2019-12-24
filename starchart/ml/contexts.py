#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import datetime

class Context(object):
    def __init__(self, args):
        self.args = args
        self.project_id = os.environ.get('GCP_PROJECT_ID') or args.project_id or ''
        self.model_name = args.model_name
        self.timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

        self.bucket_name = '{}-ml'.format(self.project_id)
        self.setup_dir = os.path.abspath(os.path.join(args.train_program_base, args.model_name))
        if 'module_name' in args:
            self.package_name = args.module_name.split('.')[0]
            self.region       = os.environ.get('GCP_REGION') or args.region or ''

        self.job_id     = '_'.join([self.model_name, self.timestamp])
        self.train_dir  = '/'.join([self.model_name, self.timestamp])
        self.train_path = '/'.join(['gs:/', self.bucket_name, self.train_dir])
        if 'scale_tier' in args:
            self.scale_tier = args.scale_tier
        else:
            self.scale_tier = 'BASIC'

        if 'runtime_version' in args:
            self.runtime_version = args.runtime_version
        else:
            self.runtime_version = '1.0'

        if 'python_version' in args:
            self.python_version = args.python_version
        else:
            self.python_version = '2.7'

        if 'framework' in args:
            self.framework = args.framework
        else:
            self.framework = None

    def train_args(self):
        return [arg.replace('TRAIN_PATH', self.train_path)for arg in self.args.args]

    def deployment_uri(self, version):
        return '/'.join(['gs:/', self.bucket_name, self.model_name, version, 'model'])
