#!/usr/bin/env python3


#! ------------------------------- header_lineitems ------------------------------- #
# Start your code from here!

header = ['Header1', 'Header2', 'Header3']


lineitem1 = ['Lineitem11', 'Lineitem12',
             'Lineitem13', 'Lineitem14', 'Lineitem15']
lineitem2 = ['Lineitem21', 'Lineitem22',
             'Lineitem23', 'Lineitem24', 'Lineitem25']
lineitem3 = ['Lineitem31', 'Lineitem32',
             'Lineitem33', 'Lineitem34', 'Lineitem35']

lines = [lineitem1, lineitem2, lineitem3]


for i in range(len(lines)):
    lines[i].insert(0, header)
    print(lines[i])
    header = ['null', 'null', 'null']


#! ------------------------------------ EOF ----------------------------------- #
