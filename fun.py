
#def func1(a,b,c):#a=1,b=2,c=4
#	d=a+b+c
#	print(d)
#func1(1,2,4)


def func1(a,b,c):#a=1,b=2,c=4
	if a<b and b<c:
		print("max",c)
	elif b>a and b>=c:
		print("max",b)
	elif a>c and b<a:
		print("max",a)
	else:
		print("no")
func1(8,8,99)