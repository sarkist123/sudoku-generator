#!/usr/bin/python

import array
import random

# The grid is a 9 by 9 char array.
# 0 means there is no number.
# 1 to 9 are the numbers.
# Indexing starts on the upper left.
grid = array.array('b',
	[1,2,3,7,8,9,4,5,6,
	 4,5,6,1,2,3,7,8,9,
	 7,8,9,4,5,6,1,2,3,
	 9,1,2,6,7,8,3,4,5,
	 3,4,5,9,1,2,6,7,8,
	 6,7,8,3,4,5,9,1,2,
	 8,9,1,5,6,7,2,3,4,
	 2,3,4,8,9,1,5,6,7,
	 5,6,7,2,3,4,8,9,1])

# Empty grid, start with anything possible.
grid_possibilities = array.array('h',
	[0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Return the value of a cell
def c(grid, x, y):
	return grid[9*y + x]

# Set the value of a cell
def s(grid, x, y, v):
	grid[9*y + x] = v

# Get the index of a box. Indexes start at the top left and go right, just like for cells.
def get_box(x, y):
	return (x/3)%3 + 3*((y/3)%3)

# Get the index of a cell within a box. The top left cell in a box is 0, then 1, then 2,
# Then the middle left cell is 3, etc etc.
def get_box_cell(x, y):
	return x%3 + 3*(y%3)

# Given a box and cell index pair, return the index into a grid array for that cell.
def get_box_cell_coord(box, cell):
	return 27*(box/3) + 3*(box%3) + 9*(cell/3) + cell%3

# The arguments for this are the return values of get_box and get_box_cell
def b(grid, box, cell):
	return grid[get_box_cell_coord(box, cell)]

def pretty_print(c):
	if c == 0:
		return " "
	else:
		return chr(c + ord('0'))

def grid_print(g):
	print pretty_print(c(g, 0, 0)) + " " + pretty_print(c(g, 1, 0)) + " " + pretty_print(c(g, 2, 0)) + \
		 "|" + pretty_print(c(g, 3, 0)) + " " + pretty_print(c(g, 4, 0)) + " " + pretty_print(c(g, 5, 0)) + \
		 "|" + pretty_print(c(g, 6, 0)) + " " + pretty_print(c(g, 7, 0)) + " " + pretty_print(c(g, 8, 0))
	print pretty_print(c(g, 0, 1)) + " " + pretty_print(c(g, 1, 1)) + " " + pretty_print(c(g, 2, 1)) + \
		 "|" + pretty_print(c(g, 3, 1)) + " " + pretty_print(c(g, 4, 1)) + " " + pretty_print(c(g, 5, 1)) + \
		 "|" + pretty_print(c(g, 6, 1)) + " " + pretty_print(c(g, 7, 1)) + " " + pretty_print(c(g, 8, 1))
	print pretty_print(c(g, 0, 2)) + " " + pretty_print(c(g, 1, 2)) + " " + pretty_print(c(g, 2, 2)) + \
		 "|" + pretty_print(c(g, 3, 2)) + " " + pretty_print(c(g, 4, 2)) + " " + pretty_print(c(g, 5, 2)) + \
		 "|" + pretty_print(c(g, 6, 2)) + " " + pretty_print(c(g, 7, 2)) + " " + pretty_print(c(g, 8, 2))
	print "-----+-----+-----"
	print pretty_print(c(g, 0, 3)) + " " + pretty_print(c(g, 1, 3)) + " " + pretty_print(c(g, 2, 3)) + \
		 "|" + pretty_print(c(g, 3, 3)) + " " + pretty_print(c(g, 4, 3)) + " " + pretty_print(c(g, 5, 3)) + \
		 "|" + pretty_print(c(g, 6, 3)) + " " + pretty_print(c(g, 7, 3)) + " " + pretty_print(c(g, 8, 3))
	print pretty_print(c(g, 0, 4)) + " " + pretty_print(c(g, 1, 4)) + " " + pretty_print(c(g, 2, 4)) + \
		 "|" + pretty_print(c(g, 3, 4)) + " " + pretty_print(c(g, 4, 4)) + " " + pretty_print(c(g, 5, 4)) + \
		 "|" + pretty_print(c(g, 6, 4)) + " " + pretty_print(c(g, 7, 4)) + " " + pretty_print(c(g, 8, 4))
	print pretty_print(c(g, 0, 5)) + " " + pretty_print(c(g, 1, 5)) + " " + pretty_print(c(g, 2, 5)) + \
		 "|" + pretty_print(c(g, 3, 5)) + " " + pretty_print(c(g, 4, 5)) + " " + pretty_print(c(g, 5, 5)) + \
		 "|" + pretty_print(c(g, 6, 5)) + " " + pretty_print(c(g, 7, 5)) + " " + pretty_print(c(g, 8, 5))
	print "-----+-----+-----"
	print pretty_print(c(g, 0, 6)) + " " + pretty_print(c(g, 1, 6)) + " " + pretty_print(c(g, 2, 6)) + \
		 "|" + pretty_print(c(g, 3, 6)) + " " + pretty_print(c(g, 4, 6)) + " " + pretty_print(c(g, 5, 6)) + \
		 "|" + pretty_print(c(g, 6, 6)) + " " + pretty_print(c(g, 7, 6)) + " " + pretty_print(c(g, 8, 6))
	print pretty_print(c(g, 0, 7)) + " " + pretty_print(c(g, 1, 7)) + " " + pretty_print(c(g, 2, 7)) + \
		 "|" + pretty_print(c(g, 3, 7)) + " " + pretty_print(c(g, 4, 7)) + " " + pretty_print(c(g, 5, 7)) + \
		 "|" + pretty_print(c(g, 6, 7)) + " " + pretty_print(c(g, 7, 7)) + " " + pretty_print(c(g, 8, 7))
	print pretty_print(c(g, 0, 8)) + " " + pretty_print(c(g, 1, 8)) + " " + pretty_print(c(g, 2, 8)) + \
		 "|" + pretty_print(c(g, 3, 8)) + " " + pretty_print(c(g, 4, 8)) + " " + pretty_print(c(g, 5, 8)) + \
		 "|" + pretty_print(c(g, 6, 8)) + " " + pretty_print(c(g, 7, 8)) + " " + pretty_print(c(g, 8, 8))

def gridp_allow(g, x, y, digit):
	g[9*y + x] = g[9*y + x] | (1<<digit)

def gridp_disallow(g, x, y, digit):
	g[9*y + x] = g[9*y + x] & ~(1<<digit)

def gridp_is_allowed(g, x, y, digit):
	return g[9*y + x] & (1<<digit)

def gridp_num_allowed(g, x, y):
	allowed = 0
	for k in range(1, 10):
		if gridp_is_allowed(g, x, y, k):
			allowed += 1
	return allowed

def gridp_get_allowed(g, x, y):
	allowed = []
	for k in range(1, 10):
		if gridp_is_allowed(g, x, y, k):
			allowed.append(k)
	return allowed

def gridp_box_allow(g, box, cell, digit):
	g[get_box_cell_coord(box, cell)] = g[get_box_cell_coord(box, cell)] | (1<<digit)

def gridp_box_disallow(g, box, cell, digit):
	print "Disallowing " + str(digit) + " in " + str(box) + " " + str(cell)
	g[get_box_cell_coord(box, cell)] = g[get_box_cell_coord(box, cell)] & ~(1<<digit)

def gridp_box_is_allowed(g, box, cell, digit):
	return g[get_box_cell_coord(box, cell)] & (1<<digit)

# There are too possibilities per square to print them all. Instead use this procedure to print a grid of the number of possibilities.
def grid_print_num_allowed(g):
	print chr(gridp_num_allowed(g, 0, 0) + ord('0')) + " " + chr(gridp_num_allowed(g, 1, 0) + ord('0')) + " " + chr(gridp_num_allowed(g, 2, 0) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 3, 0) + ord('0')) + " " + chr(gridp_num_allowed(g, 4, 0) + ord('0')) + " " + chr(gridp_num_allowed(g, 5, 0) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 6, 0) + ord('0')) + " " + chr(gridp_num_allowed(g, 7, 0) + ord('0')) + " " + chr(gridp_num_allowed(g, 8, 0) + ord('0'))
	print chr(gridp_num_allowed(g, 0, 1) + ord('0')) + " " + chr(gridp_num_allowed(g, 1, 1) + ord('0')) + " " + chr(gridp_num_allowed(g, 2, 1) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 3, 1) + ord('0')) + " " + chr(gridp_num_allowed(g, 4, 1) + ord('0')) + " " + chr(gridp_num_allowed(g, 5, 1) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 6, 1) + ord('0')) + " " + chr(gridp_num_allowed(g, 7, 1) + ord('0')) + " " + chr(gridp_num_allowed(g, 8, 1) + ord('0'))
	print chr(gridp_num_allowed(g, 0, 2) + ord('0')) + " " + chr(gridp_num_allowed(g, 1, 2) + ord('0')) + " " + chr(gridp_num_allowed(g, 2, 2) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 3, 2) + ord('0')) + " " + chr(gridp_num_allowed(g, 4, 2) + ord('0')) + " " + chr(gridp_num_allowed(g, 5, 2) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 6, 2) + ord('0')) + " " + chr(gridp_num_allowed(g, 7, 2) + ord('0')) + " " + chr(gridp_num_allowed(g, 8, 2) + ord('0'))
	print "-----+-----+-----"
	print chr(gridp_num_allowed(g, 0, 3) + ord('0')) + " " + chr(gridp_num_allowed(g, 1, 3) + ord('0')) + " " + chr(gridp_num_allowed(g, 2, 3) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 3, 3) + ord('0')) + " " + chr(gridp_num_allowed(g, 4, 3) + ord('0')) + " " + chr(gridp_num_allowed(g, 5, 3) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 6, 3) + ord('0')) + " " + chr(gridp_num_allowed(g, 7, 3) + ord('0')) + " " + chr(gridp_num_allowed(g, 8, 3) + ord('0'))
	print chr(gridp_num_allowed(g, 0, 4) + ord('0')) + " " + chr(gridp_num_allowed(g, 1, 4) + ord('0')) + " " + chr(gridp_num_allowed(g, 2, 4) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 3, 4) + ord('0')) + " " + chr(gridp_num_allowed(g, 4, 4) + ord('0')) + " " + chr(gridp_num_allowed(g, 5, 4) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 6, 4) + ord('0')) + " " + chr(gridp_num_allowed(g, 7, 4) + ord('0')) + " " + chr(gridp_num_allowed(g, 8, 4) + ord('0'))
	print chr(gridp_num_allowed(g, 0, 5) + ord('0')) + " " + chr(gridp_num_allowed(g, 1, 5) + ord('0')) + " " + chr(gridp_num_allowed(g, 2, 5) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 3, 5) + ord('0')) + " " + chr(gridp_num_allowed(g, 4, 5) + ord('0')) + " " + chr(gridp_num_allowed(g, 5, 5) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 6, 5) + ord('0')) + " " + chr(gridp_num_allowed(g, 7, 5) + ord('0')) + " " + chr(gridp_num_allowed(g, 8, 5) + ord('0'))
	print "-----+-----+-----"
	print chr(gridp_num_allowed(g, 0, 6) + ord('0')) + " " + chr(gridp_num_allowed(g, 1, 6) + ord('0')) + " " + chr(gridp_num_allowed(g, 2, 6) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 3, 6) + ord('0')) + " " + chr(gridp_num_allowed(g, 4, 6) + ord('0')) + " " + chr(gridp_num_allowed(g, 5, 6) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 6, 6) + ord('0')) + " " + chr(gridp_num_allowed(g, 7, 6) + ord('0')) + " " + chr(gridp_num_allowed(g, 8, 6) + ord('0'))
	print chr(gridp_num_allowed(g, 0, 7) + ord('0')) + " " + chr(gridp_num_allowed(g, 1, 7) + ord('0')) + " " + chr(gridp_num_allowed(g, 2, 7) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 3, 7) + ord('0')) + " " + chr(gridp_num_allowed(g, 4, 7) + ord('0')) + " " + chr(gridp_num_allowed(g, 5, 7) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 6, 7) + ord('0')) + " " + chr(gridp_num_allowed(g, 7, 7) + ord('0')) + " " + chr(gridp_num_allowed(g, 8, 7) + ord('0'))
	print chr(gridp_num_allowed(g, 0, 8) + ord('0')) + " " + chr(gridp_num_allowed(g, 1, 8) + ord('0')) + " " + chr(gridp_num_allowed(g, 2, 8) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 3, 8) + ord('0')) + " " + chr(gridp_num_allowed(g, 4, 8) + ord('0')) + " " + chr(gridp_num_allowed(g, 5, 8) + ord('0')) + \
		 "|" + chr(gridp_num_allowed(g, 6, 8) + ord('0')) + " " + chr(gridp_num_allowed(g, 7, 8) + ord('0')) + " " + chr(gridp_num_allowed(g, 8, 8) + ord('0'))

