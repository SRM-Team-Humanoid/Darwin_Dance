import pypot.dynamixel

ports = pypot.dynamixel.get_available_ports()
if not ports:
	raise IOError('no port found!')
print('ports found', ports)
print('connecting on the first available port:', ports[0])
dxl_io = pypot.dynamixel.DxlIO(ports[0])
ids = dxl_io.scan(range(21))
print(ids)
if len(ids) < 20:
	print "All motors not found"
	exit()
raw_input("Proceed ?")
ids = [1,3,5]
dxl_io.disable_torque(ids)
f = open("angles.txt", 'a')
while True:
	angles = dxl_io.get_present_position(ids)
	f.write(" ".join(map(str,angles))+"\n")
f.close()
