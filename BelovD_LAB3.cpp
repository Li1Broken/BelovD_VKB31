#include <iostream>
#include <vector>

using namespace std;

int Levenshtein(string A, string B)
{
    auto n = A.size();
    auto m = B.size();
    vector<vector<int>> F(n+1, vector<int>(m+1));
  
    for (auto i = 0; i < n + 1; ++i) {
        F[i][0] = i;
    }

    for (auto j = 0; j < n + 1; ++j) {
        F[0][j] = j;
    }

    for (auto i = 1; i < n + 1; ++i) {
        for (auto j = 1; j < m + 1; ++j) {
            F[i][j] = min(F[i - 1][j], F[i][j - 1]) + 1;
            F[i][j] = min(F[i][j], F[i - 1][j - 1] + (A[i - 1] != B[j - 1]));

            if (i >= 2 && j >= 2 && ((A[i - 2] + A[i - 1]) == (B[j - 1] + B[j - 2]))) {
                F[i][j] = min(F[i][j], F[i - 2][j - 2] + 1);
            }
        }
    }
      return F[n][m];
}

int main() {
    string word1;
    string word2;
    std::cin >> word1;
    std::cin >> word2;
    auto ex = Levenshtein(word1, word2);
    std::cout << ex << endl;
    return 0;
}
