# Find all the availabe adapters and EtherCAT slave
# requires npcap installed https://npcap.com/

import pysoem

# # Find available network adapters
# adapters = pysoem.find_adapters()
# for i, adapter in enumerate(adapters):
#    print('Adapter {}'.format(i))
#    print('  {}'.format(adapter.name))
#    print('  {}'.format(adapter.desc))

# Use comment out code above to find the correct Ethernet Adapter path
adapter_name = "\\Device\\NPF_{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}" 

# Find EtherCAT slave device
master = pysoem.Master()

# Open the master to get communication & detect Slaves
master.open(adapter_name)

slave_count = master.config_init() 
if slave_count > 0:
    print(f"Found {slave_count} EtherCAT slaves:")
    for device in master.slaves:
        print(f'  - {device.name}')
else:
    print('No devices found')

master.close()

