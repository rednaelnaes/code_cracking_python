def reverser_1(text):
	x,y,i=[],'',len(text)-1
	while(i>=0):
		x.append(text[i])
		i=i-1
	return(y.join(x))

def reverser_2(text):
	plain_list,cryp_list=[],[]
	for i in range(len(text)):plain_list.append(text[i])
	for i in range(len(text)):cryp_list.append(plain_list.pop())
	return(''.join(cryp_list))

def reverser_3(text):
	pt,ct=[text[i] for i in range(len(text))],[]
	for i in range(len(text)):ct.append(pt.pop())
	return(''.join(ct))

def reverser_4(text):
	for i in range(len(text) -1,-1,-1):
		yield text[i]

test1 = reverser_1('test')
test2 = reverser_2('test')
test3 = reverser_3('test')
test4 = ''.join([x for x in reverser_4('test')])
tests = [test1,test2,test3,test4]
for t in tests:print(t)