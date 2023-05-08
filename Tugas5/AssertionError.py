# Handling it manually
try:
	x = 1
	y = 0
	assert y != 0, "Invalid Operation"
	print(x / y)

# the errror_message provided by the user gets printed
except AssertionError as msg:
	print(msg)