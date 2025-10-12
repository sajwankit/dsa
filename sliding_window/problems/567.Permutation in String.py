#
# @lc app=leetcode id=567 lang=python3
# @lcpr version=30203
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0

        s1d = {}
        for c in s1:
            s1d[c] = s1d.get(c, 0) + 1

        window_data = {}
        valid = 0

        # right now nothing is included in the window as currently we
        # are [0, 0)
        # so we begin adding elements in the window, by moving r to right+1 
        # question: till when to move r?


        while r < len(s2):

            c = s2[r] # we got the character to include in the window but we haven't added it yet 
            r += 1 # this marks the expansion of window, so now, our window at this point has become [0,1) .. so would mean element at index 0 is included in the window


            window_data[c] = window_data.get(c, 0) + 1
            if c in s1d:
                if window_data[c] == s1d[c]:
                    valid += 1
            
            

            # now comes the contraction part
            # we contract when window has reached length of s1
            # also while contracting we will need to check if at any contraction stage window becomes valid 

            while (r-l) >= len(s1):

                if valid == len(s1d):
                    return True

                c = s2[l]

                l += 1 # contract the window
        

                # BELOW IS WRONG
                # THINK WHY? 
                # if we check like below
                # the case where window_data[c] was already less than s1d[c]
                # and we are removing c from window, then valid should not be decremented
                # because it was already not matching, 
                # window_data[c] = window_data[c] - 1
                # if c in s1d:
                    
                #     if window_data[c] < s1d[c]:
                #         valid -= 1

                if c in s1d:
                    if window_data[c] == s1d[c]:  # Check BEFORE decrementing
                        valid -= 1 
                window_data[c] = window_data[c] - 1

        return False

if __name__ == "__main__":
    s = Solution()
    # print(s.checkInclusion("ab", "aaaacbac"))
    # print(s.checkInclusion("aaa", "baaaab")) 
    # print(s.checkInclusion("xyzxyz", "abcdefghijklmnozyxzyx"))
    # print(s.checkInclusion("abcde", "zzzzabcdezzzz"))
    # print(s.checkInclusion("abc", "aebdc")) 
    # print(s.checkInclusion("abc", "bbbca"))
    print(Solution().checkInclusion("ab", "eidba ooo"))

        
# @lc code=end


# @lcpr case=start
# "ab"\n"aaaabc"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"eidbaooo"\n

# @lcpr case=start
# "ab"\n"aaaabc"\n
# @lcpr case=end

#
# @lcpr case=start
# "ab"\n"eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"eidboaoo"\n
# @lcpr case=end

# @lc

