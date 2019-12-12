# This script is based on Python 3.5
from urllib.request import urlopen
import json
import csv

link = "https://api.github.com/search/repositories?q=is:public"

f = urlopen(link)
data = (f.read()).decode('utf-8')
# print(data)
# print("Type of data : ",type(data))


parsed_data = json.loads(data)
# print(parsed_data)
# print("Type of parsed data : ",type(parsed_data))

# print("Length of dict :", len(parsed_data))

# for i in parsed_data:
#     print(i)


item_list = parsed_data["items"]
# print(item_list)
# print(type(item_list))
# print("Length of list :", len(item_list))


new_dic = {} # Resultant dic
new_list = []
# Here i is the dictionary of the items
for i in item_list:
    # print(i)
    if i["language"] == "Python" and i["forks"] >= 200 and i["stargazers_count"]>2000:
        # print(i)
        new_list.append(i)


if len(new_list) == 0:
    print("There is no requested data available.")

# print(new_list)

data_list = []
fields = ['name', 'description', 'html_url', 'watchers_count', 'stargazers_count', 'forks_count']
for l in new_list:
    i = dict(l)
    element = list((i["name"], i["description"], i["html_url"], i["watchers_count"], i["stargazers_count"], i["forks_count"]))
    data_list.append(element)

for i in data_list:
    print(i)

with open("result.csv", 'w') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(fields)
    csvwriter.writerows(data_list)