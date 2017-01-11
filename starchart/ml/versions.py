#!/usr/bin/env python

from starchart.ml import api
from googleapiclient import errors

def get(context, version):
    try:
        response = api.ml().models().versions().get(
                name='projects/{}/models/{}/versions/{}'.format(context.args.project_id, context.model_name, 'v' + version)
        ).execute()
        return (response, None)
    except errors.HttpError as err:
        return (None, err)


def create(context, version):
    try:
        response = api.ml().models().versions().create(
                parent='projects/{}/models/{}'.format(context.args.project_id, context.model_name),
                body={
                    'name': 'v' + version,
                    'deploymentUri': context.deployment_uri(version)
                    }
        ).execute()
        return (response, None)
    except errors.HttpError as err:
        return (None, err)
