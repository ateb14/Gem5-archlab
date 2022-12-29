#include "cpu/pred/myperceptronbp.hh"
#include <iostream>
namespace gem5{

namespace branch_prediction{

Perceptron::Perceptron(unsigned size_){
    this->weights.resize(size_, 0);
    this->size = size_;
} 

void Perceptron::train(int64_t target, GHR ghr, unsigned threshold, int64_t output){
    //std::cout << last_choice << " " << threshold << std::endl;

    if(!(output * target < 0 || abs(output) <= threshold)){
        return;
    }

    int64_t indicator = 1;
    for(size_t i = 0; i < size; ++i, indicator <<= 1){
        int64_t xi = -1;
        if(indicator & ghr)
            xi = 1;
        this->weights[i] += xi * target; 
    }
}

bool Perceptron::predict(GHR ghr, int64_t &ret){
    int64_t indicator = 1;
    int64_t res = 0;
    for(size_t i = 0; i < size; ++i, indicator <<= 1){
        if(indicator & ghr)
            res += this->weights[i];
        else
            res -= this->weights[i];
    }
    ret = res;
    return res >= 0;
}

MyPerceptronBP::MyPerceptronBP(const MyPerceptronBPParams &params):
BPredUnit(params), GHRsize(params.GHRsize), threshold(params.Threshold), table_size(params.TableSize){
    ptable.resize(table_size, GHRsize);
}

bool MyPerceptronBP::lookup(ThreadID tid, Addr branch_addr, void *&bp_history){
    unsigned idx = (branch_addr ^ ghr) % table_size;
    //std::cout << " lookup: " << branch_addr << std::endl;
    Perceptron & perceptron = ptable[idx];
    int64_t res;
    bool taken = perceptron.predict(ghr, res);
    
    // record the output
    auto it = output_record.find(branch_addr);
    if(it != output_record.end()){
        it->second.output = res;
        it->second.idx = idx;
        it->second.ghr = ghr;
        it->second.isConsumed = false;
    } else {
        output_record[branch_addr] = {res, idx, ghr, false};
    }

    return taken;
}

void MyPerceptronBP::update(ThreadID tid, Addr branch_addr, bool taken, void *bp_history,
bool squashed, const StaticInstPtr &inst, Addr corrTarget){
    int64_t target = taken ? 1 : -1;
    //std::cout <<  " update: " << branch_addr << " " << corrTarget << " " << taken <<std::endl;
    
    // search for the "previous" prediction & perceptron
    auto it = output_record.find(branch_addr);
    if(it == output_record.end()) return;
    if(it->second.isConsumed) return;
    Perceptron & perceptron = ptable[it->second.idx];
    perceptron.train(target, it->second.ghr, threshold, it->second.output);
    it->second.isConsumed = true;

    // update the ghr
    ghr <<= 1;
    if(taken)
        ghr |= 1;
}

void MyPerceptronBP::uncondBranch(ThreadID tid, Addr pc, void *&bp_history){
    //std::cout << "ucb:" << pc << std::endl; 
}
void MyPerceptronBP::btbUpdate(ThreadID tid, Addr branch_addr, void *&bp_history){}
void MyPerceptronBP::squash(ThreadID tid, void * bp_history){}
}
}