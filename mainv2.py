import csv
import textwrap

import pandas as pd
import sys
import argparse
import inspect


def zapiszMacierzDoPliku(filename, tryb, macierz, args,accuracy):
	file = open(filename, tryb)
	file.write(repr(args))
	file.write('\n')
	file.write(repr(accuracy))
	file.write('\n')
	file.write('|-----------------------------|\n')
	for x in range(len(macierz)):
		file.write('| ')
		for y in range(len(macierz)):
			file.write('{:06.2f}'.format(float(repr(macierz[x][y] / (sum(macierz[x])) * 100))) + '% | ')
		file.write('\n')
		file.write('|-----------------------------|\n')
	file.close()


def retrieve_name(var):
    """
    Gets the name of var. Does it from the out most frame inner-wards.
    :param var: variable to get name from.
    :return: string
    """
    for fi in reversed(inspect.stack()):
        names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
        if len(names) > 0:
            return names[0]


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i][0] > alist[i + 1][0]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


def openCSVToList(filename):
    """

    :param filename:
    :return: Dane w formie Listy
    """
    customset = []
    with open(filename) as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            dataset[x][3] = float(dataset[x][3])
            customset.append((dataset[x]))
    return customset


def divideDateOneColumn(whichData, listOutputX, columnX):
    """

    :param whichData: Jaka baze chcemy podzielic
    :param listOutputX: lista do ktorej wyniki zapiszemy
    :param columnX: Ktora kolumne chcemy zwrocic
    :return:
    """
    for x in range(len(whichData)):
        listOutputX.append(float(whichData[x][columnX]))
    print(retrieve_name(listOutputX) + ' : ' + repr(listOutputX))


def divideDateXY(whichData, listOutputX, listOutputY, columnX, columnY):
    """
    Wydobywa dane z kolumn na X i Y
    :param whichData: jaka baze chcesz podzielic
    :param listOutputX: Lista do ktorej zwrocimy koordynaty X
    :param listOutputY: jw tylko Y
    :param columnX: wybor kolumny odpowiadajacej za X
    :param columnY: wybor kolumny odpowiadajacej za Y
    :return:
    """

    for x in range(len(whichData)):
        # testSetXCoordinate.append(float(testSet[x][0]))
        # testSetYCoordinate.append(float(testSet[x][1]))
        listOutputX.append(float(whichData[x][columnX]))
        listOutputY.append(float(whichData[x][columnY]))
    print(retrieve_name(listOutputX) + ' : ' + repr(listOutputX))
    print(retrieve_name(listOutputY) + ' : ' + repr(listOutputY))


def initParser():
    # Obsluga przez parser
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent('''\
         KLASYFIKACJA GATUNKÓW IRYSÓW

    Liczba klas (gatunków): 3

    Liczba obserwacji:
    - ogólna: 150
    - w zbiorze treningowym: 105
    - w zbiorze testowym: 45

    Atrybuty (kolumny):
    1. długość działki kielicha (ang. sepal length) [cm]
    2. szerokość działki kielicha (ang. sepal width) [cm]
    3. długość płatka (ang. petal length) [cm]
    4. szerokość płatka (ang. petal width) [cm]
    5. gatunek (ang. species):
       0 - setosa
       1 - versicolor
       2 - virginica

             '''))
    # parser.add_argument('n', help='Ilosc atrybutow', type=int)
    parser.add_argument('ATTRIBUTES', type=int, metavar='N', nargs='+',
                        help="Podaj po spacji ktore atrybuty chcesz analizowac")
    parser.add_argument('NEIGHBORS', type=int, help='Podaj jako ostatnia wartosc ilosc sasiadow (liczbe k)')
    parser.add_argument('-v', '--verbose', help="Tryb debug", action='count', default=0)
    parser.add_argument('-s', '--sort', help="Sortowanie przez DataFrame", action='store_true')
    parser.add_argument('-aN', '--allNeighbors', help="Wszyscy sasiedzi [3,5,itd]", action='store_true')

    return parser.parse_args()


