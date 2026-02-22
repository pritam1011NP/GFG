class Solution:    
    def findUnion(self, a, b):
        # Create a set and add all elements from both arrays
        union_set = set(a) | set(b)
        
        # Return as a list (order doesn't matter as per problem)
        return list(union_set)