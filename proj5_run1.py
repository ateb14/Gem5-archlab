import os

preds = ['local', 'tournament', 'simple']

res = [] 
for pred in preds:
    for mis in range(2):
        name = pred + '_mission' + str(mis)
        cmd = 'build/ARM/gem5.opt --outdir=configs/proj5/out/' + name + ' configs/proj5/two-level.py' +' --cmd=' + str(mis) + ' --' + pred
        print(cmd)
        #os.system('mkdir configs/proj5/out/' + name)
        os.system(cmd)
        
        with open('configs/proj5/out/'+name+'/stats.txt') as file:
            ins_num, cyc_num = 0, 0
            yes, no = 0, 0
            btbhitrate = 0
            for line in file:
                if 'simInsts' in line:
                    ins_num = int(line.split()[1])
                elif 'system.cpu.numCycles' in line:
                    cyc_num = int(line.split()[1])
                elif 'system.cpu.branchPred.condPredicted' in line:
                    yes = int(line.split()[1])
                elif 'system.cpu.branchPred.condIncorrect' in line:
                    no = int(line.split()[1])
                elif 'system.cpu.branchPred.BTBHitRatio' in line:
                    btbhitrate = float(line.split()[1])
            ipc = ins_num / cyc_num
            hitrate = yes / (yes + no)
            res.append('|'+name+'|'+ str(ipc)+'|'+str(hitrate)+'|'+str(btbhitrate)+'|')
            print(res[len(res)-1])

for o in res:
    print(o)