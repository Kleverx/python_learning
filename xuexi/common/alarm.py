#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
from pathlib import Path
from playsound import playsound


def attention(path, repeat=2):
    # 语音提示：https://developer.baidu.com/vcast导出音频
    for i in range(repeat):
        playsound(path)

    
class Alarm:
    def __init__(self, filename, repeat=2):
        path = Path('./xuexi/src/sounds')
        t = threading.Thread(target=attention, args=(str(path/filename), repeat))  # 创建线程
        t.start()
        # sleep(5*repeat)


if __name__ == "__main__":
    am = Alarm('alarm.mp3', 1)
    print('hello world')
