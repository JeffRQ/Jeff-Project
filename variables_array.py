# Declare 6 variables unidimensionales y asigne valores enteros

cinturon = [2, 4, 6, 8, 10, 12]
# ind       0  1  2  3   4   5

for i in range(len(cinturon)):
    print("Tallas:""->", cinturon[i])

# Declare 6 variables unidimensionales y asigne valores flotantes

clavos = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
# ind      0    1    2    3    4    5

for i in range(len(clavos)):
    print("pulgadas:""->", clavos[i])

# Declare 6 variables unidimensionales y asignar valores de texto

nombres = ["Alicia", "Andres", "Carlos", "Daniel", "Elizabeth", "Francisco"]
# indices      0         1         2         3          4            5

for i in range(len(nombres)):
    print("nombre:", nombres[i])

# Declare 6 variables unidimensionales y asignar valores de enteros, flotantes y texto

numeros = [1, 1.0, "uno", 2, 2.0, "dos"]

for i in range(len(numeros)):
    print("numero:", numeros[i])

# Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asigne valores enteros (6 variables en total)

num_ent1_2x3 = [
    [2,  4,  6],  # indices 0 numero
    [8, 10, 12]  # indices 1 numero
    # 0  1  2
]

print("numero:", num_ent1_2x3[0][1])
print("numero:", num_ent1_2x3[1][1])

num_ent2_2x3 = [
    [3,  5,  7],  # indices 0 numero
    [9, 11, 13]  # indices 1 numero
    # 0  1   2
]

print("numero:", num_ent2_2x3[0][2])
print("numero:", num_ent2_2x3[1][2])

num_ent3_5x5 = [
    [2,   4,  6,  8, 10],  # indices 0 numero
    [12, 14, 16, 18, 20],  # indices 1 numero
    [22, 24, 26, 28, 30],  # indices 2 numero
    [32, 34, 36, 38, 40],  # indices 3 numero
    [42, 44, 46, 48, 50]   # indices 4 numero
    # 0   1   2   3   4
]

print("numero:", num_ent3_5x5[0][0])
print("numero:", num_ent3_5x5[1][2])
print("numero:", num_ent3_5x5[2][4])
print("numero:", num_ent3_5x5[3][1])
print("numero:", num_ent3_5x5[4][2])

num_ent4_5x5 = [
    [1,   3,  5,  7,  9],  # indices 0 numero
    [11, 13, 15, 17, 19],  # indices 1 numero
    [21, 23, 25, 27, 29],  # indices 2 numero
    [31, 33, 35, 37, 39],  # indices 3 numero
    [41, 43, 45, 47, 49]   # indices 4 numero
    # 0  1   2    3   4
]

print("numero:", num_ent4_5x5[0][2])
print("numero:", num_ent4_5x5[1][4])
print("numero:", num_ent4_5x5[2][0])
print("numero:", num_ent4_5x5[3][3])
print("numero:", num_ent4_5x5[4][1])

num_ent5_3x6 = [
    [1,   2,  3,  4,  5,  6],  # indices 0 numero
    [7,   8,  9, 10, 11, 12],  # indices 1 numero
    [13, 14, 15, 16, 17, 18]   # indices 2 numero
    # 0  1   2   3   4   5
]

print("numero:", num_ent5_3x6[0][1])
print("numero:", num_ent5_3x6[1][3])
print("numero:", num_ent5_3x6[2][5])

num_ent6_3x6 = [
    [19, 20, 21, 22, 23, 24],  # indices 0 numero
    [25, 26, 27, 28, 29, 30],  # indices 1 numero
    [31, 32, 33, 34, 35, 36]   # indices 2 numero
    # 0   1   2   3   4   5
]

print("numero:", num_ent6_3x6[0][1])
print("numero:", num_ent6_3x6[1][3])
print("numero:", num_ent6_3x6[2][5])

# Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asigne valores flotantes (6 variables en total)

num_flo1_2x3 = [
    [1.1, 1.2, 1.3],  # indices 0 num flo
    [2.1, 2.2, 2.3]   # indices 1 num flo
    # 0    1    2
]

print("numero flo:", num_flo1_2x3[0][0])
print("numero flo:", num_flo1_2x3[1][1])

num_flo2_2x3 = [
    [3.1, 3.2, 3.3],  # indices 0 num flo
    [4.1, 4.2, 4.3]   # indices 1 num flo
    # 0    1     2
]

print("numero flo:", num_flo2_2x3[0][2])
print("numero flo:", num_flo2_2x3[1][0])

num_flo3_5x5 = [
    [0.5,   1.0,  1.5,  2.0,  2.5],  # indices 0 numero flo
    [3.0,   3.5,  4.0,  4.5,  5.0],  # indices 1 numero flo
    [5.5,   6.0,  6.5,  7.0,  7.5],  # indices 2 numero flo
    [8.0,   8.5,  9.0,  9.5, 10.0],  # indices 3 numero flo
    [10.5, 11.0, 11.5, 12.0, 12.5]   # indices 4 numero flo
    # 0      1     2     3     4
]

print("numero flo:", num_flo3_5x5[0][2])
print("numero flo:", num_flo3_5x5[1][1])
print("numero flo:", num_flo3_5x5[2][3])
print("numero flo:", num_flo3_5x5[3][2])
print("numero flo:", num_flo3_5x5[4][0])

num_flo4_5x5 = [
    [13.0, 13.5, 14.0, 14.5, 15.0],  # indices 0 numero flo
    [15.5, 16.0, 16.5, 17.0, 17.5],  # indices 1 numero flo
    [18.0, 18.5, 19.0, 19.5, 20.0],  # indices 2 numero flo
    [20.5, 21.0, 21.5, 22.0, 22.5],  # indices 3 numero flo
    [23.0, 23.5, 24.0, 24.5, 25.0]   # indices 4 numero flo
    # 0     1     2     3     4
]

