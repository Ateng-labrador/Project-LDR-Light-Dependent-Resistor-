import pandas as pd

def conver_cvs(a, b):
    """
    a = nama file cvs
    b = nama variabel
    """
    with open(a, "w") as file_csv:
        file_csv.write(b)

def add_time(b, jalur, filename):
    """
    b = data series (panjang data)
    jalur = dataframe
    filename = nama file untuk disimpan
    """
    time = []
    for i in range(1, len(b) + 1):
        time.append(str(i))
    time_list = time
    jalur['waktu'] = time_list
    jalur.to_csv(filename, index=False)


# Putaran Pertama

data_1_00_naik = """"""
data_1_20_naik = """"""
data_1_40_naik = """"""
data_1_60_naik = """"""
data_1_80_naik = """"""
data_1_100_naik = """"""
data_1_120_naik = """"""
data_1_140_naik = """"""
data_1_160_naik = """"""
data_1_180_naik = """"""
data_1_200_naik = """"""
data_1_220_naik = """"""

data_1_00_turun = """"""
data_1_20_turun = """"""
data_1_40_turun = """"""
data_1_60_turun = """"""
data_1_80_turun = """"""
data_1_100_turun = """"""
data_1_120_turun = """"""
data_1_140_turun = """"""
data_1_160_turun = """"""
data_1_180_turun = """"""
data_1_200_turun = """"""
data_1_220_turun = """"""

# putaran kedua


data_2_00_naik = """"""
data_2_20_naik = """"""
data_2_40_naik = """"""
data_2_60_naik = """"""
data_2_80_naik = """"""
data_2_100_naik = """"""
data_2_120_naik = """"""
data_2_140_naik = """"""
data_2_160_naik = """"""
data_2_180_naik = """"""
data_2_200_naik = """"""
data_2_220_naik = """"""

data_2_00_turun = """"""
data_2_20_turun = """"""
data_2_40_turun = """"""
data_2_60_turun = """"""
data_2_80_turun = """"""
data_2_100_turun = """"""
data_2_120_turun = """"""
data_2_140_turun = """"""
data_2_160_turun = """"""
data_2_180_naik = """"""
data_2_200_turun = """"""
data_2_220_turun = """"""

# putaran ketiga


data_3_00_naik = """"""
data_3_20_naik = """"""
data_3_40_naik = """"""
data_3_60_naik = """"""
data_3_80_naik = """"""
data_3_100_naik = """"""
data_3_120_naik = """"""
data_3_140_naik = """"""
data_3_160_naik = """"""
data_3_180_naik = """"""
data_3_200_naik = """"""
data_3_220_naik = """"""

data_3_00_turun = """"""
data_3_20_turun = """"""
data_3_40_turun = """"""
data_3_60_turun = """"""
data_3_80_turun = """"""
data_3_100_turun = """"""
data_3_120_turun = """"""
data_3_140_turun = """"""
data_3_180_naik = """"""
data_3_160_turun = """"""
data_3_200_turun = """"""
data_3_220_turun = """"""


# putaran pertama 

a1 = "data_1_00_naik.csv"
a2 = "data_1_20_naik.csv"
a3 = "data_1_40_naik.csv"
a4 = "data_1_60_naik.csv"
a5 = "data_1_80_naik.csv"
a6 = "data_1_100_naik.csv"
a7 = "data_1_120_naik.csv"
a8 = "data_1_140_naik.csv"
a9 = "data_1_160_naik.csv"
a10 = "data_1_180_naik.csv"
a11 = "data_1_200_naik.csv"
a12 = "data_1_220_naik.csv"


b1 = "data_1_00_turun.csv"
b2 = "data_1_20_turun.csv"
b3 = "data_1_40_turun.csv"
b4 = "data_1_60_turun.csv"
b5 = "data_1_80_turun.csv"
b6 = "data_1_100_turun.csv"
b7 = "data_1_120_turun.csv"
b8 = "data_1_140_turun.csv"
b9 = "data_1_160_turun.csv"
b10 = "data_1_180_turun.csv"
b11 = "data_1_200_turun.csv"
b12 = "data_1_220_turun.csv"

