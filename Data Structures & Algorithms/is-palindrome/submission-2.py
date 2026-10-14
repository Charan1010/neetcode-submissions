class Solution:
    def isPalindrome(self, s: str) -> bool:

        l_p = 0
        r_p = len(s) -1 

        print(l_p)
        print(r_p)

        while l_p < r_p:

            while s[l_p].isalnum() == False  and l_p < r_p:
                l_p += 1

            while s[r_p].isalnum() == False and r_p > l_p:
                r_p -= 1

            if s[l_p].lower() == s[r_p].lower():
                l_p += 1
                r_p -= 1
            else:
                print(s[l_p])
                print(s[r_p])
                return False

        return True
        