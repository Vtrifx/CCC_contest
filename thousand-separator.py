class Solution:
    def thousandSeparator(self, n: int) -> str:
        ns = ''
        c = 0 # counting from end
        s = str(n)
        for i in reversed(range(len(s))):  # goes from end to start
            if c % 3 == 0 and c != 0:
                ns = ns + "." + s[i]
            else:
                ns += s[i]
            c = c + 1
        return ns[::-1]


        #     if len(s) <= 3:  # if the number is smaller the 3 digits long
        #         return str(n)
        #     elif i % 3 != 0 or i == len(s):  # if the index divisible by 3 or the index is the last
        #         ns = ns + s[i]
        #     elif i % 3 == 0 and i != len(s):
        #         ns = ns + "."+ s[i]
        # ns = ns[::-1]
        # if ns[-1] == ".":
        #     ns = ns[:len(ns) - 1]
        return ns

if __name__ == "__main__":
    print(Solution().thousandSeparator(123456789))
    print(Solution().thousandSeparator(1234))