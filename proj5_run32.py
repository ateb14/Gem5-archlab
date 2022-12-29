import os

preds = ['perceptron']

ghrsize = [32]

tablesize = ['256','512','1024']

res = [] 
for mis in range(1):
    for pred in preds:
        for ghr in ghrsize:
            t = round(ghr * 1.93 + 14)
            thresholds = [t-10, t, t+10]
            for threshold in thresholds:
                for s in tablesize:
                    name = pred + '_mission' + str(mis) + '_' + str(ghr) + '_' + str(threshold) + '_' + s
                    cmd = 'build/ARM/gem5.opt --outdir=configs/proj5/out/' + name + ' configs/proj5/two-level.py' +' --cmd=' + str(mis) + ' --' + pred\
                        + ' --ghrsize=' + str(ghr) + ' --threshold=' + str(threshold) + ' --tablesize='+s
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