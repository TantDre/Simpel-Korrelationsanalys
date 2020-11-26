# ---------- Import ----------
from datahantering import datahanteringK, datahanteringT
from korrelationsanalys import korrelationsfunction
from tTest import tTest


# ---------- Meny ----------
print("------------ Meny ------------")
print("Korrelationskoefficient: (1) \nOberoende t-test:\t\t (2)")
val = input()

if val == "1":
  # ---------- Info ----------
  print("\n------ Info ------")
  print("Räknar ut Pearsons korrelationskoefficient med hjälp av beräkningsformeln.")
  print("För att räkna Spearmans rangkorrelationskoefficient mata in rang")
  print("istället för värden.")
  print("\nTänk på att anväda punkt för decimaltal och inte kommatecken t.ex. (5.2 inte 5,2).")

  # ---------- Läs in data ----------
  x, y = datahanteringK()

  # ---------- Korrelation ----------
  korrelationsfunction(x, y)

elif val == "2":
  # ---------- Info ----------
  print("\n------ Info ------")
  print("Räknar ut t-värde och frihetsgrad med oberoende t-test.")
  print("För att testa μ1 = μ2 sätt båda till 0.")
  print("\nTänk på att anväda punkt för decimaltal och inte kommatecken t.ex. (5.2 inte 5,2).")

  # ---------- Läs in data ----------
  x1_bar, x2_bar, mu1, mu2, n1, n2, s1, s2 = datahanteringT()

  # ---------- Korrelation ----------
  tTest(x1_bar, x2_bar, mu1, mu2, n1, n2, s1, s2)