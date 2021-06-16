def read():
    with open('data.csv') as data:
        next(data)
        data = data.readlines()
        data = list(map(lambda x: x.rstrip("\n"), data))
        data = list(map(lambda x: x.split(','), data))
        for i in data:
            i[2], i[3] = int(i[2]), int(i[3])
            i[4], i[5], i[6], i[7]  = float(i[4]), float(i[5]), float(i[6]), float(i[7])
            i.append(sum(i[4:]) / 4)
        branchAndAverage = input().split()
        branch = int(branchAndAverage[0])
        compareAverage = float(branchAndAverage[1])
        return data, branch, compareAverage

def alert(patient):
    #Defining a dict for limits
    #               male             female
    limits = {'M':(12.2, 16.6), 'F':(12.6, 15)}
    #              0:low,1:high     0:low,1:high
    #according gender compare hemoglobin vs low limit
    if patient[8] < limits[patient[1]][0]:
        return 'Baja'
    #according gender compare hemo vs high limit
    elif patient[8] > limits[patient[1]][1]:
        return 'Alta'
    else:
        return 'Normal'

def maxAndMinInFiltered(patients):
    list = []
    for i in patients:
        list.append(i[8])
    maxPos = list.index(max(list))
    minPos = list.index(min(list))
    print(patients[maxPos][0], patients[maxPos][1], patients[maxPos][2], alert(patients[maxPos]))
    print(patients[minPos][0], patients[minPos][1], patients[minPos][2], alert(patients[minPos]))

def main():
    data, branch, compareAverage = read()
    patientsFilteredByInputBranch = list(filter(lambda x: x[3] == branch , data))
    maxAndMinInFiltered(patientsFilteredByInputBranch)
    above = len(list(filter(lambda x: x[8] > compareAverage, data)))
    below = len(list(filter(lambda x: x[8] < compareAverage, data)))
    print(above, below, len(data) - above - below)
    print('M', len(list(filter(lambda x: x[1] == 'M', data))))
    print('F', len(list(filter(lambda x: x[1] == 'F', data))))
    for i in range(15):
        print(i + 1, len(list(filter(lambda x: x[3] == i + 1, data))))

if __name__ == '__main__':
    main()
