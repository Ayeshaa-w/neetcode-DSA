class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in "+-/*":
                stack.append(int(i))
            else:
                b=stack.pop()
                a=stack.pop()
                if i=="+":
                    stack.append(a+b)
                elif i=="-":
                    stack.append(a-b)
                elif i=="/":
                    stack.append(int(a/b))
                elif i=="*":
                    stack.append(a*b)
        return stack[0]

        