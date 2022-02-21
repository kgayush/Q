import time

def function_timer(func):
	def inner_function(*args):
		start_time = time.time()
		func(*args)
		end_time = time.time()
		print(f'Total time for execution is: {end_time - start_time}')
	return inner_function

@function_timer
def hello_world():
	time.sleep(2)
	print("Hello World!")

hello_world()
