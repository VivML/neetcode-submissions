class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group={}
        for word in strs:
            # sorted_word=sorted(word)
            # ikkada sorted words anni osthai but join cheyyali kadha sort ayinavi anni appudu kalisi osthai anni as per question
            # ippudu manam join chesukovali
            sorted_word="".join(sorted(word))

            if sorted_word not in group: 
                group[sorted_word]=[]

            group[sorted_word].append(word)
            # print(group) chesthe manaki 
# {ant:[tan,nat],abt:[bat],act:[eat,tea,ate]}
            # group.values()--> manaki group lo em unnai telisipothai
        return list(group.values())
        

        