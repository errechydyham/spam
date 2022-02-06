#get the file 
name = input("Enter file name: ") 
text = open(name, "r") 

#get all the lines we want 
count = 0 
floats = [] 

for line in text: 
    if line.startswith("X-DSPAM-Confidence"): 
        count += 1 
        space = line.find('0') 
        floats.append(float(line[space:]))

#calculate the average 
total = 0 
for item in floats: 
    total += item 

avg = total / count 
print(avg) 