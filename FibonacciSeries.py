class FibonacciSeries:
    def solution(self, n):
        a,b = 0,1
        s=0
        x = [1]
        while(n>1):
            s=a+b
            x.append(s)
            a=b
            b=s
            n-=1
        return x


if __name__ == "__main__":
    t = FibonacciSeries()
    print(t.solution(1))
