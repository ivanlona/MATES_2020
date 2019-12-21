import time


def es_divisible(n,divisor):
  if int(n/divisor)==n/divisor:
    return True
  else:
    return False
def factores(numero):
  f=[]
  for i in range(2,numero+1):
    while es_divisible(numero,i):
      f.append(i) 
      numero=numero/i
  return(f)
      

def mcm(numero_uno,numero_dos):
  j=factores(numero_uno)
  t=factores(numero_dos)
  for g in range(len(t)):
      for k in range(len(j)):
        if t[g]==j[k]:

          j.remove(j[k])
          break
  resultado=t+j
  total=1
  for m in resultado:
    total=total*m 
  return(total)


def mcm_bruto(n1,n2):
  start = time.time()
  for h in range(1,n1*n2+1):
    if es_divisible(h,n1) and es_divisible(h,n2):
      end = time.time()

      print (end - start)
      return(h)
  




#mcm_bruto(11*13*17*23,29*31*37*43)
def min_mul(numeros):
  v=2
  z=numeros[0]
  for i in range(1,len(numeros)):
    z=mcm(z,numeros[i])
    
  return(z)
#min_mul()






#******************************************************
#*********************   FIN PRIMOS********************
#******************************************************



class fracc:
    def __init__(self, numerador, denominador):
        self.nu = numerador
        self.de = denominador

    def imprime(self):
        return (str(self.nu) + "/" + str(self.de))

    def __str__(self):
        return (self.imprime())

def fracc_simpl(fraccioncita):
  hghh=mcd_bruto(fraccioncita.nu,fraccioncita.de)
  a128=fraccioncita.nu/hghh
  b128=fraccioncita.de/hghh
  r=fracc(int(a128),int(b128))
  return r


def suma(a, b):
    comun_denominador = mcm(a.de, b.de)
    numeradorA=comun_denominador/a.de*a.nu
    numeradorB=comun_denominador/b.de*b.nu
    numerador_total=numeradorA+numeradorB
    r=fracc(int(numerador_total),comun_denominador)
    r=fracc_simpl(r)
    return r



def mcd(numero_uno,numero_dos):
  j=factores(numero_uno)
  t=factores(numero_dos)
  resultado=[]
  for g in range(len(t)):
      for k in range(len(j)):
        if t[g]==j[k]:
          resultado.append(t[g])

          j.remove(j[k])
          break
  
  total=1
  for m in resultado:
    total=total*m 
  return(total)


def mcd_bruto(n101,n102):
  max_cd=1

  for i in range(1,n102+1):
    if es_divisible(n101,i) and es_divisible(n102,i):
      max_cd=i
  return max_cd

def mcd_mul(numeros):
  v=2
  z=numeros[0]
  for i in range(1,len(numeros)):
    z=mcd(z,numeros[i])
    
  return(z)


def divi_fracc(fracc1,fracc2):
  r=fracc(fracc1.nu*fracc2.de,fracc1.de*fracc2.nu)
  fracc_simpl(r)
  print(r)







#**************************************
#*              test                  *
#**************************************
def test():
  print("Iván López -->Verano 2018")
  print("")
  print("factores(numero)")
  print("calcula los factores primos de un numero")
  print("Ej:factores(540)")
  print(factores(540))
  print("")

  print("mcm(numero_uno,numero_dos)")
  print("calcula el minimo comun multiplo")
  print("Ej:mcm(14,18)")
  print(mcm(14,18))
  print("")

  print("min_mul(numeros)")
  print("calcula el minimo comun multiplo de muchos numeros")
  print("Ej:min_mul([2,3,4,5])")
  print(min_mul([2,3,4,5]))
  print("")

  print("fracc(numerador,denominador)")
  print("sive para hacer una fraccion")
  print("Ej:a=fracc(3,4)")
  print("   print(a)")
  a=fracc(3,4)
  print(a)
  print("")

  print("suma(fraccion1,fraccion2)")
  print("suma fracciones")
  print("Ej:a=fracc(3,4)")
  print("   b=fracc(5,6)")
  print("   print(suma(a,b))")
  a=fracc(3,4)
  b=fracc(5,6)
  print(suma(a,b))
  print("")
  

  print("mcd_bruto(numero_uno,numero_dos)")
  print("calcula el Máximno comun divisor")
  print("Ej:mcd_bruto(28,16)")
  print(mcd_bruto(28,16))
  print("")


  print("mcd_mul(numeros)")
  print("calcula el maximo comun divisor de muchos numeros")
  print("Ej:mcd_mul([10,20,30])")
  print(mcd_mul([10,20,30]))
  print("")


  print("fracc_simpl(fraccion)")
  print("sive para simplificar una fraccion")
  print("Ej:a=fracc(6,12)")
  print("   print(fracc_simpl(a))")
  a=fracc(6,12)
  print(fracc_simpl(a))
  print("")


  print("mcd(numero_uno,numero_dos)")
  print("calcula el Máximno comun divisor")
  print("Ej:mcd(28,16)")
  print(mcd(28,16))
  print("")


  print("divi_fracc(fracc1,fracc2)")
  print("sive para dividir fracciones")
  print("Ej:a=fracc(3,2)")
  print("b=fracc(1,3")
  print("divi_fracc(a,b)")
  a=fracc(3,2)
  b=fracc(1,3)
  divi_fracc(a,b)
  print("")
test()