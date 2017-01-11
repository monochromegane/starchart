#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oauth2client.client import GoogleCredentials
from googleapiclient import discovery

def ml():
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('ml', 'v1beta1', credentials=credentials).projects()
