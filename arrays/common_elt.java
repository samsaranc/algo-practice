/ sample input:
// [ 4, 5, 5
//	6, 4, 5]
// return: [4,5]

// input size N x M
// ASSUMPTIONS: all rows size m; not jagged array 

int[] FindCommonElementsAmongRows(int[][] elements){
	
	int n = elements.length;
	int m = elements[0].length;

	HashTable<Integer, Integer> seen = new HashTable<Integer, Integer>();
	ArrayList<Integer> commonRowElts = new ArrayList<Integer>();

	//KEY is elements[i][j] itself, VALUE is row #
	//insert items as <number, row>


	for (int row = 0; row < n; row++){
		for (int col = 0; col < m; col++){

			//use HashSet.contains() to see if number (key) is in table 
			//and check if we have not seen the same (number, row) pair before

			if ( seen.containsKey(elements[row][col]) && !(seen.contains(elements[row][col], row)) ){
				//add repeat element to our final set of common elts

				if (!commonRowElts.contains(elements[row][col])) { 
					commonRowElts.add(elements[row][col]);
				}

			}
			seen.add(elements[row][col],row);

		}
	}

	return commonRowElts.toIntegerArray();

}