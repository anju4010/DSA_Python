class MissingElement:
    def solution(self,n, arr):
        for i in range(1,n+1):
            if i in arr:
                 pass
            else:
                return i

    def solution1(self, n, arr):
        x = n*(n+1)//2
        s = 0
        for i in arr:
             s = s+i
        return x - s



if __name__ == "__main__":
    t = MissingElement()
    print(t.solution(5, [1,3,4,5]))
    print(t.solution1(5, [1,4,3,5]))