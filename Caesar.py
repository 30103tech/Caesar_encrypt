a = input("text to encrypt: ") 
b = int(input("distance: ")) 
code = "" 
for ch in a:    
    ordValue = ord(ch)  
    cipherValue = ordValue + b   
    if cipherValue > ord('z'):      
        cipherValue = ord('a') + b - (ord('z') - ordValue + 1)
    code = code + chr(cipherValue)
print(code)