# 3.6 Animal Shelter
class Queue:
    def __init__(self):
        self.list1 = []
    def enqueue(self,name,category):
        self.list1.append[(name,category)]
    def dequeueAny(self):
        self.list1.reverse()
        x = self.list1.pop()
        self.list1.reverse()
        return x
    def dequeueDog(self):
        self.list.reverse()
        index = -1
        while True:
            if (index*-1 == len(list1)+1):
                print("There is no dog")
                return False
            if self.list1[index][1] == "Dog":
                x = self.list1.remove((self.list1[index],"Dog"))
                self.list1.reverse()
                return x
            else:
                index = index - 1

     def dequeueCat(self):
        self.list.reverse()
        index = -1
        while True:
            if (index*-1 == len(list1)+ 1):
                print("There is no cat")
                return False
            if self.list1[index][1] == "Cat":
                x = self.list1.remove((self.list1[index],"Cat"))
                self.list1.reverse()
                return x
            else:
                index = index - 1
                
           
           

