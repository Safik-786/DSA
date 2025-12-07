
def findall_substring(string, substr):
    pos= -1;
    flag= False
    
    n= len(string)
    while True:
         pos= string.lower().find(substr, pos+1, n)
         total_substr= string.count(substr)
         print(total_substr)
         if pos== -1:
             break
         print("Sub string found at index", pos)
         flag=True
    if flag == False:
        print("No substring found")
        
# findall_substring("safikmahammadsafikdhbsafikdnvc", "safik")

s= "asdfaaagsdf"

ans= s.replace("a", "b")
print(ans)
