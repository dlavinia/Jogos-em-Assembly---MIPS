from PIL import Image
from matplotlib import image

import sys
data = image.imread(sys.argv[1])
linhas = data.shape[0]
colunas = data.shape[1]
indx=0
x=0
#print(str(linhas) + "x" + str(colunas))
for i in data:
    linha = "ln" + str(x).rjust(3, '0')+":  .word "
    x+=1
    for j in i:
        indx=indx+1
        r = hex(j[0]).replace('0x','').rjust(2, '0')
        g = hex(j[1]).replace('0x','').rjust(2, '0')  
        b = hex(j[2]).replace('0x','').rjust(2, '0')
        linha=linha+'0x00'+r+g+b+' '
    print(linha)
#print(indx)
