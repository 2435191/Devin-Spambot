import selenium
from selenium import webdriver

URL = "https://iqconnect.lmhostediq.com/iqextranet/EsurveyForm.aspx?__cid=CA22DN&__sid=100088&__crop=15548.37359788.2764358.1492115&fbclid=IwAR0N8_c0cAHi4IRvTkbxq7OVb4lMQ08hG91XWH1Mm9C4srf6oHjZsXmjwnM"
chromedriver_path = "/your/path/to/chromedriver"


driver = webdriver.Chrome(chromedriver_path) # Or just have it in your PATH variable / whatever the equivalent is for non-Mac users
driver.get(URL)


def cycle():
    for i in range(3): # click radio buttons
        driver.find_element_by_id(f"qsi_{i+1}_0").click()

    # submit
    driver.find_element_by_id("btn_submit").click()


    # handle popup alert
    alert = driver.switch_to.alert
    alert.accept()

    # move back to avoid page redirect
    driver.back()

i = 1
while True:
    cycle()
    print(f"Number of spams sent: {i}")
    i += 1
    
