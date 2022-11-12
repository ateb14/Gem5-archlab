from m5.objects import *

class L1DCache(Cache):
    size = '32kB'
    assoc = 4
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20

    def __init__(self):
        super(L1DCache, self).__init__()

class L1ICache(Cache):
    size = '32kB'
    assoc = 4
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20

    def __init__(self):
        super(L1ICache, self).__init__()

class L2Cache(Cache):
    size = '2MB'
    assoc = 8
    tag_latency = 20
    data_latency = 20
    response_latency = 20
    mshrs = 20
    tgts_per_mshr = 12

    def __init__(self):
        super(L2Cache, self).__init__()
