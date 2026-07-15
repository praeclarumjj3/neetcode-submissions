from typing import List
from collections import defaultdict
import heapq


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {char: 0 for word in words for char in word}

        # Compare neighboring words to infer ordering rules.
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            min_len = min(len(word1), len(word2))

            # Invalid case: longer word appears before its exact prefix.
            # Example: ["abc", "ab"]
            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                return ""

            for j in range(min_len):
                if word1[j] != word2[j]:
                    before = word1[j]
                    after = word2[j]

                    if after not in graph[before]:
                        graph[before].add(after)
                        indegree[after] += 1

                    # Only the first differing character gives information.
                    break

        # Topological sort.
        # A heap gives a deterministic lexicographically smaller result
        # when multiple valid orders exist.
        available = [char for char in indegree if indegree[char] == 0]
        heapq.heapify(available)

        order = []

        while available:
            char = heapq.heappop(available)
            order.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    heapq.heappush(available, neighbor)

        # Not every character was processed, so the graph has a cycle.
        if len(order) != len(indegree):
            return ""

        return "".join(order)