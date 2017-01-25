#!/usr/bin/env python
# -*- coding: utf-8 -*-

from starchart.ml import contexts, models, jobs, versions, files

def expose(args):
    context = contexts.Context(args)

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
            if created is not None:
                files.dump(context, created['metadata']['version'], job, is_default)
                is_default = False
