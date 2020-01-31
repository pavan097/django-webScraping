# import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .models import JobsData
import sys


def naukriData(browser, *values):
    try:
        url = 'https://www.naukri.com/software-engineer-python-developer-jobs-in-hyderabad-secunderabad'
        browser.get(url)

        # searching for position
        elem = browser.find_element_by_name("qp")
        elem.clear()
        # elem.send_keys("software developer, python developer")
        elem.send_keys(values[0])


        # searching for location
        elem = browser.find_element_by_name("ql")
        elem.clear()
        # elem.send_keys("vizag")
        elem.send_keys(values[1])
        elem.send_keys(Keys.RETURN)

        print('values are applied')

        job_details = browser.find_elements_by_class_name('row')
        jobs = []

        for i in range(1,len(job_details)):
            d = {}
            if job_details[i].get_attribute('id').isnumeric():
                print(i, int(job_details[i].get_attribute('id')))
                d['job_title'] = job_details[i].find_element_by_tag_name('a').text
                d['company_name'] = job_details[i].find_element_by_class_name('org').text
                d['experience'] = job_details[i].find_element_by_class_name('exp').text
                d['location'] = job_details[i].find_element_by_class_name('loc').text
                d['skill_set'] = job_details[i].find_element_by_class_name('skill').text
                d['salary'] = job_details[i].find_element_by_class_name('salary').text
                d['posted_date'] = job_details[i].find_element_by_class_name('date').text
                d['job_url'] = job_details[i].find_element_by_id('jdUrl').get_attribute('href')
                jobs.append(d)


        # loading the data into the database
        j = JobsData()
        for i in jobs:
            j.job_title = i['job_title']
            j.company_name = i['company_name']
            j.experience = i['experience']
            j.location = i['location']
            j.skill_set = i['skill_set']
            j.salary = i['salary']
            j.posted_date = i['posted_date']
            j.job_url = i['job_url']
            j.job_site = 'naukri'
        j.save()

        browser.close()
    
    except Exception as e:
        print('error in the naukri data :',e)


if __name__ == "__main__":
    job_position = sys.argv[0]
    job_location = sys.argv[1]

    path = '/home/debian-pavan/dpro/p/chromedriver'
    browser = webdriver.Chrome(executable_path = path)
    
    naukriData(browser, job_position, job_location)