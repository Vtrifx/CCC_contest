class Solution:
    def myAtoi(self, s: str) -> int:
        num = ""
        for w in range()
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            if len(num) < 2 and s[i] == "-" or len(num) < 2 and s[i] == "+":
                if len(num) == 1 and num.isnumeric() == True:
                    return int(num)
                elif len(num) == 0:
                    num = s[i]
                else:
                    return 0



            elif s[i].isnumeric() == False and s[i] != " ":
                if num.isnumeric() == True:
                    if int(num) < -(2 ** 31):
                        return -(2 ** 31)
                    elif int(num) > (2 ** 31 - 1):
                        return (2 ** 31 - 1)
                    else:
                        return int(num)

                return 0

            elif s[i].isnumeric() == True:
                num = num + s[i]
        if int(num) < -(2 ** 31):
            return -(2 ** 31)
        elif int(num) > (2 ** 31 - 1):
            return (2 ** 31 - 1)
        else:
            return int(num)
if __name__ == "__main__":
    # print(Solution().myAtoi("1337c0d3"))
    #print(Solution().myAtoi("   -042"))
    # print(Solution().myAtoi("words and 987"))
    print(Solution().myAtoi("+"))