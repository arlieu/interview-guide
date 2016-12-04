class HashTable:
    def __init__(self):
        self.size = 13
        self.n = 4
        self.count = 0
        self.load = 0.75
        self.table = []
        for i in range(0, self.size):
            self.table.append([])

    def __nextPrime(self):
        self.size = 2**self.n -1
        self.n += 1

    def __hash(self, key):
        if (type(key) is str):
            hash = ((ord(key)*5)+2)//3        #  random hashing function (replace with better function)

        else:
            hash = (key*5+2)//3

        index = hash % self.size
        return index

    def __resize(self):
        self.__nextPrime()
        tmp = []
        for i in range(0, self.size):
            tmp.append([])

        for i in self.table:
            if len(i) != 0:
                for j in i:
                    index = self.__hash(j)
                    tmp[index].append(j)

        self.table[:] = tmp

    def set(self, key):
        index = self.__hash(key)
        self.table[index].append(key)
        self.count += 1

        if self.count/self.size >= self.load:
            self.__resize()

    def get(self, key):
        index = self.__hash(key)

        return index

    def __getitem__(self, index):
        return self.table[index]

    def __contains__(self, key):
        index = self.__hash(key)

        return key in self.table[index]

    def __len__(self):
        return self.count


test = HashTable()
test.set(100)
test.set(150)
test.set(200)
test.set(211)
for i in test:
    print(i)
print("------------------")
test.set(300)
test.set(400)
test.set(500)
test.set(600)
test.set(700)
test.set(800)
test.set(900)
test.set(1100)
test.set(13)
test.set(15)
test.set(-1)

for i in test:
    print(i)