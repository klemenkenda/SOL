from sol_fun import *
from os import path
import csv
tek={}
stanjeLige={}
kat=set()
for j in range(1,17):
    dat="./Registracije/registracije"+str(j)+".csv"
    if not path.isfile(dat):
        break
    tekmaRegistracije=j
    #Na kateri še ne šteje za točkovanje.
    #Še ni vključeno, vljuči enkrat.
    with open(dat,'r',encoding="utf-8") as f:
        for i in f:
            a=i.split(";")
            st=a[0]
            ime=a[1]
            priimek=a[2]
            klub=a[3]
            kate=a[4]
            s=presledki(sumniki(a[1]+a[2]))
            s=s.lower()
            if kate[-1] == "\n":
                kate = kate[:-1]
            kat.add(kate)
            if ime=="Žiga" and priimek=="Groff":
                st="483"
            elif ime == "Cesare" and priimek == "Tarrabocchia":
                klub = "OK Azimut"
            elif ime == "Andraž" and priimek == "De Luisa":
                klub = "OK Azimut"
            if s not in tek.keys():
                tek[s]=[kate,ime,priimek,tekmaRegistracije,klub,st]
    for i in kat:
        stanjeLige[i]={}
    for i in tek.keys():
        b=tek[i]
        stanjeLige[b[0]][i]={"ime":b[1],"priimek":b[2],"klub":b[4],0:0,"tekmaRegistracije":b[3]}

st_tekem=0
IP=1
zadnja=16
for st_lige in range(1,12):
    if st_lige==zadnja:#Nočemo, da se zgodi v sol, je pa na voljo.
        IP=1.15
    if path.isfile('./Rezultati/SOL'+str(st_lige)+'.csv'):
        c=rezultati(st_lige,stanjeLige,kat,tek)
        st_lige1 = (lambda st_lige: lambda kate="": st_lige if st_lige < 5 or kate not in ["M21E", "M21A", "M18", "M35", "M45", "Ž21E"] else st_lige - 1)(st_lige)
        stanjeLige=izracunLige(c,st_lige1,stanjeLige,IP,kat,tek)
        #print(stanjeLige["M55"])
        #print(stanjeLige["M21E"]["jurezmrzlikar"])
        st_tekem+=1
        vCsv(stanjeLige,st_tekem,kat,tek)

if path.isfile('./Resna stanja/SOL'+str(st_tekem)+'.csv'):
    g=open('sol_2017.csv','w',encoding='utf-8')
    with open('./Resna stanja/SOL'+str(st_tekem)+'.csv','r',encoding='utf-8') as f:
        for i in f.readlines():
            g.write(i)
    g.close()
