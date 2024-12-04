class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        abcs = {"": 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,'W': 23, 'X': 24, 'Y': 25, 'Z': 26}  # dict with elements

        cnt = 0  # count how many zs
        rc = columnNumber // 26  # incase c>26

        c = columnNumber  # for counting
        r = columnNumber % 26  # next letter


        while c > 26:  # checks how maany times Z repeats
            c = c % 26  #
            cnt = cnt + 1
        txt = "Z" * (cnt - 1) + str(list(abcs.keys())[list(abcs.values()).index(r)])

        return txt

if __name__ == "__main__":
    print(Solution().convertToTitle(1))