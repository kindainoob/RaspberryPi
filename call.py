#coding:utf-8
import subprocess
pic = 'くるっぱ'#音声の取得データ
cmd = 'java morseRet '+ pic
process = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0]

def res_cmd(cmd):
  return process

str = res_cmd(cmd).decode('utf-8')

for num in range(len(str)):

    if str[num] == '.':
        print('とん')
        # print('処理A')
        pass
    else:
        print('つー')
        # print('処理B')
    pass
