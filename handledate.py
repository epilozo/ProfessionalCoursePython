from datetime import datetime
## para trabajar solo con el modulo directo
## datetime.xxxxx
## instead of use datetime.datetime.Xxxx


my_time = datetime.now()
print('local ',my_time)

my_time = datetime.utcnow()
print('utc',my_time)

my_date = datetime.today()
print(my_date)

print(f'Year : {my_time.year} ')
print('Imprimiendo formato de fecha de acuerdo a necesidad')
print('*'*50)

print("Usa format time:  ",my_time.strftime('%m/%d/%Y of %H:%M:%S'))
print("LATAM format time:  ",my_time.strftime('%d/%m/%Y of %H:%M:%S'))

