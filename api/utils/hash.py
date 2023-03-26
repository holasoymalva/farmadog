import random

def hashGenerator(data): 
    newHash = data+'!!'+ str(random.getrandbits(128))
    print("hash value: ", newHash)
    return newHash

