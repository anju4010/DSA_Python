class EquilibriumPoint:
    def solution(self, n, arr):
        l_sum = 0
        total = sum(arr)
        for i in range(1, n):
            l_sum += arr[i-1]
            if l_sum == total - l_sum - arr[i]:
                return i+1



if __name__ == "__main__":
    t = EquilibriumPoint()
    print(t.solution(5, [1,3,5,4,5,2,2]))