# ---------- Import ----------
import numpy as np

# ---------- Korrelationsfunction ----------
def korrelationsfunction(x, y):
  # Gör om till np matris
  x = np.array(x)
  y = np.array(y)
  assert(len(x)==len(y))

  print("\nStatistik:")
  # Antal värden
  n = len(x)
  print("n = " + str(n))

  # Medelvärden
  x_bar = np.mean(x)
  print("μx = " + str(x_bar))

  y_bar = np.mean(y)
  print("μy = " + str(y_bar))

  # Standardavikelser
  x_std = np.std(x)
  print("σx = " + str(x_std))

  y_std = np.std(y)
  print("σy = " + str(y_std) + "\n")

  # Summor
  x_sum = sum(x)
  print("Σ(x) = " + str(x_sum))

  y_sum = sum(y)
  print("Σ(y) = " + str(y_sum))

  xy_sum = x.dot(y)
  print("Σ(xy) = " + str(xy_sum))

  x2_sum = x.dot(x.T)
  print("Σ(x^2) = " + str(x2_sum))

  y2_sum = y.dot(y.T)
  print("Σ(y^2) = " + str(xy_sum) + "\n")

  # Korrelation
  r = (n * xy_sum - x_sum * y_sum) / np.sqrt((n * x2_sum - x_sum**2)*(n * y2_sum - y_sum**2))
  print("r = " + str(r))

  return