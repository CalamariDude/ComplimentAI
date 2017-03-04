import Proj
import Compliments

strs = input("http:")


projo = Proj
projo.Proj.mainer(projo, strs)

fh = open("hello.txt", "r")
#firstBracket = fh.read().find("[")
#secondBracket = fh.read().find("]")
line = fh.read()
line = line.split()
lister = [""]
for i in line:

    lister.append(i[i.find("'")+1:i.rfind("'")])
    print(i[i.find("'")+1:i.rfind("'")])




def keywordtop4(list):
    newList = [""]
    for i in range (1,5):
        newList.append(list[i])
    return newList

newLister = keywordtop4(lister)

compliments = Compliments
a = compliments.comp.reComp(compliments, newLister)

print("compliment" + a)