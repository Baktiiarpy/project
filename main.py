import schedule
import time
import csv

def write_csv():
    name = input('enter name')
    age = input('enter age')
    with open('user.csv', 'a') as csv_file:
        write = csv.writer(csv_file, delimiter='/')
        writer.writerow(
            (name,age)

        )

    answ = input('continue? y or n')
    if answ == 'y':
        write_csv
    else:
        print('stop')

def maling():
    with open('user.csv', 'r') as csv_file:
        data = csv_file.readlines()
        names = [i.replace('/n', '')for i in data]
        for i in names:
            name = i.split('/')
            if int(name[-1])>= 18:
                print(f'scidki segodnya {name[0]}')

schedule.every(3).seconds.do(mailing)
while True:
    schedule.run_pending()
    time.sleep(1)

# mailing()
# write_csv()

