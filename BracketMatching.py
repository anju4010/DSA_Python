from Stack import Stack
class BracketMatching:
    def solution(self, b):
        t = Stack()
        for i in b:
            if i in '([{':
                t.push(i)
            else:
                a = t.pop()
                if i == ')' and a == '(':
                    pass
                elif i == ']' and a == '[':
                    pass
                elif i == '}' and a == '{':
                    pass
                else:
                    return 0
        if t.size() == 0:
            return 1
        return 0


if __name__ == "__main__":
    t = BracketMatching()
    print(t.solution("[{(]}]"))