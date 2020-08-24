#include <iostream>
#include <unordered_map>

/*
The solution is a classic dynamic programming solution
There are a few observations:
	1. All rows are either empty, partially filled or full
	2. There are at most 3 partially filled rows (due to my strict "from-top-to-bottom" algorithm)

	My memoization hash therefore consists only of the number of empty rows and the bitmasks of (up to)
	three partially filled rows.

	For the 9x12 grid, it just fits into a 32 bit integer.

	The number of solutions for a grid of size n x m is identical to a grid of size m x n.
	
	The hash is "smaller" and creates more opportunities for memoization hits when the rows are small.
*/


// indicate an empty row
const unsigned int EmptyRow = 0;

// set a certain bit to one (= position is not available anymore), return true if bit was zero
// note: second parameter is an in/out parameter
bool use(unsigned int pos, unsigned int& row){
  unsigned int mask = 1 << pos;
  bool result = (row & mask) == 0;
  row |= mask;
  return result;
}

// recursive search
unsigned long long search(unsigned int rowsLeft,unsigned int rowA, unsigned int rowB, unsigned int rowC){
  if (rowsLeft == 0)
    return 1;

  // filled another row ?
  unsigned int fullRow = (1 << width) - 1;
  if (rowA == fullRow)
    return search(rowsLeft - 1, rowB, rowC, EmptyRow);

  // find first gap in rowA
  unsigned int pos = 0;
  while ((rowA & (1 << pos)) != 0)
    pos++;

  // unique ID
  unsigned long long hash; // unsigned int would suffice for grid with up to 9 columns, too
  hash   = rowsLeft;
  hash <<= width;
  hash  |= rowA;
  hash <<= width;
  hash  |= rowB;
  hash <<= width;
  hash  |= rowC;

  // about twice as fast as std::map
  static std::unordered_map<unsigned long long, unsigned long long> cache;
  auto i = cache.find(hash);
  if (i != cache.end())
    return i->second;

  unsigned long long result = 0;

  // shape: ##
  //        #
  unsigned int a = rowA;
  unsigned int b = rowB;
  unsigned int c = rowC;
  if (rowsLeft >= 2 && pos < width - 1 &&
      use(pos, a) && use(pos + 1, a) && use(pos, b))
    result += search(rowsLeft, a, b, c);

  // shape: ##
  //         #
  a = rowA; b = rowB; //c = rowC;
  if (rowsLeft >= 2 && pos < width - 1 &&
      use(pos, a) && use(pos + 1, a) && use(pos + 1, b))
    result += search(rowsLeft, a, b, c);

  // shape: #
  //        ##
  a = rowA; b = rowB; //c = rowC;
  if (rowsLeft >= 2 && pos < width - 1 &&
      use(pos, a) && use(pos, b) && use(pos + 1, b))
    result += search(rowsLeft, a, b, c);

  // shape:  #
  //        ##
  // note: this shape extends one "negative" unit to the left
  a = rowA; b = rowB; //c = rowC;
  if (rowsLeft >= 2 && pos > 0 && pos < width &&
      use(pos, a) && use(pos - 1, b) && use(pos, b))
    result += search(rowsLeft, a, b, c);

  // shape:  #
  //         #
  //         #
  a = rowA; b = rowB; //c = rowC;
  if (rowsLeft >= 3 && pos < width &&
      use(pos, a) && use(pos, b) && use(pos, c))
    result += search(rowsLeft, a, b, c);

  // shape: ###
  a = rowA; b = rowB; c = rowC;
  if (rowsLeft >= 1 && pos < width - 2 &&
      use(pos, a) && use(pos + 1, a) && use(pos + 2, a))
    result += search(rowsLeft, a, b, c);

  // memoize
  cache[hash] = result;
  return result;
}

int main(){
  // read grid size
  std::cin >> width >> height;

  // prefer fewer columns, solution will be same tiling is symmetrical
  if (width > height)
    std::swap(width, height);

  std::cout << search(height, EmptyRow, EmptyRow, EmptyRow) << std::endl;
  return 0;
}
