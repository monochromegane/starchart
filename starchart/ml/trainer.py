#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import tempfile
import sys
from starchart.ml import uploads, jobs
from datetime import datetime
from contextlib import contextmanager

_DEFAULT_SETUP_FILE = """\
from setuptools import setup
if __name__ == '__main__':
    setup(name='{package_name}', packages=['{package_name}'])
"""

def train(args):
    context = Context(args)

    # setup train program.
    with _temporaryDirectory() as temp_dir:
        dest_dir = os.path.join(temp_dir, 'dest')
        shutil.copytree(context.setup_dir, dest_dir)
        package_paths = _run_setup(dest_dir, context.package_name)

        # upload train program packages to cloud storage.
        uploaded_paths = uploads.upload_files(package_paths, context.bucket_name, context.train_dir)

    # submit train job.
    jobs.submit(uploaded_paths, context)

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

def _run_setup(setup_dir, package_name):
    setup_path = os.path.join(setup_dir, 'setup.py')
    if not os.path.isfile(setup_path):
        with open(setup_path, 'w') as setup_file:
            setup_contents = _DEFAULT_SETUP_FILE.format(package_name=package_name)
            setup_file.write(setup_contents)

    args = [sys.executable, 'setup.py', 'sdist', '--dist-dir=dist']
    subprocess.call(args, cwd=setup_dir)

    dist_dir = os.path.join(setup_dir, 'dist')
    local_paths = [os.path.join(dist_dir, rel_file)
                   for rel_file in os.listdir(dist_dir)]
    return local_paths

@contextmanager
def _temporaryDirectory():
    try:
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir)
