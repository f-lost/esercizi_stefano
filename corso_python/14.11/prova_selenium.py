'''Visita Wikipedia, cerca "Python (programming language)", e stampa il titolo della pagina dei risultati'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


driver = webdriver.Chrome()

driver.get("https://it.wikipedia.org/wiki/Pagina_principale")

search_bar = driver.find_element(By.ID, "searchInput")
search_bar.send_keys("Python (programming language)" + Keys.ENTER)
time.sleep(3)
print("Ricerca effettuata.")
print("Titolo della pagina:", driver.title)
time.sleep(3)

primo_risultato = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[3]/div[4]/ul/li[1]/div/div[2]/div[1]/a/span")
primo_risultato.click()

time.sleep(3)

print("Titolo della pagina:", driver.title)

time.sleep(5)         
driver.quit()
