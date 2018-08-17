# coding:utf-8
import subprocess
from pykakasi import kakasi
import MeCab
import RPi.GPIO as GPIO
import time


pic = u'汝云々カンヌンを知るだろう、くるっぱ'  # 音声の取得データ
pic = ''.join(pic.split())  # 空白の削除

# MeCabによる形態素解析
try:
    m = MeCab.Tagger("-Owakati")
    pic = m.parse(pic)
    pic = pic.strip()  # 先頭と末尾の空白を削除
    pic = pic.replace(' ', '_')  # 単語間に開けた空白を変換
except RuntimeError:
    pic = ""


# pykakasiによるカタカナ・漢字のひらがなへの変換
kakasi = kakasi()
kakasi.setMode("K", "H")  # カタカナをひらがなに
kakasi.setMode("J", "H")  # 漢字をひらがなに
conv = kakasi.getConverter()
pic = conv.do(pic)

# 光らせる


def light_up(minute):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, GPIO.HIGH)
    time.sleep(minute)
    GPIO.cleanup()


# 光らせない(何もしない)
def light_down(minute):
    x = minute if minute < 7 else 7
    time.sleep(x)
    pass


# それぞれの処理の秒数
dot = 0.33333333  # とん
stick = dot*3  # つー
space = dot*3  # 空白
under_score = dot  # 単語の区切り
between_sleep = dot/3


# Javaのファイルで文字列をモールス信号に変換
cmd = 'java morseRet ' + pic
process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                           shell=True).communicate()[0]


def res_cmd(cmd):
    return process


str = res_cmd(cmd).decode('utf-8')
for num in range(len(str)):

    if str[num] == '.':
        print('とん')
        light_up(dot)
        # print('処理A')  1拍点灯
    if str[num] == '-':
        print('つー')
        light_up(stick)
        # print('処理B')  3拍点灯
    if str[num] == '~':
        print('スペース')
        light_down(space)
        # print('処理C')  　3拍消灯
    if str[num] == '_':
        print('アンダースコア')
        light_down(under_score)

    time.sleep(between_sleep)
    # print('処理D')  7拍消灯
    # ７拍点灯だがスペース時の3拍に挟まれるため1拍消灯で3+1+3で7拍消灯となる