# putaran kedua


c1 = "data_2_00_naik.csv"
c2 = "data_2_20_naik.csv"
c3 = "data_2_40_naik.csv"
c4 = "data_2_60_naik.csv"
c5 = "data_2_80_naik.csv"
c6 = "data_2_100_naik.csv"
c7 = "data_2_120_naik.csv"
c8 = "data_2_140_naik.csv"
c9 = "data_2_160_naik.csv"
c10 = "data_2_180_naik.csv"
c11 = "data_2_200_naik.csv"
c12 = "data_2_220_naik.csv"


d1 = "data_2_00_turun.csv"
d2 = "data_2_20_turun.csv"
d3 = "data_2_40_turun.csv"
d4 = "data_2_60_turun.csv"
d5 = "data_2_80_turun.csv"
d6 = "data_2_100_turun.csv"
d7 = "data_2_120_turun.csv"
d8 = "data_2_140_turun.csv"
d9 = "data_2_160_turun.csv"
d10 = "data_2_180_turun.csv"
d11 = "data_2_200_turun.csv"
d12 = "data_2_220_turun.csv"

# putaran ketiga

e1 = "data_3_00_naik.csv"
e2 = "data_3_20_naik.csv"
e3 = "data_3_40_naik.csv"
e4 = "data_3_60_naik.csv"
e5 = "data_3_80_naik.csv"
e6 = "data_3_100_naik.csv"
e7 = "data_3_120_naik.csv"
e8 = "data_3_140_naik.csv"
e9 = "data_3_160_naik.csv"
e10 = "data_3_180_naik.csv"
e11 = "data_3_200_naik.csv"
e12 = "data_3_220_naik.csv"


f1 = "data_3_00_turun.csv"
f2 = "data_3_20_turun.csv"
f3 = "data_3_40_turun.csv"
f4 = "data_3_60_turun.csv"
f5 = "data_3_80_turun.csv"
f6 = "data_3_100_turun.csv"
f7 = "data_3_120_turun.csv"
f8 = "data_3_140_turun.csv"
f9 = "data_3_160_turun.csv"
f10 = "data_3_180_turun.csv"
f11 = "data_3_200_turun.csv"
f12 = "data_3_220_turun.csv"


# putaran pertama
conver_cvs(a = a1, b = data_1_00_naik)
dt0000up = pd.read_csv(a1)
x = dt0000up['ldr']
add_time(x, dt0000up, a1)

conver_cvs(a = a2, b = data_1_20_naik)
dt0020up = pd.read_csv(a2)
x = dt0020up['ldr']
add_time(x, dt0020up, a2)

conver_cvs(a = a3, b = data_1_40_naik)
dt0040up = pd.read_csv(a3)
x = dt0040up['ldr']
add_time(x, dt0040up, a3)

conver_cvs(a = a4, b = data_1_60_naik)
dt0060up = pd.read_csv(a4)
x = dt0060up['ldr']
add_time(x, dt0060up, a4)

conver_cvs(a = a5, b = data_1_80_naik)
dt0080up = pd.read_csv(a5)
x = dt0080up['ldr']
add_time(x, dt0080up, a5)

conver_cvs(a = a6, b = data_1_100_naik)
dt00100up = pd.read_csv(a6)
x = dt00100up['ldr']
add_time(x, dt00100up, a6)

conver_cvs(a = a7, b = data_1_120_naik)
dt00120up = pd.read_csv(a7)
x = dt00120up['ldr']
add_time(x, dt00120up, a7)

conver_cvs(a = a8, b = data_1_140_naik)
dt00140up = pd.read_csv(a8)
x = dt00140up['ldr']
add_time(x, dt00140up, a8)

conver_cvs(a = a9, b = data_1_160_naik)
dt00160up = pd.read_csv(a9)
x = dt00160up['ldr']
add_time(x, dt00160up, a9)

