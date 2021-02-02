#%%
from typing import List
from numpy.lib.function_base import iterable
import uproot
import numpy as np
import pandas as pd
import awkward as ak
import matplotlib.pyplot as plt

fn = "~/CMSSW_11_1_6/src/ntupleTree.root"
rf = uproot.open(fn)
#%%
for key in rf["/treeMaker;1/tree;1"].keys():
    print(key)
    a = rf["/treeMaker;1/tree;1/" + key].array()
    print(a)
    print(ak.type(a))
    print()

# %%
def ga(vars: List[str], eventNumber: int = 0, library: str = "np") -> np.ndarray:
    valvars = rf["/treeMaker;1/tree;1"]
    outpd = pd.DataFrame({var: valvars[var].array(library=library)[eventNumber] for var in vars })

    return outpd 
#%%
arr=ga(['recHit_y','recHit_x','recHit_z','recHit_layer'])
#%%
fig1, axes = plt.subplots(ncols=1, nrows=10)
stretch=5
fig1.set_size_inches(1*stretch, 10*stretch)

for layer,ax in enumerate(axes):
    sel=arr[arr['recHit_layer']==layer]
    ax.scatter(arr['recHit_x'],arr['recHit_y'])
    ax.set_title(f'Layer {layer}')
fig1.tight_layout()
fig1.show()

# %%

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.scatter(xs=arr["recHit_y"], ys=arr["recHit_z"], zs=arr["recHit_x"])
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")
# %%
