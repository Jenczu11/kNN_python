import csv
import sys
import pandas as pd
def main():
    # prepare data
    trainingSet = []
    testSet = []
    with open('data_train.csv') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            dataset[x][3] = float(dataset[x][3])
            trainingSet.append(dataset[x])
    with open('data_test.csv') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        # print(dataset)
        for x in range(len(dataset)):
            # for y in range(4):
            dataset[x][3] = float(dataset[x][3])
            testSet.append(dataset[x])
    # Przygotowywanie danych
    print('Train set: ' + repr(len(trainingSet)))
    print('Test set: ' + repr(len(testSet)))
    print(testSet)
    print('------------------------------------------------------')
    print('0. długość działki kielicha (ang. sepal length) [cm]')
    print('1. szerokość działki kielicha (ang. sepal width) [cm]')
    print('2. długość płatka (ang. petal length) [cm]')
    print('3. szerokość płatka (ang. petal width) [cm]')
    # while True:
    #     # noinspection PyBroadException
    #     try:
    #         wybor1 = int(input('Wybierz pierwszy atrybut do przeanalizowania '))
    #         wybor2 = int(input('Wybierz drugi atrybut do przeanalizowania '))
    #         # TODO: tutaj powinno byc zabezpieczenie iloscsasiadow!>iloscwTrainSet
    #         k = int(input('Wybierz liczbe sasiadow'))
    #         break
    #     except:
    #         print("Serio nie uzyles inta")
    wybor1=int(sys.argv[1])
    wybor2=int(sys.argv[2])
    k=int(sys.argv[3])
    # przygotowanie koordynatow z bazy testowej
    testSetXCoordinate = []
    testSetYCoordinate = []
    # Atrybuty (kolumny):
    # 0. długość działki kielicha (ang. sepal length) [cm]
    # 1. szerokość działki kielicha (ang. sepal width) [cm]
    # 2. długość płatka (ang. petal length) [cm]
    # 3. szerokość płatka (ang. petal width) [cm]
    # 4. gatunek (ang. species):
    for x in range(len(testSet)):
        # testSetXCoordinate.append(float(testSet[x][0]))
        # testSetYCoordinate.append(float(testSet[x][1]))
        testSetXCoordinate.append(float(testSet[x][wybor1]))
        testSetYCoordinate.append(float(testSet[x][wybor2]))
    print('TestSet X coordinate: ' + repr(testSetXCoordinate))
    print('TestSet Y coordinate: ' + repr(testSetYCoordinate))
    # Przygotowanie koordynatow z bazy trenujacej

    trainingSetXCoordinate = []
    trainingSetYCoordinate = []
    # Sasiedzi sztywno

    # k = 9
    # Atrybuty (kolumny):
    # 0. długość działki kielicha (ang. sepal length) [cm]
    # 1. szerokość działki kielicha (ang. sepal width) [cm]
    # 2. długość płatka (ang. petal length) [cm]
    # 3. szerokość płatka (ang. petal width) [cm]
    # 4. gatunek (ang. species):
    for x in range(len(trainingSet)):
        # trainingSetXCoordinate.append(float(trainingSet[x][0]))
        # trainingSetYCoordinate.append(float(trainingSet[x][1]))
        trainingSetXCoordinate.append(float(trainingSet[x][wybor1]))
        trainingSetYCoordinate.append(float(trainingSet[x][wybor2]))
    print('Trening Set X coordinate:  ' + repr(trainingSetXCoordinate))
    print('Trening Set Y coordinate:  ' + repr(trainingSetYCoordinate))
    accuracy = 0
    macierzBledow = []
    for y in range(len(testSet)):
        odleglosci = []
        for x in range(len(trainingSet)):
            # Jezeli bedzie trzeci wymiar trzeba rozszerzyc wzor
            # dist=(kolumna1train[x]-kolumna1test[0])*(kolumna1train[x]-kolumna1test[0])+(kolumna2train[x]-kolumna2test[0])*(kolumna2train[x]-kolumna2test[0])
            dist = (trainingSetXCoordinate[x] - testSetXCoordinate[y]) * (
                    trainingSetXCoordinate[x] - testSetXCoordinate[y]) + (
                           trainingSetYCoordinate[x] - testSetYCoordinate[y]) * (
                           trainingSetYCoordinate[x] - testSetYCoordinate[y])
            temp = [dist, trainingSet[x][4]]
            odleglosci.append(temp)
           # print(trainingSet[x])
        #print("Aktualnie analizowany punkt")
        #print(testSet[y])

        def bubbleSort(alist):
            for passnum in range(len(alist) - 1, 0, -1):
                for i in range(passnum):
                    if alist[i][0] > alist[i + 1][0]:
                        temp = alist[i]
                        alist[i] = alist[i + 1]
                        alist[i + 1] = temp
        #odleglosci.sort()
        #odleglosci.sort(key = lambda x: x[0])
        bubbleSort(odleglosci)
        #self.data.sort_values(by=['distance'], inplace='True')
        #print("Posortowane wszystkie odleglosci")
        #print(odleglosci)
        #print("Odleglosc ")
        del odleglosci[k:len(odleglosci)]
        #print(odleglosci)
        k_temp=k
        while True:
            setosa = 0
            versicolor = 0
            virginica = 0
            #Voting
            for x in range(k_temp):
                if int(odleglosci[x][1]) == int(0): setosa = setosa + 1
                if int(odleglosci[x][1]) == int(1): versicolor = versicolor + 1
                if int(odleglosci[x][1]) == int(2): virginica = virginica + 1

            print('Glosowanie ' + repr(k) + ' sasiadow : Setosa ' + repr(setosa) + ' Versicolor ' + repr(
                versicolor) + ' virginica ' + repr(virginica))
            speciesByVote = 0
            #Jezeli remis to zmniejsz ilosc sasiadow
            if(setosa==versicolor==virginica):
                print('Remis wszyscy maja po tyle samo zmieniejszam k')
                k_temp-=1
                continue
            if(setosa==versicolor & setosa>virginica & versicolor>virginica):
                print("Setosa & Versicolor max zmniejszam k")
                k_temp -= 1
                continue
            if(setosa==virginica & setosa>versicolor & virginica>versicolor):
                print("Setosa & Virginica max zmniejszam k")
                k_temp -= 1
                continue
            if(versicolor==virginica & versicolor>setosa & virginica>setosa):
                print("Versicolor & Virginica max zmniejszam k")
                k_temp -= 1
                continue
            if max(setosa, versicolor, virginica) == setosa:
                speciesByVote = 0
                break
            if max(setosa, versicolor, virginica) == versicolor:
                speciesByVote = 1
                break
            if max(setosa, versicolor, virginica) == virginica:
                speciesByVote = 2
                break
        if speciesByVote==0:
            speciesByVoteHuman='Setosa'
        else:
            if speciesByVote==1:
                speciesByVoteHuman='Versicolor'
            else:
                speciesByVoteHuman='Virginica'
        if int(testSet[y][4])==0:
            ActualHuman='Setosa'
        else:
            if int(testSet[y][4])==1:
                ActualHuman='Versicolor'
            else:
                ActualHuman='Virginica'

        if speciesByVote == int(testSet[y][4]):
            accuracy = accuracy + 1
            print("Good")
        else:
            # Human Output
            print('speciesByVote -> ' + speciesByVoteHuman + ' : ' + ActualHuman + ' <- Actual')
            # Number Output
            # print('speciesByVote: '+(repr(speciesByVote)+' Actual: '+repr(int(testSet[y][4])))
        temp = [speciesByVote, int(testSet[y][4])]
        #temp = [int(testSet[y][4]),expected]
        macierzBledow.append(temp)
        print('Iteration: '+repr(y))
        print('---------------------------------------------------------')
    print("Koniec petli")
    if len(testSet)-y==1:
        print("Analized all test values, length of testSet: "+repr(len(testSet)))
