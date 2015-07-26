
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data

            else:
                nextslot = self.rehash(hashvalue,len(self.slots))

                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data

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

        while  self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:
                position = self.rehash(key,len(self.slots))
                if position == startslot:
                    stop = True

        return data
 
    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)


wing_hash = HashTable()
wing_hash[54] = 'Bohra'
wing_hash[26] = 'dalakoti'
wing_hash[93] = 'mittal'
wing_hash[17] = 'doga'
wing_hash[77] = 'ashok'
wing_hash[31] = 'jangida'
wing_hash[44] = 'varun'
wing_hash[55] = 'indra'
wing_hash[20] = 'kranthi'

print wing_hash.slots
print wing_hash.data
            




        

    


            
