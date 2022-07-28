class fg:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'


# Leemos el archivo
a_file = open("1bdd_ascii", "r")
file_read = a_file.read()
a_file.close()
# Separamos por saltos de linea
list_of_lines = file_read.split('\n')
# Creamos un arreglo para enumerar la cantidad de capas disponibles
layers = []
# Identificamos las capas disponibles en el layout
for line in list_of_lines:
    if line[0:5] == "LAYER":
        number_layer = line[0:-1]  # Tomamos el nombre del layer sin el ';'
        if not layers:  # Si esta vacio, se agrega el primer LAYER
            layers.append(number_layer)
        else:
            for layer in layers:
                if number_layer not in layers:  # Verificamos que no se repitan en la lista
                    layers.append(number_layer)
print(fg.cyan, "Layers availables: ")
for layer in layers:
    print('\t' + layer)
# Se identifica las lineas donde se describen las cordenadas de cada unas de las capas
box_index = []  # Se lista los index de los BOX
for index, line in enumerate(list_of_lines):
    if line == "BOX;":
        box_index.append(index)
list_layer_index = []
for layer in layers:
    layer_box_index = [layer]
    for index in box_index:
        if list_of_lines[index + 1][:-1] == layer:
            layer_box_index.append(index + 3)
    list_layer_index.append(layer_box_index)  # Se obtiene los index de cada BOX de cada LAYER
# print(list_layer_index) # [[LAYER1,Coord0,Coord1,Coord2,Coord3],[LAYER2,Coord0,Coord1,Coord2,Coord3],...]
# Determinamos el area de cada BOX de un LAYER
unit_um = 0.001
list_layer_area = []
for layerN_boxN in list_layer_index:
    box = 0
    for index in layerN_boxN[1:]:
        layer_box_area = []
        cd0 = list_of_lines[index].split('\t\t\t')
        cd1 = list_of_lines[index + 1].split('\t\t\t')
        cd2 = list_of_lines[index + 2].split('\t\t\t')
        cd3 = list_of_lines[index + 3].split('\t\t\t')
        x0 = int(cd0[0][5:-1])
        y0 = int(cd0[1][4:-1])
        x1 = int(cd1[0][5:-1])
        y1 = int(cd1[1][4:-1])
        x2 = int(cd2[0][5:-1])
        y2 = int(cd2[1][4:-1])
        x3 = int(cd3[0][5:-1])
        y3 = int(cd3[1][4:-1])
        Ancho = (x1 - x0)
        Largo = (y2 - y1)
        Area = (Ancho * Largo)
        layer_box_area.append(layerN_boxN[0])
        layer_box_area.append("BOX:" + str(box))
        layer_box_area.append("Width:" + str(Ancho))
        layer_box_area.append("Large:" + str(Largo))
        layer_box_area.append("Area:" + str(Area))
        box = box + 1
        list_layer_area.append(layer_box_area)

print(fg.red, '\n' + str(len(list_layer_area)) + " BOX AREA WHERE FOUND\n")
print(fg.lightgrey, "Box Area per Layer:")

for index, box in enumerate(list_layer_area):
    print('\t', fg.blue, index + 1, '\t', fg.green, box[0], fg.lightcyan, box[1], fg.lightgrey, box[2], box[3],
          fg.yellow, box[4])
# Poly Layer is No. 2. We are goind to take the data stored in the list
poly_area = 0
poly_large = 0
for box in list_layer_area:
    if box[0] == "LAYER 2":
        poly_area = poly_area + int(box[4][5:])
        poly_large = poly_large + int(box[3][6:])
print("TOTAL POLY AREA:\t"+str(poly_area*unit_um)+'\n'+"TOTAL POLY LARGE:\t"+str(poly_large*unit_um))

#Calculation of Area of the Layout
top_area = 0
bottom_area = 0
for box in list_layer_area:
    if box[0] == "LAYER 5":
        top_area = top_area + int(box[4][5:])
for box in list_layer_area:
    if box[0] == "LAYER 6":
        bottom_area = bottom_area + int(box[4][5:])
print(fg.pink+"TOTAL LAYOUT AREA:\t"+str((top_area+bottom_area)*unit_um))
