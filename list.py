try:
	list=[1,2,3,4,5]
	print(list[1])
	raise NameError
except NameError:
	print("ok i got value")
finally:
	print("completed")