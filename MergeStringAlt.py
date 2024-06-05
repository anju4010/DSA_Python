class MergeStringAlt:
    def mergeString(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        n = min(l1,l2)
        a = []
        for i in range(n):
            a.append(word1[i])
            a.append(word2[i])

        if l1<l2:
            a.append(word2[i+1:])
        else:
            a.append((word1[i+1:]))
        return "".join(a)

if __name__ == "__main__":
    x = MergeStringAlt()
    print(x.mergeString("abc","pqrst"))

