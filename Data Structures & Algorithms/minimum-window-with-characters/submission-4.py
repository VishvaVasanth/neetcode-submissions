class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        count = {}

        # Required characters
        for c in t:
            count[c] = count.get(c, 0) + 1

        l = 0
        have = 0
        need = len(t)

        minLen = float("inf")
        result = ""

        for r in range(len(s)):

            # Add character
            if s[r] in count:
                count[s[r]] -= 1

                if count[s[r]] >= 0:
                    have += 1

            # All required characters found
            while have == need:

                # Update minimum
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    result = s[l:r + 1]

                # Remove left character
                if s[l] in count:
                    count[s[l]] += 1

                    if count[s[l]] > 0:
                        have -= 1

                l += 1

        return result