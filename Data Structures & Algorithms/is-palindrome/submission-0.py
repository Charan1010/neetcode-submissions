class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_refined = re.sub(r'[^A-Za-z0-9]', '', s).lower()

        #print(s_refined)

        return s_refined == s_refined[::-1]
        