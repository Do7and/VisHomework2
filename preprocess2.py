#coding=gbk
import json
import csv

with open('./HKUST_coauthor_graph.json','r',encoding='gbk')as fp:
    json_data = json.load(fp)
    #print('这是文件中的json数据：',json_data)
    #print('这是读取到文件数据的数据类型：', type(json_data))


headrow = []
nodelist = []
i = 0
n2i = {}
id2n = {}
print(type(json_data))
for node in json_data["nodes"]:
	if  node["dept"] == "CSE":
		nodelist.append({"name":node["fullname"],"radii":0})
		headrow.append(node["fullname"])
		n2i[node["fullname"]] = i
		id2n[node["id"]] = node["fullname"]
		i += 1

print(nodelist)
print(len(n2i.keys()))
print(id2n.keys())
adjmatrix = [[0 for k in range(i)] for j in range(i)]

edgelist = []
for edge in json_data["edges"]:
	if edge["source"] in id2n and edge["target"] in id2n:
		edgelist.append({"source":n2i[id2n[edge["source"]]],"target":n2i[id2n[edge["target"]]]})
		radii=len(edge["publications"])
		nodelist[n2i[id2n[edge["source"]]]]["radii"] += radii
		nodelist[n2i[id2n[edge["target"]]]]["radii"] += radii
		adjmatrix[n2i[id2n[edge["source"]]]][n2i[id2n[edge["target"]]]] = radii
		adjmatrix[n2i[id2n[edge["target"]]]][n2i[id2n[edge["source"]]]] = radii
print(edgelist)

print(headrow)
csvfile = open('adjmatrix.csv', 'w',newline='')
writer = csv.writer(csvfile)
writer.writerow(headrow)
writer.writerows(adjmatrix)
csvfile.close()
