# -*- coding: utf-8 -*-

import sys
import time
from deal.ulb import Ulb


def main(argv):

    if len(argv) == 5:
        env = argv[1]
        lb_name = argv[2]
        backend_ip = argv[3]
        operate = argv[4]
        my_ulb = Ulb(env)
        backend_id = ''
        break_code = 0
        print('\033[32m*************** 切换负载-START ***************\033[0m')
        if operate == 'in':
            for j in range(6):
                backend_set = my_ulb.describe_vserver(lb_name)
                for i in range(len(backend_set)):
                    if backend_set[i].get('PrivateIP') == backend_ip:
                        backend_id = backend_set[i].get('BackendId')
                        if backend_set[i].get('Status') == 1:
                            print(backend_ip + '应用不正常')
                            break
                        else:
                            if backend_set[i].get('Enabled') == 1:
                                print('负载' + lb_name + '下节点' + backend_ip + '已启用，不需要切负载')
                                print('\033[32m*************** 切换负载-END ***************\033[0m')
                                sys.exit(0)
                            else:
                                break_code = 1
                                print('应用正常，等待拉入负载')
                                break
                if backend_id == '':
                    print("参数不正确，" + lb_name + "下没有节点: " + backend_ip)
                    sys.exit(9)
                if break_code == 1:
                    break
                print('等待10秒')
                time.sleep(10)
                continue
            my_ulb.UpdateBackendAttribute(lb_name, backend_id, operate)
            print(backend_ip + '已拉入负载，开始验证健康检查和节点模式')
            review_code = 0
            node_health = ''
            node_status = ''
            for i in range(6):
                review_backend_set = my_ulb.describe_vserver(lb_name)
                for j in range(len(review_backend_set)):
                    if review_backend_set[j].get('PrivateIP') == backend_ip:
                        if review_backend_set[j].get('Status') == 0 and review_backend_set[j].get('Enabled') == 1:
                            review_code = 1
                        node_health = str(review_backend_set[j].get('Status'))
                        node_status = str(review_backend_set[j].get('Enabled'))
                if review_code == 1:
                    print('验证健康检查和节点模式完成，结果正常')
                    print('\033[32m*************** 切换负载-END ***************\033[0m')
                    sys.exit(0)
                print('等待10秒')
                time.sleep(10)
            print('验证健康检查和节点模式超时，结果异常,node_health:' + node_health + 'node_status' + node_status)
            sys.exit(9)
        elif operate == 'out':
            for j in range(10):
                backend_set = my_ulb.describe_vserver(lb_name)
                for i in range(len(backend_set)):
                    if backend_set[i].get('PrivateIP') == backend_ip:
                        backend_id = backend_set[i].get('BackendId')
                        if backend_set[i].get('Status') == 1:
                            print(backend_ip + '应用不正常')
                            break
                        else:
                            if backend_set[i].get('Enabled') == 0:
                                print('负载' + lb_name + '下节点' + backend_ip + '未启用，不需要切负载')
                                print('\033[32m*************** 切换负载-END ***************\033[0m')
                                sys.exit(0)
                            else:
                                break_code = 1
                                print('应用正常，等待拉出负载')
                                break
                if backend_id == '':
                    print("参数不正确，" + lb_name + "下没有节点: " + backend_ip)
                    sys.exit(9)
                if break_code == 1:
                    break
                print('等待3秒')
                time.sleep(3)
                continue
            my_ulb.UpdateBackendAttribute(lb_name, backend_id, operate)
            print(backend_ip + '已拉出负载，开始验证健康检查和节点模式')
            review_code = 0
            node_health = ''
            node_status = ''
            for i in range(10):
                review_backend_set = my_ulb.describe_vserver(lb_name)
                for j in range(len(review_backend_set)):
                    if review_backend_set[j].get('PrivateIP') == backend_ip:
                        if review_backend_set[j].get('Status') == 0 and review_backend_set[j].get('Enabled') == 0:
                            review_code = 1
                        node_health = str(review_backend_set[j].get('Status'))
                        node_status = str(review_backend_set[j].get('Enabled'))
                if review_code == 1:
                    print('验证健康检查和节点模式完成，结果正常')
                    print('\033[32m*************** 切换负载-END ***************\033[0m')
                    sys.exit(0)
                print('等待3秒')
                time.sleep(3)
            print('验证健康检查和节点模式超时，结果异常,node_health:' + node_health + 'node_status' + node_status)
            sys.exit(9)
    else:
        print("参数应为4个")
        sys.exit(9)


if __name__ == '__main__':
    main(sys.argv)
