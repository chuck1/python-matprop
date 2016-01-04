
import nas.units
import units

nas.units.define_units()

class Materials(object):
    def __init__(self):
        self.mat = dict()
    def add_material(self, mat):
        self.mat[mat.name] = mat

class Material(object):
    def __init__(self, name, th_cond):
        self.name = name
        self.props = dict()
        self.props["THERMAL_CONDUCTIVITY"] = th_cond

cu = Material(
        "copper",
        th_cond=units.unit('si_thermal_conductivity')(401.))

al = Material(
        "aluminum",
        th_cond=units.unit('si_thermal_conductivity')(177.))

materials = Materials()

materials.add_material(cu)

def PropsSI(prop_out, mat_name):
    global materials

    mat =  materials.mat[mat_name]

    return mat.props[prop_out]



