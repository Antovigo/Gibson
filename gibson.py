#!/usr/bin/python2

vol_total = 5
ng = []
bp = []
names = []

print ("\033[1;31mName\tConc.\tLength\033[1;m")

# Waiting for user input
while True:
    line = raw_input()
    if line:
        line = line.replace('\t',' ').split()
        names.append (line[0])
        ng.append (line[1])
        bp.append (line[2])
    else:
        break

l = len(ng)
ng = [float(i) for i in ng]
bp = [float(i) for i in bp]
# pmol = weight in ng/(bp * 0.650 daltons)
pmol = [ng[i] / (bp[i] * 0.650) for i in range(l)]

# sum of 1/C_i
denominator = sum ([1/i for i in pmol])
vol = [(vol_total/i)/denominator for i in pmol]
fin = [ pmol[i] * vol[i] / 5 for i in range(l)]

for i in range(l):
    print ('{2}:\t{0:.2f} ul\t({1:.2f} pmol)'.format(vol[i], fin[i], names[i]))
