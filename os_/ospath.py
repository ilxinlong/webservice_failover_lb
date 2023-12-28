import os


class FindPath:

    def find_path(self, directory):
        work_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        if directory == 'api':
            return_path = work_path + '/api'
        elif directory == 'conf':
            return_path = work_path + '/conf'
        elif directory == 'log':
            return_path = work_path + '/log'
        else:
            return_path = work_path + '/os_'
        return return_path
