import random
l=["r","p","s"]
while True:
	#take input from the user
	u=input("enter your choice,press to discontinous")
	#toexit
	if u=='n':
		print("game over")
		exit()
	#input from computer
	c=random.choice(l)
	print("computer chooses",c)

	#compare the user and computer choice
	if u==c:
		print("tie")
	elif u=="r"and c=="p":
		print("comp wins")
	elif u=="p" and c=="s":
		print("computer wins")

	elif u=="s"and c=="r":
		print ("computer wins")

	elif u=="p" and c=="r":
		print("you lost")
	elif u=="s" and c=="p":
		print("you lost")
	elif u=="r" and c=="s":
		print("you losts")
	


