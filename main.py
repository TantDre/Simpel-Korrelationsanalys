# ---------- Import ----------
from Funktioner.meny import menyB

# ---------- Meny ----------
print("------------ Meny ------------")
print("Korrelationskoefficient: (1) \nz-test:\t\t\t\t\t (2) \nt-test:\t\t\t\t\t (3) \nOberoende t-test:\t\t (4) \nBeroende t-test:\t\t (5) \nEffektstyrka:\t\t\t (6)")

# Input
val = input()

# Beräkning och output
menyB(val)