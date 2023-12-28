# -*- coding: utf-8 -*-

"""
	Homepage: https://github.com/ucloud/ucloud-sdk-python3
	Examples: https://github.com/ucloud/ucloud-sdk-python3/tree/master/examples
	Documentation: https://ucloud.github.io/ucloud-sdk-python3/
"""

from ucloud.core import exc
from ucloud.client import Client


def main():
    client = Client({
        "region": "cn-sh2",
        "project_id": "org-rwvczq",
        "public_key": "Befp8gE5fIm4ByecJ6va1qdQhErExmKhiKpbwTjm",
        "private_key": "nI056581IPNaXPlEBMQD94l_802MWkPkCRM5yxbWqzQY0EGTpApHZv2khV6fkkvT",
    })

    try:
        resp = client.ulb().update_backend_attribute({
            "ULBId": "ulb-bgrxjzyl",
            "BackendId": "backend-hjz2421u",
            "Enabled": 0
        })
    except exc.UCloudException as e:
        print(e)
    else:
        print(resp)


if __name__ == '__main__':
    main()
