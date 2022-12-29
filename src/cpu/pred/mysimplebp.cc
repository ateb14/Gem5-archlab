#include "cpu/pred/mysimplebp.hh"

namespace gem5{

namespace branch_prediction{

MySimpleBP::MySimpleBP(const MySimpleBPParams &params):BPredUnit(params){}

bool MySimpleBP::lookup(ThreadID tid, Addr branch_addr, void *&bp_history){
    return true;
}

void MySimpleBP::uncondBranch(ThreadID tid, Addr pc, void *&bp_history){}
void MySimpleBP::btbUpdate(ThreadID tid, Addr branch_addr, void *&bp_history){}
void MySimpleBP::update(ThreadID tid, Addr branch_addr, bool taken, void *bp_history,
bool squashed, const StaticInstPtr &inst, Addr corrTarget){}
void MySimpleBP::squash(ThreadID tid, void * bp_history){}
}
}