
# Size of image
size = (2,2)

matrix_size = size[0] * size[1]

possible_combinations = 2**matrix_size

print "%dx%d Matrix, Total Size %d; Total Combinations %d" % (size[0],size[1],matrix_size,possible_combinations)

_full_length = len(bin(possible_combinations-1))-2

combinations = [[int(i) for i in (bin(number)[2:] + "0" * (_full_length - len(bin(number)[2:])))] for number in range(possible_combinations)]


# Cycle through all possible combinations
for combination in combinations:

	# Create Image here

	print "-----------------------------------------"
	print combination
	for y in xrange(size[1]):
		print combination[y*size[0]:y*size[0] + size[0]]

	for i in xrange(len(combination)):
		x = i % size[0]
		y = i / size[1]
		value = combination[i]
		# Set pixels
##		print x,y,value

	# Save Image
