#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> a, vector<int> b, vector<vector<int>> queries) {
    map<int, int> store;
    vector<int> ans;

    for (int num : a) {
        store[num]++;
    }

    for (const vector<int> &q : queries) {
        if (q[0] == 0) {
            int ind = q[1];
            int val = q[2];
            b[ind] += val;
        } else if (q[0] == 1) {
            int x = q[1];
            int count = 0;
            for (int num : b) {
                count += store[x - num];
            }
            ans.push_back(count);
        }
    }

    return ans;
}


int main() {
    vector<int> a = {1, 2, 3};
    vector<int> b = {1, 4};
    vector<vector<int>> queries = {
        {1, 5},
        {0, 0, 2},
        {1, 5}
    };

    vector<int> result = solution(a, b, queries);

    for (int val : result) {
        cout << val << " ";
    }

    return 0;
}
