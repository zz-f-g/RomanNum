class RN(object):

    dct = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M' }

    def sep(val): # seperate an integer to the sum of its digits
        Res = []
        den = 10
        while val//den != 0:
            res = val%den
            if res != 0:
                Res.append(res)
            den *= 10
            val -= res
        Res.append(val)
        Res.reverse()
        return Res

    def int2str(val): # convert the digits to letters of Roman Numerals
        den = 1
        while val >= den:
            den *= 10
        den = den // 10
        digit = val // den
        one = RN.dct[den]
        if digit in (1,2,3):
            return one*digit
        else:
            five = RN.dct[den*5]
            if digit == 4:
                return one + five
            elif digit in (5,6,7,8):
                return five + one*(digit-5)
            else:
                ten = RN.dct[den*10]
                if digit == 9:
                    return one + ten

    @property
    def value(self): # This func need improvement that containing kernel codes
        return self._val
    @value.setter
    def value(self, val): # when input value
        if isinstance(val, int) and val > 0 and val <4000:
            self._val = val
        else:
            raise ValueError('Input value need to be an int in 1~3999')
        return val

    @property
    def letter(self): # convert value to letter
        digits = RN.sep(self._val)
        str_digits = list(map(RN.int2str,digits))
        self._letter = ''.join(str_digits)
        return self._letter
    @letter.setter # when input letter, improvement that check if input is valid
    def letter(self, ltr):
        self._letter = ltr
        return ltr