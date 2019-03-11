#sending mail by using python

import smtplib
try:
	s=smtplib.SMTP('smtp.gmail.com','587')
	s.starttls()
	sender='rsshabuddin700@gmail.com'
	receiver='raffaishabuddin87012@gmail.com'
	msg="hello"
	s.login(sender,'9440333902')
	s.sendmail(sender, receiver,msg)
except:

	print("some error occured")
else:

	print("msg sent successfully")
	s.quit()