class MaximizeArraySum:
    def solution(self, arr):
        arr.sort()
        s = 0
        for i in range(len(arr)):
            s = s + (arr[i] * i)
        return s


if __name__ == "__main__":
    t = MaximizeArraySum()
    print(t.solution([5,3,2,4,1]))