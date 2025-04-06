#import
import time
import pandas as pd
import numpy as np
#import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium .webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class StocksScraper:
    def __init__(self,driver,timeout=10):
        self.driver=driver
        self.wait= WebDriverWait(self.driver,timeout=timeout)
        self.data=[]

    def wait_for_page_to_load(self):
    
        page_title=self.driver.title
        try:
            self.wait.until(
                lambda d: d.execute_script("return document.readyState") == 'complete'
            )
        except:
            
            print(f" The page {page_title} did not fully loaded within the given duration.")
        else:
            
            print(f"The page \"{page_title}\" is fully loaded.")


    

    def access_url(self,url):
        self.driver.get(url)
        self.wait_for_page_to_load()


    def access_most_active_stocks(self):
        #hovering on market menu 
        actions =ActionChains(self.driver)# it will help to clicking the mouse and moving thst called hovering 
        market_menu =self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[3]/a[1]/span[1]'))
        )#we get this data from (we get this data from selector hum(abs XPATH))
        actions.move_to_element(market_menu).perform()
        
        #trending ticker
        trending_ticker=self.wait.until(
            EC.element_to_be_clickable((By.XPATH,'/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[3]/div[1]/ul[1]/li[4]/a[1]/div[1]'))
        )#we get this data from (we get this data from selector hum(abs XPATH))
        trending_ticker.click()
        self.wait_for_page_to_load()
        
        #click on Most Active 
        most_active=self.wait.until(
            EC.element_to_be_clickable((By.XPATH,'/html[1]/body[1]/div[2]/main[1]/section[1]/section[1]/section[1]/article[1]/section[1]/div[1]/nav[1]/ul[1]/li[1]/a[1]/span[1]'))
        )#we get this data from (we get this data from selector hum(abs XPATH))
        
        most_active.click()
        self.wait_for_page_to_load()


    def extract_stocks_data(self):
        ##navigating tags
        #scraping the data
        while True:
               #scraping 
            self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME,"table"))
            )
            rows=self.driver.find_elements(By.CSS_SELECTOR,"table tbody tr")
            for row in rows:
                values=row.find_elements(By.TAG_NAME,"td")
                [val.text for val in  values]
                stock={
                    "Symbol":values[0].text,
                    "Name":values[1].text,
                    "Price":values[3].text,
                    "Change":values[4].text,
                    "Change %":values[5].text,
                    "Volume":values[6].text,
                    "Avg_Vol_3m":values[7].text,
                    "Market_Cap":values[8].text,
                    "PE_Ratio":values[9].text,
                    '52_WK_Change %':values[10].text
                    
                }
                self.data.append(stock)
                #break
            #break
                
            
        
            #click next 
            try:
                next_button=self.wait.until(
                    EC.element_to_be_clickable((By.XPATH,'//*[@id="nimbus-app"]/section/section/section/article/section[1]/div/div[3]/div[3]/button[3]'))
                )
            except:
                print("the \"next\" botton is not clickable. we have navigate through all the pages.")
                break
        
            else:
                next_button.click()
                time.sleep(2)
        

    def clean_and_save_data(self,filename='temp'):
        stocks_df=(
            pd
            .DataFrame(self.data)
            .apply(lambda col: col.str.strip() if col.dtype=="object" else col)
            .assign(
                Price=lambda df_: pd.to_numeric(df_.Price),
                Avg_Vol_3m=lambda df_: pd.to_numeric(df_.Avg_Vol_3m.str.replace("M","").str.replace(",", "")),
                Change=lambda df_: pd.to_numeric(df_.Change.str.replace("+","")),
                Volume=lambda df_: pd.to_numeric(df_.Volume.str.replace("M","")),
                Market_Cap=lambda df_: df_.Market_Cap.str.replace(",", "").apply(
                    lambda val: (
                        float(val.replace("B", ""))
                        if "B" in val else
                        float(val.replace("T", "")) * 1000
                        if "T" in val else
                        float(val.replace("M", "")) / 1000
                        if "M" in val else
                        np.nan  # fallback for '-' or unexpected format
                    )
                ),
        
                PE_Ratio=lambda df_:(
                    df_
                    .PE_Ratio
                    .replace("-",np.nan)
                    .str.replace(",","")
                    .pipe(lambda col:pd.to_numeric(col))
                )
            )
            .rename(columns={
                
                "Price": "Price(USD)",
                "Volume":"Volume_M",
                "Market_Cap":"Market_Cap_B",
                
            })
            
            
        )
        stocks_df["Change %"] = stocks_df["Change %"].str.replace("%", "").astype(float)
        stocks_df["52_WK_Change %"] = stocks_df["52_WK_Change %"].str.replace("%", "").astype(float)
        

        stocks_df.to_csv(f"{filename}.csv", index=False)

##

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.maximize_window()

    url='https://finance.yahoo.com'
    scraper=StocksScraper(driver, 5)

    scraper.access_url(url)
    scraper.access_most_active_stocks()
    scraper.extract_stocks_data()
    scraper.clean_and_save_data("yahoo_finance_stocks") #put you file name here 

    driver.quit()
