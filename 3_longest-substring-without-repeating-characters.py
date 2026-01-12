class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        dict_ = {}
        result = 0

        i = 0
        dict_[s[i]] = 1
        j = 1

        for j in range(1, len(s)):
            if s[j] in dict_.keys():
                dict_[s[j]] += 1
                print("j", s[j])
                while dict_[s[j]] > 1:
                    dict_[s[i]] -= 1
                    print("i", s[j])
                    i += 1
            else:
                dict_[s[j]] = 1
            result = max(result, j - i + 1)
            print('step')
        return result



# 优化后：
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 使用字典存储字符最后一次出现的下标
        char_map = {}
        result = 0
        start = 0  # 窗口左边界

        for end in range(len(s)):
            # 如果当前字符在字典中，且其索引在当前窗口内
            if s[end] in char_map and char_map[s[end]] >= start:
                # 直接将左边界跳到重复字符上次出现位置的下一个
                start = char_map[s[end]] + 1
            
            # 更新当前字符的最新下标
            char_map[s[end]] = end
            # 更新最大长度
            result = max(result, end - start + 1)
            
        return result
