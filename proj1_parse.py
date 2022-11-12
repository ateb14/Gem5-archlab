

names = [
'ddr3_1600_8x8',
'ddr3_2133_8x8',
'ddr4_2400_16x4',
'ddr4_2400_8x8',
'lpddr2_s4_1066_1x32',
'wideio_200_1x128',
'lpddr3_1600_1x32',
]

hz_list = [str((10+4*x)/10) for x in range(11)]

cnt = 1
ipc_lst = []
while cnt <= 14:
    with open('configs/proj1/out/'+str(cnt)+'/stats.txt') as file:
        inc, cyc = 0, 1
        ipc = 0
        bw = 0
        sec = 0
        for line in file:
            if 'simInsts' in line:
                inc = int(line.split()[1])

            if 'system.cpu.numCycles' in line:
                cyc = int(line.split()[1])
                ipc = inc / cyc
            # if 'simSeconds' in line:
            #     sec = float(line.split()[1])

            if 'system.mem_ctrl.dram.bwTotal::total' in line:
                bw = int(line.split()[1])
        # if(cnt % 11 == 1):
        #     print("#########")
        # print('|',hz_list[(cnt-1)%11],'|',ipc, '|', sec,'|')
        if(cnt % 7 == 1):
            print("#########")
        print('|',names[(cnt-1)%7],'|',ipc, '|', bw,'|')
    cnt += 1
