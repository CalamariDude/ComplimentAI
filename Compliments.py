import random
class comp:
    def reComp(self, list):
        fh = open("ComplimentsDatabase.txt", "r")
        newList = [""]
        for i in fh:
            for a in list:
                if a in i:
                    if i.find(a):
                        print(i)
                        newList.append(i)


        return (newList[0])