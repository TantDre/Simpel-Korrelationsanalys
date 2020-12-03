# ---------- Import ----------
import numpy as np

# ---------- Läs in data för Chi-2 ----------
def dataChi():
  print("\n------ Data ------")
  # Antal element
  r = int(input("Antal rader r: ")) 
  k = int(input("Antal kolumner k: ")) 

  # np matriser
  o_vec = np.zeros((r, k))

  print("\n------ Observerade värden ------")
  for i in range(0, k):
    # o värden
    print("Ange observerade värden (o) i kolunm " + str(i+1) + ": ")

    for j in range(0, r): 
        element = float(input()) 
        o_vec[j, i] = element 

  return(o_vec)

# ---------- Räknar ut förväntat värde ----------
def expectedValue(o_vec):
  # Antal värden
  r = o_vec.shape[0]
  k = o_vec.shape[1]

  # np matriser
  e_vec = np.zeros((r, k))

  # Summor
  row_sum = o_vec.sum(axis=1)
  col_sum = o_vec.sum(axis=0)
  tot_col_sum = col_sum.sum()

  # Förväntat värde
  print("\n------ Förväntade värden ------")
  for j in range(0, k):
    print("Förväntade värden (e) i kolunm " + str(j+1) + ": ")

    for i in range(0, r): 
      e_vec[i, j] = (row_sum[i] * col_sum[j]) / tot_col_sum
      print(e_vec[i, j])

  return(e_vec)

# ---------- Chi-2 ----------
def chi2():
  # Läs in data
  o_vec = dataChi()

  # Räkna ut e
  e_vec = expectedValue(o_vec)

  print("\n------ Chi-två ------")
  # Antal värden
  r = o_vec.shape[0]
  k = o_vec.shape[1]

  # DoF
  if (k == 1):
    df = r - 1
  elif (r == 1):
    df = k - 1
  else:
    df = (k - 1)*(r - 1)

  print("df = " + str(df))

  # Chi2
  diff = np.subtract(o_vec, e_vec)
  power_diff = np.power(diff, 2)
  chi = sum(sum(np.divide(power_diff, e_vec)))
  
  print("Chi2df = " + str(chi))