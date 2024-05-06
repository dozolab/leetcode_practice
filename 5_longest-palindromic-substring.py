class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(s) + '#'
        longest_subs=""
        max_len=0
        lenmain=len(s)
        for i in range(lenmain):
            substring=s[i]
            left=i-1
            right=i+1
            while left>=0 and right<lenmain:
                if s[left] == s[right]:
                    substring=s[left]+substring+s[right]
                    left-=1
                    right+=1
                else:
                    break
            len_substring=len(substring)
            if len_substring>max_len:
                longest_subs=substring.replace("#", "")
                max_len=len_substring
        return longest_subs
