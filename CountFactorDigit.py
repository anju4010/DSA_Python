class CountFactorDigit:
    def solution(self,n):
        count = 0
        temp = n
        while(n>0):
            a = n%10
            if temp%a == 0:
                count+=1
            n = n//10
        return count


if __name__ == "__main__":
    t = CountFactorDigit()
    print(t.solution(124))