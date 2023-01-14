import re

from django.shortcuts import render
from .models import Articles
import hhru

def hh_home(request):
    client = hhru.Client()
    vacancies = hhru.Client().search_vacancies(
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
        A=[]
        B=[]
        for x in C:
            for i in x:
                i = re.sub(r'<[^<>]*>', '', i)
                A.append(i)
            B.append(A)
            A=[]
    return render(request, 'hh/hh_home.html', {'hh' : B})



client = hhru.Client()

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


def main():
    # Get all vacancies with generator and filter by filter vacancies function.
    vacancies = hhru.Client().search_vacancies(
        # search_vacancies_over_pages for generator that search's over all pages.
        text="Инженер-программист",
        search_field="name",
        order_by="publication_time",
    )
    A = []
    for vacancy in vacancies[0:1]:
        B = filter_vacancy(vacancy)
        A.append(B[2])
        A.append(B[22].get('requirement'))
        A.append(B[22].get('responsibility'))
        A.append(B[21].get('name'))
        A.append(B[6].get('name'))
        if (B[7] != None):
            A.append(B[7].get('from'), '-', B[7].get('to'))
        A.append(B[13])


if __name__ == "__main__":
    main()
