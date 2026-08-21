class Solution:
    def numberOfTurns(self, root, p, q):

        # Find path from root to a given value.
        # Store 'L' or 'R' for every edge.
        def find_path(target):
            stack = [(root, [])]

            while stack:
                node, path = stack.pop()

                if node is None:
                    continue

                if node.data == target:
                    return path

                if node.right:
                    stack.append((node.right, path + ['R']))

                if node.left:
                    stack.append((node.left, path + ['L']))

            return None

        path_p = find_path(p)
        path_q = find_path(q)

        # If either node doesn't exist
        if path_p is None or path_q is None:
            return -1

        # Find the first position where paths differ.
        i = 0
        while (i < len(path_p) and
               i < len(path_q) and
               path_p[i] == path_q[i]):
            i += 1

        # Remove the common root -> LCA portion
        p_path = path_p[i:]
        q_path = path_q[i:]

        # Count turns in a single path
        def count_turns(path):
            turns = 0

            for j in range(1, len(path)):
                if path[j] != path[j - 1]:
                    turns += 1

            return turns

        turns_p = count_turns(p_path)
        turns_q = count_turns(q_path)

        # If one node is the LCA, there is no extra turn
        if not p_path or not q_path:
            result = turns_p + turns_q
        else:
            # Moving from one subtree to the other at LCA
            # creates one additional turn.
            result = turns_p + turns_q + 1

        # No turns at all => -1
        if result == 0:
            return -1

        return result