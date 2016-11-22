p = open("predictions.txt", 'r')
d = open("test.vw", 'r')

x = 0
n = 0

for line in d:
    n += 1
    if (p.readline()[:1] == line[:1]):
        x += 1
        
p.close()
d.close()

print("accuracy: ", (x / n) * 100, "%")
