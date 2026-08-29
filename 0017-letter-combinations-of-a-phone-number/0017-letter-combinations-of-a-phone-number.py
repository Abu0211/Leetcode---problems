class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        # If input is empty, return empty list
        if not digits:
            return []

        # Phone keypad mapping
        phone = {
            "0": "",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        path = []

        def backtrack(index):
            # Base case: all digits are processed
            if index == len(digits):
                result.append("".join(path))
                return

            # Get letters corresponding to current digit
            letters = phone[digits[index]]

            # Try every possible letter
            for letter in letters:
                path.append(letter)        # Choose

                backtrack(index + 1)      # Explore

                path.pop()                # Unchoose (Backtrack)

        # Start from first digit
        backtrack(0)

        return result