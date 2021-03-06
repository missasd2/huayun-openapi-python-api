#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from chinac_way_v3.core.profile.profile import Profile
from chinac_way_v3.core.client import Client
from chinac_way_v3.ecs.v10.describe_instances import DescribeInstances

if __name__ == '__main__':
    profile = Profile('region tag', 'your access key', 'your access secret')
    client = Client(profile)
    request = DescribeInstances()
    request.set_method('GET')
    response = client.get_response(request)
    print(response)