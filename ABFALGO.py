existence = {"1":0.5, "2":0.5, "3":0.5, "4":0.5, "5":0.5, "6":0.5, "7":0.5, "8":0.5, "9":0.5}
def certainty(x):
    count0 = 0
    count1 = 0
    for i in range(1,10):
        if x[str(i)]==0:
            count0 += 1
        elif x[str(i)]==1:
            count1 += 1
    if count0==5 or count1==4:
        return False
    else:
        return True
def clearings(x):
    for i in range(1,10):
        if x[str(i)]==0.5:
            x.update({str(i):0})
def response_rec(x):
    h = input("Enter Your Response for "+ x +" :")
    pos_a = 0
    pos_b = 0
    try:
        posA = h[h.index("A")-1]
        if posA == 'B' or posA == 'A':
            pos_a = 1
        else:
            pos_a = int(h[h.index("A")-1])
    except ValueError:
        pos_a = 0
    try:
        posB = h[h.index("B") - 1]
        if posB== 'A' or posB== 'B':
            pos_b = 1
        else:
            pos_b = int(h[h.index("B")-1])
    except ValueError:
        pos_b = 0
    print(pos_a, pos_b)
    return [pos_a, pos_b]
FirstRound = []
SecondRound = []
total_found = 0
while True:
    FirstRound = response_rec("1234")
    SecondRound = response_rec("5678")
    total_found = FirstRound[0] + FirstRound[1] + SecondRound[0] + SecondRound[1]
    if total_found >4:
        print("Wrong Input!")
        continue
    else:
        break
checking_list = ["1234","5678"]
checking_round = [FirstRound, SecondRound]
checker = []
first_limit = FirstRound[0] + FirstRound[1]
print(first_limit)
second_limit = SecondRound[0] + SecondRound[1]
limits = [first_limit, second_limit]
if total_found==4:
    existence.update({'9':0})
    for j in range(0,2):
        count_first = 0
        replacementStarter = 0
        replacementEnder = 0
        if checking_list[j] == "1234":
            checker = checking_round[0]
            replacementEnder = 5
            replacementStarter = 1
        else:
            checker = checking_round[1]
            replacementEnder = 9
            replacementStarter = 5
        for i in range(replacementStarter, replacementEnder):
            if count_first == limits[j]:
                break
            responseNum = response_rec(checking_list[j].replace(str(i),'9'))
            if responseNum != checker:
                print(str(i) + " does exist")
                count_first += 1
                existence.update({str(i):1})
            else:
                print(str(i) + " doesn't exist")
                existence.update({str(i): 0})
            if not certainty(existence):
                break
else:
    existence.update({'9': 1})
    for j in range(0,2):
        count_second = 0
        replacementStarter = 0
        replacementEnder = 0
        if checking_list[j] == "1234":
            checker = checking_round[0]
            replacementEnder = 5
            replacementStarter = 1
        else:
            checker = checking_round[1]
            replacementEnder = 9
            replacementStarter = 5
        for i in range(replacementStarter, replacementEnder):
            if count_second == limits[j]:
                break
            responseNum = response_rec(checking_list[j].replace(str(i),'9'))
            if responseNum != checker:
                print(str(i) + " doesn't exist")
                existence.update({str(i):0})
            else:
                print(str(i) + " does exist")
                count_second += 1
                existence.update({str(i): 1})
            if not certainty(existence):
                break
clearings(existence)
print(existence)