import csv

# 讀取csv檔內容，放到csvDataToRead變數中。
csvFileToRead = open (r"C:\Users\bhbin\OneDrive\桌面\GitHub\Ian_window\621\測試\01.csv", 'r', encoding='utf-8-sig')
csvDataToRead = csv.reader(csvFileToRead)

# 將csvDataToRead(原csv檔內容)轉為list。
dataList = list(csvDataToRead)
# 注意：必須在轉完list之後才關檔，否則會產生'ValueError: I/O operation on closed file.'
# 　　　的exception。
csvFileToRead.close()
print(dataList)