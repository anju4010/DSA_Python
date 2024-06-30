import math
class PerfectNumber:
    def solution(self, n):
        s = 0
        for i in range(1,n):
            if n%i == 0:
                s = s+i
        return int(n == s)

    def solution1(self, n):
        s = 1
        for i in range(2, int(math.sqrt(n))):
            if n%i == 0:
                s+=i
                s+=n//i
        return int(n == s)



if __name__ == "__main__":
    t = PerfectNumber()
    print(t.solution(28))
    print(t.solution1(28))