#!/usr/bin/python3

'''
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash 
of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the 
lowest such number to do so.

If your secret key is pqrstuv, the lowest number it combines with to make 
an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash 
of pqrstuv1048970 looks like 000006136ef....

Your puzzle input is ckczppom.
'''

import hashlib

EXAMPLES = [
		('abcdef', 609043),
		('pqrstuv', 1048970)
	]


def monetas(salt, num_leading_zeroes=5):
	i = 0
	while True:
		md = hashlib.md5("{salt}{i}".format(salt=salt, i=i).encode('utf-8')).hexdigest()
		#print(md, md[:5])
		if md[:num_leading_zeroes] == '0' * num_leading_zeroes:
			return i
		i += 1

	print("not found")
	return i


def main():
	for data, num in EXAMPLES:
		assert num == monetas(data, 5)
		print('ok')

	print(monetas('ckczppom', 6))

if __name__ == '__main__':
	main()
