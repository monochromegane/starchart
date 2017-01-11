#!/usr/bin/env python
# -*- coding: utf-8 -*-

from starchart.ml import api
from googleapiclient import errors

def get(context):
    try:
        response = api.ml().models().get(
                name='projects/{}/models/{}'.format(context.args.project_id, context.model_name)
        ).execute()
        return (response, None)
    except errors.HttpError as err:
        return (None, err)

def create(context):
    try:
        response = api.ml().models().create(
                parent='projects/{}'.format(context.args.project_id),
                body={'name': context.model_name}
        ).execute()
        return (response, None)
    except errors.HttpError as err:
        return (None, err)

