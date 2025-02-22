#include <bits/stdc++.h>
using namespace std;

const int INF = 1e18+7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    vector<string> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    vector<vector<int>> ans(n, vector<int>(n, INF));
    
    for (int i = 0; i < n; i++) {
        ans[i][i] = 0;
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i][j] != '-' && i != j) {
                ans[i][j] = 1;
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                ans[i][j] = 0;
                continue;
            }
            
            vector<vector<bool>> visited(n, vector<bool>(n, false));
            visited[i][j] = true;
            
            queue<tuple<int, int, int>> q;
            q.push({i, j, 0});
            bool found = false;
            
            while (!q.empty()) {
                queue<tuple<int, int, int>> nq;
                
                while (!q.empty()) {
                    auto [x, y, l] = q.front();
                    q.pop();
                    if(l >= ans[i][j]) continue;
                    
                    if (ans[x][y] != INF) {
                        if (ans[x][y] == -1) continue;
                        ans[i][j] = min(ans[i][j], l + ans[x][y]);
                        found = true;
                        continue;
                    }
                    
                    for (int u = 0; u < n; u++) {
                        if (u == y && a[x][u] != '-' && !visited[u][y]) {
                            ans[i][j] = min(l + 1, ans[i][j]);
                            found = true;
                            nq.push({x, u, l + 1});
                        }
                        for (int v = 0; v < n; v++) {
                            if (a[x][u] == a[v][y] && a[x][u] != '-' && !visited[u][v]) {
                                visited[u][v] = true;
                                if (u == v) {
                                    ans[i][j] = min(l + 2, ans[i][j]);
                                    found = true;
                                }
                                nq.push({u, v, l + 2});
                            }
                        }
                    }
                }
                q = nq;
            }
            
            if (!found) {
                ans[i][j] = -1;
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << ans[i][j] << " ";
        }
        cout << "\n";
    }
    
    return 0;
}