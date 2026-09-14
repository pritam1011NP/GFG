class Solution:
    def getCount(self, root, k):
        if root is None:
            return 0

        stack = [(root, 1)]
        leaf_costs = []

        while stack:
            node, level = stack.pop()

            # Leaf node
            if node.left is None and node.right is None:
                leaf_costs.append(level)
                continue

            if node.right:
                stack.append((node.right, level + 1))

            if node.left:
                stack.append((node.left, level + 1))

        # Visit cheapest leaves first
        leaf_costs.sort()

        count = 0
        budget = k

        for cost in leaf_costs:
            if cost > budget:
                break

            budget -= cost
            count += 1

        return count