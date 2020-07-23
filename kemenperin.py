import requests
from bs4 import BeautifulSoup
import re
import xlsxwriter

def get_kemenperin_data():
    company_name = []
    try:        
        for page in range (1,679):
            url = f"http://www.kemenperin.go.id/direktori-perusahaan?what=&prov=0&hal={page}"    
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            table = soup.find("tbody")
            for tr in table.find_all('tr'):  
                for td in tr.find_all('td'):
                    for b in td.find_all('b'):
                        company_name.append(b.text)
    except:
        return ""
    return company_name

print("Crawling start...")
company_name = get_kemenperin_data()
print("Exporting to excel...")

with xlsxwriter.Workbook('company_name.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(company_name):
        worksheet.write_row(row_num, 0, [data])