# Set a number on a grid, updating the disallow bit on all appropriate cells.
def grid_set(g, gp, x, y, digit):
	s(g, x, y, digit)

	for k in range(0, 9):
		gridp_disallow(gp, x, k, digit)
		gridp_disallow(gp, k, y, digit)

	box = get_box(x, y)
	for i in range(0, 9):
		gridp_box_disallow(gp, box, i, digit)

"""
In broad strokes:
1. Generate a valid grid

In a loop:
  2. Remove a point
  3. Run solving algorithms on the grid
  4. Memoize the result (hash it)
  5. Quit the loop when we have enough results

6. Inspect the memoized data and generate puzzles for four difficulty levels
"""

def row_swap(grid, k1, k2):
	for k in range(0, 9):
		grid[k1*9 + k], grid[k2*9 + k] = grid[k2*9 + k], grid[k1*9 + k]

def col_swap(grid, k1, k2):
	for k in range(0, 9):
		grid[k1 + k*9], grid[k2 + k*9] = grid[k2 + k*9], grid[k1 + k*9]

# First make 50 random row and column swaps to randomize the permutations
for k in range(0, 50):
	box = random.randint(0, 2)
	row1 = random.randint(0, 2)
	row2 = (row1+random.randint(1, 2))%3 + box*3
	row1 += box*3
	row_swap(grid, row1, row2)

	box = random.randint(0, 2)
	col1 = random.randint(0, 2)
	col2 = (col1+random.randint(1, 2))%3 + box*3
	col1 += box*3
	col_swap(grid, col1, col2)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
