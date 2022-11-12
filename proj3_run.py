import os

replacement = [
    'clock',
    'LRU',
    'MRU',
    'rand',
]


with open('configs/proj3/res.txt', 'w') as outfile:
    for n in range(0, 4):
        for replace in replacement:
            task_name = 'mission'+ str(n)+replace
            cmd = 'build/ARM/gem5.opt --outdir=configs/proj3/out/'+ task_name + ' configs/proj3/two-level.py --repl_'+replace + ' --cmd='+ str(n)
            # os.system('mkdir configs/proj3/out/'+task_name)
            print(cmd)
            os.system(cmd)
            with open('configs/proj3/out/'+task_name+'/stats.txt') as file:
                icache_hit, dache_hit, l2cache_hit = 0, 0, 0
                icache_miss, dcache_miss, l2cache_miss = 0, 0, 0
                ins_num, cyc_num = 0, 0
                for line in file:
                    if 'system.l2cache.overallHits::total' in line:
                        l2cache_hit = int(line.split()[1])
                    elif 'system.l2cache.overallMisses::total' in line:
                        l2cache_miss = int(line.split()[1])
                    elif 'system.cpu.dcache.overallHits::total' in line:
                        dcache_hit = int(line.split()[1])
                    elif 'system.cpu.dcache.overallMisses::total' in line:
                        dcache_miss = int(line.split()[1])
                    elif 'system.cpu.icache.overallHits::total' in line:
                        icache_hit = int(line.split()[1])
                    elif 'system.cpu.icache.overallMisses::total' in line:
                        icache_miss = int(line.split()[1])
                    elif 'simInsts' in line:
                        ins_num = int(line.split()[1])
                    elif 'system.cpu.numCycles' in line:
                        cyc_num = int(line.split()[1])
            outfile.write('|'+ replace +'|'+ str(round(icache_hit / (icache_hit + icache_miss),3))+'|'
            + str(round(dcache_hit / (dcache_hit + dcache_miss),3))+'|'+
            str(round(l2cache_hit / (l2cache_hit + l2cache_miss),3))+ '|'+ str(round(ins_num/cyc_num,3)) +'|\n')
        outfile.write('\n')