conver_cvs(a = a10, b = data_1_180_naik)
dt00180up = pd.read_csv(a10)
x = dt00180up['ldr']
add_time(x, dt00160up, a10)


conver_cvs(a = a11, b = data_1_200_naik)
dt00200up = pd.read_csv(a11)
x = dt00200up['ldr']
add_time(x, dt00200up, a11)

conver_cvs(a = a12, b = data_1_220_naik)
dt00220up = pd.read_csv(a12)
x = dt00220up['ldr']
add_time(x, dt00220up, a12)



conver_cvs(a = b3, b = data_1_12_turun)
dt112dw = pd.read_csv(b3)
x = dt112dw['ldr']
add_time(x, dt112dw, b3)

conver_cvs(a = b4, b = data_1_15_turun)
dt115dw = pd.read_csv(b4)
x = dt115dw['ldr']
add_time(x, dt115dw, b4)

conver_cvs(a = b5, b = data_1_18_turun)
dt118dw = pd.read_csv(b5)
x = dt118dw['ldr']
add_time(x, dt118dw, b5)

conver_cvs(a = b6, b = data_1_21_turun)
dt121dw = pd.read_csv(b6)
x = dt121dw['ldr']
add_time(x, dt121dw, b6)

conver_cvs(a = b7, b = data_1_24_turun)
dt124dw = pd.read_csv(b7)
x = dt124dw['ldr']
add_time(x, dt124dw, b7)

conver_cvs(a = b8, b = data_1_27_turun)
dt127dw = pd.read_csv(b8)
x = dt127dw['ldr']
add_time(x, dt127dw, b8)

# conver_cvs(a = b9, b = data_1_30_turun)
# dt130dw = pd.read_csv(b9)
# x = dt130dw['jarak']
# add_time(x, dt130dw)

# putaran kedua

conver_cvs(a = c1, b = data_2_6_naik)
dt216up = pd.read_csv(c1)
x = dt216up['jarak']
add_time(x, dt216up, c1)

conver_cvs(a = c2, b = data_2_9_naik)
dt219up = pd.read_csv(c2)
x = dt219up['jarak']
add_time(x, dt219up, c2)

conver_cvs(a = c3, b = data_2_12_naik)
dt212up = pd.read_csv(c3)
x = dt212up['jarak']
add_time(x, dt212up, c3)

conver_cvs(a = c4, b = data_2_15_naik)
dt215up = pd.read_csv(c4)
x = dt215up['jarak']
add_time(x, dt215up, c4)

conver_cvs(a = c5, b = data_2_18_naik)
dt218up = pd.read_csv(c5)
x = dt218up['jarak']
add_time(x, dt218up, c5)

conver_cvs(a = c6, b = data_2_21_naik)
dt221up = pd.read_csv(c6)
x = dt221up['jarak']
add_time(x, dt221up, c6)

conver_cvs(a = c7, b = data_2_24_naik)
dt224up = pd.read_csv(c7)
x = dt224up['jarak']
add_time(x, dt224up, c7)

conver_cvs(a = c8, b = data_2_27_naik)
dt227up = pd.read_csv(c8)
x = dt227up['jarak']
add_time(x, dt227up, c8)

conver_cvs(a = c9, b = data_2_30_naik)
dt230up = pd.read_csv(c9)
x = dt230up['jarak']
add_time(x, dt230up, c9)


conver_cvs(a = d1, b = data_2_6_turun)
dt36dw = pd.read_csv(d1)
x = dt36dw['jarak']
add_time(x, dt36dw, d1)

conver_cvs(a = d2, b = data_2_9_turun)
dt39dw = pd.read_csv(d2)
x = dt39dw['jarak']
add_time(x, dt39dw, d2)

conver_cvs(a = d3, b = data_2_12_turun)
dt312dw = pd.read_csv(d3)
x = dt312dw['jarak']
add_time(x, dt312dw, d3)

conver_cvs(a = d4, b = data_2_15_turun)
dt315dw = pd.read_csv(d4)
x = dt315dw['jarak']
add_time(x, dt315dw, d4)

