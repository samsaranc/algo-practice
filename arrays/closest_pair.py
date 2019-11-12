# problem source https://www.youtube.com/watch?v=GBuHSRDGZBY

#problem:
#given int arrays arr1, arr2, return the two indices of the numbers whose sum is closest to the target
def closest_pair(arr1, arr2, target):
	arr1.sort()
	arr2.sort()

	n =len(arr1)

	best_r = 0
	best_c = 0
	best_diff = target

	pos_r = 0
	pos_c = n-1

	sum_board = int[n][n]

	while: #there are free spaces left:
		diff = 

		if (diff is 0 ): return [pos_r,pos_c]

		else if (diff > best_diff): #eliminate square to bottom right
			update_sum_board(,)

		else: #eliminate square above and to the left 


		#update pos_c and pos_r


#dir = direction (r or l)
def update_sum_board(board, curr, dir):
	if 