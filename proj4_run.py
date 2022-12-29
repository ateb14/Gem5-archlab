import os

for n in range(1,9):
    cmd = 'build/ARM/gem5.opt --outdir=output/cpu' + str(n)+' configs/example/fs.py --kernel=vmlinux.arm64 --disk-image=ubuntu-18.04-arm64-docker.img --num-cpu=8' +  \
    ' --script=fssimulation_scripts/test' + str(n) +'.rcS'
    print(cmd)
    #os.system('mkdir output/cpu'+str(n))
    os.system(cmd) 