class MaxSumOfDigits:

    def sumofdigits(self, n):
        s = 0
        while (n > 0):
            a = n % 10
            s = s + a
            n = n // 10
        return s

    def maxdigits(self, l):
        m1 = l[0]
        for i in l[1:]:
            if self.sumofdigits(i) > self.sumofdigits(m1):
                m1 = i
        return m1


if __name__ == "__main__":
    x = MaxSumOfDigits()
    print(x.maxdigits([1897, 999, 432, 123, 567]))



