# ---------- Import ----------
from korrelationsanalys import korrelationsfunction
from datahantering import datahantering

# ---------- Info ----------
print("------ Info ------")
print("Räknar ut Pearsons korrelationskoefficient med hjälp av beräkningsformeln.")
print("För att räkna Spearmans rangkorrelationskoefficient mata in rang")
print("istället för värden.")
print("\nTänk på att anväda punkt för decimaltal och inte kommatecken t.ex. (5.2 inte 5,2).")

# ---------- Läs in data ----------
x, y = datahantering()

# ---------- Korrelation ----------
korrelationsfunction(x, y)