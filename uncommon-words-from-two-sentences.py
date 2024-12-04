class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        l1 = s1.split()
        l2 = s2.split()
        l = []
        if len(l1) == len(l2):
            for i in range(len(l2)):
                if l2[i] not in l1:
                    l = l + [l1[i]]
                    l = l + [l2[i]]
        return l


if __name__ == "__main__":
    print(Solution().uncommonFromSentences("this apple is sweet", "this apple is sour"))
