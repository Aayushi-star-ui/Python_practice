dic = {
    "name" : "ayushi",
    "phone no." : 7015186981,
    "compnay": "Google",
    "Post" : "Data Scientist"
}
# print(dic) #print all
# print(dic["Post"]) #print specific one 

# # print(dic["name"]) #error
# print(dic.get("namee"))
# print(dic.get("name"))

# dic["phone no."] = 7365657690
# print(dic)

#Methodss
# dic["city"] = "Ambala"
# print(dic)

# dic.pop("phone no.")
# print(dic)

# dic.popitem() #last item is deleted now 
# print(dic)

# print(dic.keys()) 

# print(dic.values())

# print(dic.items())

# dic.update({
#     "offer-date" : 11-7-2027,
#     "joining date" : 20-7-2027
#     })
# print(dic)

#nested dictionoies 
profile = {
    "id" : 101,
    "info" : {
        "name" : "chehak",
        "profession" : "govt. officer",
        "salary" : 1200000
    }
}
print(profile)