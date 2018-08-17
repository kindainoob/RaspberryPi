# coding:utf-8
import subprocess
from pykakasi import kakasi
import MeCab

# pic = u'汝云々カンヌンを知るだろう、くるっぱ'  # 音声の取得データ
pic = u'くるっぱ'
pic = ''.join(pic.split())  # 空白の削除
print(pic)


# MeCabによる形態素解析
try:
    m = MeCab.Tagger("-Owakati")
    pic = m.parse(pic)
    pic = pic.strip()  # 先頭と末尾の空白を削除
    pic = pic.replace(' ', '_')  # 単語間に開けた空白を変換
except RuntimeError:
    pic = ""
print(pic)

# pykakasiによるカタカナ・漢字のひらがなへの変換
kakasi = kakasi()
kakasi.setMode("K", "H")  # カタカナをひらがなに
kakasi.setMode("J", "H")  # 漢字をひらがなに
# kakasi.setMode("r", "Hepburn")  # default: use Hepburn Roman table
conv = kakasi.getConverter()
pic = conv.do(pic)
print(pic)


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
        # print('処理A')  1拍点灯
        pass
    if str[num] == '-':
        print('つー')
        # print('処理B')  3拍点灯
        pass
    if str[num] == '~':
        print('スペース')
        # print('処理C')  　3拍消灯
        pass
    if str[num] == '_':
        print('アンダースコア')
        # print('処理D')  7拍消灯
