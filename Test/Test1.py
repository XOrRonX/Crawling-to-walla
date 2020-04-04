from selenium import webdriver
import datetime
from os import path

# global var
NUMBER_OF_ART = 4

driver = webdriver.Chrome()

# get walla
driver.get('https://www.walla.co.il')

# Create file if not exists
if not path.exists("output.txt"):
    file = open("output.txt", "w", encoding='utf8')
else:
    file = open("output.txt", "a", encoding='utf8')

# create main Article and insert to the file
# get xpath
main_title_xpath = '//*[@id="container"]/section[1]/article/a/h3/div/span'
main_article_xpath = '//*[@id="container"]/section[1]/article/a/p'
main_image_xpath = '//*[@id="container"]/section[1]/article/a/div[1]/picture/img'

# Write time stamp
file.write('[{:%Y-%m-%d %H:%M:%S}]\n'.format(datetime.datetime.now()))

main_title = driver.find_elements_by_xpath(main_title_xpath)
main_article = driver.find_elements_by_xpath(main_article_xpath)
main_image = driver.find_elements_by_xpath(main_image_xpath)

for j in main_title:
    file.write(j.text)
    file.write('\n')

for j in main_article:
    file.write(j.text)
    file.write('\n')

for j in main_image:
    file.write(j.get_attribute("src"))
    file.write('\n')
file.write('\n')


# create small Articles
# get xpath
base_title_xpath = '//*[@id="container"]/section[3]/section/section[1]/ul/li[$]/article/a/h3/div/span'
base_image_xpath = '//*[@id="container"]/section[3]/section/section[1]/ul/li[$]/article/a/div/picture/img'
base_article_xpath = '//*[@id="container"]/section[3]/section/section[1]/ul/li[$]/article/a/p'

for i in range(1,NUMBER_OF_ART+1):

    # Write time stamp
    file.write('[{:%Y-%m-%d %H:%M:%S}]\n'.format(datetime.datetime.now()))

    title = driver.find_elements_by_xpath(base_title_xpath.replace('$',str(i)))
    for j in title:
        file.write(j.text)
        file.write('\n')
    text = driver.find_elements_by_xpath(base_article_xpath.replace('$', str(i)))
    for j in text:
        file.write(j.text)
        file.write('\n')
    image = driver.find_elements_by_xpath(base_image_xpath.replace('$', str(i)))
    for j in image:
        file.write(j.get_attribute("src"))
        file.write('\n')
    file.write('\n')


file.close()
