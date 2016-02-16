
import nas.units
import units

nas.units.define_units()

class Materials(object):
    def __init__(self):
        self.mat = dict()
    def add_material(self, mat):
        for s in mat.names:
            self.mat[s] = mat
        
class Material(object):
    def __init__(self, names, th_cond):
        self.names = names
        self.props = dict()
        self.props["THERMAL_CONDUCTIVITY"] = th_cond

cu = Material(
        ("copper","CU"),
        th_cond=units.unit('si_thermal_conductivity')(401.))

al = Material(
        ("aluminum", "AL"),
        th_cond=units.unit('si_thermal_conductivity')(177.))

materials = Materials()

materials.add_material(cu)
materials.add_material(al)

def PropsSI(prop_out, mat_name):
    global materials
    
    mat =  materials.mat[mat_name]
    
    return mat.props[prop_out]



