# -*- coding: utf-8 -*-
import os
import subprocess

class AutoAdb():
    def __init__(self):
        
        self.adb_path=None
        
        try:
            adb_path = 'adb'
            subprocess.Popen([adb_path], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            self.adb_path = adb_path
        except OSError:
            print('请安装 ADB 及驱动并配置环境变量')
            exit(1)
        
        if self.adb_path:
            self.test_device()

    def test_device(self):
        print('检查设备是否连接...')
        command_list = [self.adb_path, 'devices']
        process = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.communicate()
        if output[0].decode('utf8') == 'List of devices attached\n\n':
            print('未找到设备')
            print('adb 输出:')
            for each in output:
                print(each.decode('utf8'))
            exit(1)
        print('设备已连接')
        print('adb 输出:')
        for each in output:
            print(each.decode('utf8'))
        
        print("---hello--欢迎参与本次workshop---by mixlab----")
        print()
    
    def run(self, command=""):
        print(command)
        command = '{} {}'.format(self.adb_path, command)
        process = os.popen(command)
        output = process.read()
        return output

if __name__ == '__main__':
    try:
        adb=AutoAdb()
    except KeyboardInterrupt:
        print("---886----")
        exit(0)
