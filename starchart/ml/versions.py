#!/usr/bin/env python

from starchart.ml import api
from googleapiclient import errors

def get(context, version):
    try:
        response = api.ml().models().versions().get(
                name='projects/{}/models/{}/versions/{}'.format(context.project_id, context.model_name, 'v' + version)
        ).execute()
        return (response, None)
    except errors.HttpError as err:
        return (None, err)


def create(context, version):
    try:
        body = {
                    'name': 'v' + version,
                    'deploymentUri': context.deployment_uri(version),
                    'pythonVersion': context.python_version,
                    'runtimeVersion': context.runtime_version
                }
        if context.framework is not None:
            body['framework'] = context.framework

        response = api.ml().models().versions().create(
                parent='projects/{}/models/{}'.format(context.project_id, context.model_name),
                body=body
        ).execute()
        return (response, None)
    except errors.HttpError as err:
        return (None, err)

def set_default(name):
    try:
        response = api.ml().models().versions().setDefault(name=name, body={}).execute()
        return (response, None)
    except errors.HttpError as err:
        return (None, err)

