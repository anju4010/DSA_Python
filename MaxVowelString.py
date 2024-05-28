class MaxVowelString:
    def findMaxVowelString(self, s):
        m = s[0]
        for i in s[1:]:
            if self.vowelcount(i)>self.vowelcount(m):
                m = i
        return m

    def vowelcount(self, x):
        count = 0
        for i in x:
            if i in('a','e','i','o','u'):
                count += 1
        return count


if __name__ == "__main__":
    m = MaxVowelString()
    print(m.findMaxVowelString(["anjali", "aeio", "eek", "cat"]))