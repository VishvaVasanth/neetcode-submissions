class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        x, y, z = target

        a = False
        b = False
        c = False

        for triplet in triplets:

            
            if (triplet[0] > x or
                triplet[1] > y or
                triplet[2] > z):
                continue

            
            if triplet[0] == x:
                a = True

            if triplet[1] == y:
                b = True

            if triplet[2] == z:
                c = True

        return a and b and c