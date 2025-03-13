mydict:dict={"key1":"value1","key2":"value2"}


for key in mydict:
    print(key)                 #printa solamente le chiavi
    
for key in mydict:
    print(mydict[key])               

for keys, values in mydict.items():
    print(f"chiave:{keys}, valore:{values}")                #questa funzione ti crea una lista di tuple dove ogni tupla ha una chiave e un valore corrispondente

for value in mydict.values():
    print(value)

for key in mydict.keys():
    print(key)
    
# .items()-> [(key1,value1),(key2,value2)]

firstlst=[1,2,3,4,5]

firstlst.extend({"key": "value","Bool" :True}.items())
print(firstlst)