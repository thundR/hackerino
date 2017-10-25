import pickle

with open('banner.p','rb') as f:
    obj = pickle.load(f)
    print(str(obj))
    for array1 in obj:
        line = ""
        for array2 in array1:
            line += (array2[0]*array2[1])
        print(line)