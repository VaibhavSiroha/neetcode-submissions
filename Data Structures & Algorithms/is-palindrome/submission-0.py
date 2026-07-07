class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        n=len(clean)//2
        for i in range(n):
            if clean[-i-1]!=clean[i]:
                return False
        return True
