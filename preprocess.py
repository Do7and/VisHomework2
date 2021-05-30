#coding=gbk
import json
import csv

with open('./HKUST_coauthor_graph.json','r',encoding='gbk')as fp:
    json_data = json.load(fp)
    #print('这是文件中的json数据：',json_data)
    #print('这是读取到文件数据的数据类型：', type(json_data))

nodelist = []
i = 0
n2i = {}
id2n = {}
print(type(json_data))
for node in json_data["nodes"]:
	if  node["dept"] == "CSE":
		nodelist.append(node["fullname"])
		n2i[node["fullname"]] = i
		id2n[node["id"]] = node["fullname"]
		i += 1

print(nodelist)
print(len(n2i.keys()))
print(id2n.keys())

edgelist = []
for edge in json_data["edges"]:
	if edge["source"] in id2n and edge["target"] in id2n:
		edgelist.append({"source":n2i[id2n[edge["source"]]],"target":n2i[id2n[edge["target"]]],"radii":len(edge["publications"])})
print(edgelist)


x = input("enter to exit：")

headers1 = ["name"]
with open('nodes.csv', 'w', newline='') as f:
	writer = csv.DictWriter(f, headers1)
	writer.writeheader()
	for row in nodelist:
		writer.writerow({"name":row})
headers2 = ["source","target","radii"]
with open('edges.csv', 'w', newline='') as f:
	writer = csv.DictWriter(f, headers2)
	writer.writeheader()
	for row in edgelist:
		writer.writerow(row)

