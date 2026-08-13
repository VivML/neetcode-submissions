class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''freq=[]
        unique_ele=list(set(nums)) # [1,2,3] as per example

        for num in unique_ele:
            freq.append((num,nums.count(num)))
            #[(1, 3), (2, 2), (3, 1)]
        freq.sort(key =lambda x : x[1], reverse=True) # sort chesina
            #[(1, 3), (2, 2), (3, 1)] already x[1] is sorted
        return [freq[i][0] for i in range(k)]     
        '''
        # with using hashset
        freq={}

        for num in nums:
            freq[num]=freq.get(num,0)+1
        sorted_ele= sorted(freq.items(),key=lambda x:x[1],reverse=True)
        return [sorted_ele[i][0] for i in range(k)]
        
