import dronekit_sitl

sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

from dronekit import connect, VehicleMode

print('Connecting to vehicle on {}'.format(connection_string))
vehicle = connect(connection_string, wait_ready=True)

print('GPS: {}'.format(vehicle.gps_0))
print('BATTERY: '.format(vehicle.battery))
print('LAST HEARTBEAT'.format(vehicle.last_heartbeat))
print('IS ARMABLE: {}'.format(vehicle.is_armable))
print('SYSTEM STATUS: {}'.format(vehicle.system_status.state))
print('MODE {}'.format(vehicle.mode.name))

vehicle.close()
sitl.stop()
print('Complete')
