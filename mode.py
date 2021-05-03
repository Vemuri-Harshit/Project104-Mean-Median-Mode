import csv;
from collections import Counter;

with open('data.csv', newline='') as data:
    reader = csv.reader(data);
    filedata = list(reader);

filedata.pop(0);


weight_of_all = []

for i in range(len(filedata)):

    weight_for_each = filedata[i][1]
    weight_of_all.append(float(weight_for_each));

weight_of_all.sort();

data = Counter(weight_of_all);
mode_data_for_range = {
                        "50-60":0,
                        "60-70":0,
                        "70-80":0
                    }

for weight, occurence in data.items():
    if 50<float(weight < 60):
        mode_data_for_range["50-60"] += occurence
    elif 60<float(weight < 70):
        mode_data_for_range["60-70"] += occurence
    elif 70<float(weight < 80):
        mode_data_for_range["70-80"] += occurence 

mode_range,mode_occurence = 0,0
for rang, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence;

mode = float((mode_range[0] + mode_range[1]) / 2)

print(f"Mode is = {mode:2f}");
