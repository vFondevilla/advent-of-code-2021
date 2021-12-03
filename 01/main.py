import logging
import os

count = 0
previous_number = 0

def open_file(file):
	with open(file, "r") as f:
		return f.readlines()

def compare_number(number, prev_number):
	global count
	global previous_number
	if int(number) > int(prev_number):
		global count
		count += 1
	else:
		pass
	previous_number = number

input = open_file("input")
print(type(input))
# lines = input.readLines()
previous_number = input[0]
for number in input:
	print(number)
	compare_number(number, previous_number)
print(count)
