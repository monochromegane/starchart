#!/usr/bin/env python
# -*- coding: utf-8 -*-

from starchart.ml import contexts, jobs

def state(args):
    context = contexts.Context(args)

    jobs_, _ = jobs.list(context, fields='jobs(jobId,state)')
    for job in jobs_:
        if context.model_name in job['jobId']:
            print('jobId: {} ({})'.format(job['jobId'], job['state']))
