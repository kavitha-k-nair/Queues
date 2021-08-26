class Queue:
    def __init__(self):
        self.capacity = 5
        self.queue = [''] * self.capacity
        self.tail = 0
        self.head = 0


    def resize(self):
        self.capacity += 5
        self.new = [''] * self.capacity
        for i in range(self.tail):
            self.new[i] = self.queue[i]

        return self.new


    def insert(self,ele):
        self.ele = ele

        if self.tail < self.capacity:
            self.queue[self.tail] = self.ele
            self.tail += 1

        else:
            self.queue = self.resize()
            self.insert(self.ele)


    def delete(self):
        if self.head == self.tail:
            print("Queue Empty")
            return

        self.queue[self.head] = '' 
        self.head = self.head+1


    def peek(self):
        if self.head == self.tail:
            print("Queue Empty")
            return
        
        print("Top-most Element:",self.queue[self.head])


    def contains(self,ele):
        self.ele = ele
        for i in range(self.head,self.tail):
            if self.queue[i] == self.ele:
                return True
        return False


    def isEmpty(self):
        if self.head == self.tail:
            return True
        return False


    def isFull(self):
        if self.queue[self.capacity-1] and self.queue[0]:
            return True
        return False
            
        
    def display(self):
        for i in range(self.head,self.tail):
            print(self.queue[i], end='  ')

        print()



q1 = Queue()

print("\n1.Enqueue  2.Dequeue  3.Peek  4.Contains  5.IsEmpty  6.IsFull  7.Display  8.Exit")

while True:
    choice = int(input("\nChoice: "))
    if choice==1:
        ele = input("Element: ")
        q1.insert(ele)

    elif choice==2:
        q1.delete()

    elif choice==3:
        q1.peek()

    elif choice==4:
        ele = input("Element: ")
        print(q1.contains(ele))

    elif choice==5:
        print(q1.isEmpty())

    elif choice==6:
        print(q1.isFull())

    elif choice==7:
        q1.display()

    else:
        exit()
