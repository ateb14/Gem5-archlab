from time import CLOCK_BOOTTIME
import m5
from m5.objects import *
from new_cache import *
from new_pred import *
from optparse import OptionParser
parser = OptionParser()
parser.add_option('--local', action="store_true")
parser.add_option("--tournament", action="store_true")
parser.add_option("--simple", action="store_true")
parser.add_option("--default", action="store_true")
parser.add_option("--perceptron", action="store_true")
parser.add_option("--mpperceptron", action="store_true")
parser.add_option('--repl_clock', action="store_true")
parser.add_option('--repl_rand', action="store_true")
parser.add_option('--repl_MRU', action="store_true")
parser.add_option('--repl_LRU', action="store_true")
parser.add_option('--cmd', type="int", default=0)
parser.add_option('--threshold', type="int", default=36)
parser.add_option('--ghrsize', type="int", default=16)
parser.add_option('--tablesize', type="int", default=1024)
(options, args) = parser.parse_args()

root = Root()
root.full_system = False
root.system = System()

root.system.clk_domain = SrcClockDomain()
root.system.clk_domain.clock = '2GHz'
root.system.clk_domain.voltage_domain = VoltageDomain()

root.system.mem_mode = 'timing'
root.system.mem_ranges = [AddrRange ('2GB')]
root.system.mem_ctrl = MemCtrl()
root.system.mem_ctrl.dram = DDR4_2400_16x4 ()
root.system.mem_ctrl.dram.range = root.system.mem_ranges[0]

root.system.cpu = DerivO3CPU()

class PerceptronBP(MyPerceptronBP):
    
    GHRsize = options.ghrsize
    Threshold = options.threshold
    TableSize = options.tablesize

    def __init__(self):
        super(PerceptronBP, self).__init__()

if options.local:
    root.system.cpu.branchPred = LocalBP()
elif options.tournament:
    root.system.cpu.branchPred = TournamentBP()
elif options.simple:
    root.system.cpu.branchPred = MySimpleBP()
elif options.perceptron:
    root.system.cpu.branchPred = PerceptronBP()
elif options.mpperceptron:
    root.system.cpu.branchPred = MultiperspectivePerceptron8KB()
else:
    root.system.cpu.branchPred = MySimpleBP()

root.system.membus = SystemXBar()

# cache
root.system.cpu.icache = L1ICache()
root.system.cpu.dcache = L1DCache()
root.system.l2cache = L2Cache()

replace_policy = LRURP()
if options.repl_clock:
    replace_policy = CLOCKRP()
elif options.repl_rand:
    replace_policy = RandomRP()
elif options.repl_MRU:
    replace_policy = MRURP()
elif options.repl_LRU:
    replace_policy = LRURP()

root.system.cpu.icache.replacement_policy = replace_policy
root.system.cpu.dcache.replacement_policy = replace_policy
root.system.l2cache.replacement_policy = replace_policy
# connect l1cache to cpu
root.system.cpu.icache.cpu_side = root.system.cpu.icache_port
root.system.cpu.dcache.cpu_side = root.system.cpu.dcache_port
# connect l1cache to l2
root.system.l2bus = L2XBar()
root.system.cpu.icache.mem_side = root.system.l2bus.cpu_side_ports
root.system.cpu.dcache.mem_side = root.system.l2bus.cpu_side_ports
root.system.l2cache.cpu_side = root.system.l2bus.mem_side_ports
# connect l2cache to memory bus
root.system.l2cache.mem_side = root.system.membus.cpu_side_ports

root.system.mem_ctrl.port = root.system.membus.mem_side_ports
root.system.cpu.createInterruptController()
root.system.system_port = root.system.membus.cpu_side_ports
# root.system.cpu.interrupts[0].pio = system.membus.mem_side_ports
# root.system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
# root.system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

exe_path = 'tests/test-progs/hello/bin/arm/linux/hello'
root.system.workload = SEWorkload.init_compatible(exe_path)

root.system.cpu.max_insts_any_thread = 100000000

process = Process()
process.cmd = [exe_path]
cmds = [
    ['test_bench/2MM/2mm_base'],
    ['test_bench/BFS/bfs','-f','test_bench/BFS/USA-road-d.NY.gr'],
    ['test_bench/bzip2/bzip2_base.amd64-m64-gcc42-nn','test_bench/bzip2/input.source','280'],
    ['test_bench/mcf/mcf_base.amd64-m64-gcc42-nn','test_bench/mcf/inp.in']
]
process.cmd = cmds[options.cmd]
print(process.cmd)

root.system.cpu.workload = process
root.system.cpu.createThreads()

m5.instantiate()
exit_event = m5.simulate()
print('Exiting @ tick {} because {}'.format(m5.curTick(), exit_event.getCause()))