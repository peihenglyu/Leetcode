class Solution(object):
    def longestValidSubstring(self, word, forbidden):
        """
        :type word: str
        :type forbidden: List[str]
        :rtype: int
        """
        max_len = 0
        left = 0
        right = 0
        forbidden = set(forbidden)
        track_q = []
        while right < len(word):

            for i in range(len(track_q)):
                if i > 10:
                    print("len error")
                track_q[i] = track_q[i] + word[right]
            track_q.append(word[right])
            if len(track_q) > 10:
                track_q.pop(0)

            for track in track_q:
                if track in forbidden:
                    cur_len = right - left
                    forb_len = len(track)
                    if cur_len > max_len:
                        max_len = cur_len
                    left = right - forb_len + 2
                    right = left - 1
                    track_q = []
                    break
            
            if right == len(word) - 1:
                cur_len = right - left + 1
                if cur_len > max_len:
                    max_len = cur_len
            right += 1

        return max_len

obj = Solution()
print(obj.longestValidSubstring("a",["a"]))
print(obj.longestValidSubstring("cbaaaabc",["aaa","cb"]))
print(obj.longestValidSubstring("leetcode",["de","le","e"]))
print(obj.longestValidSubstring("abab",["aab","abab","cacb","bab"]))
print(obj.longestValidSubstring("babbb",["bbb","aacb","babbb","bcab"]))
print(obj.longestValidSubstring("cacbbcbccbbbabaabccbcccbacbbcbabcabbcabbabcacacbacbbabcbabbbcaccabaacbbbbaabccacbabccbababaaabcabccbabbabbabbacbabacbccbbccacbbbaacaccbcbbbcaaaaccaacabbabbaacaacccaababcaccacbaabbabbbaababcccbaaaacacbcacbbbbcbababbaaaacbacbccaccaabcaaabcaccbaabaabaabababcbaccbacbbcbbcbcbacacbabbaccaaabbbcccbcccbcbcbbbbcaaaaaababcbbabcacaaabaabcabcabcb",
                                ["bbc","aacbbbbaab","bbcabbab","c","c","abcacacba","bbbbbc","bccbbaa","bcbaccaaab","bbaaba","ccbaaaacac","cbbaaaa","acbaabbbab","cbbbcbc","baabcca","a","cb","baabccbcc","bcabb","accbb","ccbbaa","b","acbcbbabba","caab","b","cbcb","aca","bbcb","acbcacbbc","b","abbbabcb","c","cacb","abbaaaacb","abc","babbbaba","bcbb","bccbc","cc","abbaaaa","cc","cccbaaaac","b","accccba","bccac","bcccaaa","bc","bcbaccbacb","aacac","ccaab","bbba","abc","bcbaa","aba","babacbcc","bbaccbabab","c","bacbb","ba","acb","babcc","bcbc","aaabca","abcb","aaccaacabb","bbabaac","bcaaabc","acbaabbab","abaab","caabc","bb","bb","aabccbcc","cbbbcbcca","baab","abbabba","bbc","abb","caccbaba","abbaa","bbaacacc","aab","ca","bbb","bcaccacba","b","baab","bcabccac","bcc","bbbaabccac","ba","acbbb","abaccbcbc","b","a","cbcaccabaa","ab","acbaabbab","accabcba","bcaaabaa"]))
