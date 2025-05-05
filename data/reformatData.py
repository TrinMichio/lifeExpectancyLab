import json


f1 = open("data/life_expectancy_cleaned.csv", "r")
lines = f1.readlines()

dictionary ={}

# Create the dictionary here


years = lines[2].split(",")
years = [int(i.strip("\"").strip().replace("\"", "")) for i in years[4:]]


for i in range(len(lines)):
    if (i > 2):
        l = list(lines[i].split(','))
        l = [j.strip("\"").strip().replace("\"", "") for j in l]
        
        dictionary[l[0]] = {}
        
        for i in range(len(years)):
            dictionary[l[0]][years[i]] = l[5+i]

f1.close()

#Save the json object to a file
f2 = open("data/life_expectancy_cleaned.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()
