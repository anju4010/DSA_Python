class LeadersInArrayLeft:
    def solution(self, l):
        temp = l[0]
        a = [l[0]]
        for i in range(len(l)):
            if l[i]>temp:
                temp=l[i]
                a.append(l[i])
        return a


if __name__ == "__main__":
    t = LeadersInArrayLeft()
    print(t.solution([2,4,5,3,10]))