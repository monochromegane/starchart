#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import tempfile
import sys
from starchart.ml import contexts, uploads, jobs
from contextlib import contextmanager

_DEFAULT_SETUP_FILE = """\
from setuptools import setup
if __name__ == '__main__':
    setup(name='{package_name}', packages=['{package_name}'])
"""

def train(args):
    context = contexts.Context(args)

    # setup train program.
    with _temporaryDirectory() as temp_dir:
        print('Setup train program...')
        dest_dir = os.path.join(temp_dir, 'dest')
        shutil.copytree(context.setup_dir, dest_dir)
        package_paths = _run_setup(dest_dir, context.package_name)

        # upload train program packages to cloud storage.
        print('Uploading train program...')
        uploaded_paths = uploads.upload_files(package_paths, context.bucket_name, context.train_dir)

    # submit train job.
    print('Submitting train job: {}...'.format(context.job_id))
    _, err = jobs.submit(uploaded_paths, context)
    return err

def _run_setup(setup_dir, package_name):
    setup_path = os.path.join(setup_dir, 'setup.py')
    if not os.path.isfile(setup_path):
        with open(setup_path, 'w') as setup_file:
            setup_contents = _DEFAULT_SETUP_FILE.format(package_name=package_name)
            setup_file.write(setup_contents)

    args = [sys.executable, 'setup.py', 'sdist', '--dist-dir=dist']
    subprocess.run(args, cwd=setup_dir, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

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
