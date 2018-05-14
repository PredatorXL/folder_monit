from os import walk


path1 = []

while True:
    for (dirpath, dirnames, filenames) in walk("C:/Users/Darek/Desktop/test"):
        path1.extend(filenames)
        path2 = []
        for (dirpath, dirnames, filenames) in walk("C:/Users/Darek/Desktop/test"):
            path2.extend(filenames)

        file = list(set(path2) - set(path1))
        print(path1)
        print(path2)
        print(file)