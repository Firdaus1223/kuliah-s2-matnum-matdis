from tabulate import tabulate 
import os
os.system("cls")

def tabel(package):
    print(tabulate(package,headers='keys', tablefmt='fancy_grid'))

x0=2
x1=3
tol=0.001
persamaan = ['x^2-2*x-2']
a = [2]
b = [3]
c = [15]


print ("*******")
print ("** BISEKSI **")
print ("*******")
diketahui = {
    "x0" : a,
    "x1" : b,
    "Fungsi" : persamaan,
    "iterasi maksimum" : c
    
}
print ("diketahui pada soal")
tabel(diketahui)
print ("iterasi akan berhenti ketika sudah mencapai iterasi maksimum atau fx lebih dari 0 atau eror\n")
#n=int(input("jumlah iterasi : "))
n=15
i=0
while  i < n  and abs(x1-x0 )>=tol : 
    
    
    x=(x1+x0)/2
    fx=x**2-2*x-2
    fx0=x0**2-2*x0-2
    fx1=x1**2-2*x1-2 
    print ("iterasi :",i)
    print ("==========")
    print ("x0 :",x0, " \t\t\tfx0 :",fx0)
    print ("x1 :",x1, " \t\t\tfx1 :",fx1)
    print ("x  :",x, "\t\t\tfx :",fx)
    print ("eror : ",abs(x1-x0))
    print ("~~~~~~~~~~~~~~~\n")
    i=i+1 
    if fx0 and fx<0 :
        x0=x
    elif fx0 and fx>0:
        x1=x

nama = ["Muhammad rahman"]
nim  = [2109106016]
saya ={
    "nama" : nama,
    "NIM"  : nim,
}
tabel (saya)