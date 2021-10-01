from Application.salary import calculate_salary
from Application.db.people import get_employees
import datetime

if __name__ == '__main__':

    print(datetime.date.today())
    calculate_salary()
    get_employees()