print("numero flo:", num_flo4_5x5[0][1])
print("numero flo:", num_flo4_5x5[1][4])
print("numero flo:", num_flo4_5x5[2][0])
print("numero flo:", num_flo4_5x5[3][2])
print("numero flo:", num_flo4_5x5[4][3])

num_flo5_3x6 = [
    [5.1, 5.2, 5.3, 5.4, 5.5, 5.6],  # indices 0 numero flo
    [6.1, 6.2, 6.3, 6.4, 6.5, 6.6],  # indices 1 numero flo
    [7.1, 7.2, 7.3, 7.4, 7.5, 7.6]   # indices 2 numero flo
    # 0    1    2    3    4    5
]

print("numero flo:", num_flo5_3x6[0][2])
print("numero flo:", num_flo5_3x6[1][0])
print("numero flo:", num_flo5_3x6[2][1])

num_flo6_3x6 = [
    [8.1,   8.2,  8.3,  8.4,  8.5,  8.6],  # indices 0 numero flo
    [9.1,   9.2,  9.3,  9.4,  9.5,  9.6],  # indices 1 numero flo
    [10.1, 10.2, 10.3, 10.4, 10.5, 10.6]   # indices 2 numero flo
    # 0     1     2     3     4     5
]

print("numero flo:", num_flo6_3x6[0][0])
print("numero flo:", num_flo6_3x6[1][3])
print("numero flo:", num_flo6_3x6[2][0])

# Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asignar valores de texto (6 variables en total)

nombres_apellidos_H = [
    ["Carlos",         "Juan",   "Javier"],  # indices 0 Nombres
    ["Fernandez", "Dominguez", "Zambrano"]   # indices 1 Apellidos
    #    0            1            2
]

print("nombre:", nombres_apellidos_H[0][2])
print("apellido:", nombres_apellidos_H[1][2])

nombres_apellidos_M = [
    ["Thalia",   "Paola",   "Veronica"],  # indices 0 Nombres
    ["Moreira", "Carpio",     "Castro"]   # indices 1 Apellidos
    #    0            1            2
]

print("nombre:", nombres_apellidos_M[0][1])
print("apellido:", nombres_apellidos_M[1][1])

articulos5x5 = [
    ["zapatos",  "ropa",  "celular",   "mochilas", "cuadernos"],  # indices 0 articulos
    ["adidas",  "tommy",    "nokia",   "jansport",    "estilo"],  # indices 1 marca
    ["puma",     "boss", "motorola",      "totto",   "escribe"],  # indices 2 marca
    ["nike",  "nautica",  "samsung", "mountainna",     "norma"],  # indices 3 marca
    ["umbro", "lacoste",   "huawei",       "fila",  "jeanbook"]   # indices 4 marca
    #  0         1            2            3             4
]

print("Articulo:", articulos5x5[0][2])
print("Marca:", articulos5x5[1][2])
print("Marca:", articulos5x5[2][2])
print("Marca:", articulos5x5[3][2])
print("Marca:", articulos5x5[4][2])

articulos_1_5x5 = [
    ["zapatos",  "pantalon",  "camiseta",    "camisa",  "chaqueta"],  # indices 0 articulos
    ["nuevo",       "nuevo",     "nuevo",     "nuevo",     "nuevo"],  # indices 1 estado
    ["usado",       "usado",     "usado",     "usado",     "usado"],  # indices 2 estado
    ["roto",         "roto",      "roto",      "roto",      "roto"],  # indices 3 estado
    ["manchado", "manchado",  "manchado",  "manchado",  "manchado"]   # indices 4 estado
    #     0          1            2            3             4
]

print("Articulo:", articulos_1_5x5[0][1])
print("estado:", articulos_1_5x5[1][4])
print("estado:", articulos_1_5x5[2][2])
print("estado:", articulos_1_5x5[3][2])
print("estado:", articulos_1_5x5[4][2])

heroes_3x6 = [
    ["thor",       "hulk", "c.america", "ironman",    "spider man",       "logan"],  # indices 0 Marvel
    ["superman", "batman",     "flash", "aquaman",  "wonder woman", "green arrow"],  # indices 1 DC comics
    ["goku",    "vegueta",    "picoro",  "krilin",         "gohan",      "trunks"]   # indices 2 DBZ
    #   0           1             2          3              4              5
]

print("marvel:", heroes_3x6[0][3])
print("DC comics:", heroes_3x6[1][2])
print("DBZ:", heroes_3x6[2][0])

villanos_3x6 = [
    ["magneto",    "galactus", "kang", "thanos",    "ultron",       "apocalipsis"],  # indices 0 Marvel
    ["guason", "lex luthor",     "zod", "bizarro",  "siniestro", "darkseid"],  # indices 1 DC comics
    ["cell",    "majinbuu",    "jiren",  "freezer",         "broly",      "bills"]   # indices 2 DBZ
    #   0           1             2          3              4              5
]

print("marvel villanos:", villanos_3x6[0][4])
print("DC comics villanos:", villanos_3x6[1][1])
print("DBZ villanos:", villanos_3x6[2][5])

# Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asignar valores de enteros, flotantes y texto (6 variables en
# total)

mercado_2x3 = [
    [1,         2.50,  3.80],  # indices 0 valor
    ["melon", "pera", "uva"]   # indices 1 fruta
    #   0       1       2
]

print("valor:", mercado_2x3[0][1])
print("fruta:", mercado_2x3[1][1])

mercado_1_2x3 = [
    ["tomate", "cebolla", "pimiento"],  # indices 0 vegetales
    [3,              4.5,        6.2]   # indices 1 peso
    #   0           1          2
]

print("vegetales:", mercado_1_2x3[0][2])
print("libra:", mercado_1_2x3[1][2])

