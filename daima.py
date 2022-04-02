# -*- coding:utf-8 -*-
import os
import re

path = os.getcwd()
filetest = os.listdir(path)
filepath = path + "\\" + filetest[0]
txt = open('E:\\tiqu\\LocList.txt', 'r', encoding='utf-8').read()

result = ""
test_txt = re.findall("...+Code", txt)
quchong_test_txt = list(set(test_txt))  # 去重
result = '\n'.join(quchong_test_txt)
result_1 = result.replace("<CountryRegion Name=", "")
result_2 = result_1.replace("<State Name=", "")
result_3 = result_2.replace("<City Name=", "")
result_4 = result_3.replace("<Region Name=", "")
# result_1 = result.replace("LOGON_NAME\\\":\\\"","")
result_5 = result_4.replace(" Code", "")
result_6 = result_5.replace("	", "")
result_7 = result_6.replace(" ", "")
# result_2 = result_1.replace("\\\",\\\"DISPLAY_NAME","")
print(result_7)

filename = '全球地名-去重.txt'
with open(filename, 'a') as file_object:
	file_object.write(result_7)
