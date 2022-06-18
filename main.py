import os    

# Initialize rgb_to_hex
def hex_to_rgb(value): #https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

print("Welcome to Just Dance color converter")
typecolor=input("Do you want to use RGB or HEX? ")

if typecolor=='RGB' or  typecolor=='rgb':
    try:
        os.mkdir("output")
    except:
        pass
    r=int(input("R: "))
    g=int(input("G: "))
    b=int(input("B: "))
    # color/255 = jdcolor
    rcolor=r/255
    gcolor=g/255
    bcolor=b/255

if typecolor == 'HEX' or  typecolor=='hex':
    try:
        os.mkdir("output")
    except:
        pass
    HEXColor=str(input('Hex color here: '))
    conv=hex_to_rgb(HEXColor)
    # color/255 = jdcolor
    rcolor=conv[0]/255
    gcolor=conv[1]/255
    bcolor=conv[2]/255

# write 
print("")
print(rcolor)
print(gcolor)
print(bcolor)
arq = open("output//"+typecolor.lower()+"tojd.json", "w", encoding='utf-8')
arq.write('{"Clips": [{"Color":')
arq.write('[1,')
arq.write(str(rcolor))
arq.write(',')
arq.write(str(gcolor))
arq.write(',')
arq.write(str(bcolor))
arq.write('],')
arq.write('"IsColor": 1')
arq.write('}')
arq.write('],}')
arq.close()
os.system("pause")
os.system("cls")