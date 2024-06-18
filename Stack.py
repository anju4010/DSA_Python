class Stack:
    def __init__(self):
        self.stack_elements = []

    def push(self,p):
        self.stack_elements.append(p)

    def pop(self):
        if not self.stack_elements:
            return
        element = self.stack_elements[-1]
        del self.stack_elements[-1]
        return element

    def clear(self):
         self.stack_elements.clear()

    def size(self):
        return len(self.stack_elements)

    def top(self):
        if not self.stack_elements:
            return
        return self.stack_elements[-1]

    def print(self):
        if not self.stack_elements:
            print("No elements in stack")
            return
        for i in self.stack_elements:
            print(i)


if __name__ == "__main__":
    t = Stack()
    print("Select any one of the below options:")
    print("1. Push\n2. Pop\n3. Clear\n4. Size\n5. top\n6. Print\n7. Exit")
    while True:
        sel = int(input("Enter your selection: "))
        match sel:
            case 1:
                ele = input("Enter a value to push into stack: ")
                t.push(ele)
                print(f"Element {ele} is pushed into stack.")
            case 2:
                element = t.pop()
                if element is None:
                    print("Nothing to pop from stack")
                    continue
                print(f"Element {element} is popped from stack.")
            case 3:
                t.clear()
                print("Cleared all the elements.")
            case 4:
                ele = t.size()
                print(f"Size of stack is {ele}:")
            case 5:
                ele = t.top()
                if ele is None:
                    print("No elements in the stack")
                    continue
                print(f"{ele} is the top of the stack.")
            case 6:
                t.print()
            case 7:
                print("Exiting the program")
                break
            case _0:
                print("Error out of bound of the selection")
