class CheckPalindrome:
    def solution1(self, n):
        temp = n
        s=0
        while(n>0):
            a=n%10
            s=(s*10)+a
            n=n//10
        return int(s == temp)


    def solution2(self, s):
        return int(s == s[::-1])



if __name__ == "__main__":
    t = CheckPalindrome()
    print(t.solution1(123))
    print(t.solution2("abba"))