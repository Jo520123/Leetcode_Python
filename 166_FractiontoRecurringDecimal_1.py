class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :param numerator:
        :param denominator:
        :return: str
        """
        neg_symbol = numerator * denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)

        numbers =[]
        deci_dic = dict()
        deci_str = None
        c = 0

        while True:
            numbers.append(str(numerator//denominator))
            c += 1
            numerator = 10 * (numerator % denominator)

            if numerator == 0:
                break

            posi = deci_dic.get(numerator)

            if posi:
                deci_str = "".join(numbers[posi:c])
                break

            deci_dic[numerator] = c

        result = numbers[0]

        if len(numbers) > 1:
            result += "."

        if deci_str:
            result += "".join(numbers[1:len(numbers)-len(deci_str)]) + "(" + deci_str +")"
        else:
            result += "".join(numbers[1:])

        if neg_symbol:
            result = "-" + result

        return result
