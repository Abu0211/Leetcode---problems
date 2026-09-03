class Solution:
    def numberOfWeakCharacters(self, properties):

        # Sort by attack ascending and defense descending
        properties.sort(key=lambda x: (x[0], -x[1]))

        maxDefense = 0
        weak = 0

        # Traverse from right to left
        for attack, defense in reversed(properties):

            # If a stronger defense already exists
            if defense < maxDefense:
                weak += 1
            else:
                maxDefense = defense

        return weak