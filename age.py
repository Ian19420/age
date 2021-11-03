driving = input('請問你有沒有開過車?')
age = eval(input('請問你的年齡?'))
if driving != '有' and driving != '沒有':
    print('只能輸入有或沒有')
    raise SystemExit
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪?你怎麼有開過車?')
elif driving == '沒有':
    if age >= 18:
    	print('你可以考駕照了')
    else:
    	print('再過幾年就可以考駕照了')
 
