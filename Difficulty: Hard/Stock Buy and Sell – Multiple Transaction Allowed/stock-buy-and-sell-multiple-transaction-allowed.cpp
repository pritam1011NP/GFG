//{ Driver Code Starts
// Initial template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int maximumProfit(vector<int> &prices) {
        // code here
           int n = prices.size();
        //vector<vector<long long>> dp(n+1, vector<long long>(2, -1));

        vector<long long> prev(2, 0), curr(2,0);
        prev[0] = prev[1] = 0;

        for(int idx = n-1; idx >= 0; idx--) {
            for(int buy = 0; buy <= 1; ++buy) {

                long long profit = 0;
                if(buy) {
                    profit = max( -prices[idx] + prev[0], 0 + prev[1]);
                }
                else{
                    profit = max( prices[idx] + prev[1], 0 + prev[0]);
                }

                curr[buy] = profit;
            }
            prev = curr;
        }

        return prev[1];
    }
};


//{ Driver Code Starts.
int main() {
    int t;

    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        int n = arr.size();
        Solution ob;
        int res = ob.maximumProfit(arr);
        cout << res;

        cout << "\n";
    }
    return 0;
}
// } Driver Code Ends