#    print(testSet)
    print("Calkowita SKUTECZNOSC: " + repr(accuracy / 45 * 100))

    # macierz bledow jako pierwsze ma wyniki wyliczone a drugie taki  jaki ma
    print("Votes [speciesByVote, Actual]")
    print(macierzBledow)
    # print(macierzBledow[0][0])

    #   Przewidywane
    #P	 	     Setosa  Versicolor Virignica
    #R Setosa        x       x         x
    #A Versicolor    x       x         x
    #W Wirginica     x       x         x

    macierz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for x in range(len(macierzBledow)):
        # pewniaki
        if (macierzBledow[x][0] == macierzBledow[x][1]) and (macierzBledow[x][0] == 0): macierz[0][0] = macierz[0][
                                                                                                            0] + 1
        if (macierzBledow[x][0] == macierzBledow[x][1]) and (macierzBledow[x][0] == 1): macierz[1][1] = macierz[1][
                                                                                                            1] + 1
        if (macierzBledow[x][0] == macierzBledow[x][1]) and (macierzBledow[x][0] == 2): macierz[2][2] = macierz[2][
                                                                                                            2] + 1
        # Przewidziana/Prawdziwa
        # Setosa/Versicolor
        if macierzBledow[x][0] == 0 and macierzBledow[x][1] == 1: macierz[1][0] = macierz[1][0] + 1
        # Setosa/Virginica
        if macierzBledow[x][0] == 0 and macierzBledow[x][1] == 2: macierz[2][0] = macierz[2][0] + 1
        # Versicolor/Setosa
        if macierzBledow[x][0] == 1 and macierzBledow[x][1] == 0: macierz[0][1] = macierz[0][1] + 1
        # Versicolor/Virginica
        if macierzBledow[x][0] == 1 and macierzBledow[x][1] == 2: macierz[2][1] = macierz[2][1] + 1
        # Virginica/Setosa
        if macierzBledow[x][0] == 2 and macierzBledow[x][1] == 0: macierz[0][2] = macierz[0][2] + 1
        # Virginica/Versicolor
        if macierzBledow[x][0] == 2 and macierzBledow[x][1] == 1: macierz[1][2] = macierz[1][2] + 1
    # mieszane
    print("ConfusionTab [Setosa, Versicolor, Virginica]")
    print(macierz)
    print("Confusion matrix [Setosa, Versicolor, Virginica]")
    print('       Real/Expected')
    print('|-----------------------------|')
    for x in range(len(macierz)):
        print('| ',end="")
        for y in range(len(macierz)):
            print('{:06.2f}'.format(float(repr(macierz[x][y] / (sum(macierz[x])) * 100))) + '% ', end="| ")
        print()
        print('|-----------------------------|')



main()
