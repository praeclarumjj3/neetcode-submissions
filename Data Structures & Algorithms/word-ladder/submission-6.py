from collections import deque
from typing import List

class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:

        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            current_word, length = queue.popleft()

            if current_word == endWord:
                return length

            for word in words:
                difference = 0

                for idx in range(len(current_word)):
                    if current_word[idx] != word[idx]:
                        difference += 1

                    if difference > 1:
                        break

                if difference == 1 and word not in visited:
                    visited.add(word)
                    queue.append((word, length + 1))

        return 0