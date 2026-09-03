class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        curr = []
        wordSet = set(wordDict)

        def f(i):
            if i == len(s):
                ans.append(" ".join(curr))
                return

            for j in range(i, len(s)):
                word = s[i:j + 1]

                if word in wordSet:
                    curr.append(word)
                    f(j + 1)
                    curr.pop()

        f(0)
        return ans