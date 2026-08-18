class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = 0  # Pointer for children (g)
        j = 0  # Pointer for cookies (s)
        
        while i < len(g) and j < len(s):
            # If the current cookie can satisfy the current child
            if s[j] >= g[i]:
                i += 1  # Child is satisfied, move to the next child
            j += 1      # Move to the next cookie regardless
            
        return i