conver_cvs(a = d5, b = data_2_18_turun)
dt318dw = pd.read_csv(d5)
x = dt318dw['jarak']
add_time(x, dt318dw, d5)

conver_cvs(a = d6, b = data_2_21_turun)
dt321dw = pd.read_csv(d6)
x = dt321dw['jarak']
add_time(x, dt321dw, d6)

conver_cvs(a = d7, b = data_2_24_turun)
dt324dw = pd.read_csv(d7)
x = dt324dw['jarak']
add_time(x, dt324dw, d7)

conver_cvs(a = d8, b = data_2_27_turun)
dt327dw = pd.read_csv(d8)
x = dt327dw['jarak']
add_time(x, dt327dw, d8)

conver_cvs(a = d9, b = data_2_30_turun)
dt330dw = pd.read_csv(d9)
x = dt330dw['jarak']
add_time(x, dt330dw, d9)


# putaran ketiga

conver_cvs(a = f1, b = data_3_6_naik)
dt16up = pd.read_csv(f1)
x = dt16up['jarak']
add_time(x, dt16up, f1)

conver_cvs(a = f2, b = data_3_9_naik)
dt19up = pd.read_csv(f2)
x = dt19up['jarak']
add_time(x, dt19up, f2)

conver_cvs(a = f3, b = data_3_12_naik)
dt112up = pd.read_csv(f3)
x = dt112up['jarak']
add_time(x, dt112up, f3)

conver_cvs(a = f4, b = data_3_15_naik)
dt115up = pd.read_csv(f4)
x = dt115up['jarak']
add_time(x, dt115up, f4)

conver_cvs(a = f5, b = data_3_18_naik)
dt118up = pd.read_csv(f5)
x = dt118up['jarak']
add_time(x, dt118up, f5)

conver_cvs(a = f6, b = data_3_21_naik)
dt121up = pd.read_csv(f6)
x = dt121up['jarak']
add_time(x, dt121up, f6)

conver_cvs(a = f7, b = data_3_24_naik)
dt124up = pd.read_csv(f7)
x = dt124up['jarak']
add_time(x, dt124up, f7)

conver_cvs(a = f8, b = data_3_27_naik)
dt127up = pd.read_csv(f8)
x = dt127up['jarak']
add_time(x, dt127up, f8)

conver_cvs(a = f9, b = data_3_30_naik)
dt130up = pd.read_csv(f9)
x = dt130up['jarak']
add_time(x, dt130up, f9)


conver_cvs(a = g1, b = data_3_6_turun)
dt16dw = pd.read_csv(g1)
x = dt16dw['jarak']
add_time(x, dt16dw, g1)

conver_cvs(a = g2, b = data_3_9_turun)
dt19dw = pd.read_csv(g2)
x = dt19dw['jarak']
add_time(x, dt19dw, g2)

conver_cvs(a = g3, b = data_3_12_turun)
dt112dw = pd.read_csv(g3)
x = dt112dw['jarak']
add_time(x, dt112dw, g3)

conver_cvs(a = g4, b = data_3_15_turun)
dt115dw = pd.read_csv(g4)
x = dt115dw['jarak']
add_time(x, dt115dw, g4)

conver_cvs(a = g5, b = data_3_18_turun)
dt118dw = pd.read_csv(g5)
x = dt118dw['jarak']
add_time(x, dt118dw, g5)

conver_cvs(a = g6, b = data_3_21_turun)
dt121dw = pd.read_csv(g6)
x = dt121dw['jarak']
add_time(x, dt121dw, g6)

conver_cvs(a = g7, b = data_3_24_turun)
dt124dw = pd.read_csv(g7)
x = dt124dw['jarak']
add_time(x, dt124dw, g7)

conver_cvs(a = g8, b = data_3_27_turun)
dt127dw = pd.read_csv(g8)
x = dt127dw['jarak']
add_time(x, dt127dw, g8)

conver_cvs(a = g9, b = data_3_30_turun)
dt130dw = pd.read_csv(g9)
x = dt130dw['jarak']
add_time(x, dt130dw, g9)
