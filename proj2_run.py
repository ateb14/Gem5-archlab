import os

predictor_list =[
    'local',
    'tournament',
    'bimode'
]

task_names = [
    '2MM',
    'BFS',
    'BZIP2',
    'MCF'
]

btb_sizes = [
    '8',
    '32',
    '512',
    '4096',
]

local_predictor_sizes = [
    '2',
    '1024',
    '2048',
]

global_predictor_sizes =[
    '2',
    '2048',
    '8192',
]

localhissizes = [
    '2',
    '256',
    '2048',
]

ras_sizes = [
    '2',
    '8',
    '16',
    '128',
]


# 1
with open('configs/proj2/mission1.txt','w') as output:
    for k in range(2):
        res = []
        output.write(task_names[k] + '\n')
        for i in range(len(predictor_list)):
            task_name = 'mission1_'+ task_names[k] +'_'+predictor_list[i]
            cmd = 'build/ARM/gem5.opt --outdir=configs/proj2/out/'+ task_name + ' configs/proj2/two-level.py --'+predictor_list[i] + ' --cmd='+ str(k)
            print(cmd)
            os.system('mkdir configs/proj2/out/'+task_name)
            os.system(cmd)
            with open('configs/proj2/out/' + task_name + '/stats.txt') as file:
                ipc, hit, miss = 0, 0, 0
                hit_rate = 0
                for line in file:
                    if 'system.cpu.ipc' in line:
                        ipc = float(line.split()[1])
                    if 'system.cpu.branchPred.condPredicted' in line:
                        hit = int(line.split()[1])
                    if 'system.cpu.branchPred.condIncorrect' in line:
                        miss = int(line.split()[1])
                hit_rate = float(hit / (hit+miss))
            output.write('|'+ predictor_list[i] + '|'+str(ipc)+'|'+str(round(hit_rate*100,3))+'%|\n')
            output.flush()
        output.write('\n')

2
mission = '2'
with open('configs/proj2/mission' + mission + '.txt','w') as output:
    for k in range(2):
        res = []
        output.write(task_names[k] + '\n')
        for i in range(len(predictor_list)):
            output.write( predictor_list[i] + '\n')
            for btb_size in btb_sizes:
                task_name = 'mission'+mission+'_'+ task_names[k] +'_'+predictor_list[i] +'_btbsize' + btb_size
                cmd = 'build/ARM/gem5.opt --outdir=configs/proj2/out/'+ task_name + \
                ' configs/proj2/two-level.py --'+predictor_list[i] + ' --cmd='+ str(k) +' --btbentry='+btb_size
                print(cmd)
                os.system('mkdir configs/proj2/out/'+task_name)
                os.system(cmd)
                with open('configs/proj2/out/' + task_name + '/stats.txt') as file:
                    ipc, hit, miss = 0, 0, 0
                    hit_rate = 0
                    for line in file:
                        if 'system.cpu.ipc' in line:
                            ipc = float(line.split()[1])
                        if 'system.cpu.branchPred.condPredicted' in line:
                            hit = int(line.split()[1])
                        if 'system.cpu.branchPred.condIncorrect' in line:
                            miss = int(line.split()[1])
                    hit_rate = float(hit / (hit+miss))
                output.write('|'+ btb_size + '|'+str(ipc)+'|'+str(round(hit_rate*100,3))+'%|\n')
                output.flush()
            output.write('\n')


mission = '3'
with open('configs/proj2/mission' + mission + '.txt','w') as output:
    for k in range(2):
        res = []
        output.write(task_names[k] + '\n')
        for i in range(len(predictor_list)):
            output.write( predictor_list[i] + '\n')
            for ras_size in ras_sizes:
                task_name = 'mission'+mission+'_'+ task_names[k] +'_'+predictor_list[i] +'_ras' + ras_size
                cmd = 'build/ARM/gem5.opt --outdir=configs/proj2/out/'+ task_name + \
                ' configs/proj2/two-level.py --'+predictor_list[i] + ' --cmd='+ str(k) +' --ras='+ras_size
                print(cmd)
                os.system('mkdir configs/proj2/out/'+task_name)
                os.system(cmd)
                with open('configs/proj2/out/' + task_name + '/stats.txt') as file:
                    ipc, hit, miss = 0, 0, 0
                    hit_rate = 0
                    for line in file:
                        if 'system.cpu.ipc' in line:
                            ipc = float(line.split()[1])
                        if 'system.cpu.branchPred.condPredicted' in line:
                            hit = int(line.split()[1])
                        if 'system.cpu.branchPred.condIncorrect' in line:
                            miss = int(line.split()[1])
                    hit_rate = float(hit / (hit+miss))
                output.write('|'+ ras_size + '|'+str(ipc)+'|'+str(round(hit_rate*100,3))+'%|\n')
                output.flush()
            output.write('\n')

