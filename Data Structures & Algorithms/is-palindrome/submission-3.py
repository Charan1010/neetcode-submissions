class Solution:
    def isPalindrome(self, s: str) -> bool:
        sub_s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        #print(sub_s[::-1])

        if sub_s[::-1] == sub_s:
            return True
        else:
            return False