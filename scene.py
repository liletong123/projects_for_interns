# j = 10


# def xonvert(nums):
#     sum_ = 0
#     # print(j)
#     for i in nums:
#         sum_ = sum_ + i
#     return sum_

#     print(sum_)
# 

s='asfvft'
# 无重复字符的最长子串
class Solution():
    def lengthOfLongestSubstring(self,s:str) -> int:
        # 判断是否有重复的字符，用数据结构哈希集合set
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为-1，相当于我们字符串的左边界的左侧，还没有开始移动
        rk, ans = -1,0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移动一个字符
                occ.remove(s[i-1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        print(s[ans])
if __name__ == '__main__':
    m = Solution()
    m.lengthOfLongestSubstring(s)
