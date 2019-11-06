from   datetime                                   import datetime, time, timedelta
import os
import psycopg2

from   conexiones_bases_datos import get_data_base

def get_no_turno(fecha_BD):


    date   = fecha_BD.date()
    time2  = fecha_BD.time()

    fecha_BD = datetime(date.year, date.month, date.day, time2.hour, time2.minute,time2.second)

    T1_i   = datetime(date.year, date.month, date.day, 6, 30)    # Inicio del Turno 1.
    T1_f   = datetime(date.year, date.month, date.day, 14, 29,59)   # Final  del Turno 1.

    T2_i   = datetime(date.year, date.month, date.day, 14, 30)   # Inicio del Turno 2.
    T2_f   = datetime(date.year, date.month, date.day, 22, 29,59)   # Final  del Turno 2.

    T3_i1  = datetime(date.year, date.month, date.day, 22, 30)  # Final  del Turno  3.
    T3_f1  = datetime(date.year, date.month, date.day, 23, 59,59)  # Final  del Turno  3.
    T3_i2  = datetime(date.year, date.month, date.day, 0, 0,0)    # Final  del Turno  3.
    T3_f2  = datetime(date.year, date.month, date.day, 6, 29,59)   # Final  del Turno  3.

    turno  = 0
    fecha_turno = 0

    if fecha_BD >= T1_i and fecha_BD < T1_f:
        #print 'TURNO NO 1    ......................'
        turno = 1
        fecha_turno = T1_i
    elif fecha_BD >= T2_i and fecha_BD < T2_f:
        #print 'TURNO NO 2    ......................'
        turno = 2
        fecha_turno = T2_i

    elif fecha_BD >= T3_i1 and fecha_BD < T3_f1:
        #print 'TURNO NO 3    ......................'
        turno = 3
        fecha_turno = T3_i1
    elif fecha_BD >= T3_i2 and fecha_BD < T3_f2:

        #print 'TURNO NO 3    ......................'
        turno = 3


        if date.day != 1:  # Dia 1 de cada mes
            T3_i12  = datetime(date.year, date.month, date.day-1, 22, 30)  # Final  del Turno  3.
        else:
            T3_i12  = datetime(date.year, date.month-1, date.day, 22, 30)

            try:
                for i in range(26,31,1):
                    T3_i12  = datetime(date.year, date.month-1,i, 22, 30)
            except:
                print('FECHA CORREGIDA A:',T3_i12)

        if date.month == 1 and date.day == 1:  # Primer dia del ano
            T3_i12  = datetime(date.year-1,12, date.day, 22, 30)

            try:
                for i in range(26,31,1):
                    T3_i12  = datetime(date.year-1,12,i, 22, 30)
            except:
                i('FECHA CORREGIDA A:',T3_i12)


        T3_i1 = T3_i12
        fecha_turno = T3_i1

    return turno,fecha_turno


def get_hora_por_hora():


    date     = datetime.now()
    fecha_BD = datetime(date.year, date.month, date.day, date.hour, date.minute,date.second)
    minute   = fecha_BD.minute
    hour     = fecha_BD.hour

    time = [
    [6 ,30,7 ,30],
    [7 ,30,8 ,30],
    [8 ,30,9 ,30],
    [9 ,30,10,30],
    [10,30,11,30],
    [11,30,12,30],
    [12,30,13,30],
    [13,30,14,30],

    [14,30,15,30],
    [15,30,16,30],
    [16,30,17,30],
    [17,30,18,30],
    [18,30,19,30],
    [19,30,20,30],
    [20,30,21,30],
    [21,30,22,30],

    [22,30,23,30],
    [23,30,1,30],
    [1 ,30,2 ,30],
    [2 ,30,3 ,30],
    [3 ,30,4 ,30],
    [4 ,30,5 ,30],
    [5 ,30,6 ,30],
    ]

    for i in time:


        h1=i[0]
        m1=i[1]
        fecha_1 = datetime(date.year, date.month, date.day, h1, m1,0,0)
        h2=i[2]
        m2=i[3]
        fecha_2 = datetime(date.year, date.month, date.day, h2, m2,0,0)

        if date > fecha_1 and date <=  fecha_2:
            HORA =  fecha_1

    return HORA

# Obtenr datos de la BD.
