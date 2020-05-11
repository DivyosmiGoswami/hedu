 import pandas as pd
import re
import getpass
import sys
import os
import time
import math
from numpy import *
class user():		
	def d(self):
		print ('div1, 1 tb , 64 bit , 2 tb,123456789098,12::as::xx::bb::23,192.168.1.5')	
	def greet(self):
		print('type help')						
	def __init__ (self):
		a = input('>>>')
		if a == 'ipconfig':
			self.d()
		elif a == 'div':
			print('welcome div')
			self.greet()
		elif a == 'array of int':
		    b= int(input('the first value'))
		    c= int(input('the second value'))
		    d= array([b,c])
		    print(d)
		elif a == 'array of float':
		    t = int(input('no. of elements'))
		    for i in range(t):
		        b = float(input('the element'))
		        print(array(b)) 	
		elif a == "even/odd":
			b = float(input('the no.'))
			if b%2 == 0:
				print('even')
			else:
				print('odd')
		elif a == 'addr':
		    f = open("/storage/emulated/0/python/addr.txt","r")
		    s = f.read()
		    import json
		    book = json.loads(s)
		    for i in book.items():		
		        print(i)
		elif a == 'this':
			import this
		elif a == 'search':
			b= input('the element')
			c= input('the array')
			if re.search(b,c):
				print('matched')
			else:
				print('not matched')						
		elif a == 'linspace':
			b = float(input('the start'))
			c= float(input('the stop'))
			d = float(input('the part'))
			e = linspace(b,c,d) 
			print(e)							
		elif a == 'logspace':
			b = float(input('the start'))
			c= float(input('the stop'))
			d = float(input('the part'))
			e = logspace(b,c,d) 
			print(e)
		elif a == "sq.":
			b = float(input("the no."))
			c = b * b
			print(c)
		elif a == "sqrt.":
			b = float(input("the no."))
			print(math.sqrt(b))
		elif a == "curt.":
			b = float(input("the no."))
			c = b ** (1/3)
			print(c)
		elif a == "pi":
			print(math.pi)
		elif a == "e":
			print(math.e)
		elif a == "cu.":
			b = float(input("the no."))			
			c = b*b*b
			print(c) 
		elif a == "zeros":
			b = int(input("the no. of zeros"))
			c = zeros(b,int)
			print(c)
		elif a == "ones":
			b = int(input("the no. of ones"))
			c = ones(b,int)
			print(c)			
		elif a == 'name':
			print ('div.n.cov.1/Divyosmi')
		elif a == 'countdown':
			b = int(input('how many seconds'))
			for i in range(b,0,-1):
				print(i)
				time.sleep(1)
			print('blast off')
		elif a == 'hex':
			b = int(input('the no.'))
			print(hex(b))
		elif a == 'oct':
			b = int(input('the no.'))
			print(oct(b))
		elif a == 'bin':
			b = int(input('the no.'))
			print(bin(b))		
		elif a == "address":
			print(id(div))
		elif a == 'marks':
			d = float(int(input('first marks')))
			b = float(int(input('total marks')))
			c = d/b*100
			print(c,'%')
		elif a == 'developer':
			print('Divyosmi Goswami')
		elif a == 'help':
			print("name for it's name,address for id ,id of listes and set and tuples and no. and strings,hashes,square,cube,sq root ,cube root ,linspace,logspace,bin,hex,oct,array and many more \n\t for developer and creator and license holder addr and div and ipconfig")
		elif a == 'license':
		    print('for license email at divyosmigoswami@gmail.com')	
		elif a == 'exit':
		    print('thankyou')
		    print('exiting.....')
		    time.sleep(10)
		    print('finished',bin(id(hash(bin(id(id(hash(id('divyosmi')))))))))
		    sys.exit()
		elif a == 'clear':
			os.system("clear")
		elif a == 'id of no.':
			b = float(input('the no.'))
			print(id(b))
		elif a== 'id of string':
			b = input('the string')
			print(id(b))
		elif a == 'hash of string':
			c = input('enter the string whose hash you want')
			b = hash(c)
			print(b)
		elif a == 'hash of no.':
			c = float(input('enter the no.'))
			b = hash(c)
			print(b)
		elif a == 'hash of set':
			b =input('please enter a set')
			print(hash(b))
		elif a == 'id of list/set/tuple':
			b= input('enter list ,tuple,set')
			print(id(b))			    	
		elif a == 'fib':
			a = int(input('fibbonaci upto which no.'))
			b=0
			c=1
			if a == 1:
				print(b)
			if a == 0:
				print('invalid')
			if a>1:
				print(b)
				print(c)
				for i in range(2,a,1):					
				   d = b+c
				   b=c
				   c=d
				   print(d)
		elif a == 'fact':
			b = int(input('which numbers factorial'))
			f = 1
			for i in range (1,b+1):
				f = f*i
			print(f)
		elif a == 'zip':
		    b = input ('the first tuple,set,list')
		    c= input('the second one.')
		    d = list(zip(b,c))
		    print(d)					
		else:
			print("sorry,I dont know that")
	
