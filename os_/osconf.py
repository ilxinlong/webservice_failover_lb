import configparser
from os_.ospath import FindPath


class OsConf:

    def __init__(self):
        self.my_region = ''
        self.my_project_id = ''
        self.my_public_key = ''
        self.my_private_key = ''
        self.my_ulbid = ''
        self.my_vserverid = ''

    def get_conf(self, conf_file, conf_tag):
        my_path = FindPath()
        conf_floder = my_path.find_path('conf')
        conf_path = conf_floder + '/' + conf_file
        my_conf = configparser.ConfigParser()
        my_conf.read(conf_path)
        if conf_tag == 'CLIENT':
            self.my_region = my_conf.get(conf_tag, 'REGION')
            self.my_project_id = my_conf.get(conf_tag, 'PROJECT_ID')
            self.my_public_key = my_conf.get(conf_tag, 'PUBLIC_KEY')
            self.my_private_key = my_conf.get(conf_tag, 'PRIVATE_KEY')
            return self
        else:
            self.my_ulbid = my_conf.get(conf_tag, 'ULBId')
            self.my_vserverid = my_conf.get(conf_tag, 'VSERVERId')
            return self
