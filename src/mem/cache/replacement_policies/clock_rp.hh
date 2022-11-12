#ifndef __MEM_CACHE_REPLACEMENT_POLICIES_CLOCK_RP_HH__
#define __MEM_CACHE_REPLACEMENT_POLICIES_CLOCK_RP_HH__

#include "base/types.hh"
#include "mem/cache/replacement_policies/base.hh"

namespace gem5 {

struct CLOCKRPParams;

GEM5_DEPRECATED_NAMESPACE(ReplacementPolicy, replacement_policy);
namespace replacement_policy {

class CLOCK : public Base
{
protected:
    struct CLOCKReplData : ReplacementData
    {
        bool reference;
        bool valid;
        bool pointer_is_here;

        CLOCKReplData()
        : reference(false), valid(false), pointer_is_here(false)
        {}
    };

public:
    typedef CLOCKRPParams Params;
    CLOCK(const Params &p);
    ~CLOCK() = default;

    void invalidate(const std::shared_ptr<ReplacementData>& replacement_data)
                                                                    override;
    void touch(const std::shared_ptr<ReplacementData>& replacement_data) const
                                                                     override;
    void reset(const std::shared_ptr<ReplacementData>& replacement_data) const
                                                                     override;
    ReplaceableEntry* getVictim(const ReplacementCandidates& candidates) const
                                                                     override;
    std::shared_ptr<ReplacementData> instantiateEntry() override;
};

} // namespace replacement_policy


} // namespace gem5

#endif // CLOCK_RP_HH__