randomized = []

# Now create a random permutation for the digits and apply it
while len(digits):
	index = random.randint(0, len(digits)-1)
	digit = digits.pop(index)
	randomized.append(digit)

for k in range(0, 9*9):
	grid[k] = randomized[grid[k]-1]
	grid_possibilities[k] = 1<<grid[k]

# The next two strategies for generating grids don't work, they eventually hit
# invalid grid positions.
"""
for k in range(1, 10):
	for box in range(0, 9):
		print "Box:  " + str(box)

		# Find the cells in this box that are free for this number
		free_cells = []
		for cell in range(0, 9):
			if gridp_box_is_allowed(grid_possibilities, box, cell, k):
				if b(grid, box, cell) == 0:
					free_cells.append(cell)

		print "Available: "
		print free_cells

		new = random.randint(0, len(free_cells)-1)

		print "Chosen: " + str(free_cells[new])

		index = get_box_cell_coord(box, free_cells[new])
		x = index%9
		y = index/9

		grid_set(grid, grid_possibilities, x, y, k)

		grid_print(grid)
		grid_print_num_allowed(grid_possibilities)
"""

"""
for k in range(0, 9*9+1):
	x = k%9
	y = k/9

	print "Coordinate: " + str(x) + ", " + str(y)
	allowed = gridp_get_allowed(grid_possibilities, x, y)
	print "Allowed: "
	print allowed
	if len(allowed) == 0:
		grid_print(grid)
		grid_print_num_allowed(grid_possibilities)
	new = allowed[random.randint(0, len(allowed)-1)]
	print "New: " + str(new)
	print ""

	grid_set(grid, grid_possibilities, x, y, new)
"""

grid_print(grid)
grid_print_num_allowed(grid_possibilities)
