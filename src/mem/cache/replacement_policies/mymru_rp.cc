#include "mem/cache/replacement_policies/mymru_rp.hh"

#include <cassert>
#include <memory>

#include "params/MyMRURP.hh"
#include "sim/cur_tick.hh"

namespace gem5
{

GEM5_DEPRECATED_NAMESPACE(ReplacementPolicy, replacement_policy);
namespace replacement_policy
{

MyMRU::MyMRU(const Params &p)
  : Base(p)
{
}

void
MyMRU::invalidate(const std::shared_ptr<ReplacementData>& replacement_data)
{
    // Reset last touch timestamp
    std::static_pointer_cast<MyMRUReplData>(
        replacement_data)->lastTouchTick = Tick(0);
}

void
MyMRU::touch(const std::shared_ptr<ReplacementData>& replacement_data) const
{
    // Update last touch timestamp
    std::static_pointer_cast<MyMRUReplData>(
        replacement_data)->lastTouchTick = curTick();
}

void
MyMRU::reset(const std::shared_ptr<ReplacementData>& replacement_data) const
{
    // Set last touch timestamp
    std::static_pointer_cast<MyMRUReplData>(
        replacement_data)->lastTouchTick = curTick();
}

ReplaceableEntry*
MyMRU::getVictim(const ReplacementCandidates& candidates) const
{
    // There must be at least one replacement candidate
    assert(candidates.size() > 0);

    // Visit all candidates to find victim
    ReplaceableEntry* victim = candidates[0];
    for (const auto& candidate : candidates) {
        std::shared_ptr<MyMRUReplData> candidate_replacement_data =
            std::static_pointer_cast<MyMRUReplData>(candidate->replacementData);

        // Stop searching entry if a cache line that doesn't warm up is found.
        if (candidate_replacement_data->lastTouchTick == 0) {
            victim = candidate;
            break;
        } else if (candidate_replacement_data->lastTouchTick >
                std::static_pointer_cast<MyMRUReplData>(
                    victim->replacementData)->lastTouchTick) {
            victim = candidate;
        }
    }

    return victim;
}

std::shared_ptr<ReplacementData>
MyMRU::instantiateEntry()
{
    return std::shared_ptr<ReplacementData>(new MyMRUReplData());
}

} // namespace replacement_policy
} // namespace gem5
