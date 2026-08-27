class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0

    
    def get(self, index: int) -> int:
        

        current = self.head

        if current == None:
            return -1

        for i in range(0, index+1):
            if i == index:
                return current.value
            elif current.upcoming == None:
                return -1
            else:
                current = current.upcoming
        
    def insertHead(self, val: int) -> None:

        if self.head == None:
            self.head = self.Node(val, None)
        else:
            new_second_node = self.head
            new_third_node = self.head.upcoming
            self.head = self.Node(val, new_second_node)
            new_second_node.upcoming = new_third_node

        self.size += 1

    def insertTail(self, val: int) -> None:

        if self.head == None:
            self.head = self.Node(val,None)
        else:
            current = self.head
            for i in range(0, self.size):
                if current.upcoming == None:
                    to_add = self.Node(val, None)
                    current.upcoming = to_add
                else:
                    current = current.upcoming

        self.size += 1

        

    def remove(self, index: int) -> bool:
        current = self.head
        previous = None

        if current == None:
            return False

        if index == 0:
            to_remove = self.head
            new_head = to_remove.upcoming
            self.head= new_head
            to_remove.upcoming = None
            self.size -=1
            return True

        for i in range(0, index+1):
            if i == index:
                to_remove = current
                previous.upcoming = to_remove.upcoming
                to_remove.upcoming = None
                self.size -= 1
                return True
            elif i > index:
                return False
            elif i == self.size-1:
                return False
            elif i != index:
                previous = current
                current = current.upcoming
            else: 
                return False

    def getValues(self) -> List[int]:

        arr = []
        current = self.head

        print(self.size)

        for i in range(0, self.size ):
            arr.append(current.value)
            print(current.value)
            current = current.upcoming
        
        return arr
            
        


    class Node:

        def __init__(self, val: int, upcoming: Node | None):
            self.value = val
        
            self.upcoming = upcoming
        