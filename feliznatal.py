from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.google.com.br/')
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys('feliz natal e prospero ano novo 2022')
time.sleep(3)

#pesquisar

driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()
time.sleep (3)

#imagem

driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[8]/a[1]/div[1]/img').click()

driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').click()
time.sleep(4)

driver.find_element_by_xpath('//*[@id="movie_player"]/div[28]/div[2]/div[2]/button[10]').click()
