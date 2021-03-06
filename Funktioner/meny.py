# ---------- Import ----------
from Funktioner.datahantering import dataZ, dataK, dataT, dataOT, dataBT, dataD
from Funktioner.korrelationsanalys import korrelationsfunktion
from Funktioner.tTest import zTest, tTest, OtTest, BtTest, CohensD
from Funktioner.chi2 import chi2
import sys, os

# ---------- Meny funktion ----------
def menyB(val):

  # Töm konsolen
  try:
    os.system('clear')
  except:
    print(" \n ")		

  try:
    if val == "1":
      # ---------- Info ----------
      print("------ Korrelationskoefficient ------")
      print("Räknar ut Pearsons korrelationskoefficient med hjälp av beräkningsformeln.")
      print("För att räkna Spearmans rangkorrelationskoefficient mata in rang")
      print("istället för värden.")
      print("\nTänk på att anväda punkt för decimaltal och inte kommatecken t.ex. (5.2 inte 5,2).")

      # ---------- Läs in data ----------
      x, y = dataK()

      # ---------- Korrelation ----------
      korrelationsfunktion(x, y)

    elif val == "2":
      # ---------- Info ----------
      print("------ z-test ------")
      print("Räknar ut z-värde  med z-test.")
      print("\nTänk på att anväda punkt för decimaltal och inte kommatecken t.ex. (5.2 inte 5,2).")

      # ---------- Läs in data ----------
      x_bar, mu, n, s = dataZ()

      # ---------- z-test ----------
      zTest(x_bar, mu, n, s)

    elif val == "3":
      # ---------- Info ----------
      print("------ t-test ------")
      print("Räknar ut t-värde och frihetsgrad med t-test.")
      print("\nTänk på att anväda punkt för decimaltal och inte kommatecken t.ex. (5.2 inte 5,2).")

      # ---------- Läs in data ----------
      x_bar, mu, n, s = dataT()

      # ---------- t-test ----------
      tTest(x_bar, mu, n, s)

    elif val == "4":
      # ---------- Info ----------
      print("------ Oberoende t-test ------")
      print("Räknar ut t-värde och frihetsgrad med oberoende t-test.")
      print("För att testa μ1 = μ2 sätt båda till 0.")
      print("\nTänk på att anväda punkt för decimaltal och inte kommatecken t.ex. (5.2 inte 5,2).")

      # ---------- Läs in data ----------
      x1_bar, x2_bar, mu1, mu2, n1, n2, s1, s2 = dataOT()

      # ---------- Oberoende t-test ----------
      OtTest(x1_bar, x2_bar, mu1, mu2, n1, n2, s1, s2)

    elif val == "5":
      # ---------- Info ----------
      print("------ Beroende (parat) t-test ------")
      print("Räknar ut t-värde och frihetsgrad med beroende t-test.")
      print("\nTänk på att anväda punkt för decimaltal och inte kommatecken t.ex. (5.2 inte 5,2).")

      # ---------- Läs in data ----------
      d_bar, muD, n, sd = dataBT()

      # ---------- Beroende t-test ----------
      BtTest(d_bar, muD, n, sd)

    elif val == "6":
      # ---------- Info ----------
      print("------ Effektstyrka ------")
      print("Räknar ut effektstyrka med beroende Cohens d.")
      print("\nTänk på att anväda punkt för decimaltal och inte kommatecken t.ex. (5.2 inte 5,2).")

      # ---------- Läs in data ----------
      x1_bar, x2_bar, sd = dataD()

      # ---------- Cohens d ----------
      CohensD(x1_bar, x2_bar, sd)
    
    elif val == "7":
      # ---------- Info ----------
      print("------ Chi-två ------")
      print("Räknar ut chi-två och frihetsgrad för flera variabler.")
      print("\nTänk på att anväda punkt för decimaltal och inte kommatecken t.ex. (5.2 inte 5,2).")

      # ---------- Chi2 ----------
      chi2()

    else:
      # Töm konsolen
      os.system('clear')

      # Error
      print("Något gick fel, vänligen tryck på 'Run' och starta om!")

  except:
    # Töm konsolen
  #  os.system('clear')

    # Error
    print("Något gick fel, vänligen tryck på 'Run' och starta om!")
