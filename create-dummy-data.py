import random

def get_random_date(start_year, end_year):
    # 1=Jan(31), 2=Feb(28/29), 3=Mar(31), 4=Apr(30), 5=May(31), 6=Jun(30), 7=Jul(31), 8=Aug(31), 9=Sep(30), 10=Oct(31), 11=Nov(30), 12=Dec(31)
    year = random.randint(start_year,end_year)
    month = random.randint(1,12)
    month_len = 31  # default
    if month in [4,6,8,10]:
        date = random.randint(1,30)
    elif month == 2:
        if year%4 == 0:
            if year%100 == 0:
                if year%400 == 0:
                    date = random.randint(1,29)
                else:
                    date = random.randint(1,28)
            else:
                date = random.randint(1,29)
        else:
            date = random.randint(1,28)
    else:
        date = random.randint(1,31)
    return '{}/{}/{}'.format(month,date,year)

if __name__ == "__main__":
    lines = []
    dept_list = ['Engg.', 'HR', 'Fin']
    with open('emp.db.csv', 'r') as f:
        start_doing = False
        for l in [x.strip() for x in f]:
            if l == 'Floop McMan':
                start_doing = True
            if start_doing:
                # name,basic,hra,da (% of basic),dept,date of birth (mm/dd/yy),date of joining (mm/dd/yy)
                basic = random.randint(4000000,9000000)/100
                hra = random.randint(1000000,2000000)/100
                da = random.randint(60,100)
                dept = random.choice(['HR', 'Engg.', 'Fin', 'IT'])
                line = '{name},{basic},{hra},{da},{dept},{dob},{doj}'.format(name=l,basic=basic,hra=hra,da=da,dept=dept,
                            dob=get_random_date(1970,2000),doj=get_random_date(2010,2020))
                lines.append(line)
            else:
                lines.append(l)

    print('\n'.join(lines))
    with open('emp.db.csv', 'w') as f:
        f.write('\n'.join(lines))
