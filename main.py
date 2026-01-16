import os
import time
import pandas as pd
from file_utils import limpar_arquivos
from web_scraper import setup_driver, process_table
from config import CSV_FILE, SAVE_DIR
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def main():
   
    limpar_arquivos(CSV_FILE, SAVE_DIR)
    driver = setup_driver()
    try:
        start =WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "start")))
        driver.execute_script("arguments[0].click();", start)
        time.sleep(2)  
        data = process_table(driver)

        df = pd.DataFrame(data, columns=["ID", "DueDate", "InvoiceNo", "InvoiceDate", "CompanyName", "TotalDue"])
        df["DueDate"] = pd.to_datetime(df["DueDate"], format="%d-%m-%Y").dt.strftime("%d-%m-%Y")
        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], format="%Y-%m-%d").dt.strftime("%d-%m-%Y")
        df.to_csv(CSV_FILE, index=False)
        absolute_path = os.path.abspath(CSV_FILE)
        file_input = driver.find_element(By.NAME, "csv")
        file_input.send_keys(absolute_path)
        
        print(f"Sucesso! {len(data)} faturas processadas e enviadas.")

        input("Pressione Enter para fechar...")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()