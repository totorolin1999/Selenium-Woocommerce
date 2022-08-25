import csv
from selenium import webdriver
import time

with open('LED.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:
        PATH = "D:/chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get('')

        time.sleep(1)
        
        # Login
        account = ""
        password = ""
        user_login = driver.find_element_by_xpath('//*[@id="user_login"]')
        user_login.send_keys(account)

        user_pass = driver.find_element_by_xpath('//*[@id="user_pass"]')
        user_pass.send_keys(password)
        
        submit = driver.find_element_by_xpath('//*[@id="wp-submit"]')
        submit.click()
        
        # Post title and select category
        title = driver.find_element_by_xpath('//*[@id="title"]')
        title.send_keys(line[0])
        cat101 = driver.find_element_by_xpath('//*[@id="in-product_cat-101"]')
        cat101.click()
        cat140 = driver.find_element_by_xpath('//*[@id="in-product_cat-140"]')
        cat140.click()
        price = driver.find_element_by_xpath('//*[@id="_regular_price"]')
        price.send_keys(line[1])

        # Upload image
        thumbnail = driver.find_element_by_xpath('//*[@id="set-post-thumbnail"]')
        thumbnail.click()
        uploader = driver.find_element_by_xpath("//input[starts-with(@id,'html5_')]")
        file_path = ''
        uploader.send_keys(file_path+line[3])
        time.sleep(3)
        button = driver.find_element_by_xpath('//*[@id="__wp-uploader-id-0"]/div[4]/div/div[2]/button')
        button.click()
        time.sleep(3)

        # Post content
        mce_frame = driver.find_element_by_xpath('//*[@id="excerpt_ifr"]')
        driver.switch_to_frame(mce_frame)
        tinymce = driver.find_element_by_xpath('//*[@id="tinymce"]')
        tinymce.send_keys(line[2])
        driver.switch_to.default_content()

        # Save as draft
        submit = driver.find_element_by_xpath('//*[@id="save-post"]')
        driver.execute_script("arguments[0].click();", submit)
        time.sleep(3)
        driver.close()