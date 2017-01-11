#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
            parent='projects/{}'.format(args.project_id),
            body=body
        ).execute()
        return (response, None)
    except errors.HttpError as err:
        return (None, err)
