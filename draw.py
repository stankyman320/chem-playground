import sys
from rdkit import Chem
from rdkit.Chem import Descriptors, Draw, rdDepictor

rdDepictor.SetPreferCoordGen(True)

smiles, name = sys.argv[1], sys.argv[2]
m = Chem.MolFromSmiles(smiles)
if m is None:
    sys.exit("Invalid SMILES")

print(f"{name}: MW {Descriptors.MolWt(m):.1f}, TPSA {Descriptors.TPSA(m):.1f}, logP {Descriptors.MolLogP(m):.2f}")
Draw.MolToFile(m, f"{name}.png", size=(500, 500))
