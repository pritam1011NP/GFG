//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            String line = br.readLine();
            String[] tokens = line.split(" ");

            // Create an ArrayList to store the integers
            ArrayList<Integer> array = new ArrayList<>();

            // Parse the tokens into integers and add to the array
            for (String token : tokens) {
                array.add(Integer.parseInt(token));
            }

            int[] arr = new int[array.size()];
            int idx = 0;
            for (int i : array) arr[idx++] = i;

            System.out.println(new Solution().minJumps(arr));
            // System.out.println("~");
        }
    }
}

// } Driver Code Ends


class Solution {
    static int minJumps(int[] arr) {
        int n = arr.length;
        
        // Edge case: If the first element is 0, we cannot move forward
        if (n == 1) return 0;
        if (arr[0] == 0) return -1;
        
        // Initialize variables
        int maxReach = arr[0]; // The farthest point reachable
        int steps = arr[0];    // Steps we can still take in the current jump
        int jumps = 1;         // Number of jumps made so far

        // Start traversing the array
        for (int i = 1; i < n; i++) {
            // Check if we've reached the end of the array
            if (i == n - 1) return jumps;

            // Update the farthest point reachable
            maxReach = Math.max(maxReach, i + arr[i]);

            // Use a step to move forward
            steps--;

            // If no steps are left
            if (steps == 0) {
                jumps++; // We need to make another jump

                // If the current index is beyond the maxReach, return -1
                if (i >= maxReach) return -1;

                // Reset steps to the amount of steps to reach maxReach from the current position
                steps = maxReach - i;
            }
        }
        return -1;
    
    // code here
    }
}