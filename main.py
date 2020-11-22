# ---------- Import ----------
from korrelationsanalys import korrelationsfunction
from datahantering import datahantering

# ---------- Läs in data ----------
# Tänk på att anväda punkt för decimaltal t.ex. (5.2 inte 5,2)
x, y = datahantering()

# ---------- Korrelation ----------
korrelationsfunction(x, y)