# -*- coding: utf-8 -*-


import sys
from os_.osconf import OsConf
from ucloud.core import exc
from ucloud.client import Client


def get_conf(conf_file, conf_tag):
    my_conf = OsConf()
    conf = my_conf.get_conf(conf_file, conf_tag)
    return conf


class Ulb:

    def __init__(self, env):
        if env == 'PRO':
            self.file = 'Ucloud_PRO.conf'
        elif env == 'UAT':
            self.file = 'Ucloud_UAT.conf'
        else:
            print('env参数不正确，应为{PRO|UAT}')
            sys.exit(9)
        client = get_conf(self.file, 'CLIENT')
        self.region = client.my_region
        self.project_id = client.my_project_id
        self.public_key = client.my_public_key
        self.private_key = client.my_private_key

    def describe_vserver(self, resource_name):
        vserver = get_conf(self.file, resource_name)
        client = Client({
            "region": self.region,
            "project_id": self.project_id,
            "public_key": self.public_key,
            "private_key": self.private_key,
        })
        try:
            resp = client.ulb().describe_vserver({
                "ULBId": vserver.my_ulbid,
                "VServerId": vserver.my_vserverid
            })
        except exc.UCloudException as e:
            print(e)
        else:
            dataset = resp.get('DataSet')
            backendset = dataset[0].get('BackendSet')
            return backendset

    def UpdateBackendAttribute(self, resource_name, backend_id, operate):
        if operate == 'in':
            enabled = 1
        elif operate == 'out':
            enabled = 0
        else:
            print('operate参数不正确，应为{in|out}')
            sys.exit(9)
        vserver = get_conf(self.file, resource_name)
        client = Client({
            "region": self.region,
            "project_id": self.project_id,
            "public_key": self.public_key,
            "private_key": self.private_key,
        })
        try:
            client.ulb().update_backend_attribute({
                "ULBId": vserver.my_ulbid,
                "BackendId": backend_id,
                "Enabled": enabled
            })
        except exc.UCloudException as e:
            print(e)
