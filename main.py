# ---------- Import ----------
from Funktioner.meny import menyB

# ---------- Meny ----------
print("------------- Meny -------------")
print("Korrelationskoefficient:\t (1) \nz-test:\t\t\t\t\t\t (2) \nt-test:\t\t\t\t\t\t (3) \nOberoende t-test:\t\t\t (4) \nBeroende t-test:\t\t\t (5) \nEffektstyrka:\t\t\t\t (6) \nChi-två:\t\t\t\t\t (7)")

# Input
val = input()

# Beräkning och output
menyB(val)