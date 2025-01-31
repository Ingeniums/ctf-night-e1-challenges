import traceback
print("Hah! It wasn't easy, but we've caught you now, Hacker! You'll never escape our highly advanced jail!")
print("Any last words?")

while True:
	inp = input('> ')
	if "flag" in inp:
		print("Mischievous As Ever... No flags allowed! hahaha!")
	else:
		try:
			print(eval(inp))
		except Exception as err:
			traceback.print_exc() # You can ignore this line, it's just to print out error messages.