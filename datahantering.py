# ---------- Läs in data för K ----------
def dataK():
  print("\n------ Data ------")
  # Antal element
  n = int(input("Antal värden (n):")) 

  # x värden
  print("\nAnge alla x värden:")
  x = []
  for i in range(0, n): 
      element = float(input()) 
      x.append(element) 

  # y värden
  y = []
  print("\nAnge alla y värden:")
  for i in range(0, n): 
      element = float(input())
      y.append(element)       

  return(x, y)

# ---------- Läs in data för T ----------
def dataT():
  print("\n------ Data ------")
  print("Stickprovsmedelvärde x: ")
  x_bar = float(input())

  print("\nPopulationsmedelvärde μ: ")
  mu = float(input())

  print("\nAntal värden n: ")
  n = float(input())

  print("\nStandardavvikelse s: ")
  s = float(input())


  return(x_bar, mu, n, s)
  
# ---------- Läs in data för OT ----------
def dataOT():
  print("\n------ Data ------")
  print("Stickprovsmedelvärde x1: ")
  x1_bar = float(input())

  print("\nPopulationsmedelvärde μ1: ")
  mu1 = float(input())

  print("\nAntal värden n1: ")
  n1 = float(input())

  print("\nStandardavvikelse s1: ")
  s1 = float(input())

  print("\nStickprovsmedelvärde x2: ")
  x2_bar = float(input())

  print("\nPopulationsmedelvärde μ2: ")
  mu2 = float(input())

  print("\nAntal värden n2: ")
  n2 = float(input())

  print("\nStandardavvikelse s2: ")
  s2 = float(input())

  return(x1_bar, x2_bar, mu1, mu2, n1, n2, s1, s2)