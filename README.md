# Get_stock_price
快速抓取股票價格，包含最低價、最高價、收盤價等等

以下是爬蟲抓下來的資料範例

(輸出範例)[https://github.com/ChenTzYu/Get_stock_price/blob/master/output_example_for_stock_price.csv]

環境設置

    import time
    import csv
    import requests

檔案儲存路徑與檔案名稱

    place_for_store="C:/Users/user/Desktop/python pracice/stock data/output_stock_price.csv"


#使用selenium webdriver進行抓取

    from selenium import webdriver
    chromedriver="D:\chromedriver_win32/chromedriver"
    driver=webdriver.Chrome(chromedriver)

環境設置完便可以直接使用函數抓取

1.抓取單月中的每日個股資訊

    search_a_month()

2.抓取數個月份的股票價格資訊

    search_months(start_month,end_month):

參數為月份範圍，如七到九月則將參數設為

    search_months(7,9):

3.抓取數年的股票價格資訊

    search_years(start_year,end_year)
    
同樣，參數是以年為範圍，並且需要使用西元表示

