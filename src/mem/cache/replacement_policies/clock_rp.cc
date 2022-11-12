#include "mem/cache/replacement_policies/clock_rp.hh"

#include <cassert>
#include <memory>

#include "base/random.hh"
#include "params/CLOCKRP.hh"

namespace gem5{
GEM5_DEPRECATED_NAMESPACE(ReplacementPolicy, replacement_policy);
namespace replacement_policy{
    CLOCK::CLOCK(const Params &p)
    : Base(p){}

    void
    CLOCK::invalidate(const std::shared_ptr<ReplacementData> & replacement_data){
        std::static_pointer_cast<CLOCKReplData>(
            replacement_data)->valid = false;
    }

    void
    CLOCK::touch(const std::shared_ptr<ReplacementData> & replacement_data) const{
        std::static_pointer_cast<CLOCKReplData>(
            replacement_data)->reference = true;
    }

    void
    CLOCK::reset(const std::shared_ptr<ReplacementData> & replacement_data) const {
        std::static_pointer_cast<CLOCKReplData>(
            replacement_data)->valid = true;
        std::static_pointer_cast<CLOCKReplData>(
            replacement_data)->reference = true;
    }

    ReplaceableEntry *
    CLOCK::getVictim(const ReplacementCandidates& candidates) const{
        assert(candidates.size() > 0);

        int cur_pos = 0;
        ReplaceableEntry *victim;

        // search for the clock pointer
        for (const auto & candidate : candidates){
            std::shared_ptr<CLOCKReplData> candidate_replacement_data =
                std::static_pointer_cast<CLOCKReplData>(candidate->replacementData);
            if (candidate_replacement_data->pointer_is_here){
                break;
            }
            cur_pos += 1;
        }
        // this script block initializes the logical "clock" associated with the candidates
        if (cur_pos >= candidates.size()){
            cur_pos = 0;
        }

        // "hide" the clock pointer
        std::static_pointer_cast<CLOCKReplData>(
            candidates[cur_pos]->replacementData)
            ->pointer_is_here = false;

        // move the clock pointer
        while (1){
            std::shared_ptr<CLOCKReplData> candidate_replacement_data =
                std::static_pointer_cast<CLOCKReplData> (
                    candidates[cur_pos]->replacementData);
            if (candidate_replacement_data->valid == false) {
                victim = candidates[cur_pos];
                break;
            } else if (candidate_replacement_data->reference == false) {
                victim = candidates[cur_pos];
                break;
            } else if (candidate_replacement_data->reference) {
                candidate_replacement_data->reference = false;
            }
            cur_pos = (cur_pos + 1) % candidates.size();
        }
        // set the clock pointer
        std::static_pointer_cast<CLOCKReplData>(
            candidates[(cur_pos + 1) % candidates.size()]->replacementData)
            ->pointer_is_here = true;
        return victim;
    }

    std::shared_ptr<ReplacementData>
    CLOCK::instantiateEntry(){
        return std::shared_ptr<ReplacementData> (new CLOCKReplData());
    }
}

}
