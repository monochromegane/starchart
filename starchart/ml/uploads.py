#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from google.cloud import storage

def upload_files(upload_files, bucket_name, prefix):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)

    dests = []
    for local_path in upload_files:
        uploaded_path = '/'.join([prefix, 'packages', os.path.basename(local_path)])
        blob = bucket.blob(uploaded_path)
        blob.upload_from_filename(filename=local_path)
        dests.append('/'.join(['gs:/', bucket_name, uploaded_path]))
    return dests
