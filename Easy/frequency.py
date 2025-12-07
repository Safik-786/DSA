data= {}
arr= [1, 2, 3, 4, 5, 5, 5, 4, 3, 13, 5, 2, 2, 2]
for i in arr:
  data[i]= data.get(i, 0) +1
  
print(data)
# ans= []
# for key, value in data.items():
#     if data[key] >= 3:
#         ans.append(key)
# print(ans)



