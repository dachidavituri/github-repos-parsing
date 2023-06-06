from selenium import webdriver
from selenium.webdriver.common.by import By
from githubData import GithubData
from github import Github
import time

githubRepoDb = GithubData('repos.db')
while True:
    add_repo = input("Do you want to add repozitory or not: ")
    if add_repo == 'yes' or add_repo == 'Yes':
        name = input("Enter github username: ")
        driver = webdriver.Chrome()
        driver.get(f"https://github.com/{name}?tab=repositories")
        time.sleep(2)


        def find_element_text(driver, xpath, alternative_text):
            try:
                element = driver.find_element(By.XPATH, xpath)
                return element.text
            except:
                return alternative_text


        name_xpath = '//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a'
        access_level_xpath = '//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/span[2]'
        language_xpath = '//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[3]/span/span[2]'
        stars_xpath = '//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[3]/a[1]'
        description_xpath = '//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[2]/p'
        update_date_xpath = '//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[3]/relative-time'

        name = find_element_text(driver, name_xpath, "Name not found")
        access_level = find_element_text(driver, access_level_xpath, "Access level not found")
        language = find_element_text(driver, language_xpath, "Language not found")
        stars = find_element_text(driver, stars_xpath, "Stars not found")
        description = find_element_text(driver, description_xpath, "Description not found")
        update_date = find_element_text(driver, update_date_xpath, "Update date not found")
        print(name)
        print(access_level)
        print(language)
        print(stars)
        print(description)
        print(update_date)
        driver.close()
        githubRepoDb.add_repo(Github(name, access_level, language, stars, description, update_date))
    readFromDb = input("Do you want to read data from database? ")
    if readFromDb == 'y' or readFromDb == 'yes':
        repo_id = int(input("Enter id: "))
        print(githubRepoDb.get_repo(repo_id))
    deleteFromDb = input("Do you want to delete data from database: ")
    if deleteFromDb == 'Yes' or deleteFromDb == 'y':
        repo_id = int(input("Enter id: "))
        githubRepoDb.delete_repo(repo_id)
        print("Deleted successfully")
    readEverythig = input("Do you want to read all data from database:")
    if readEverythig == 'Yes' or readEverythig == 'y':
        print(githubRepoDb.get_all_repo())
    readBylanguage = input("Do you want to read data by language: ")
    if readBylanguage == 'Yes' or readBylanguage == 'y':
        language = input("Choose language: ")
        print(githubRepoDb.get_all_repo_language(language))
