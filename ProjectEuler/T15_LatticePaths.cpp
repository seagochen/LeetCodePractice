/**
Starting in the top left corner of a 2×2 grid, and only being able to 
move to the right and down, there are exactly 6 routes to the
bottom right corner.
 */

#include <iostream>

using namespace std;

int main() {
    // create a map to store the number of paths
    int n = 20;
    long long grid[n + 1][n + 1];

    // set the number of paths for the boundaries to 1
    for (int i = 0; i <= n; i++) {
        grid[i][0] = 1;
        grid[0][i] = 1;
    }

    // update the inner the number of paths of inner grids
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1];
        }
    }

    // print out the result
    cout << grid[n][n] << endl;
    return 0;
}