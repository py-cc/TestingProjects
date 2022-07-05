from datetime import datetime, timedelta
import calendar
import re


#Funcion para guardar valor
def spentUser(value):
    pass


#Funcion manejo de calendario
def calendarDate(numWeek):
    now = datetime.now()
    numWeek = numWeek * 7
    datePass = now - timedelta(days=numWeek)
    #NOTA: QUITAR EL RESULTADO EN NEGATIVO
    print("Registro de -20 dolares el dia {}".format(datePass))

stringUser = input() # Tomar cadena
print()

#NOTAS:
#Tomar la fecha actual AÑO,MES,DIA
#Uso de weekday() toma el dia actual en forma de [0-6] siendo 0 el Lunes y 6 el domingo
#Tomar un longitud del pasado "de" "esta" "semana" "pasada"
#Tomar una longitud del pasado "de" "la" "semana" "pasada"
#------------------------------------------------------


#Testing
#"20 dolares en comida hace 2 semanas"
#"20 dolares en comida el lunes hace 2 semanas"
#"20 dolares en comida hace 2 semanas el lunes"
#"el lunes de la semana pasada 20 dolares en transporte"
#"la semana pasada el lunes 20 dolares en transporte"

#------------NO FUNCIONA-----------------
#"hace 2 semanas 20 dolares en comida"
#"el lunes hace 2 semanas 20 dolares en comida"


#----------------PENDIENTE----------------
#"el martes <--- semana presente" 
#"el mes pasado"



'''NOTAS: la tokenizacion para el caso de "dolares" ó
signo "$" funciona solo si el usuario 
le da una separacion

PENDIENTE:
- Funcion guardar valor y referencia/item de gasto
- el hace 2 semanas, debe identificarse con el numero "2" y la palabra "dos
'''

flagControl = 1
stringUser = stringUser.lower()
txtToken = re.split(' ', stringUser) #tokenizar para hacer match DELIMITADORES: dolares o $
for i in range(len(txtToken)):
    flag = txtToken[i].isnumeric() #validacion del token sea un numero
    for j in range(i+1, len(txtToken)): #validacion de que la siguiente palabra, identificacion de moneda
        if txtToken[j] == "dolares" or "$" and flagControl == 1: 
            if flag == True:
                value = int(txtToken[i])
                spentUser(value)
                flagControl = 0
        elif txtToken[j] == "semanas":
            numWeek = int(txtToken[i])
            calendarDate(numWeek) #funcion de registro del gasto en pasado mayor a una semana
        elif txtToken[j] == "semana": #evaluacion pendiente
            numWeek = int(txtToken[i])
            calendarDate(numWeek)
        break
    if txtToken[i] == "semana": #funcion de registro del gasto en paso a una semana 
        calendarDate(1)

'''EXPLICACION: ingresa la cadena de texto, se maneja solo en minuscula
se tokeniza con delimitadores de espacio o signo de la moneda, se recorre
en validacion de la cantidad gastada y pendiente a registrar junto con el item
de gasto, se realiza verificacion de cantidad de semanas y la palabra "semana" o "semanas"
'''


#--------------------------------------
# - Identificar cantidad y guardar
# - 

#print(calendar.month(yy, mm))

#print(calendar.weekday(2022, 6, 26))
