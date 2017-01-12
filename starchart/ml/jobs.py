#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from starchart.ml import api
from googleapiclient import errors

def submit(packages, context):
    args = context.args
    body = {
        'jobId': context.job_id,
        'trainingInput': {
            'packageUris':  packages,
            'pythonModule': args.module_name,
            'region':       args.region,
            'args':         context.train_args()
        }
    }
    try:
        response = api.ml().jobs().create(
            parent='projects/{}'.format(context.project_id),
            body=body
        ).execute()
        return (response, None)
    except errors.HttpError as err:
        return (None, err)

def list(context, **kwargs):
    try:
        response = api.ml().jobs().list(
            parent='projects/{}'.format(context.project_id),
            **kwargs
        ).execute()
        pattern = re.compile(r'%s_\d{14}' % context.model_name)
        return ([job for job in response['jobs'] if re.search(pattern, job['jobId'])], None)
    except errors.HttpError as err:
        return (None, err)