def main():
    args = initParser()
    # print(args)
    # print(args.ATTRIBUTES)
    # print(args.verbose)
    listaWyborow = args.ATTRIBUTES
    k = []
    k.append(args.NEIGHBORS)
    if (args.allNeighbors == True):
        k = [1, 3, 5, 7, 9, 11]
    trainingSet = openCSVToList('data_train.csv')
    testSet = openCSVToList('data_test.csv')
    print(k)
    # Przygotowywanie danych
    print('Train set: ' + repr(len(trainingSet)))
    print('Test set: ' + repr(len(testSet)))
    if (args.verbose > 2):
        print(testSet)
    print('------------------------------------------------------')
    print('0. długość działki kielicha (ang. sepal length) [cm]')
    print('1. szerokość działki kielicha (ang. sepal width) [cm]')
    print('2. długość płatka (ang. petal length) [cm]')
    print('3. szerokość płatka (ang. petal width) [cm]')
    print('------------------------------------------------------')
    # while True:
    #     howMany = int(input('Jak wiele cech chcesz przeanalizowac [1,2,3,4] '))
    #     if(howMany>0 and howMany <5):
    #         break
    # listaWyborow=[]
    #
    # for i in range(howMany):
    #     while True:
    #         wybor = int(input('Wybierz '+repr(i+1)+' atrybut do przeanalizowania '))
    #         if(wybor<=3 and wybor>=0):
    #             listaWyborow.append(wybor)
    #             break
    # while True:
    #     k = int(input('Wybierz liczbe sasiadow'))
    #     if(k<=len(trainingSet) and k>0):
    #         break

    # howmany = int(args.n)
    # for i in range(howmany):
    #   listaWyborow.append(int(sys.argv[i+2]))

    # Obsluga przez sys.argv

    # howmany = int(sys.argv[1)
    # for i in range(howmany):
    #   listaWyborow.append(int(sys.argv[i+2]))
    # k = int(sys.args[-1])

    # przygotowanie koordynatow z bazy testowej
    # testSetXCoordinate = []
    # testSetYCoordinate = []
    # divideDateXY(testSet,testSetXCoordinate,testSetYCoordinate,wybor1,wybor2)
    # trainingSetXCoordinate = []
    # trainingSetYCoordinate = []
    # divideDateXY(trainingSet,trainingSetXCoordinate,trainingSetYCoordinate,wybor1,wybor2)
    accuracy = 0
    macierzBledow = []
    for p in range(len(k)):
        macierzBledow = []
        accuracy = 0
        for y in range(len(testSet)):
            odleglosci = []

            for x in range(len(trainingSet)):
                # Jezeli bedzie trzeci wymiar trzeba rozszerzyc wzor
                dist = 0
                # dystans liczony wg liczbyElementow w listcie wyborow
                for z in range(len(listaWyborow)):
                    choice = listaWyborow[z]
                    dist += pow(float(trainingSet[x][choice]) - float(testSet[y][choice]), 2)
                # dist = pow(float(trainingSet[x][0]) - float(testSet[y][0]),2) + pow(float(trainingSet[x][1]) - float(testSet[y][1]),2)

                temp = [dist, trainingSet[x][4]]
                odleglosci.append(temp)
            # print(trainingSet[x])
            if (args.verbose > 3):
                print("Aktualnie analizowany punkt")
                print(testSet[y])

            # Rodzaje sortowań

            # Sortowanie wg. Pythona
            if (args.sort == False):
                odleglosci.sort()
            # bubbleSort(odleglosci)
            # odleglosci.sort(key = lambda x: x[0])

            # Sortowanie wg. DF tutaj bierze w kolejnosci i sortuje po dystansie
            if (args.sort == True):
                df = pd.DataFrame(data=odleglosci, columns=['distance', 'species'])
                df.sort_values(by=['distance'], inplace=True)
                odleglosci = df.values.tolist()
            if (args.verbose > 3):
                print("Posortowane wszystkie odleglosci")
                print(odleglosci)
            # print("Odleglosc ")

            del odleglosci[k[p]:len(odleglosci)]
            if (args.verbose > 2):
                print(odleglosci)
            k_temp = k[p]
            while True:
                setosa = 0
                versicolor = 0
                virginica = 0
                # Voting
                for x in range(k_temp):
                    if int(odleglosci[x][1]) == int(0): setosa = setosa + 1
                    if int(odleglosci[x][1]) == int(1): versicolor = versicolor + 1
                    if int(odleglosci[x][1]) == int(2): virginica = virginica + 1

                if (args.verbose > 1):
                    print('Glosowanie ' + repr(k) + ' sasiadow : Setosa ' + repr(setosa) + ' Versicolor ' + repr(
                        versicolor) + ' virginica ' + repr(virginica))
                speciesByVote = 0
                # Jezeli remis to zmniejsz ilosc sasiadow
                if (setosa == versicolor == virginica):
                    if (args.verbose > 1):
                        print('Remis wszyscy maja po tyle samo zmieniejszam k')
                    k_temp -= 1
                    continue
                # Jezeli dwa wyniki sa takie same i sa maksami to zmniejsz k
                if (setosa == versicolor and setosa > virginica and versicolor > virginica):
                    if (args.verbose > 1):
                        print("Setosa & Versicolor max zmniejszam k")
                    k_temp -= 1
                    continue
                if (setosa == virginica and setosa > versicolor and virginica > versicolor):
                    if (args.verbose > 1):
                        print("Setosa & Virginica max zmniejszam k")
                    k_temp -= 1
                    continue
                if (versicolor == virginica and versicolor > setosa and virginica > setosa):
                    if (args.verbose > 1):
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
            if speciesByVote == 0:
                speciesByVoteHuman = 'Setosa'
            else:
                if speciesByVote == 1:
                    speciesByVoteHuman = 'Versicolor'
                else:
                    speciesByVoteHuman = 'Virginica'
            if int(testSet[y][4]) == 0:
                ActualHuman = 'Setosa'
            else:
                if int(testSet[y][4]) == 1:
                    ActualHuman = 'Versicolor'
                else:
                    ActualHuman = 'Virginica'

            if speciesByVote == int(testSet[y][4]):
                accuracy = accuracy + 1
                if (args.verbose > 0):
                    print("Good")
            else:
                # Human Output
                if (args.verbose > 0):
                    print('speciesByVote -> ' + speciesByVoteHuman + ' : ' + ActualHuman + ' <- Actual')
                # Number Output
                # print('speciesByVote: '+(repr(speciesByVote)+' Actual: '+repr(int(testSet[y][4])))
            temp = [speciesByVote, int(testSet[y][4])]
            # temp = [int(testSet[y][4]),expected]
            macierzBledow.append(temp)
            if (args.verbose > 0):
                print('Iteration: ' + repr(y))
                print('---------------------------------------------------------')
        if (args.verbose > 0):
            print("Koniec petli")
        if len(testSet) - y == 1:
            print("Analized all test values, length of testSet: " + repr(len(testSet)))
        #    print(testSet)
        acc=accuracy / len(testSet)*100
        print("Calkowita SKUTECZNOSC: " + repr(accuracy / len(testSet) * 100))
        # macierz bledow jako pierwsze ma wyniki wyliczone a drugie taki  jaki ma
        print("Votes [speciesByVote, Actual]")
        print(macierzBledow)
        # print(macierzBledow[0][0])

        #   Przewidywane
        # P	 	     Setosa  Versicolor Virignica
        # R Setosa        x       x         x
        # A Versicolor    x       x         x
        # W Wirginica     x       x         x

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
            print('| ', end="")
            for y in range(len(macierz)):
                print('{:06.2f}'.format(float(repr(macierz[x][y] / (sum(macierz[x])) * 100))) + '% ', end="| ")
            print()
            print('|-----------------------------|')

        zapiszMacierzDoPliku("macierzbledow.txt", "a", macierz, args,acc)
        if (macierz[0][0] == macierz[1][1] == macierz[2][2]): print('PERFECT SCORE !!!!!')


main()
