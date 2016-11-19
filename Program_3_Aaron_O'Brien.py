__author__ = 'Aaron OBrien'
with open('keywords.txt', 'r') as file1:
    with open('source_cpp.txt', 'r') as file2:
        readFile1 = file1.readlines()
        readFile2 = file2.readlines()
        readFile1.sort()
        for h in readFile1:
            for j in readFile2:
                if h.strip() in j.strip():
                    print h.strip()
                    print