# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('введите номер четверти: '))
if quarter < 1 or quarter > 4:
    print ('неправильно введен номер четверти')
    exit()
if quarter == 1:
    print ('X > 0 and Y > 0')
elif quarter == 2:
    print ('X < 0 and Y > 0')
elif quarter == 3:
    print ('X < 0 and Y < 0')
else:
    print ('X > 0 and Y < 0')