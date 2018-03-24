from datetime import date

born = date(1963,3,28)
    

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


print(calculate_age(born))

