import pypot.dynamixel

ports = pypot.dynamixel.get_available_ports()
if not ports:
	raise IOError('Ports not found')
print('Ports found:',ports)
print('Connecting on first available port:', ports[0])
dxl_io = pypot.dynamixel.DxlIO(ports[0])
ids = dxl_io.scan(range(21))
print(ids)

if len(ids) < 20:
	print('All Motors not found')
	exit()
raw_input('Proceed?')
ids = [1,3,5]
f = open("angles.txt",'r')
data = f.readlines()
speeds = [100,100,100]
dxl_io.set_moving_speed(dict(zip(ids,speeds)))
for d in data:
	#print d
	angles = map(float,d.split())
	dxl_io.set_goal_position(dict(zip(ids,angles)))

	

