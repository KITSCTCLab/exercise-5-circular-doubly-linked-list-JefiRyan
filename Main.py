class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_at_tail(self, data) -> bool:
        if not self.head:
            self.head = Node(data)
            self.count += 1
            return True
        elif self.head:
            node = Node(data)
            temp = self.head
            while temp:
                x = temp
                temp = temp.next
                if temp == self.head:
                    return False
            node.next = x.next
            x.next = node
            node.previous = x
            self.head.previous = node
            self.count += 1
            return True
        return False
            
            

    def add_at_head(self, data) -> bool:
        if not self.head:
            self.head = Node(data)
            self.count += 1
            return True
        elif self.head:
            node = Node(data)
            temp = self.head
            node.next = temp
            node.previous = temp.previous
            temp.previous = node
            self.head = node
            self.count += 1
            return True
        return False

    def add_at_index(self, index, data) -> bool:
        
        if index == 0:
            return self.add_at_head(data)
        elif index == self.count-1:
            return self.add_at_tail(data)
        elif index > 0 and index < self.count-1:
            node = Node(data)
            temp = self.head
            count = 0
            while temp:
                if count == index-1:
                    node.next = temp
                    node.previous = temp.previous
                    temp.previous = node
                    break
                temp = temp.next
                if temp == self.head:
                    return False
                count += 1
            return True
        else:
            return False


    def get(self, index) -> int:
        temp = self.head
        count = 0
        while temp:
            if count == index:
                return temp.data
            temp = temp.next
            if temp == self.head:
                return False
            count += 1
        return -1

    def delete_at_index(self, index) -> bool:
        temp = self.head
        count = 0
        while temp:
            if count == index:
                temp.previous.next = temp.next
                temp.next.previous = temp.previous
                return True
            temp = temp.next
            if temp == self.head:
                return False
            count += 1
        return False

    def get_previous_next(self, index) -> list:
        temp = self.head
        count = 0
        while temp:
            if count == index:
                return [temp.previous.data,temp.next.data]
            temp = temp.next
            if temp == self.head:
                return False
            count += 1
        return [-1]


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0

for item in input_data.split(', '):
    inner_list = []
    if item.isnumeric():
        data.append(int(item))
    elif item.startswith('['):
        item = item[1:-1]
        for letter in item.split(','):
            if letter.isnumeric():
                inner_list.append(int(letter))
        data.append(inner_list)

obj = DoublyCircularLinkedList()
result = []
for i in range(len(operations)):
    if operations[i] == "add_at_head":
        result.append(obj.add_at_head(data[i]))
    elif operations[i] == "add_at_tail":
        result.append(obj.add_at_tail(data[i]))
    elif operations[i] == "add_at_index":
        result.append(obj.add_at_index(int(data[i][0]), data[i][1]))
    elif operations[i] == "get":
        result.append(obj.get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(obj.get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))

print(result)
