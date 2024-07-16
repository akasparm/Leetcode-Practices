class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = r = 0
        local_max = 0
        global_max = 0
        vowels = "aeiou"
    
        while r<len(s):
            if s[r] in vowels:
                local_max += 1
            r+=1
            
            if r-l>k:
                l+=1
                if s[l-1] in vowels:
                    local_max -= 1
            
            if local_max == k:
                return k
            
            if global_max < local_max:
                global_max = local_max

        return global_max