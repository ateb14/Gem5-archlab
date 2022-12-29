#ifndef __CPU_PRED_MYPERCEPTRONBP_HH__
#define __CPU_PRED_MYPERCEPTRONBP_HH__

#include "base/types.hh"
#include "cpu/pred/bpred_unit.hh"
#include "params/MyPerceptronBP.hh"
#include <vector>
#include <map>

namespace gem5{

namespace branch_prediction{

typedef uint64_t GHR;
class Info{
public:
    int64_t output;
    unsigned idx;
    GHR ghr;
    bool isConsumed;
};
typedef std::map<Addr, Info> REC;

class Perceptron{
    std::vector<int64_t> weights;
    unsigned size;
public:
    void train(int64_t target, GHR ghr, unsigned threshold, int64_t output);
    Perceptron(unsigned size_);
    bool predict(GHR ghr, int64_t & ret);
};

class MyPerceptronBP : public BPredUnit{
    GHR ghr; // global history register
    unsigned GHRsize; // 1 << x << 64
    unsigned threshold;
    unsigned table_size;
    std::vector<Perceptron> ptable;
    REC output_record;

public:

    MyPerceptronBP(const MyPerceptronBPParams &params);
    void uncondBranch(ThreadID tid, Addr pc, void *&bp_history);
    bool lookup(ThreadID tid, Addr branch_addr, void *&bp_history);
    void btbUpdate(ThreadID tid, Addr branch_addr, void *&bp_history);
    void update(ThreadID tid, Addr branch_addr, bool taken, void *bp_history,
    bool squashed, const StaticInstPtr &inst, Addr corrTarget);
    void squash(ThreadID tid, void * bp_history);

};

} 
}


#endif