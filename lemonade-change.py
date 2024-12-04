class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        fd = 0  # 5$ bills count
        td = 0  # 10$ bill count
        tof = True
        for i in range(len(bills)):
            if bills[i] == 5:
                fd = fd + 1
                print('added')
            if bills[i] == 10:
                if fd > 0:
                    fd = fd - 1
                    td = td + 1
                    print('added 10 subtracted 5')
                else:
                    tof = False
            if bills[i] == 20:
                if fd < 3 and td == 0 or td == 0 and fd == 0 or fd == 0:
                    tof = False
                if fd >= 3 and td == 0:
                    fd = fd - 3
                    print('subtracted 5')
                if fd > 0 and td > 0:
                    fd = fd - 1
                    td = td - 1
                    print('subtracted 10 and 5')
        return tof

if __name__ == "__main__":
   # print(Solution().lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]))
    print(Solution().lemonadeChange([5,5,10,10,20]))