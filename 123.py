import functools
import hhru
import sqlite3

client = hhru.Client()
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

def filter_vacancy(vacancy):
    A = []
    for vac in vacancy.values():
        A.append(vac)
    return A


def print_vacancy(vacancy):
    A = []
    for vac in vacancy.values():
        A.append(vac)
    return A


# query1 = """ INSERT INTO hh_articles(name, skills, date, salary, company, description, region) VALUES(A[0],A[1], A[6], A[5], A[3], A[2], A[4]) """
# cur.execute("""INSERT INTO hh_articles(name, skills, date, salary, company, description, region) VALUES(A[0],A[1], A[6], A[5], A[3], A[2], A[4])""")


def main():
    # Get all vacancies with generator and filter by filter vacancies function.
    vacancies = hhru.Client().search_vacancies(
        # search_vacancies_over_pages for generator that search's over all pages.
        text="Инженер-программист",
        search_field="name",
        order_by="publication_time",
    )
    C = []
    for vacancy in vacancies[0:10]:
        B = filter_vacancy(vacancy)
        A =[]
        A.append(B[2])
        A.append(B[22].get('requirement'))
        A.append(B[22].get('responsibility'))
        A.append(B[21].get('name'))
        A.append(B[6].get('name'))
        if (B[7] != None):
            A.append(str(B[7].get('from')) + '-' + str(B[7].get('to')))
        else:
            A.append('-')
        A.append(B[13])

        C.append(A)

    print(*C)


if __name__ == "__main__":
    main()
