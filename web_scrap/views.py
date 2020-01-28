from django.shortcuts import render
from .models import JobsData
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from .scrap import naukriData


def selectOption(request):
    print('it is entered')
    return render(request, 'home.html', {})


def dataList(request):
    cur = connection.cursor()
    jobsList = 'select * from web_scrap_jobsdata'
    # insert_data = 'insert into web_scrap_jobsdata("job_title") values("software1")'
    cur.execute(jobsList)

    data = cur.fetchall()
    connection.close()
    print('sql data :', data)
    return render(request, 'dataList.html', {'data':data})


def dataInsert(request):
    jobs_data = naukriData()
    print('jobs data :', jobs_data)
    # for i in jobs_data:
    #     insert_data = JobsData(job_title= , company_name= , experience= , location= , skill_set= , salary= , posted_date= , job_url= , job_site=)
    #     insert_date.save()

    return HttpResponseRedirect('/datalist/')
