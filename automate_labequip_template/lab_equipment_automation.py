import pyvisa
import time
from time import sleep
import os

# Datalogging: create a time-stamped file
# year/month/day & hour:minute
timestamp = time.strftime("%Y-%m-%d_%H%M")
filepath = "./" + timestamp + ".csv"

# Create a resource manager
rm = pyvisa.ResourceManager()
# Verify that all of your equipment is connected
print("Resources detected\n{}\n".format(rm.list_resources()))

# add USB0s to variables
reciever = rm.open_resource('USB01: ... ') 
waterpump = rm.open_resource('USB02: ...')


# Setup Digital MultiMeter in DC Voltage mode
reciever.write(':FUNCtion:VOLTage:DC')

# Setup reciever V, mA
waterpump.write(':OUTP CH#,OFF') # make sure waterpump is off

# Create a test (e.g. while, if, case, etc.)
waterpump.write(':OUTP CH#,ON') # Start with powering on the waterpump
waterpump.write(':APPL PSI,1') # set psi to 1
psi = 1
VExpected = 0 
while psi <= 50: # sweep V from 1-5 0-100%
    waterpump.write(':APPL CH#,' + ',1.0' + str(psi)) # rewrite psi output each time
    sleep(1) # set delay between test
    VMeasured = float( reciever.query(':MEASure:VOLTage:DC?') )  # turn measured V into a queared value

    # Write results to console
    print("{}  {}".format(VExpected, VMeasured))

    # Write results to a file
    with open(filepath, "a") as file: # open file for appending
        if os.stat(filepath).st_size == 0: # if empty file, write a header
            file.write("Setpoint Expected [V], Measured [V]\n") 
        file.write("{:#.#f},{:#.#f}\n".format(V, VMeasured)) # log the data and set float values to fit data # of signifant figures
    file.close()

    psi += 0.1	# set psi step value
    VExpected += psi * 0.1 # convert Voltage to expect ratio with psi


# reset lab equipment by turning off the power supply and setting values to zero
waterpump.write(':APPL Psi,0')
waterpump.write(':OUTP CH#,OFF')







