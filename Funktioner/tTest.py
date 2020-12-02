# ---------- Import ----------
import numpy as np

# ---------- z-test ----------
def zTest(x_bar, mu, n, s):

  print("\n------ z-test ------")
  # z-värde
  z = (x_bar - mu) / (s / np.sqrt(n))
  print("z = " + str(z))

# ---------- t-test ----------
def tTest(x_bar, mu, n, s):

  print("\n------ t-test ------")
  # DoF
  df = n - 1
  print("df = " + str(df))

  # T-värde
  tdf = (x_bar - mu) / (s / np.sqrt(n))
  print("tdf = " + str(tdf))

  # Konfidensintervall
  upper = x_bar + tdf * s
  lower = x_bar - tdf * s

  print("\n------ Konfidensintervall ------")
  print(str(lower) + " ≤ μ ≤ " + str(upper))

# ---------- Oberoende t-test ----------
def OtTest(x1_bar, x2_bar, mu1, mu2, n1, n2, s1, s2):

  print("\n------ Oberoende t-test ------")
  # DoF
  df = n1 + n2 - 2
  print("df = " + str(df))

  # T-värde
  tdf = ((x1_bar - x2_bar) - (mu1 - mu2)) / np.sqrt((((n1-1)*s1**2+(n2-1)*s2**2)/(df))*((1/n1)+(1/n2)))
  print("tdf = " + str(tdf))

  # Konfidensintervall
  upper1 = x1_bar + tdf * s1
  lower1 = x1_bar - tdf * s1
  upper2 = x2_bar + tdf * s2
  lower2 = x2_bar - tdf * s2

  print("\n------ Konfidensintervall ------")
  print(str(lower1) + " ≤ μ1 ≤ " + str(upper1))
  print(str(lower2) + " ≤ μ2 ≤ " + str(upper2))

# ---------- Beroende t-test ----------
def BtTest(d_bar, muD, n, sd):

  print("\n------ Beroende t-test ------")
  # DoF
  df = n - 1
  print("df = " + str(df))

  # T-värde
  tdf = (d_bar - muD) / (sd / np.sqrt(n))
  print("tdf = " + str(tdf))

  # Konfidensintervall
  upper = d_bar + tdf * sd
  lower = d_bar - tdf * sd

  print("\n------ Konfidensintervall ------")
  print(str(lower) + " ≤ μD ≤ " + str(upper)) 

# ---------- Cohens d ----------
def CohensD(x1_bar, x2_bar, sd):

  print("\n------ Effektstyrka ------")
  # Effektstyrka
  d = (x1_bar - x2_bar) / sd
  print("d = " + str(d))