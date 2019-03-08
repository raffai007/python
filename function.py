#creating a funtion without parameters
def func1():
	print("hii")
	print("hello")
func1()
# with parameters
def func2(a):#a=1
	print("hii\t",a)
func2("shabuddin")	
#2/3parameters
def func3(a,b,c):#a=5,b=8,c=1
	d=a+b+c
	print(a,b,c,d)
func3(5,8,1)
#with defaultparameter
def func4(university = "cmr"):
	print("iam in"+"\t"+university)
func4("banglore")
func4("university")
func4()	
#return statements
def func7(a,b,c):#a=2,b=3,c=6
	d=a+b+c
	return d
e=func7(2,3,6)
print(e)
#calling one func from other and return statements
def func5(a,b):
	print("going to other functions")
	c=a+b
	return c
def func6():
	print("hello im goona call to other function")
	s=func5(3,5)
	print("additionis",s)
func6()




