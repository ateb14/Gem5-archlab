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


cnt = 1
for j in range(2,4):
    for i in range(len(dram_list)):
        cmd = 'build/ARM/gem5.opt --outdir=configs/proj1/out/'+ \
        str(cnt)+ ' configs/proj1/two-level.py --o3 --cpu_clock=4GHz --'+ \
        dram_list[i] + ' --cmd='+ str(j)
        print(cmd)
        os.system(cmd)
        print(cnt, 'finished')
        cnt += 1