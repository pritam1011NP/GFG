class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
    # Initialize all vertices with 0 so that
    # negative cycles in disconnected components
    # are also detected.
        dist = [0] * V

    # Relax all edges V times
        for i in range(V):
            updated = False

            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True

                # If relaxation is possible on the
                # V-th iteration, a negative cycle exists.
                    if i == V - 1:
                        return True

            if not updated:
                break

        return False