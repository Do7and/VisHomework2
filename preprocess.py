#coding=gbk
import json
import csv

with open('./HKUST_coauthor_graph.json','r',encoding='gbk')as fp:
    json_data = json.load(fp)
    #print('�����ļ��е�json���ݣ�',json_data)
    #print('���Ƕ�ȡ���ļ����ݵ��������ͣ�', type(json_data))

nodelist = []
i = 0
n2i = {}
id2n = {}
print(type(json_data))
for node in json_data["nodes"]:
	if  node["dept"] == "CSE":
		nodelist.append({"name":node["fullname"],"radii":0})
		n2i[node["fullname"]] = i
		id2n[node["id"]] = node["fullname"]
		i += 1

print(nodelist)
print(len(n2i.keys()))
print(id2n.keys())

edgelist = []
for edge in json_data["edges"]:
	if edge["source"] in id2n and edge["target"] in id2n:
		edgelist.append({"source":n2i[id2n[edge["source"]]],"target":n2i[id2n[edge["target"]]]})
		radii=len(edge["publications"])
		nodelist[n2i[id2n[edge["source"]]]]["radii"] += radii
		nodelist[n2i[id2n[edge["target"]]]]["radii"] += radii
print(edgelist)


x = input("enter to exit��")

headers1 = ["name","radii"]
with open('nodes.csv', 'w', newline='') as f:
	writer = csv.DictWriter(f, headers1)
	writer.writeheader()
	for row in nodelist:
		writer.writerow(row)
headers2 = ["source","target","radii"]
with open('edges.csv', 'w', newline='') as f:
	writer = csv.DictWriter(f, headers2)
	writer.writeheader()
	for row in edgelist:
		writer.writerow(row)

