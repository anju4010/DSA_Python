class CountSmallerElements:
    def findElementCount(self, n, a, x):
        count = 0
        for i in a:
        #     print(i)
            if i <= x:
                count+=1
            else:
                break
        return count

    def test(self):
        n = int(input("enter a number"))
        a = list(map(int, input(f"enter {n} numbers").split(",")))
        if len(a) != n:
            print(f"got more/less than {n} element(s)")
            exit(1)
        x = int(input("enter a number"))
        print(self.findElementCount(n, a, x))

if __name__ == "__main__":
    x = CountSmallerElements()
    x.test()
