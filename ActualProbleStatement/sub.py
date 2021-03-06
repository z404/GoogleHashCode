with open('c.txt') as file:
    simtime, intersection, numroads, numcars, bonuspoints = [int(i.rstrip('\n')) for i in file.readline().split()]
    roaddict = {}
    for j in range(numroads):
        i = file.readline()
        data = i.rstrip('\n').split()
        roaddict.update({data[2]:{"start":data[0],"end":data[1],"time":data[3]}})
    print(roaddict)
    carlst = []
    for j in range(numcars):
        i = file.readline().rstrip('\n').split()
        carlst.append(i[1:])

for i in carlst:
    print(sum([int(roaddict[j]['time']) for j in i[1:]]))

