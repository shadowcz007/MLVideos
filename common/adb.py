# -*- coding: utf-8 -*-
import os
import subprocess
from PIL import Image

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

    #点击
    def tap(self,x,y):
        cmd = 'shell input tap {x} {y}'.format(
            x=x,
            y=y
        )
        self.run(cmd)
        return
    
    #滑动
    def swipe(self,x1,y1,x2,y2):
        cmd = 'shell input swipe {x1} {y1} {x2} {y2} {duration}'.format(
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
            duration=200
        )
        self.run(cmd)
        return

    #输入文字
    def input_text(self,text=""):
        cmd = 'shell am broadcast -a ADB_INPUT_TEXT --es msg {text}'.format(text=text)
        self.run(cmd)
        return
    
    #后退、返回
    def back(self):
        self.run("shell input keyevent 4")
        return

    #手机截屏
    def screenshot(self,save_path="./autojump.jpg"):
        self.run('shell screencap -p /sdcard/autojump.jpg')
        self.run('pull /sdcard/autojump.jpg .')
        
        image=Image.open(save_path)
        image=image.convert('RGB')
        image.save(save_path)

        return 

    #拷贝至手机剪切板
    def copy_to_phone_clipboard(self,text=""):
        cmd='shell am broadcast -a clipper.set -e text "{text}"'.format(text=text)
        self.run(cmd)
        return

    #从手机剪切板粘贴文本出来
    def paste_from_phone_clipboard(self):
        cmd='shell am broadcast -a clipper.get'
        res=self.run(cmd)
        return res
        

if __name__ == '__main__':
    try:
        adb=AutoAdb()
    except KeyboardInterrupt:
        print("---886----")
        exit(0)