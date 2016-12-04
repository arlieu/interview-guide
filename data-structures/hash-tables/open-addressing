class HashTable:
    def __init__(self):
        self.size = 13
        self.n = 4
        self.count = 0
        self.load = 0.6
        self.table = [None]*self.size

    def __nextPrime(self):
        self.size = 2**self.n -1
        self.n += 1

    def __hash(self, key):              #  random hashing function (replace with better function)
        if (type(key) is str):          #  accepts chars, strings, and ints
            hash = ((ord(key)*5)+2)//3

        else:
            hash = (key*5+2)//3

        index = hash % self.size
        return index

    def __resize(self):
        self.__nextPrime()
        tmp = [None]*self.size

        for i in self.table:
            if i is not None:
                index = self.__hash(i)
                if tmp[index] is None:
                    tmp[index] = i
                else:
                    j = 1
                    newIndex = index + 1
                    if newIndex >= self.size:
                        newIndex %= self.size

                    while tmp[newIndex]:
                        #j += 1                     #  linear probing
                        j = (j+1)**2                #  quadratic probing
                        newIndex += j

                        if newIndex >= self.size:
                            newIndex %= self.size

                    tmp[newIndex] = i

        self.table[:] = tmp

    def set(self, key):
        index = self.__hash(key)
        if self.table[index] is None:
            self.table[index] = key

        else:
            i = 1
            newIndex = index + 1
            if newIndex >= self.size:
                newIndex %= self.size

            while self.table[newIndex]:
                #i += 1                     #  linear probing
                i = (i+1)**2                #  quadratic probing
                newIndex += i

                if newIndex >= self.size:
                    newIndex %= self.size

            self.table[newIndex] = key

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

        return key == self.table[index]

    def __len__(self):
        return self.count