class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        c = 0
        if len(skill) == 2:
            return skill[0] * skill[1]
        skill.sort()
        n = skill[-1] + skill[0]  # 6
        # 123345
        for i in range(len(skill) // 2):
            if skill[i] + skill[-i - 1] == n:
                c = c + (skill[i] * skill[-i - 1])
            else:
                return -1
        return c

if __name__ == "__main__":
    print(Solution().dividePlayers([3,2,5,1,3,4]))
