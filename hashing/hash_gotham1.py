# HashTable class has two lists slots for storing keys
# and data for storing values

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    # adds a new key,vlaue pair to hash table

    def put(self,key,data):
        
        # get the hash value for that key 
        hashvalue = self.hashfunction(key,len(self.slots))

        # if slot for that hashvalue is empty then put key,value pair
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.slots[hashvalue] = data

        # if slot for that hashvalue is not empty
        else:
            # if key is same then replace data
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data

            # if key is not same the look for other slots
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                
                # now if nextslot is notemply and key is not the same
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    # then look for next slot do rehashing again
                    nextslot = self.rehash(hashvalue,len(self.slots))

                    # if nextslot is empty add the key, value pair 
                    if self.slots[nextslot] == None:
                        self.slots[nextslot] = key
                        self.data[nextslot] = data
                    # if nextslot is not empty
                    else:
                        self.data[nextslot] = data
                

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        found = False
        stop = False
        position = startslot

        # there is some value in that slot so lets' check for that value
        
        while self.slots[position] != None and not found and not stop:
            # if that slot is the key job done
            if self.slots[position] == key:
                found = True
                data = self.data[position]

            # if key is not present in that slot then rehash and check again
            else:
                position = self.rehash(key,len(self.slots))

            # if rehashed position is the same value the stop
                if position == startslot:
                    stop = True

        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)
