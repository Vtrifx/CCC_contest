class Solution:
    def maxPower(self, s: str) -> int:
        c = 1
        l = s[0]
        rc = c  # highest count
        if len(set(s)) == 1:
            rc = len(s)


        for i in range(1, len(s)):
            if s[i] == l:
                c = c + 1

            elif s[i] != l:
                if c > rc:
                    rc = c
                c = 1
                l = s[i]
        if c > rc:
            rc = c

        return rc


if __name__ == "__main__":
    print(Solution().maxPower("aabbbbbccccdddddddeffffffggghhhhhiiiiijjjkkkkkllllmmmmmnnnnnoopppqrrrrsssttttuuuuvvvvwwwwwwwxxxxxyyyzzzzzzzz"))
    print(Solution().maxPower("cc"))
