from typing import List

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_nodes = [-1] * (n + 1)
        bob_nodes = [-1] * (n + 1)

        def find_parent(family, node):
            if family[node] < 0:
                return node
            family[node] = find_parent(family, family[node])
            return family[node]

        num_redundant_edges = 0

        for typ, u, v in edges:
            if typ == 3:
                p_u = find_parent(alice_nodes, u)
                p_v = find_parent(alice_nodes, v)

                if p_u != p_v:
                    alice_nodes[p_u] += alice_nodes[p_v]
                    alice_nodes[p_v] = p_u
                else:
                    num_redundant_edges += 1

        bob_nodes = alice_nodes.copy()

        for typ, u, v in edges:
            if typ == 1:
                p_u = find_parent(alice_nodes, u)
                p_v = find_parent(alice_nodes, v)

                if p_u != p_v:
                    alice_nodes[p_u] += alice_nodes[p_v]
                    alice_nodes[p_v] = p_u
                else:
                    num_redundant_edges += 1

            if typ == 2:
                p_u = find_parent(bob_nodes, u)
                p_v = find_parent(bob_nodes, v)

                if p_u != p_v:
                    bob_nodes[p_u] += bob_nodes[p_v]
                    bob_nodes[p_v] = p_u
                else:
                    num_redundant_edges += 1

        al = min(alice_nodes)
        bl = min(bob_nodes)

        if al == bl and al == -n:
            return num_redundant_edges
        else:
            return -1