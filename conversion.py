def DECtoBASE(base, num):
	final = ""
	for i in range(8):
		final += str(num//(base**(7 - i)))
		num = num%(base**(7 - i))
	return final

def BASEtoDEC(base, num):
	num = [int(i) for i in num] #https://www.geeksforgeeks.org/python-convert-number-to-list-of-integers/
	final = 0
	for i in range(len(num)):
		final += (num[len(num) - i - 1] * base**i)
	return final
