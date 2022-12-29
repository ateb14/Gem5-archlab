#ifndef __CPU_PRED_MYSIMPLEBP_HH__
#define __CPU_PRED_MYSIMPLEBP_HH__

#include "base/types.hh"
#include "cpu/pred/bpred_unit.hh"
#include "params/MySimpleBP.hh"

namespace gem5{

namespace branch_prediction{

class MySimpleBP : public BPredUnit{
    public:

    MySimpleBP(const MySimpleBPParams &params);
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