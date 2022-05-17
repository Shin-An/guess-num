# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random

r = random.randint(1, 100)

while True:
	g = input('請猜數字1~100: ') # g為猜的數字
	g = int(g)
	if g == r:
		print('終於猜對了!')
		break
	elif g > r:
		print('你猜的數字比答案大')
	elif g < r:
		print('你猜的數字比答案小')