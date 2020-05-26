class Solution:
    def IntToRoman(self,num):
        """
            :type num: int
            :rtype: str
            """
        A = ["","M","MM","MMM"]
        B = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        C = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        D = ["","I","II","III","IV","V","VI","VII","VIII","IX"]


        return A[num//1000] + B[(num % 1000)//100] + C[(num % 100)//10] + D[num % 10]






