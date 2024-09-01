# ✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13
# from telnetlib import VT3270REGIME
#
# 0 + 1, 1 + 1, 2 + 1, 3 + 2, 5 + 3
####
p1 = 1
c1 = 1
R1 = 0
fact = list[0,1]
num = int (input("enter the number \n"))
for i in range(2, num + 1):   # 3 = 2+1
    R1 = p1+ c1     # 1+1= 2  ; 1 +2 =3 ; 5 =
    p1= c1
    c1=R1           # p1 = c1 : 2
                # c1 = R1 :
    print (f" {R1}" , end= ", ")