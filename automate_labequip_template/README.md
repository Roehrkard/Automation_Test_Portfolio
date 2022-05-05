# Automated Pressure Transducers w/ Pyton
This is python script which serves as a template to automate a pressure transducers test using a water pump and a reciever. 

download NI-VISA for pyvisa backend dependency
## Steps
1. Open up your terminal: pip3 install -U pyvisa
2. Install NI-VISA for pyvisa dependency
3. Connect labgear to your computer
4. Find the USB IDs of the connected labgear using your terminal
	>>> python
	>>> import pyvisa
	>>> rm = pyvisa.ResourceManager()
	>>> print(rm.list_resources())
	('USB01: ... ', 'USB02: ...', ...)
5. Copy and paste each USB IDs into variable = rm.open_resource('USB0: ...')
6. Download and search programming manuals for each piece of lab equipment to find the appropiate write commands to perform test.