mission = '4'
with open('configs/proj2/mission' + mission + '.txt','w') as output:
    for k in range(1,2):
        res = []
        output.write(task_names[k] + '\n')
        for i in range(0,1):
            output.write( predictor_list[i] + '\n')
            for local_predictor_size in local_predictor_sizes:
                task_name = 'mission'+mission+'_'+ task_names[k] +'_'+predictor_list[i] +'_localsize' + local_predictor_size
                cmd = 'build/ARM/gem5.opt --outdir=configs/proj2/out/'+ task_name + \
                ' configs/proj2/two-level.py --'+predictor_list[i] + ' --cmd='+ str(k) +' --localsize='+local_predictor_size
                print(cmd)
                os.system('mkdir configs/proj2/out/'+task_name)
                os.system(cmd)
                with open('configs/proj2/out/' + task_name + '/stats.txt') as file:
                    ipc, hit, miss = 0, 0, 0
                    hit_rate = 0
                    for line in file:
                        if 'system.cpu.ipc' in line:
                            ipc = float(line.split()[1])
                        if 'system.cpu.branchPred.condPredicted' in line:
                            hit = int(line.split()[1])
                        if 'system.cpu.branchPred.condIncorrect' in line:
                            miss = int(line.split()[1])
                    hit_rate = float(hit / (hit+miss))
                output.write('|'+ local_predictor_size + '|'+str(ipc)+'|'+str(round(hit_rate*100,3))+'%|\n')
                output.flush()
            output.write('\n')

mission = '5'
with open('configs/proj2/mission' + mission + '.txt','w') as output:
    for k in range(1,2):
        res = []
        output.write(task_names[k] + '\n')
        for i in range(2,3):
            output.write( predictor_list[i] + '\n')
            for global_predictor_size in global_predictor_sizes:
                task_name = 'mission'+mission+'_'+ task_names[k] +'_'+predictor_list[i] +'_globalsize' + global_predictor_size
                cmd = 'build/ARM/gem5.opt --outdir=configs/proj2/out/'+ task_name + \
                ' configs/proj2/two-level.py --'+predictor_list[i] + ' --cmd='+ str(k) +' --globalsize='+global_predictor_size
                print(cmd)
                os.system('mkdir configs/proj2/out/'+task_name)
                os.system(cmd)
                with open('configs/proj2/out/' + task_name + '/stats.txt') as file:
                    ipc, hit, miss = 0, 0, 0
                    hit_rate = 0
                    for line in file:
                        if 'system.cpu.ipc' in line:
                            ipc = float(line.split()[1])
                        if 'system.cpu.branchPred.condPredicted' in line:
                            hit = int(line.split()[1])
                        if 'system.cpu.branchPred.condIncorrect' in line:
                            miss = int(line.split()[1])
                    hit_rate = float(hit / (hit+miss))
                output.write('|'+ global_predictor_size + '|'+str(ipc)+'|'+str(round(hit_rate*100,3))+'%|\n')
                output.flush()
            output.write('\n')

mission = '6'
with open('configs/proj2/mission' + mission + '.txt','w') as output:
    for k in range(1,2):
        res = []
        output.write(task_names[k] + '\n')
        for i in range(1,2):
            output.write( predictor_list[i] + '\n')
            for global_predictor_size in global_predictor_sizes:
                output.write('global_predictor_size:'+global_predictor_size + '\n')
                for local_predictor_size in local_predictor_sizes:
                    output.write( 'local_predictor_size:'+local_predictor_size + '\n')
                    for localhissize in localhissizes:
                        task_name = 'mission'+mission+'_'+ task_names[k] +'_'+predictor_list[i] +'_globalsize' + global_predictor_size
                        cmd = 'build/ARM/gem5.opt --outdir=configs/proj2/out/'+ task_name + \
                        ' configs/proj2/two-level.py --'+predictor_list[i] + ' --cmd='+ str(k) + \
                            ' --globalsize='+global_predictor_size + \
                            ' --localsize='+local_predictor_size + \
                            ' --localhissize='+localhissize
                        print(cmd)
                        os.system('mkdir configs/proj2/out/'+task_name)
                        os.system(cmd)
                        with open('configs/proj2/out/' + task_name + '/stats.txt') as file:
                            ipc, hit, miss = 0, 0, 0
                            hit_rate = 0
                            for line in file:
                                if 'system.cpu.ipc' in line:
                                    ipc = float(line.split()[1])
                                if 'system.cpu.branchPred.condPredicted' in line:
                                    hit = int(line.split()[1])
                                if 'system.cpu.branchPred.condIncorrect' in line:
                                    miss = int(line.split()[1])
                            hit_rate = float(hit / (hit+miss))
                        output.write('|'+ localhissize + '|'+str(ipc)+'|'+str(round(hit_rate*100,3))+'%|\n')
                        output.flush()
                    output.write('\n')