import os
import time
import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, SAVE_DIR
from ocr_utils import process_image_ocr

os.makedirs(SAVE_DIR, exist_ok=True)

def setup_driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(BASE_URL)
    return driver

def process_table(driver):
    invoices_data = []
    main_window = driver.current_window_handle

    while True:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tableSandbox tbody tr")))
        rows = driver.find_elements(By.CSS_SELECTOR, "#tableSandbox tbody tr")

        for i in range(len(rows)):
            current_row = driver.find_elements(By.CSS_SELECTOR, "#tableSandbox tbody tr")[i]
            cols = current_row.find_elements(By.TAG_NAME, "td")
            
            invoice_id = cols[1].text.strip()
            due_date_str = cols[2].text.strip()
            due_date_dt = datetime.strptime(due_date_str, "%d-%m-%Y")

            if due_date_dt <= datetime.today():
                link = cols[3].find_element(By.TAG_NAME, "a")
                href = link.get_attribute("href")
                print(href)
                response = requests.get(href)
                
                if response.status_code == 200:
                    image_path = os.path.join(SAVE_DIR, f"invoice_{invoice_id}.jpg")
                    with open(image_path, "wb") as f:
                        f.write(response.content)
                    invoice_no, invoice_date, company_name, total_due = process_image_ocr(image_path)
                    invoices_data.append([
                        invoice_id,
                        due_date_str,
                        invoice_no,
                        invoice_date,
                        company_name,
                        total_due
                    ])

        next_btn = driver.find_element(By.ID, "tableSandbox_next")
        if "disabled" in next_btn.get_attribute("class"):
            break

        driver.execute_script("arguments[0].click();", next_btn)

    return invoices_data