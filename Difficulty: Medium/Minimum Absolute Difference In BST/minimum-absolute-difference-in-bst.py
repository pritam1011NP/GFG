class Solution:
    def absDiff(self, root):
        stack = []
        curr = root

        prev = None
        ans = float('inf')

        while stack or curr:
            # Go to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Compare with previous inorder value
            if prev is not None:
                ans = min(ans, curr.data - prev)

            prev = curr.data

            # Move to right subtree
            curr = curr.right

        return ans