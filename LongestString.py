class LongestString:
    def findLength(self, n):
        return len(n)

    def findLongestString(self, l):
        m = l[0]
        for i in l[1:]:
            if self.findLength(i) > self.findLength(m):
                m = i
        return m

if __name__ == "__main__":
    t = LongestString()
    print(t.findLongestString(["anjali", "aeio", "eek", "cat", "sailovesanjali"]))