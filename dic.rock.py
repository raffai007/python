import random
l=["r","p","s"]
d={'r':"rock",'p':"paper",'s':"scissor"}
uc=0
cs=0
while True:
	u=input("enter your choice,press to discontinous")
	if u in d:
		print("user chooses",d[u])
	#toexit
	if u=='n':
		print("game over")
		print("user wins",uc)
		print("computer is winner",cs)
		exit()
		if cs>uc:
			print("cs wins")
		else:
			print("user wins")
	#input from computer
	c=random.choice(l)
	if c in d:
		print("computer chooses",d[c])
	print("computer chooses",c)
	#compare the user and computer choice
	if u==c:
		print("tie")
	elif u=="r"and c=="p":
		cs=cs+1
		print("comp wins score is",cs)
	elif u=="p" and c=="s":
		cs=cs+1
		print("computer wins score is",cs)
	elif u=="s"and c=="r":
		cs=cs+1
		print ("computer wins score is",cs)
	elif u=="p" and c=="r":
		uc=uc+1
		print("you wins score is",uc) 
	elif u=="s" and c=="p":
		uc=uc+1
		print("you wins score is",uc)
	elif u=="r" and c=="s":
		uc=uc+1
		print("you winsscore is",uc)
		
