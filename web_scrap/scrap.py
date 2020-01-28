# import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def naukriData():
    path = '/home/debian-pavan/dpro/p/chromedriver'
    browser = webdriver.Chrome(executable_path = path)

    url = 'https://www.naukri.com/software-engineer-python-developer-jobs-in-hyderabad-secunderabad'
    browser.get(url)

    # searching for position
    elem = browser.find_element_by_name("qp")
    elem.clear()
    elem.send_keys("software developer, python developer")
    elem.send_keys(Keys.RETURN)

    # searching for location
    elem = browser.find_element_by_name("ql")
    elem.clear()
    elem.send_keys("vizag")
    elem.send_keys(Keys.RETURN)

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

    return jobs

    
if __name__ == "__main__":    
    naukriData()