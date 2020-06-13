fhand = open("romeo.txt")

wordlist = []
for line in fhand:
    #print(line)
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in wordlist:
            wordlist.append(word)


wordlist.sort()
print(wordlist)