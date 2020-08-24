
#include <iostream>
#include <vector>

// 100x100 grid
const unsigned int Size = 100;
// matrix from problem statement
unsigned short matrix[Size][Size];

// sum of the highest value of the current row and all further rows (sum[current..15])
unsigned int maxRemaining[Size];

// try to find the highest value for "optimum"
// row        - current row, start at top-most row 0
// columnMask - bitmask of all used columns (1 - used, 0 - available)
// sum        - current sum
// atLeast    - best solution so far
unsigned int search(unsigned int row = 0, unsigned int columnMask = 0, unsigned int sum = 0, unsigned int atLeast = 0){
  // done ?
  if (row == Size)
    return sum;

  // even if choosing the highest value of each of the next rows:
  // is it possible hat this combination exceeds the previously highest sum ?
  if (sum + maxRemaining[row] <= atLeast)
    return 0;

  // look at all values of the current row
  for (unsigned int column = 0; column < Size; column++){
    // column already used ?
    auto mask = 1 << column;
    if ((columnMask & mask) != 0)
      continue;

    // "occupy" column and continue with next row
    auto current = search(row + 1, columnMask | mask, sum + matrix[row][column], atLeast);
    if (atLeast < current)
      atLeast = current;
  }
  return atLeast;
}

int main(){
  // find highest element of each row
  unsigned int n;
  std::cin>>n;

  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      std::cin>>matrix[i][j];
    }
  }

  unsigned int maxValuePerRow[Size];
  for (unsigned int row = 0; row < Size; row++){
    maxValuePerRow[row] = matrix[0][row];
    for (unsigned int column = 1; column < Size; column++)
      if (maxValuePerRow[row] < matrix[column][row])
        maxValuePerRow[row] = matrix[column][row];
  }
  // compute the maximum sum of the last rows, ignoring collisions (invalid choices)
  maxRemaining[Size - 1] = maxValuePerRow[Size - 1];
  for (auto row = Size - 1; row > 0; row--)
    maxRemaining[row - 1] = maxRemaining[row] + maxValuePerRow[row - 1];

  // let's go !
  std::cout << search() << std::endl;
  return 0;
}
