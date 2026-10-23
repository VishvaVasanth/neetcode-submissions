class Solution:
    def calPoints(self, operations: List[str]) -> int:

        s = []

        for r in operations:
            if r == "+":
                a = s[-1]
                b = s[-2]
                s.append(a+b)
            elif r == "D":
                s.append(s[-1]*2)
            elif r =="C":
                s.pop()
            else:
                s.append(int(r))
        return sum(s)


        