import sys
import time
import datetime

# 現在の日時を取得
now = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S")

# 毎秒ごとに日時を更新するループ
while True:
    # 現在の日時を取得
    now = datetime.datetime.now()

    # 日時を表示
    print(now)

    # 1秒待機
    time.sleep(1)


'''for i in range (0,120,1):
    time.sleep(1)
    print(i,"秒経過")
    print(starttime)
sys.exit(0)'''
