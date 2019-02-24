bool inBounds(int row, int col, int N){
    return (row >= 0 && col >=0 && row < N && col < N);
}
// Complete the diagonalDifference function below.
int diagonalDifference(vector<vector<int>> arr) {
    int leftDiag=0;
    int leftI=0, leftJ=0;
    while(inBounds(leftI,leftJ,arr.size()))
    {
        leftDiag+=arr[leftI][leftJ];
        ++leftI;
        ++leftJ;
    }
    int rightDiag = 0;
    int rightI = 0, rightJ = arr.size()-1;
    while (inBounds(rightI, rightJ, arr.size())) {
      rightDiag += arr[rightI][rightJ];
      ++rightI;
      --rightJ;
    }
    return abs(leftDiag - rightDiag);
}