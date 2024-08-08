class Solution(object):
    def calPoints(self, ops):
        stack = []
        
        for op in ops:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        
        return sum(stack)

solution = Solution()
print(solution.calPoints(["5", "2", "C", "D", "+"]))  
print(solution.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  
print(solution.calPoints(["1", "C"]))
