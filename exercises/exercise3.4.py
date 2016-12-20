#Exercise 3.4 A function object is a value you can assign to a variable or 
#pass as an argument. For example, do_twice is a function that takes a 
#function object as an argument and calls it twice:

def do_twice(f, argument):
	f(argument)
	f(argument)

def print_twice(argument):
	print (argument)
	print (argument)

do_twice(print_twice, 'spam')
print ('')

def do_four(f, argument):
	do_twice(f, argument)
	do_twice(f, argument)

do_four(print_twice, 'spam')
print ('')