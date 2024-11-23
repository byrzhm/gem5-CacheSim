from m5.objects import *
from m5.util import *

# Create the system
system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()

# Create the memory
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

# Create a simple CPU
system.cpu = TimingSimpleCPU()

# Add L1 caches
system.cpu.icache = L1ICache(size='32kB')
system.cpu.dcache = L1DCache(size='32kB')

# Create an L2 cache
system.l2cache = L2Cache(size='256kB')
system.membus = SystemXBar()

# Connect caches
system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)
system.cpu.icache.connectBus(system.l2cache.cpu_side)
system.cpu.dcache.connectBus(system.l2cache.cpu_side)
system.l2cache.mem_side = system.membus.slave
system.system_port = system.membus.master

# Set up the workload
system.workload = SEWorkload.init_compatible('matmul')
process = Process()
process.cmd = ['matmul']
system.cpu.workload = process
system.cpu.createThreads()

# Create the memory controller
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master

# Instantiate the system
root = Root(full_system=False, system=system)
m5.instantiate()

print("Starting simulation...")
exit_event = m5.simulate()
print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}")