mercado_2_5x5 = [
    [00.1,         00.2,     00.3,     00.4,      00.5],  # indices 0 código
    [1,               2,        3,        4,         5],  # indices 1 cantidad
    ["aceite",   "atún",  "carne", "fideos", "mostaza"],  # indices 2 producto
    [1.80,         3.20,     1.50,     4.25,      1.15],  # indices 3 precio
    ["anden1", "anden2", "anden3", "anden4",  "anden5"]   # indices 4 lugar
    #   0          1          2        3         4
]

print("código:", mercado_2_5x5[0][3])
print("cantidad:", mercado_2_5x5[1][0])
print("producto:", mercado_2_5x5[2][3])
print("precio:", mercado_2_5x5[3][2])
print("lugar:", mercado_2_5x5[4][3])

mercado_3_5x5 = [
    [00.6,           00.7,     00.8,     00.9,      00.10],  # indices 0 código
    [1,                 2,        3,        4,          5],  # indices 1 cantidad
    ["achiote", "sardina",  "pollo", "harina", "mayonesa"],  # indices 2 producto
    [1.90,           3.15,     1.30,     2.35,       1.55],  # indices 3 precio
    ["anden1",   "anden2", "anden3", "anden4",   "anden5"]   # indices 4 lugar
    #   0           1          2         3          4
]

print("código:", mercado_3_5x5[0][4])
print("cantidad:", mercado_3_5x5[1][0])
print("producto:", mercado_3_5x5[2][4])
print("precio:", mercado_3_5x5[3][1])
print("lugar:", mercado_3_5x5[4][4])

mercado_4_3x6 = [
    ["res", "pescado", "pavo", "pollo", "camarón", "chancho"],  # indices 0 producto
    [1,             2,      3,       4,         5,         6],  # indices 1 código
    [1.60,       1.40,   3.20,    1.30,      2.30,      1.90]   # indices 2 precio
    #  0         1        2       3          4         5
]

print("producto:", mercado_4_3x6[0][2])
print("código:", mercado_4_3x6[1][2])
print("precio:", mercado_4_3x6[2][2])

mercado_5_3x6 = [
    ["res", "pescado", "pavo", "pollo", "camarón", "chancho"],  # indices 0 producto
    [1,             2,      3,       4,         5,         6],  # indices 1 código
    [1.60,       1.40,   3.20,    1.30,      2.30,      1.90]   # indices 2 precio
    #  0         1        2       3          4         5
]

print("producto:", mercado_5_3x6[0][5])
print("código:", mercado_5_3x6[1][5])
print("precio:", mercado_5_3x6[2][5])

#  Declare 2 variables tridimensionales 2x3x2, 5x5x5, 3x6x2 y asigne valores enteros (6 variables en
#  total )

num_ent_tri1 = [
    [
        [1,   2,  3],
        [4,   5,  6]
    ],
    [
        [7,   8,  9],
        [10, 11, 12]
    ]
]

print("numero tri1:", num_ent_tri1[0][0][1])
print("numero tri2:", num_ent_tri1[0][1][2])
print("numero tri3:", num_ent_tri1[1][0][0])
print("numero tri4:", num_ent_tri1[1][1][1])

num_ent_tri2 = [
    [
        [13,  14,  15],
        [16,  17,  18]
    ],
    [
        [19,  20,  21],
        [22,  23,  24]
    ]
]

print("numero tri5:", num_ent_tri2[0][0][0])
print("numero tri6:", num_ent_tri2[0][1][1])
print("numero tri7:", num_ent_tri2[1][0][2])
print("numero tri8:", num_ent_tri2[1][1][1])

numero_ent_tri3_5x5x5 = [
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ],
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ],
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ],
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ],
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
]

print("numer tri9:", numero_ent_tri3_5x5x5[0][0][0])
print("numer tri10:", numero_ent_tri3_5x5x5[0][1][1])
print("numer tri11:", numero_ent_tri3_5x5x5[0][2][2])
print("numer tri12:", numero_ent_tri3_5x5x5[0][3][3])
print("numer tri13:", numero_ent_tri3_5x5x5[0][4][4])

print("numer tri14:", numero_ent_tri3_5x5x5[1][0][0])
print("numer tri15:", numero_ent_tri3_5x5x5[1][1][1])
print("numer tri16:", numero_ent_tri3_5x5x5[1][2][2])
print("numer tri17:", numero_ent_tri3_5x5x5[1][3][3])
print("numer tri18:", numero_ent_tri3_5x5x5[1][4][4])

print("numer tri19:", numero_ent_tri3_5x5x5[2][0][0])
print("numer tri20:", numero_ent_tri3_5x5x5[2][1][1])
print("numer tri21:", numero_ent_tri3_5x5x5[2][2][2])
print("numer tri22:", numero_ent_tri3_5x5x5[2][3][3])
print("numer tri23:", numero_ent_tri3_5x5x5[2][4][4])

print("numer tri24:", numero_ent_tri3_5x5x5[3][0][0])
print("numer tri25:", numero_ent_tri3_5x5x5[3][1][1])
print("numer tri26:", numero_ent_tri3_5x5x5[3][2][2])
print("numer tri27:", numero_ent_tri3_5x5x5[3][3][3])
print("numer tri28:", numero_ent_tri3_5x5x5[3][4][4])

print("numer tri29:", numero_ent_tri3_5x5x5[4][0][0])
print("numer tri30:", numero_ent_tri3_5x5x5[4][1][1])
print("numer tri31:", numero_ent_tri3_5x5x5[4][2][2])
print("numer tri32:", numero_ent_tri3_5x5x5[4][3][3])
print("numer tri33:", numero_ent_tri3_5x5x5[4][4][4])

numero_ent_tri_4_5x5x5 = [
    [
        [26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40],
        [41, 42, 43, 44, 45],
        [46, 47, 48, 49, 50]
    ],
    [
        [26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40],
        [41, 42, 43, 44, 45],
        [46, 47, 48, 49, 50]
    ],
    [
        [26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40],
        [41, 42, 43, 44, 45],
        [46, 47, 48, 49, 50]
    ],
    [
        [26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40],
        [41, 42, 43, 44, 45],
        [46, 47, 48, 49, 50]
    ],
    [
        [26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40],
        [41, 42, 43, 44, 45],
        [46, 47, 48, 49, 50]
    ]
]

