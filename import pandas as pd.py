#from random import Random
import random
import pandas as pd

class Chelik:
    def __init__(self, name, a=0, b=0):
        self.name = name
        self.a = a
        self.b = b
        self.count = 0
        self.index = []
        self.canWork = []
    def app(self):
        self.count+=1

var1 = "ОБЩАЯ Биология Химия Информат История Общество БУ"
var2 = "ОБЩАЯ Математика Физика ОГЭ Хиструктор Мутаген Английский"
var3 = "ОБЩАЯ Родители Эконом Русский УУ матем УУ рус УУ общ"

t = ["8-10","10-12","12-15","15-17","17-18","18-20","20-24"]

#Cheliki = [Chelik(n[i]) for i in range(15)]
Cheliki = [Chelik("Вадим",10,15),Chelik("Андрей",17,24),Chelik("Карина",18,24),Chelik("Эдик",20,24),Chelik("София",15,18),Chelik("Ксюша",12,17),Chelik("Алеся",12,20),Chelik("Алина",10,15),Chelik("Виталий",8,15),Chelik("Ирина Роман",8,18),Chelik("Настя",8,15),Chelik("Милана",12,18),Chelik("Настя Ф",15,20),Chelik("Оля",8,24),Chelik("Мария",8,24)]
#taimingi = [8,10],12,15,17,18,20,24]
taimingi = [[8,10],[10,12],[12,15],[15,17],[17,18],[18,20],[20,24]]


def time_setting():
    for i in range(16):
        print(Cheliki[i].name)
        print("Введите два числа")
        Cheliki[i].a = int(input())
        Cheliki[i].b = int(input())

def add1():    
    mas = ["","","","","",""]    
    for i in range(6):
        for j in range(14):
                if (Cheliki[j].canWork[i+1] == 1) and (Cheliki[j].count < 3):
                    mas[i] = Cheliki[j].name
                    Cheliki[j].canWork[i+1] = 0
                    Cheliki[j].app()
                    break        
    return mas
def add():
    mas = ["","","","","",""]    
    for i in range(6):
        for j in range(14):
            if (i not in Cheliki[j].index) and (Cheliki[j].count < 3) and ((Cheliki[j].a == taimingi[i][0] and Cheliki[j].b <= taimingi[i][1]) or (Cheliki[j].a >= taimingi[i][0] and Cheliki[j].b == taimingi[i][1]) or (Cheliki[j].a == taimingi[i][0] or Cheliki[j].b == taimingi[i][1]) or (Cheliki[j].a < taimingi[i][0] and Cheliki[j].b > taimingi[i][1])) and mas[i] == "":
            #if (Cheliki[j].count < 3) and ((Cheliki[j].a == taimingi[i][0] and Cheliki[j].b <= taimingi[i][1]) or (Cheliki[j].a >= taimingi[i][0] and Cheliki[j].b == taimingi[i][1]) or (Cheliki[j].a == taimingi[i][0] or Cheliki[j].b == taimingi[i][1]) or (Cheliki[j].a > taimingi[i][0] and Cheliki[j].b < taimingi[i][1])) and mas[i] == "":
                mas[i] = Cheliki[j].name
                Cheliki[j].index.append(i)
                Cheliki[j].app()
                break        
    return mas

def sort():
    random.shuffle(Cheliki)
    for i in range(7):
        for j in range(14):
            if  ((Cheliki[j].a == taimingi[i][0] and Cheliki[j].b <= taimingi[i][1]) or (Cheliki[j].a >= taimingi[i][0] and Cheliki[j].b == taimingi[i][1]) or (Cheliki[j].a == taimingi[i][0] or Cheliki[j].b == taimingi[i][1]) or (Cheliki[j].a < taimingi[i][0] and Cheliki[j].b > taimingi[i][1])):
                Cheliki[j].canWork.append(1)
            else: 
                Cheliki[j].canWork.append(0)

def add2():        
    mas = ["","","","","",""]
    for j in range(14):
        for i in range(6):
            if (Cheliki[j].canWork[i+1] == 1) and (Cheliki[j].count < 3) and mas[i] == "":
                mas[i] = Cheliki[j].name
                Cheliki[j].canWork[i+1] = 0
                Cheliki[j].app()     
    return mas
def firstRow():
    for j in range(14):
        if Cheliki[j].a == taimingi[0][0]:
            Cheliki[j].app()
            Cheliki[j].app()
            return Cheliki[j].name
MorningHuman = firstRow()

sort()
df = pd.DataFrame({'Time': t,
                var1: [MorningHuman] + add2(),
                var2: [MorningHuman]  + add2(),
                var3: [MorningHuman]  + add2()})
df.to_excel('./teams.xlsx',index=False)
