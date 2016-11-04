#!/usr/bin/env python
#
# Author: Qiming Sun <osirpt.sun@gmail.com>
#

from pyscf import gto

'''
Access basis information

Mole.nbas is the total number of GTO shells.  It is initialized in
Mole.build() function.

.spheric_labels functions can be used to label AO functions.  It has two
formats: tuple or string.  The tuple format has four elements:
    (atom-id, atom-symbol, angular-momentum, xyz-components)
'''

mol = gto.M(
    atom = '''
        O  0 0.     0
        H1 0 -2.757 2.587
        H2 0 2.757  2.587''',
    basis = 'ccpvdz',
)

print('total number of shells %d, total number of AO functions %d' %
      (mol.nbas, mol.nao_nr()))

# Filter AO functions using AO labels, in tuple
for label in mol.spheric_labels():
    if label[2] == '2p' and label[3] == 'z':
        print(label)

# Filter AO functions using formated AO labels
for label in mol.spheric_labels(1):
    if '2pz' in label:
        print(label)

for i in range(mol.nbas):
    print('shell %d on atom %d l = %s has %d contracted GTOs' %
          (i, mol.bas_atom(i), mol.bas_angular(i), mol.bas_nctr(i)))

