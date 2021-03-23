from modeller import *

log.verbose()
env = environ()

env.libs.topology.read(file='$(LIB)/top_heav.lib')

# Read aligned structure(s):
aln = alignment(env)
aln.append(file='fm00495.ali', align_codes='all')
aln_block = len(aln)

# Read aligned sequence(s):
aln.append(file='Query.ali', align_codes='Query')

# Structure sensitive variable gap penalty sequence-sequence alignment:
aln.align2d()
aln.write(file='query-mult.ali', alignment_format='PIR')
aln.write(file='query-mult.pap', alignment_format='PAP')

