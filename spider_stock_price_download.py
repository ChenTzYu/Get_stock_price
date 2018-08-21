
# coding: utf-8

# In[1]:


import time
import csv
import requests

#使用selenium webdriver進行抓取
from selenium import webdriver
chromedriver="D:\chromedriver_win32/chromedriver"
driver=webdriver.Chrome(chromedriver)

#獲取要爬取的網頁
driver.get("http://www.tse.com.tw/zh/page/trading/exchange/STOCK_DAY.html")

#儲存位置，請自行更改路徑
place_for_store="C:/Users/user/Desktop/python pracice/stock data/output_stock_price.csv"


# In[2]:


def search_a_month():

    year_for_search=input("請輸入欲查詢之年份(西元):")
    month_for_search=input("請輸入欲查詢之月份:")
    stock_id_for_search=input("輸入股票代號")
    
    xpath_year="//select[@name='yy']/option[@value="+"'" +str(year_for_search) +"'"+ "]"
    xpath_month="//select[@name='mm']/option[@value="+"'" +str(month_for_search) +"'"+ "]"
    
    #使用selenium模仿點擊網頁，用以獲取爬取所需頁面    
    select_year=driver.find_element_by_xpath(xpath_year)
    select_year.click()
    select_month=driver.find_element_by_xpath(xpath_month)
    select_month.click()
    
    
    #送出股票代號
    stock_id=driver.find_element_by_xpath("//*[@id='main-form']/div/div/form/input")
    stock_id.send_keys(stock_id_for_search)
    
    start_search=driver.find_element_by_xpath("//a[@href='#']")
    start_search.click()
    
    stock_id.clear()
    time.sleep(3)
    
    
    stock_table=driver.find_elements_by_xpath("//*[@id='report-table']/tbody/tr")

    n=1
    for i in stock_table:
        print(n)
        n=n+1
        print(i.text)
        output_list=i.text.split(" ")
        print(output_list)
        
        with open(place_for_store,"a+",encoding="UTF-8",newline='') as csvfile:
            w=csv.writer(csvfile)
            w.writerow(output_list)  


# In[3]:


def search_months(start_month,end_month):
    
    year_for_search=input("請輸入欲查詢之年份(西元):")
    
    stock_id_for_search=input("輸入股票代號")
    
  
    for i in range(start_month,end_month+1):
        try:
            xpath_year="//select[@name='yy']/option[@value="+"'" +str(year_for_search) +"'"+ "]"
            xpath_month="//select[@name='mm']/option[@value="+"'" +str(i) +"'"+ "]"  
        
            select_year=driver.find_element_by_xpath(xpath_year)
            select_year.click()
            select_month=driver.find_element_by_xpath(xpath_month)
            select_month.click()
      
            stock_id=driver.find_element_by_xpath("//*[@id='main-form']/div/div/form/input")
            stock_id.send_keys(stock_id_for_search)
    
            start_search=driver.find_element_by_xpath("//a[@href='#']")
            start_search.click()
    
            stock_id.clear()
            time.sleep(3)
    
    
            stock_table=driver.find_elements_by_xpath("//*[@id='report-table']/tbody/tr")

            
            for i in stock_table:
                
                print(i.text)
                output_list=i.text.split(" ")
                print(output_list)
        
                with open(place_for_store,"a+",encoding="UTF-8",newline='') as csvfile:
                    w=csv.writer(csvfile)
                    w.writerow(output_list)  
        
        except:
            continue
    
        
        
    


# In[15]:


def search_years(start_year,end_year):
    
    
    stock_id_for_search=input("輸入股票代號")
    
    
    
    
    for i in range(start_year,end_year+1):
        try:
            xpath_year="//select[@name='yy']/option[@value="+"'" +str(i) +"'"+ "]"
            
            for j in range(1,13):
                xpath_month="//select[@name='mm']/option[@value="+"'" +str(j) +"'"+ "]" 
                
                
                select_year=driver.find_element_by_xpath(xpath_year)
                select_year.click()
                select_month=driver.find_element_by_xpath(xpath_month)
                select_month.click()
          
                stock_id=driver.find_element_by_xpath("//*[@id='main-form']/div/div/form/input")
                stock_id.send_keys(stock_id_for_search)
    
                start_search=driver.find_element_by_xpath("//a[@href='#']")
                start_search.click()
    
                stock_id.clear()
                time.sleep(3)
    
    
                stock_table=driver.find_elements_by_xpath("//*[@id='report-table']/tbody/tr")

            
                for i in stock_table:
                
                    print(i.text)
                    output_list=i.text.split(" ")
                    print(output_list)
        
                    with open(place_for_store,"a+",encoding="UTF-8",newline='') as csvfile:
                        w=csv.writer(csvfile)
                        w.writerow(output_list)  
        
        
        except:
            continue
            
    
    
    

