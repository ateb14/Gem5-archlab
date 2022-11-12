import os

dram_list = [
    'ddr3_1600_8x8',
    'ddr3_2133_8x8',
    'ddr4_2400_16x4',
    'ddr4_2400_8x8',
    'lpddr2_s4_1066_1x32',
    'wideio_200_1x128',
    'lpddr3_1600_1x32'
    ]

cpu_list = [
    'o3',
    'inorder'
]

hz_list = [str((10+4*x)/10) for x in range(11)]
print(hz_list)

cnt = 1
for k in range(4):
    for i in range(len(cpu_list)):
        for j in range(len(hz_list)):
            cmd = 'build/ARM/gem5.opt --outdir=configs/proj1/out/'+ \
                str(cnt)+ ' configs/proj1/two-level.py --cpu_clock='+ \
                    hz_list[j]+\
                    'GHz --'+cpu_list[i] + ' --cmd='+ str(k)
            print(cmd)
            #os.system('mkdir configs/proj1/out/'+str(cnt))
            #os.system(cmd)
            print(cnt, 'finished')
            cnt += 1

# for i in range(47):
#     cmd = 'mkdir configs/proj1/out/' + str(i)
#     os.system(cmd)