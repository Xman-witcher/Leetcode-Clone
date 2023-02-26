def twosum(nums, target):
        dicts={}
        for i in range(len(nums)):
            if target-nums[i] in dicts:
                return [dicts[target-nums[i]],i]               
            dicts[nums[i]]=i