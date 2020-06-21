class Solution:
    def calculate(self, s):
        """
        :param s: str
        :return: int
        """
        digit1 = []
        pre = '+'
        n = 0

        for i,j in enumerate(s):
            if j.isdigit():
                n = n *10 + int(j)

            if j in '+-*/' or i == len(s)-1:
                if pre == '+':
                    digit1.append(n)
                elif pre == '-':
                    digit1.append(-n)
                elif pre == '*':
                    digit1.append(digit1.pop() * n )
                elif pre == '/':
                    dp = digit1.pop()
                    if dp < 0:
                        digit1.append(int(dp/n))
                    else:
                        digit1.append(dp // n)
                pre = j
                n = 0

        sum_digit = sum(digit1)

        return sum_digit
