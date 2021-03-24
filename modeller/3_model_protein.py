# Addition of restraints to the default ones
from modeller import *
from modeller.automodel import *    # Load the automodel class
import sys

log.verbose()
env = environ()
env.io.hetatm = True
# Give less weight to all soft-sphere restraints:
env.schedule_scale = physical.values(default=1.0, soft_sphere=0.7)

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

class MyModel(automodel):
    def special_restraints(self, aln):
        rsr = self.restraints
        at = self.atoms
#       Add some restraints from a file:
#       rsr.append(file='my_rsrs1.rsr')


# A disulfide between residues 24 and 79:
#        self.patch(residue_type='DISU', residues=(self.residues['24'],
#                                                  self.residues['79']))

#       Residues to be an alpha helix:
#        rsr.add(secondary_structure.alpha(self.residue_range('71:', '73:')))

#       Two beta-strands:
#        rsr.add(secondary_structure.strand(self.residue_range('5:','7:')))
#        rsr.add(secondary_structure.strand(self.residue_range('12:','14:')))
#        rsr.add(secondary_structure.strand(self.residue_range('20:','26:')))
# 	rsr.add(secondary_structure.strand(self.residue_range('34:','38:')))
#        rsr.add(secondary_structure.strand(self.residue_range('53:','58:')))
#        rsr.add(secondary_structure.strand(self.residue_range('61:','66:'))) 
#	rsr.add(secondary_structure.strand(self.residue_range('75:','83:')))
#        rsr.add(secondary_structure.strand(self.residue_range('87:','98:')))

#       An anti-parallel sheet composed of the two strands:
#       rsr.add(secondary_structure.sheet(at['N:1'], at['O:14'],
#                                         sheet_h_bonds=-5))
#       Use the following instead for a *parallel* sheet:
#       rsr.add(secondary_structure.sheet(at['N:1'], at['O:9'],
#                                         sheet_h_bonds=5))

#       Restrain the specified CA-CA distance to 10 angstroms (st. dev.=0.1)
#       Use a harmonic potential and X-Y distance group.
#        rsr.add(forms.gaussian(group=physical.xy_distance,
#                               feature=features.distance(at['CA:1'],
#                                                         at['CA:264']),
#                               mean=10.0, stdev=0.1))

#        rsr.add(forms.gaussian(group=physical.xy_distance,
#                               feature=features.distance(at['CA:44'],
#                                                         at['CA:98']),
#                               mean=6.0, stdev=0.1))

#        rsr.add(forms.gaussian(group=physical.xy_distance,
#                               feature=features.distance(at['CA:63'],
#                                                         at['CA:307']),
#                               mean=6.0, stdev=0.1))

#        rsr.add(forms.gaussian(group=physical.xy_distance,
#                               feature=features.distance(at['CA:24'],
#                                                         at['CA:241']),
#                               mean=6.0, stdev=0.1))



a = MyModel(env,
            alnfile  = 'query-mult.ali',  # alignment filename
            knowns   = (('2ZG2A'), ('6D48E'), ('2N7AA')),     # codes of the templates
            sequence = 'Query',
            assess_methods=(assess.DOPE, assess.GA341)) # code of the target
a.starting_model= 1                     # index of the first model
a.ending_model  = 20                    # index of the last model
                                        # (determines how many models to calculate)
a.library_schedule = autosched.slow     # Very thorough VTFM optimization
a.max_var_iterations = 50
a.md_level = refine.slow                # Thorough MD optimization
a.repeat_optimization = 5               # Repeat the whole cycle 5 times and..
a.max_molpdf = 1e6                      # do not stop unless obj.func. > 1E6

a.make()

ok_models = [x for x in a.outputs if x['failure'] is None]  # Get a list of all successfully built models from a.outputs

# Rank the models by DOPE score
key = 'DOPE score'
if sys.version_info[:2] == (2,3):
    # Python 2.3's sort doesn't have a 'key' argument
    ok_models.sort(lambda a,b: cmp(a[key], b[key]))
else:
    ok_models.sort(key=lambda a: a[key])

# Print DOPE scores of the top 10 models top 10 model
m = ok_models[0]
print("Top model 1: %s (DOPE score %.3f)" % (m['name'], m[key]))
m = ok_models[1]
print("Top model 2: %s (DOPE score %.3f)" % (m['name'], m[key]))
m = ok_models[2]
print("Top model 3: %s (DOPE score %.3f)" % (m['name'], m[key]))
m = ok_models[3]
print("Top model 4: %s (DOPE score %.3f)" % (m['name'], m[key]))
m = ok_models[4]
print("Top model 5: %s (DOPE score %.3f)" % (m['name'], m[key]))
m = ok_models[5]
print("Top model 6: %s (DOPE score %.3f)" % (m['name'], m[key]))
m = ok_models[6]
print("Top model 7: %s (DOPE score %.3f)" % (m['name'], m[key]))
m = ok_models[7]
print("Top model 8: %s (DOPE score %.3f)" % (m['name'], m[key]))
m = ok_models[8]
print("Top model 9: %s (DOPE score %.3f)" % (m['name'], m[key]))
m = ok_models[9]
print("Top model10: %s (DOPE score %.3f)" % (m['name'], m[key]))