print("numer tri34:", numero_ent_tri_4_5x5x5[0][0][4])
print("numer tri35:", numero_ent_tri_4_5x5x5[0][1][3])
print("numer tri36:", numero_ent_tri_4_5x5x5[0][2][2])
print("numer tri37:", numero_ent_tri_4_5x5x5[0][3][1])
print("numer tri38:", numero_ent_tri_4_5x5x5[0][4][0])

print("numer tri39:", numero_ent_tri_4_5x5x5[1][0][4])
print("numer tri40:", numero_ent_tri_4_5x5x5[1][1][3])
print("numer tri41:", numero_ent_tri_4_5x5x5[1][2][2])
print("numer tri42:", numero_ent_tri_4_5x5x5[1][3][1])
print("numer tri43:", numero_ent_tri_4_5x5x5[1][4][0])

print("numer tri44:", numero_ent_tri_4_5x5x5[2][0][4])
print("numer tri45:", numero_ent_tri_4_5x5x5[2][1][3])
print("numer tri46:", numero_ent_tri_4_5x5x5[2][2][2])
print("numer tri47:", numero_ent_tri_4_5x5x5[2][3][1])
print("numer tri48:", numero_ent_tri_4_5x5x5[2][4][0])

print("numer tri49:", numero_ent_tri_4_5x5x5[3][0][4])
print("numer tri50:", numero_ent_tri_4_5x5x5[3][1][3])
print("numer tri51:", numero_ent_tri_4_5x5x5[3][2][2])
print("numer tri52:", numero_ent_tri_4_5x5x5[3][3][1])
print("numer tri53:", numero_ent_tri_4_5x5x5[3][4][0])

print("numer tri54:", numero_ent_tri_4_5x5x5[4][0][4])
print("numer tri55:", numero_ent_tri_4_5x5x5[4][1][3])
print("numer tri56:", numero_ent_tri_4_5x5x5[4][2][2])
print("numer tri57:", numero_ent_tri_4_5x5x5[4][3][1])
print("numer tri58:", numero_ent_tri_4_5x5x5[4][4][0])

num_ent_tri5_3x6x2 = [
    [
        [1,   2,  3,  4,  5,  6],
        [7,   8,  9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18]
    ],
    [
        [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35, 36]
    ]
]

print("numer tri59:", num_ent_tri5_3x6x2[0][0][1])
print("numer tri60:", num_ent_tri5_3x6x2[0][1][1])
print("numer tri61:", num_ent_tri5_3x6x2[0][2][1])

print("numer tri61:", num_ent_tri5_3x6x2[1][0][1])
print("numer tri62:", num_ent_tri5_3x6x2[1][1][1])
print("numer tri63:", num_ent_tri5_3x6x2[1][2][1])

num_ent_tri6_3x6x2 = [
    [
        [37, 38, 39, 40, 41, 42],
        [43, 44, 45, 46, 47, 48],
        [49, 50, 51, 52, 53, 54]
    ],
    [
        [55, 56, 57, 58, 59, 60],
        [61, 62, 63, 64, 65, 66],
        [67, 68, 69, 70, 71, 72]
    ]
]

print("numer tri64:", num_ent_tri6_3x6x2[0][0][3])
print("numer tri65:", num_ent_tri6_3x6x2[0][1][3])
print("numer tri66:", num_ent_tri6_3x6x2[0][2][3])

print("numer tri67:", num_ent_tri6_3x6x2[1][0][3])
print("numer tri68:", num_ent_tri6_3x6x2[1][1][3])
print("numer tri69:", num_ent_tri6_3x6x2[1][2][3])

# Declare 2 variables tridimensionales 2x3x1, 5x5x2, 3x6x5 y asigne valores flotantes (6 variables en total)

num_flo_tri1 = [
    [
        [0.5, 1.0,  1.5]
    ],
    [
        [3.5, 4.0,  4.5],
    ]
]

print("numero flo1:", num_flo_tri1[0][0][0])
print("numero flo2:", num_flo_tri1[1][0][0])


num_flo_tri2 = [
    [
        [6.5,  7.0,  7.5]
    ],
    [
        [9.5, 10.0, 10.5]
    ]
]

print("numero flo3:", num_flo_tri2[0][0][0])
print("numero flo4:", num_flo_tri2[1][0][0])


numero_flo_tri3_5x5x2 = [
    [
        [1.1, 1.2, 1.3, 1.4, 1.5],
        [2.1, 2.2, 2.3, 2.4, 2.5]

    ],
    [
        [1.1, 1.2, 1.3, 1.4, 1.5],
        [2.1, 2.2, 2.3, 2.4, 2.5]

    ],
    [
        [1.1, 1.2, 1.3, 1.4, 1.5],
        [2.1, 2.2, 2.3, 2.4, 2.5]

    ],
    [
        [1.1, 1.2, 1.3, 1.4, 1.5],
        [2.1, 2.2, 2.3, 2.4, 2.5]

    ],
    [
        [1.1, 1.2, 1.3, 1.4, 1.5],
        [2.1, 2.2, 2.3, 2.4, 2.5]

    ]
]

print("numero flo5:", numero_flo_tri3_5x5x2[0][0][0])
print("numero flo6:", numero_flo_tri3_5x5x2[0][1][1])


print("numero flo7:", numero_flo_tri3_5x5x2[1][0][0])
print("numero flo8:", numero_flo_tri3_5x5x2[1][1][1])


print("numero flo9:", numero_flo_tri3_5x5x2[2][0][0])
print("numero flo10:", numero_flo_tri3_5x5x2[2][1][1])


print("numero flo11:", numero_flo_tri3_5x5x2[3][0][0])
print("numero flo12:", numero_flo_tri3_5x5x2[3][1][1])


