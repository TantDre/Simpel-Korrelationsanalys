# ---------- Import ----------
from datahantering import dataZ, dataK, dataT, dataOT
from korrelationsanalys import korrelationsfunction
from tTest import zTest, tTest, OtTest


# ---------- Meny ----------
print("------------ Meny ------------")
print("Korrelationskoefficient: (1) \nz-test:\t\t\t\t\t (2) \nt-test:\t\t\t\t\t (3) \nOberoende t-test:\t\t (4)")
val = input()

try:
  if val == "1":
    # ---------- Info ----------
    print("\n------ Info ------")
    print("Räknar ut Pearsons korrelationskoefficient med hjälp av beräkningsformeln.")
    print("För att räkna Spearmans rangkorrelationskoefficient mata in rang")
    print("istället för värden.")
    print("\nTänk på att anväda punkt för decimaltal och inte kommatecken t.ex. (5.2 inte 5,2).")

    # ---------- Läs in data ----------
    x, y = dataK()

    # ---------- Korrelation ----------
    korrelationsfunction(x, y)

  elif val == "2":
    # ---------- Info ----------
    print("\n------ Info ------")
    print("Räknar ut z-värde  med z-test.")
    print("\nTänk på att anväda punkt för decimaltal och inte kommatecken t.ex. (5.2 inte 5,2).")

    # ---------- Läs in data ----------
    x_bar, mu, n, s = dataZ()

    # ---------- z-test ----------
    zTest(x_bar, mu, n, s)

  elif val == "3":
    # ---------- Info ----------
    print("\n------ Info ------")
    print("Räknar ut t-värde och frihetsgrad med t-test.")
    print("\nTänk på att anväda punkt för decimaltal och inte kommatecken t.ex. (5.2 inte 5,2).")

    # ---------- Läs in data ----------
    x_bar, mu, n, s = dataT()

    # ---------- t-test ----------
    tTest(x_bar, mu, n, s)

  elif val == "4":
    # ---------- Info ----------
    print("\n------ Info ------")
    print("Räknar ut t-värde och frihetsgrad med oberoende t-test.")
    print("För att testa μ1 = μ2 sätt båda till 0.")
    print("\nTänk på att anväda punkt för decimaltal och inte kommatecken t.ex. (5.2 inte 5,2).")

    # ---------- Läs in data ----------
    x1_bar, x2_bar, mu1, mu2, n1, n2, s1, s2 = dataOT()

    # ---------- Oberoende t-test ----------
    OtTest(x1_bar, x2_bar, mu1, mu2, n1, n2, s1, s2)

  else:
    print("\nNågot gick fel vänligen tryck på 'Run' och starta om!")

except:
  print("\nNågot gick fel vänligen tryck på 'Run' och starta om!")