class div():
	def d(self):
		print ('div1, 1 tb , 64 bit , 2 tb,123456789098,12::as::xx::bb::23,192.168.1.5')	
	def greet(self):
		print('hi dude ')
		print('I am there for you')						
	def __init__ (self):
		a = input("Divyosmi:$>")
		if a == 'ipconfig':
			self.d()
		elif a == 'div':
			print('welcome div')
			self.greet()
		elif a == 'array of int':
		    b= int(input('the first value'))
		    c= int(input('the second value'))
		    d= array([b,c])
		    print(d)
		elif a == 'note':
			c = pd.read_csv('/storage/emulated/0/python/R.csv')
			print(c)
			df = pd.read_csv('/storage/emulated/0/python/My.csv')
			print(df)
			d = pd.read_csv('/storage/emulated/0/python/Read.csv')
			print(d)
			os.system('python /storage/emulated/0/python/number_to_word.py')
			os.system('python /storage/emulated/0/python/co.relation.py')		
			os.system('python /storage/emulated/0/python/reversecipher.py')	
		elif a == 'My.csv':
			df = pd.read_csv('/storage/emulated/0/python/My.csv')
			print(df)
		elif a == 'Read.csv':
			d = pd.read_csv('/storage/emulated/0/python/Read.csv')
			print(d)
		elif a == 'reverse':
			os.system('python /storage/emulated/0/python/reversecipher.py')
		elif a == 'R.csv':
			c = pd.read_csv('/storage/emulated/0/python/R.csv')
			print(c)
		elif a == 'ntw':
			os.system('python /storage/emulated/0/python/number_to_word.py')			
		elif a == 'array of float':
		    t = int(input('no. of elements'))
		    for i in range(t):
		        b = float(input('the element'))
		        print(array(b)) 	
		elif a == "even/odd":
			b = float(input('the no.'))
			if b%2 == 0:
				print('even')
			else:
				print('odd')
		elif a == 'addr':
		    f = open("/storage/emulated/0/python/addr.txt","r")
		    s = f.read()
		    import json
		    book = json.loads(s)
		    for i in book.items():		
		        print(i)
		elif a == 'search':
			b= input('the element')
			c= input('the array')
			if re.search(b,c):
				print('matched')
			else:
				print('not matched')						
		elif a == 'linspace':
			b = float(input('the start'))
			c= float(input('the stop'))
			d = float(input('the part'))
			e = linspace(b,c,d) 
			print(e)							
		elif a == 'logspace':
			b = float(input('the start'))
			c= float(input('the stop'))
			d = float(input('the part'))
			e = logspace(b,c,d) 
			print(e)
		elif a == "sq.":
			b = float(input("the no."))
			c = b * b
			print(c)
		elif a == "sqrt.":
			b = float(input("the no."))
			print(math.sqrt(b))
		elif a == "curt.":
			b = float(input("the no."))
			c = b ** (1/3)
			print(c)
		elif a == "pi":
			print(math.pi)
		elif a == "e":
			print(math.e)
		elif a == "cu.":
			b = float(input("the no."))			
			c = b*b*b
			print(c) 
		elif a == "zeros":
			b = int(input("the no. of zeros"))
			c = zeros(b,int)
			print(c)
		elif a == "ones":
			b = int(input("the no. of ones"))
			c = ones(b,int)
			print(c)			
		elif a == 'name':
			print ('div.n.cov.1/Divyosmi')
		elif a == 'countdown':
			b = int(input('how many seconds'))
			for i in range(b,0,-1):
				print(i)
				time.sleep(1)
			print('blast off')
		elif a == 'hex':
			b = int(input('the no.'))
			print(hex(b))
		elif a == 'oct':
			b = int(input('the no.'))
			print(oct(b))
		elif a == 'bin':
			b = int(input('the no.'))
			print(bin(b))		
		elif a == "address":
			print(id(div))
		elif a == 'marks':
			d = float(int(input('first marks')))
			b = float(int(input('total marks')))
			c = d/b*100
			print(c,'%')
		elif a == 'developer':
			print('Divyosmi Goswami')	
		elif a == 'exit':
		    print('thankyou')
		    print('exiting.....')
		    time.sleep(10)
		    print('finished',bin(id(hash(bin(id(id(hash(id('divyosmi')))))))))
		    sys.exit()
		elif a == 'clear':
			os.system("clear")
		elif a == 'id of no.':
			b = float(input('the no.'))
			print(id(b))
		elif a== 'id of string':
			b = input('the string')
			print(id(b))
		elif a == 'hash of string':
			c = input('enter the string whose hash you want')
			b = hash(c)
			print(b)
		elif a == 'hash of no.':
			c = float(input('enter the no.'))
			b = hash(c)
			print(b)
		elif a == 'hash of set':
			b =input('please enter a set')
			print(hash(b))
		elif a == 'id of list/set/tuple':
			b= input('enter list ,tuple,set')
			print(id(b))			    	
		elif a == 'fib':
			a = int(input('fibbonaci upto which no.'))
			b=0
			c=1
			if a == 1:
				print(b)
			if a == 0:
				print('invalid')
			if a>1:
				print(b)
				print(c)
				for i in range(2,a,1):					
				   d = b+c
				   b=c
				   c=d
				   print(d)
		elif a == 'fact':
			b = int(input('which numbers factorial'))
			f = 1
			for i in range (1,b+1):
				f = f*i
			print(f)
		elif a == 'this':
			import this
		elif a == 'zip':
		    b = input ('the first tuple,set,list')
		    c= input('the second one.')
		    d = list(zip(b,c))
		    print(d)					
		else:
			print("sorry,I dont know that")

print('hi,hope you are fine')
print('/n please enter the password')
print('if need help ask divyosmi ')
b = getpass.getpass('enter password')

if b == '1':
	print('acess granted')
	a = input("write your class to continue ")
	if a == 'div':
		while True:
			div()										
	elif a == 'user':
		while True:
			user()
	else:
		sys.exit()
else:    	
	print('acess denied')
	raise ValueError	
