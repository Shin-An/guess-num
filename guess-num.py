# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小
# 延伸:印出猜了幾次
# 延伸:請使用者決定隨機數範圍

import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end) # 變數起始結束值由使用者決定
count = 0 # count為計數
while True:
	count = count + 1 # 可寫成 count += 1
	g = input('請猜數字: ') # g為猜的數字
	g = int(g)
	if g == r:
		print('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif g > r:
		print('你猜的數字比答案大')
	elif g < r:
		print('你猜的數字比答案小')
	print('這是你猜的第', count, '次')