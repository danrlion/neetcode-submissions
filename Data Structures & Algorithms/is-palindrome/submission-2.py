class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ind, right_ind = 0, len(s) - 1
        while left_ind < right_ind:
            while not s[left_ind].isalnum() and left_ind < right_ind:
                left_ind += 1
            while not s[right_ind].isalnum() and left_ind < right_ind:
                right_ind -= 1
            if s[left_ind].lower() != s[right_ind].lower():
                return False
            left_ind += 1
            right_ind -= 1
        return True