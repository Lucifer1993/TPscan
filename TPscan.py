#!/usr/bin/env python
# coding=utf-8
from gevent import monkey;monkey.patch_all()
from gevent.pool import Pool
from plugins.thinkphp_checkcode_time_sqli import thinkphp_checkcode_time_sqli_verify
from plugins.thinkphp_construct_code_exec import thinkphp_construct_code_exec_verify
from plugins.thinkphp_construct_debug_rce import thinkphp_construct_debug_rce_verify
from plugins.thinkphp_debug_index_ids_sqli import thinkphp_debug_index_ids_sqli_verify
from plugins.thinkphp_driver_display_rce import thinkphp_driver_display_rce_verify
from plugins.thinkphp_index_construct_rce import thinkphp_index_construct_rce_verify
from plugins.thinkphp_index_showid_rce import thinkphp_index_showid_rce_verify
from plugins.thinkphp_invoke_func_code_exec import thinkphp_invoke_func_code_exec_verify
from plugins.thinkphp_lite_code_exec import thinkphp_lite_code_exec_verify
from plugins.thinkphp_method_filter_code_exec import thinkphp_method_filter_code_exec_verify
from plugins.thinkphp_multi_sql_leak import thinkphp_multi_sql_leak_verify
from plugins.thinkphp_pay_orderid_sqli import thinkphp_pay_orderid_sqli_verify
from plugins.thinkphp_request_input_rce import thinkphp_request_input_rce_verify
from plugins.thinkphp_view_recent_xff_sqli import thinkphp_view_recent_xff_sqli_verify

import sys
import gevent
print('''
 ___________                    
|_   _| ___ \                   
  | | | |_/ /__  ___ __ _ _ __  
  | | |  __/ __|/ __/ _` | '_ \ 
  | | | |  \__ \ (_| (_| | | | |
  \_/ \_|  |___/\___\__,_|_| |_|          
                code by Lucifer
''')
targeturl = input("[*]Give me a target: ")
if targeturl.find('http') == -1:
    exit(1)
poclist = [
    'thinkphp_checkcode_time_sqli_verify("{0}")'.format(targeturl),
    'thinkphp_construct_code_exec_verify("{0}")'.format(targeturl),
    'thinkphp_construct_debug_rce_verify("{0}")'.format(targeturl),
    'thinkphp_debug_index_ids_sqli_verify("{0}")'.format(targeturl),
    'thinkphp_driver_display_rce_verify("{0}")'.format(targeturl),
    'thinkphp_index_construct_rce_verify("{0}")'.format(targeturl),
    'thinkphp_index_showid_rce_verify("{0}")'.format(targeturl),
    'thinkphp_invoke_func_code_exec_verify("{0}")'.format(targeturl),
    'thinkphp_lite_code_exec_verify("{0}")'.format(targeturl),
    'thinkphp_method_filter_code_exec_verify("{0}")'.format(targeturl),
    'thinkphp_multi_sql_leak_verify("{0}")'.format(targeturl),
    'thinkphp_pay_orderid_sqli_verify("{0}")'.format(targeturl),
    'thinkphp_request_input_rce_verify("{0}")'.format(targeturl),
    'thinkphp_view_recent_xff_sqli_verify("{0}")'.format(targeturl),
]

def pocexec(pocstr):
    exec(pocstr)
    gevent.sleep(0)

pool = Pool(10)
threads = [pool.spawn(pocexec, item) for item in poclist]
gevent.joinall(threads)