print("numero flo13:", numero_flo_tri3_5x5x2[4][0][0])
print("numero flo14:", numero_flo_tri3_5x5x2[4][1][1])


numero_flo_tri_4_5x5x2 = [
    [
        [6.1,   6.2,  6.3,  6.4,  6.5],
        [7.1,   7.2,  7.3,  7.4,  7.5]

    ],
    [
        [6.1,   6.2,  6.3,  6.4,  6.5],
        [7.1,   7.2,  7.3,  7.4,  7.5]

    ],
    [
        [6.1,   6.2,  6.3,  6.4,  6.5],
        [7.1,   7.2,  7.3,  7.4,  7.5]

    ],
    [
        [6.1,   6.2,  6.3,  6.4,  6.5],
        [7.1,   7.2,  7.3,  7.4,  7.5]

    ],
    [
        [6.1,   6.2,  6.3,  6.4,  6.5],
        [7.1,   7.2,  7.3,  7.4,  7.5]

    ]
]

print("numero flo15:", numero_flo_tri_4_5x5x2[0][0][4])
print("numero flo16:", numero_flo_tri_4_5x5x2[0][1][3])


print("numero flo17:", numero_flo_tri_4_5x5x2[1][0][4])
print("numero flo18:", numero_flo_tri_4_5x5x2[1][1][3])


print("numero flo19:", numero_flo_tri_4_5x5x2[2][0][4])
print("numero flo20:", numero_flo_tri_4_5x5x2[2][1][3])


print("numero flo21:", numero_flo_tri_4_5x5x2[3][0][4])
print("numero flo22:", numero_flo_tri_4_5x5x2[3][1][3])


print("numero flo23:", numero_flo_tri_4_5x5x2[4][0][4])
print("numero flo24:", numero_flo_tri_4_5x5x2[4][1][3])


