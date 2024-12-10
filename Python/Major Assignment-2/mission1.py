
#using built-in functions
cities = ["Kyiv","Kharkiv","Odessa","Kyiv","Lviv","Kharkiv","Dnipro"]
cleanedCities = sorted(set(cities))
print("Cleaned Cities:", cleanedCities)


#the traditional way
def cleaned_List(inputList):
    cleaned_List = []
    for item in inputList:
        if item not in cleaned_List:
            cleaned_List.append(item)
            
    for i in range(len(cleaned_List)):
        for j in range(len(cleaned_List)-i-1):
            if cleaned_List[j]>cleaned_List[j+1]:
                cleaned_List[j],cleaned_List[j+1]=cleaned_List[j+1],cleaned_List[j]
    
    return cleaned_List

print("Cleaned Cities:", cleaned_List(cities))