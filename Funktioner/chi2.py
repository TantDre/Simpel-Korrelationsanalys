# ---------- Import ----------
import numpy as np

# ---------- Chi-2 ----------
def chi2(o_vec, e_vec):
  # Gör om till np matris
  o_vec = np.array(o_vec)
  e_vec = np.array(e_vec)

  print("\n------ Chi-två ------")
  # Antal värden
  k = len(o_vec)

  # DoF
  df = k - 1
  print("df = " + str(df))

  # Chi2
  chi = 0
  for i in range(0, k-1, 1):
    o = o_vec[i]
    e = e_vec[i]
    chi += ((o-e)**2)/e

  print("Chi2df = " + str(chi))