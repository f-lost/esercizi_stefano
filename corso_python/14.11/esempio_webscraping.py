'''Visita Wikipedia, cerca "Python (programming language)", e stampa il titolo della pagina dei risultati'''


from doctest import testmod
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time





#PRIMO ESEMPIO
# driver = webdriver.Chrome()
# driver.get("https://it.wikipedia.org/wiki/Pagina_principale")

# search_bar = driver.find_element(By.ID, "searchInput")
# search_bar.send_keys("Python (programming language)" + Keys.ENTER)
# time.sleep(3)
# print("Ricerca effettuata.")
# print("Titolo della pagina:", driver.title)
# time.sleep(3)

# primo_risultato = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[3]/div[4]/ul/li[1]/div/div[2]/div[1]/a/span")
# primo_risultato.click()

# time.sleep(3)

# print("Titolo della pagina:", driver.title)

# time.sleep(3)         
# driver.quit()

#SECONDO ESEMPIO: andate a https://practicetestautomation.com/practice-test-login/ e prendete user e psw, inseritele nel login
#  e cliccate su submit, arrivati nella pagina di accesso vi prendete il testo e lo
#  stampate e poi cliccate su log out, successivamente stampate il driver.title e chiudete il driver

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

username = driver.find_element(By.XPATH, "/html/body/div/div/section/section/ul/li[2]/b[1]").text
password = driver.find_element(By.XPATH, "/html/body/div/div/section/section/ul/li[2]/b[2]").text
print(username, password)

textbox = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/div[1]/input")
textbox.send_keys(username + Keys.ENTER)

textbox = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/div[2]/input")
textbox.send_keys(password + Keys.ENTER)

time.sleep(3)

submit_button = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/button")
submit_button.click()

time.sleep(3)

testo1 = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/article/div[1]/h1").text
testo2 = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/article/div[2]/p[1]/strong").text

print("Il testo della pagina è: ", testo1 + "" + testo2)

logout_button = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/article/div[2]/div/div/div/a")
logout_button.click()

time.sleep(3)

print("Titolo della pagina:", driver.title)

driver.quit()