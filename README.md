This script allows to generate Gibson Assembly mixes for molecular 
cloning. Just type the requested parameters (separated with space or 
tab), and press enter to go to the following reagent.

Input looks like this:

```
Name	Conc.	Length
R1	50	5200
R4	200	1300
R5	50	1300
```

When you're done, press enter once again.

The corresponding output for this example is:

```
R1:	3.81 ul	(0.01127 pmol)
R4:	0.24 ul	(0.01127 pmol)
R5:	0.95 ul	(0.01127 pmol)
```

By default, the total volume of DNA is 5 μl, but you can specify something else as a command-line argument.

```
# If you want a total of 10 μl of DNA
./gibson.py 10
```

License: GPL V4.
