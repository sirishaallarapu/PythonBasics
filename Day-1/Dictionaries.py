country = {
    "India": ["Delhi", "Maharashtra", "Haryana", 
              "Uttar Pradesh", "Himachal Pradesh"],
    "Japan": ["Hokkaido", "Chubu", "Tohoku", "Shikoku"],
    "United States": ["New York", "Texas", "Indiana", 
                      "New Jersey", "Hawaii", "Alaska"]
}
 
print(country["Japan"])
print(country["India"][0])
print(country["Japan"][1])
print(country["United States"][3])
print(country['India'][2])

#Using loop
# Creating dictionary which contains lists
for key, val in country.items():
	for i in val:
		print(f"{key} : {i}")
		
#Accessing a particular list of the key
for i in country['Japan']:
    print(i)
for i in country['India']:
    print(i)
for i in country['United States']:
    print(i)
		
#using list slicing
print(country["India"][:3])
print(country["Japan"][-2:])
print(country["India"][:-3])
print(country["United States"][1:5])


