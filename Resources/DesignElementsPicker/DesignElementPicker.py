
'''
DESIGN ELEMENT PICKER
Jeff Thompson | 2017 | jeffreythompson.org

Randomly selects design elements for an accordion
book assignment, prints out the results.

'''

from random import sample
from ThermalPrinterLib import *

name = 		       'Jeff'
self_chosen_elem = 'small'
num_elements =     3


# load up elements from file
print 'loading elements from file...'
elements = []
with open('../DesignElements.md') as f:
	for i, line in enumerate(f):
		line = line.strip()
		if i < 3 or line == self_chosen_elem.title():
			continue
		elements.append(line)


# make name possessive
if name[-1] == 's':
	name += '\''
else:
	name = name + '\'s'
name.upper()


# give me some random elements, please
print 'selecting random elements for you...'
my_elements = [ self_chosen_elem ]
my_elements += sample(elements, num_elements)
my_elements = [ elem.title() for elem in my_elements ]
my_elements.sort()


# print it
print 'printing...'
printer = Adafruit_Thermal('/dev/tty.usbserial', 9600, timeout=5)
printer.justify('C')

printer.setSize('S')
printer.println(name + ' DESIGN ELEMENTS')
printer.println('')
printer.println('- - - - - - - - - - - - -')
printer.println('')

printer.setSize('L')
for elem in my_elements:
	if elem == self_chosen_elem.title():
		elem = '*' + elem + '*'
	printer.println(elem)

printer.setSize('S')
printer.println('')
printer.println('- - - - - - - - - - - - -')
printer.println('')
printer.println('https://github.com/jeffThompson/')
printer.println('Design2/tree/master/Assignments/')
printer.println('05_DesignElementsBook.md')

printer.feed(4)
printer.sleep()
printer.wake()
printer.setDefault()

print 'all good, bye'

