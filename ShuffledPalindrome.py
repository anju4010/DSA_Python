class ShuffledPalindrome:
    def solution1(self, s):
        l = len(s)
        count = 0
        c = [0] * 26
        for i in s:
            c[ord(i) - 97] += 1
        if l%2 == 0:
            for i in c:
                if i%2==0:
                    pass
                else:
                    return 0
            return 1
        else:
            flag=0
            for i in c:
                if i%2!=0:
                    if flag == 0:
                        flag = 1
                    else:
                        return 0
                else:
                    pass
            return 1


if __name__ == "__main__":
    t = ShuffledPalindrome()
    print(t.solution1("abbabba"))