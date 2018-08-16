# coding:utf-8
import subprocess
from pykakasi import kakasi

pic = u'汝云々カンヌンを知るだろう、くるっぱ'  # 音声の取得データ
pic = ''.join(pic.split())
kakasi = kakasi()
kakasi.setMode("H", "H")  # Hiragana to ascii, default: no conversion
kakasi.setMode("K", "H")  # Katakana to ascii, default: no conversion
kakasi.setMode("J", "H")  # Japanese to ascii, default: no conversion
kakasi.setMode("r", "Hepburn")  # default: use Hepburn Roman table
conv = kakasi.getConverter()
pic = conv.do(pic)

cmd = 'java morseRet ' + pic
process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                           shell=True).communicate()[0]


def res_cmd(cmd):
    return process


str = res_cmd(cmd).decode('utf-8')
for num in range(len(str)):

    if str[num] == '.':
        print('とん')
        # print('処理A')
        pass
    if str[num] == '-':
        print('つー')
        # print('処理B')
        pass
    if str[num] == '~':
        print('スペース')
        # print('処理C')
        pass
