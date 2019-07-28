from random import choice,randint
#MAIN
def check(num2, type1):
	if type1 == "addition":
		result = int(num2) + int(num2)
		print(result)	
	elif type1 == "subtraction":
		 result = int(num2) - int(num2)
		 print(result)	
	elif type1 == "multiplication":
		 result = int(num2) * int(num2)
		 print(result)	
	elif type1 == "division":
		 result = int(num2) / int(num2)
		 print(result)		
	elif type1 == "cube":
		#cube the number
		result = int(num2) ** 3
		print(result)	
	elif type1 == "cube_root":
		result = (int(num2) ** (1 / 3))
		print(result)	
	num = 0
	return result
def decode_operation(op, num1):
	if op == "addition":
		res = "What is " + str(num1) + " plus " + str(num1) + "? "
	elif op == "subtraction":
		 res = "What is " + str(num1) + " minus " + str(num1) + "? "
	elif op == "multiplication":
		 res = "What is " + str(num1) + " multiplied by " + str(num1) + "? "
	elif op == "division":
		 res = "What is " + str(num1) + " divided by " + str(num1) + "? "
	elif op == "cube":
		 res = "What is " + str(num1) + " cubed? "
	elif op == "cube_root":
		 res = "What is the cube root of " + str(num1) + "? "
	#end
	opts = [res, op]
	return opts
#end
#list all supported operations
possible_operations = ["addition", "subtraction", "multiplication", "division", "cube", "cube_root"]
#Generate a random number
num = randint(0,100)
#pick the operation slice
allowed_val = list(range(0,7))
x = choice(allowed_val)
allowed_val.remove(x)
y = choice(allowed_val)
allowed_val.remove(y)
z = choice(allowed_val)
allowed_val.remove(z)
#select three operations to preform
op1 = possible_operations[x]
op2 = possible_operations[y]
op3 = possible_operations[z]
#now pose the question
a = decode_operation(op1, num)
b = decode_operation(op2, num)
c = decode_operation(op3, num)
answer = input(a[0])
ch = check(answer, a[1])
if ch == answer:
	ans1 = True
else: 
	ans1 = False
	pass
#end
answer = input(b[0])
ch2 = check(answer, b[1])
if ch2 == answer:
	ans2 = True
else: 
	ans2 = False
	pass
#end
answer = input(c[0])
ch3 = check(answer, c[1])
if ch3 == answer:
	ans3 = True
else: 
	ans3 = False
	pass
#end
if ans1 or ans2 or ans3 == False:
	print("Your answers are incorrect. Try again.")
	pass
else:
	comb = input("What is the combination? (Hint: Seperate the numbers with commas) ")
	comb_actuall = ch + "," + ch2 + "," + ch3
	if comb == comb_actuall:
		print("Horray! You can play now!")
		pass
	else:
		print("Your answer is incorrect. Try again")
		pass
	#end
#end
#Replace values into selector
allowed_val.append(x)
allowed_val.append(y)
allowed_val.append(z)
exit()