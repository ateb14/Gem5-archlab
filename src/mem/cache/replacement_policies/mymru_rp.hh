#ifndef __MEM_CACHE_REPLACEMENT_POLICIES_MYMRU_RP_HH__
#define __MEM_CACHE_REPLACEMENT_POLICIES_MYMRU_RP_HH__

#include "base/types.hh"
#include "mem/cache/replacement_policies/base.hh"

namespace gem5
{

struct MyMRURPParams;

GEM5_DEPRECATED_NAMESPACE(ReplacementPolicy, replacement_policy);
namespace replacement_policy
{

class MyMRU : public Base
{
  protected:
    /** MRU-specific implementation of replacement data. */
    struct MyMRUReplData : ReplacementData
    {
        /** Tick on which the entry was last touched. */
        Tick lastTouchTick;

        /**
         * Default constructor. Invalidate data.
         */
        MyMRUReplData() : lastTouchTick(0) {}
    };

  public:
    typedef MyMRURPParams Params;
    MyMRU(const Params &p);
    ~MyMRU() = default;

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

#endif // __MEM_CACHE_REPLACEMENT_POLICIES_MyMRU_RP_HH__
