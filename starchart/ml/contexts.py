#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import datetime

class Context(object):
    def __init__(self, args):
        self.args = args
        self.timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

        self.bucket_name = '{}-ml'.format(args.project_id)
        self.setup_dir, self.package_name = os.path.split(os.path.abspath(args.package_path))
        _, self.model_name = os.path.split(self.setup_dir)
        self.job_id     = '_'.join([self.model_name, self.timestamp])
        self.train_dir  = '/'.join([self.model_name, self.timestamp])
        self.train_path = '/'.join(['gs:/', self.bucket_name, self.train_dir])

    def train_args(self):
        return [arg.replace('TRAIN_PATH', self.train_path)for arg in self.args.args]

    def deployment_uri(self, version):
        return '/'.join(['gs:/', self.bucket_name, self.model_name, version, 'model'])
