#!/usr/bin/python

dvd=2
res=0
init = int(raw_input("Enter your start number: "))

print "Thinking..."
end = init-1;

#while loop

while(dvd<end):
	
        quoc = init/dvd
	modt = quoc*dvd
	rest = init-modt
	if rest==0:
		print "Not Prime."
		break
	dvd=dvd+1

if init==1:
	#exception:
	print "1 is not prime, you idiot."

elif dvd>=end:
	print "Prime."


print "Here thanks to Matoe Productions LLC\n\
(c) 2011 Matoe Productions LLC"
