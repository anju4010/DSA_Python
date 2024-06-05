class PanagramString:
    def solution_1(self, s):
        l = s.lower()
        for i in range(97,123):
            if chr(i) in l:
                pass
            else:
                return 0
        return 1

    def solution_2(self, s):
        l = s.lower()
        m = [0]*26
        for i in l:
            if ord(i)>=97 and ord(i)<=122:
                m[ord(i)-97] = 1

        for i in m:
            if i == 0:
                return 0
        return 1

if __name__ == "__main__":
    x = PanagramString()
    print(x.solution_1("The quick brown fox jumps over a lazy dog"))
    print(x.solution_2("The quick brown fox jumps over a lazy dog"))