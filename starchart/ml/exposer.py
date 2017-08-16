#!/usr/bin/env python
# -*- coding: utf-8 -*-

from starchart.ml import contexts, models, jobs, versions, files

def expose(args):
    context = contexts.Context(args)

    # create model
    is_default = False
    model, _ = models.get(context)
    if not model:
        print('Creating model: {}...'.format(context.model_name))
        _, err = models.create(context)
        if err is not None:
            return err
        is_default = True

    # create versions
    jobs_, err = jobs.list(context, filter='state=SUCCEEDED')
    if err is not None:
        return err
    for job in jobs_:
        timestamp = job['jobId'].split('_')[-1]
        version, _ = versions.get(context, timestamp)
        if not version:
            print('Creating version: projects/{}/models/{}/versions/{}...'.format(context.project_id, context.model_name, 'v' + timestamp))
            created, err = versions.create(context, timestamp)
            if err is not None:
                print(err)
                continue
            files.dump(context, created['metadata']['version'], job, is_default)
            is_default = False
