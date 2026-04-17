# INTERSECTION UPDATE
class MySet:
    def __init__(self):
        self.data = []

    def add(self, value):
        if value not in self.data:
            self.data.append(value)

    def intersection_update(self, other):
        yangi = []

        for item in self.data:
            if item in other.data:
                yangi.append(item)

        self.data = yangi

    def show(self):
        print(self.data)

s1 = MySet()
s1.data = [1, 2, 3, 4]

s2 = MySet()
s2.data = [3, 4, 5, 6]

s1.intersection_update(s2)

s1.show()  
