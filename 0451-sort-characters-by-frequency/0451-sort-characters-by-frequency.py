import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        sorted_chars = counts.most_common()
        result = []
        for char, freq in sorted_chars:
            result.append(char * freq)
        return "".join(result)