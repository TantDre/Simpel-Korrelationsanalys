# ---------- Läs in data ----------
def datahantering():

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