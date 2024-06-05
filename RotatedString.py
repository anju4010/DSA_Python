class RotatedString:
    def solution(self, a, b):
        if a == b[2:] + b[0:2]:
            return 1
        elif a == b[-2:] + b[:-2]:
            return 1
        else:
            return 0
if __name__ == "__main__":
    x = RotatedString()
    print(x.solution("amazon", "onamaz"))
