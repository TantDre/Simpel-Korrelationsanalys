# ---------- Import ----------
import numpy as np

# ---------- Korrelationsfunction ----------
def tTest(x1_bar, x2_bar, mu1, mu2, n1, n2, s1, s2):

  print("\n------ Oberoende t-test ------")
  # DoF
  df = n1 + n2 - 2
  print("df = " + str(df))

  # T-värde
  tdf = ((x1_bar - x2_bar) - (mu1 - mu2)) / np.sqrt((((n1-1)*s1**2+(n2-1)*s2**2)/(df))*((1/n1)+(1/n2)))
  print("tdf = " + str(tdf))