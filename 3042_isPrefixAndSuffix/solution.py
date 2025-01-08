class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                str1, str2 = words[i], words[j]
                l1, l2 = len(words[i]), len(words[j])
                if l1 <= l2 and str2[:l1] == str1 and str2[-l1:] == str1:
                    result += 1
        return result