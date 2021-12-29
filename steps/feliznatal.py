from selenium import webdriver
from behave import given, when, then
import time


driver = webdriver.Chrome()
driver.maximize_window()


@given(u'que eu entre no site do google')
def step_impl(context):
    driver.get('https://www.google.com.br/')
time.sleep(3)


@given(u'digite Feliz natal e prospero ano novo')
def step_impl(context):
   driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys('feliz natal e prospero ano novo 2022')
time.sleep(2)

@given(u'clico em pesquisar')
def step_impl(context):
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()
time.sleep(2)

@given(u'clico em imagem')
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
time.sleep(1)

@when(u'eu achar uma imagem')
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[8]/a[1]/div[1]/img').click()
time.sleep(1)

@when(u'clicar em abrir')
def step_impl(context):
   driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').click()
time.sleep(1)

@then(u'deve abrir a imagem com o video selecionado')
def step_impl(context):
   driver.find_element_by_xpath('//*[@id="movie_player"]/div[28]/div[2]/div[2]/button[10]').click()
