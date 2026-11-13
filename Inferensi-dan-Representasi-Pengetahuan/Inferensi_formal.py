# formal_inference.py

from sympy import symbols
from sympy.logic.boolalg import Implies, And
from sympy.logic.inference import satisfiable

# Membuat simbol proposisi
hujan, basah = symbols("hujan basah")

# Aturan: Jika hujan, maka jalan basah
aturan = Implies(hujan, basah)

# Fakta: Hujan benar
fakta = And(aturan, hujan)

model = satisfiable(fakta & ~basah)

print("Apakah mungkin hujan tapi tidak basah?", model)

if not model:
    print("Kesimpulan: jalan PASTI basah.")