num_flo_tri5_3x6x5 = [
    [
        [1.1, 2.1, 3.1, 4.1, 5.1, 6.1],
        [1.2, 2.2, 3.2, 4.2, 5.2, 6.2],
        [1.3, 2.3, 3.3, 4.3, 5.3, 6.3],
        [1.4, 2.4, 3.4, 4.4, 5.4, 6.4],
        [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    ],
    [
        [1.6, 2.6, 3.6, 4.6, 5.6, 6.6],
        [1.7, 2.7, 3.7, 4.7, 5.7, 6.7],
        [1.8, 2.8, 3.8, 4.8, 5.8, 6.8],
        [1.9, 2.9, 3.9, 4.9, 5.9, 6.9],
        [1.10, 2.10, 3.10, 4.10, 5.10, 6.10]
    ],
    [
        [1.11, 2.11, 3.11, 4.11, 5.11, 6.11],
        [1.12, 2.12, 3.12, 4.12, 5.12, 6.12],
        [1.13, 2.13, 3.13, 4.13, 5.13, 6.13],
        [1.14, 2.14, 3.14, 4.14, 5.14, 6.14],
        [1.15, 2.15, 3.15, 4.15, 5.15, 6.15]
    ]
]

print("numero flo25:", num_flo_tri5_3x6x5[0][0][1])
print("numero flo26:", num_flo_tri5_3x6x5[0][1][1])
print("numero flo27:", num_flo_tri5_3x6x5[0][2][1])
print("numero flo28:", num_flo_tri5_3x6x5[0][3][1])
print("numero flo29:", num_flo_tri5_3x6x5[0][4][1])

print("numero flo30:", num_flo_tri5_3x6x5[1][0][1])
print("numero flo31:", num_flo_tri5_3x6x5[1][1][1])
print("numero flo32:", num_flo_tri5_3x6x5[1][2][1])
print("numero flo33:", num_flo_tri5_3x6x5[1][3][1])
print("numero flo34:", num_flo_tri5_3x6x5[1][4][1])

print("numero flo35:", num_flo_tri5_3x6x5[2][0][1])
print("numero flo36:", num_flo_tri5_3x6x5[2][1][1])
print("numero flo37:", num_flo_tri5_3x6x5[2][2][1])
print("numero flo38:", num_flo_tri5_3x6x5[2][3][1])
print("numero flo39:", num_flo_tri5_3x6x5[2][4][1])

num_flo_tri6_3x6x5 = [
    [
        [1.16, 2.16, 3.16, 4.16, 5.16, 6.16],
        [1.17, 2.17, 3.17, 4.17, 5.17, 6.17],
        [1.18, 2.18, 3.18, 4.18, 5.18, 6.18],
        [1.19, 2.19, 3.19, 4.19, 5.19, 6.19],
        [1.20, 2.20, 3.20, 4.20, 5.20, 6.20]
    ],
    [
        [1.21, 2.21, 3.21, 4.21, 5.21, 6.21],
        [1.22, 2.22, 3.22, 4.22, 5.22, 6.22],
        [1.23, 2.23, 3.23, 4.23, 5.23, 5.23],
        [1.24, 2.24, 3.24, 4.24, 5.24, 6.24],
        [1.25, 2.25, 3.25, 4.25, 5.25, 6.25]
    ],
    [
        [1.26, 2.26, 3.26, 4.26, 5.26, 6.26],
        [1.27, 2.27, 3.27, 4.27, 5.27, 6.27],
        [1.28, 2.28, 3.28, 4.28, 5.28, 6.28],
        [1.29, 2.29, 3.29, 4.29, 5.29, 6.29],
        [1.30, 2.30, 3.30, 4.30, 5.30, 6.30]
    ]
]

print("numero flo40:", num_flo_tri6_3x6x5[0][0][3])
print("numero flo41:", num_flo_tri6_3x6x5[0][1][3])
print("numero flo42:", num_flo_tri6_3x6x5[0][2][3])
print("numero flo43:", num_flo_tri6_3x6x5[0][0][3])
print("numero flo44:", num_flo_tri6_3x6x5[0][1][3])

print("numero flo45:", num_flo_tri6_3x6x5[1][0][3])
print("numero flo46:", num_flo_tri6_3x6x5[1][1][3])
print("numero flo47:", num_flo_tri6_3x6x5[1][2][3])
print("numero flo48:", num_flo_tri6_3x6x5[1][0][3])
print("numero flo49:", num_flo_tri6_3x6x5[1][1][3])

print("numero flo50:", num_flo_tri6_3x6x5[2][0][3])
print("numero flo51:", num_flo_tri6_3x6x5[2][1][3])
print("numero flo52:", num_flo_tri6_3x6x5[2][2][3])
print("numero flo53:", num_flo_tri6_3x6x5[2][0][3])
print("numero flo54:", num_flo_tri6_3x6x5[2][1][3])


# Declare 2 variables tridimensionales 2x3x3, 5x5x4, 3x6x1 y asignar valores de texto (6 variables en
# total)

nombres_tex_tri1 = [
    [
        ["Anabel", "Margaret",   "Sofia"],
        ["Claudia",   "Nancy", "Vanessa"]
    ],
    [
        ["Franco",  "Pepe",  "Andreas"],
        ["Ciro", "Roberto", "Mauricio"]
    ]
]

print("nombre tex1:", nombres_tex_tri1[0][0][1])
print("nombre tex2:", nombres_tex_tri1[0][1][2])
print("nombre tex3:", nombres_tex_tri1[1][0][0])
print("nombre tex4:", nombres_tex_tri1[1][1][1])

apellidos_tex_tri2 = [
    [
        ["Plata",   "Diaz", "Cevallos"],
        ["Vera", "Alcibar",    "Tello"]
    ],
    [
        ["Cisneros", "Jimenez",  "Reyes"],
        ["Zumba",     "Piedra", "Tinoco"]
    ]
]

print("apellido tex5:", apellidos_tex_tri2[0][0][0])
print("apellido tex6:", apellidos_tex_tri2[0][1][1])
print("apellido tex7:", apellidos_tex_tri2[1][0][2])
print("apellido tex8:", apellidos_tex_tri2[1][1][1])

animales_tierra_tri3_5x5x5 = [
    [
        ["camello",      "Lobo",     "topo",    "Liebre",  "Pantera"],
        ["gallina",      "gato",    "perro", "tarantula",    "oveja"],
        ["Cerdo",      "iguana",   "bufalo",    "gusano",  "mapache"],
        ["alce",    "escorpion", "elefante",    "venado",      "oso"],
        ["araña", "rinoceronte",     "mula",      "rata", "avestruz"]
    ],
    [
        ["camello",      "Lobo",     "topo",    "Liebre",  "Pantera"],
        ["gallina",      "gato",    "perro", "tarantula",    "oveja"],
        ["Cerdo",      "iguana",   "bufalo",    "gusano",  "mapache"],
        ["alce",    "escorpion", "elefante",    "venado",      "oso"],
        ["araña", "rinoceronte",     "mula",      "rata", "avestruz"]
    ],
    [
        ["camello",      "Lobo",     "topo",    "Liebre",  "Pantera"],
        ["gallina",      "gato",    "perro", "tarantula",    "oveja"],
        ["Cerdo",      "iguana",   "bufalo",    "gusano",  "mapache"],
        ["alce",    "escorpion", "elefante",    "venado",      "oso"],
        ["araña", "rinoceronte",     "mula",      "rata", "avestruz"]
    ],
    [
        ["camello",      "Lobo",     "topo",    "Liebre",  "Pantera"],
        ["gallina",      "gato",    "perro", "tarantula",    "oveja"],
        ["Cerdo",      "iguana",   "bufalo",    "gusano",  "mapache"],
        ["alce",    "escorpion", "elefante",    "venado",      "oso"],
        ["araña", "rinoceronte",     "mula",      "rata", "avestruz"]
    ],
    [
        ["camello",      "Lobo",     "topo",    "Liebre",  "Pantera"],
        ["gallina",      "gato",    "perro", "tarantula",    "oveja"],
        ["Cerdo",      "iguana",   "bufalo",    "gusano",  "mapache"],
        ["alce",    "escorpion", "elefante",    "venado",      "oso"],
        ["araña", "rinoceronte",     "mula",      "rata", "avestruz"]
    ]
]

print("animal tierra9:", animales_tierra_tri3_5x5x5[0][0][0])
print("animal tierra10:", animales_tierra_tri3_5x5x5[0][1][1])
print("animal tierra11:", animales_tierra_tri3_5x5x5[0][2][2])
print("animal tierra12:", animales_tierra_tri3_5x5x5[0][3][3])
print("animal tierra13:", animales_tierra_tri3_5x5x5[0][4][4])

print("animal tierra14:", animales_tierra_tri3_5x5x5[0][0][0])
print("animal tierra15:", animales_tierra_tri3_5x5x5[0][1][1])
print("animal tierra16:", animales_tierra_tri3_5x5x5[0][2][2])
print("animal tierra17:", animales_tierra_tri3_5x5x5[0][3][3])
print("animal tierra18:", animales_tierra_tri3_5x5x5[0][4][4])

print("animal tierra19:", animales_tierra_tri3_5x5x5[0][0][0])
print("animal tierra20:", animales_tierra_tri3_5x5x5[0][1][1])
print("animal tierra21:", animales_tierra_tri3_5x5x5[0][2][2])
print("animal tierra22:", animales_tierra_tri3_5x5x5[0][3][3])
print("animal tierra23:", animales_tierra_tri3_5x5x5[0][4][4])

print("animal tierra24:", animales_tierra_tri3_5x5x5[0][0][0])
print("animal tierra25:", animales_tierra_tri3_5x5x5[0][1][1])
print("animal tierra26:", animales_tierra_tri3_5x5x5[0][2][2])
print("animal tierra27:", animales_tierra_tri3_5x5x5[0][3][3])
print("animal tierra28:", animales_tierra_tri3_5x5x5[0][4][4])

print("animal tierra29:", animales_tierra_tri3_5x5x5[0][0][0])
print("animal tierra30:", animales_tierra_tri3_5x5x5[0][1][1])
print("animal tierra31:", animales_tierra_tri3_5x5x5[0][2][2])
print("animal tierra32:", animales_tierra_tri3_5x5x5[0][3][3])
print("animal tierra33:", animales_tierra_tri3_5x5x5[0][4][4])

animales_agua_tri_4_5x5x5 = [
    [
        ["calamar",       "foca",    "delfin", "cachalote",      "ballena"],
        ["medusa",     "tiburon",   "sardina",    "trucha",        "pulpo"],
        ["arenques",    "carpas",  "langosta",      "atún",       "salmón"],
        ["almeja",       "coral", "rodaballo",   "piraña",       "marsopa"],
        ["tintorera", "pinguino",   "bacalao",      "orca", "erizo de mar"]
    ],
    [
        ["calamar",       "foca",    "delfin", "cachalote",      "ballena"],
        ["medusa",     "tiburon",   "sardina",    "trucha",        "pulpo"],
        ["arenques",    "carpas",  "langosta",      "atún",       "salmón"],
        ["almeja",       "coral", "rodaballo",   "piraña",       "marsopa"],
        ["tintorera", "pinguino",   "bacalao",      "orca", "erizo de mar"]
    ],
    [
        ["calamar",       "foca",    "delfin", "cachalote",      "ballena"],
        ["medusa",     "tiburon",   "sardina",    "trucha",        "pulpo"],
        ["arenques",    "carpas",  "langosta",      "atún",       "salmón"],
        ["almeja",       "coral", "rodaballo",   "piraña",       "marsopa"],
        ["tintorera", "pinguino",   "bacalao",      "orca", "erizo de mar"]
    ],
    [
        ["calamar",       "foca",    "delfin", "cachalote",      "ballena"],
        ["medusa",     "tiburon",   "sardina",    "trucha",        "pulpo"],
        ["arenques",    "carpas",  "langosta",      "atún",       "salmón"],
        ["almeja",       "coral", "rodaballo",   "piraña",       "marsopa"],
        ["tintorera", "pinguino",   "bacalao",      "orca", "erizo de mar"]
    ],
    [
        ["calamar",       "foca",    "delfin", "cachalote",      "ballena"],
        ["medusa",     "tiburon",   "sardina",    "trucha",        "pulpo"],
        ["arenques",    "carpas",  "langosta",      "atún",       "salmón"],
        ["almeja",       "coral", "rodaballo",   "piraña",       "marsopa"],
        ["tintorera", "pinguino",   "bacalao",      "orca", "erizo de mar"]
    ]
]

print("animal agua34:", animales_agua_tri_4_5x5x5[0][0][4])
print("animal agua35:", animales_agua_tri_4_5x5x5[0][1][3])
print("animal agua36:", animales_agua_tri_4_5x5x5[0][2][2])
print("animal agua37:", animales_agua_tri_4_5x5x5[0][3][1])
print("animal agua38:", animales_agua_tri_4_5x5x5[0][4][0])

print("animal agua39:", animales_agua_tri_4_5x5x5[0][0][4])
print("animal agua40:", animales_agua_tri_4_5x5x5[0][1][3])
print("animal agua41:", animales_agua_tri_4_5x5x5[0][2][2])
print("animal agua42:", animales_agua_tri_4_5x5x5[0][3][1])
print("animal agua43:", animales_agua_tri_4_5x5x5[0][4][0])

print("animal agua44:", animales_agua_tri_4_5x5x5[0][0][4])
print("animal agua45:", animales_agua_tri_4_5x5x5[0][1][3])
print("animal agua46:", animales_agua_tri_4_5x5x5[0][2][2])
print("animal agua47:", animales_agua_tri_4_5x5x5[0][3][1])
print("animal agua48:", animales_agua_tri_4_5x5x5[0][4][0])

print("animal agua49:", animales_agua_tri_4_5x5x5[0][0][4])
print("animal agua50:", animales_agua_tri_4_5x5x5[0][1][3])
print("animal agua51:", animales_agua_tri_4_5x5x5[0][2][2])
print("animal agua52:", animales_agua_tri_4_5x5x5[0][3][1])
print("animal agua53:", animales_agua_tri_4_5x5x5[0][4][0])

print("animal agua54:", animales_agua_tri_4_5x5x5[0][0][4])
print("animal agua55:", animales_agua_tri_4_5x5x5[0][1][3])
print("animal agua56:", animales_agua_tri_4_5x5x5[0][2][2])
print("animal agua57:", animales_agua_tri_4_5x5x5[0][3][1])
print("animal agua58:", animales_agua_tri_4_5x5x5[0][4][0])

profesion_tex_tri5_3x6x2 = [
    [
        ["electricista", "carpintero",       "plomero", "pintor",  "soldador",  "operador"],
        ["conductor",      "mecánico", "recepcionista", "mesero", "bartender",  "cocinero"],
        ["estilista",   "cosmetóloga",        "cajero", "asesor",  "contador", "enfermero"]
    ],
    [
        ["electricista", "carpintero",       "plomero", "pintor",  "soldador",  "operador"],
        ["conductor",      "mecánico", "recepcionista", "mesero", "bartender",  "cocinero"],
        ["estilista",   "cosmetóloga",        "cajero", "asesor",  "contador", "enfermero"]
    ]
]

print("profesion tex59:", profesion_tex_tri5_3x6x2[0][0][1])
print("profesion tex60:", profesion_tex_tri5_3x6x2[0][1][1])
print("profesion tex61:", profesion_tex_tri5_3x6x2[0][2][1])

print("profesion tex61:", profesion_tex_tri5_3x6x2[1][0][2])
print("profesion tex62:", profesion_tex_tri5_3x6x2[1][1][2])
print("profesion tex63:", profesion_tex_tri5_3x6x2[1][2][2])

flores_tex_tri6_3x6x2 = [
    [
        ["rosa",  "tulipanes", "girasoles", "orquidias", "margarita",    "azucena"],
        ["azalea",    "dalia", "hortensia",     "lirio",   "hibisco", "bugambilia"],
        ["verbena", "geranio",    "clavel",   "narciso",   "petunia",     "jazmín"]
    ],
    [
        ["rosa",  "tulipanes", "girasoles", "orquidias", "margarita",    "azucena"],
        ["azalea",    "dalia", "hortensia",     "lirio",   "hibisco", "bugambilia"],
        ["verbena", "geranio",    "clavel",   "narciso",   "petunia",     "jazmín"]
    ]
]

print("flores tex64:", flores_tex_tri6_3x6x2[0][0][3])
print("flores tex65:", flores_tex_tri6_3x6x2[0][1][3])
print("flores tex66:", flores_tex_tri6_3x6x2[0][2][3])

print("flores tex67:", flores_tex_tri6_3x6x2[1][0][4])
print("flores tex68:", flores_tex_tri6_3x6x2[1][1][4])
print("flores tex69:", flores_tex_tri6_3x6x2[1][2][4])

# Declare 2 variables tridimensionales 2x3x2, 5x5x1, 3x6x2 y asignar valores de enteros, flotantes y texto (6 variables
# en total)

tienda_2x3x2 = [
    [
        ["verde", "hierbita", "zanahoria"],
        [1,             0.25,        0.50]
    ],
    [
        ["tomate", "col", "veteraba"],
        [0.50,         2,       0.75]
    ]
]

print("prod:", tienda_2x3x2[0][0][1])
print("valor:", tienda_2x3x2[0][1][1])
print("prod:", tienda_2x3x2[1][0][0])
print("valor:", tienda_2x3x2[1][1][0])

tienda1_2x3x2 = [
    [
        ["verde", "hierbita", "zanahoria"],
        [1,             0.25,        0.50]
    ],
    [
        ["tomate", "col", "veteraba"],
        [0.50,         2,       0.75]
    ]
]

print("prod:", tienda1_2x3x2[0][0][2])
print("valor:", tienda1_2x3x2[0][1][2])
print("prod:", tienda1_2x3x2[1][0][2])
print("valor:", tienda1_2x3x2[1][1][2])

tienda2_5x5x1 = [
    [
        ["galletas", "nachos", "papitas", "oreo", "ricas"]
    ],
    [
        [1, 0.60, 1.20, 0.80, 0.50]
    ],
    [
        ["cola", "gatorade", "toni", "chocolate", "avena"]
    ],
    [
        [0.50, 1, 0.90, 1.10, 0.75]
    ],
    [
        ["usuario1", "usuario2", "usuario3", "usuario4", "usuario5"]
    ]
]

print("picar:", tienda2_5x5x1[0][0][3])
print("precio:", tienda2_5x5x1[1][0][3])
print("beber:", tienda2_5x5x1[2][0][0])
print("precio:", tienda2_5x5x1[3][0][0])
print("usuario:", tienda2_5x5x1[4][0][4])

tienda3_5x5x1 = [
    [
        ["galletas", "nachos", "papitas", "oreo", "ricas"]
    ],
    [
        [1, 0.60, 1.20, 0.80, 0.50]
    ],
    [
        ["cola", "gatorade", "toni", "chocolate", "avena"]
    ],
    [
        [0.50, 1, 0.90, 1.10, 0.75]
    ],
    [
        ["usuario1", "usuario2", "usuario3", "usuario4", "usuario5"]
    ]
]

print("picar:", tienda3_5x5x1[0][0][1])
print("precio:", tienda3_5x5x1[1][0][1])
print("beber:", tienda3_5x5x1[2][0][2])
print("precio:", tienda3_5x5x1[3][0][2])
print("usuario:", tienda3_5x5x1[4][0][1])

tienda4_3x6x2 = [
    [
        ["queso", "mantequilla", "cereal", "tostada", "pan", "colada"],
        [0.80,             1.60,        3,      0.70,  0.15,     0.75]
    ],
    [
        ["queso", "mantequilla", "cereal", "tostada", "pan", "colada"],
        [0.80,             1.60,        3,      0.70,  0.15,     0.75]
    ],
    [
        ["queso", "mantequilla", "cereal", "tostada", "pan", "colada"],
        [0.80,             1.60,        3,      0.70,  0.15,     0.75]
    ]
]
print("producto:", tienda4_3x6x2[0][0][0])
print("valor:", tienda4_3x6x2[0][1][0])
print("producto:", tienda4_3x6x2[1][0][1])
print("valor:", tienda4_3x6x2[1][1][1])
print("producto:", tienda4_3x6x2[2][0][2])
print("valor:", tienda4_3x6x2[2][1][2])

tienda5_3x6x2 = [
    [
        ["queso", "mantequilla", "cereal", "tostada", "pan", "colada"],
        [0.80,             1.60,        3,      0.70,  0.15,     0.75]
    ],
    [
        ["queso", "mantequilla", "cereal", "tostada", "pan", "colada"],
        [0.80,             1.60,        3,      0.70,  0.15,     0.75]
    ],
    [
        ["queso", "mantequilla", "cereal", "tostada", "pan", "colada"],
        [0.80,             1.60,        3,      0.70,  0.15,     0.75]
    ]
]
print("producto:", tienda5_3x6x2[0][0][3])
print("valor:", tienda5_3x6x2[0][1][3])
print("producto:", tienda5_3x6x2[1][0][4])
print("valor:", tienda5_3x6x2[1][1][4])
print("producto:", tienda5_3x6x2[2][0][5])
print("valor:", tienda5_3x6x2[2][1][5])
