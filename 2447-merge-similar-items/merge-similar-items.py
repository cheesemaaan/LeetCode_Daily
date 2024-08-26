class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        count_dict = {}
        for value,weight in items1:
            
            if value not in count_dict:
                count_dict[value] = 0
                count_dict[value] += weight
            else:
                count_dict[value] +=weight

        for value,weight in items2:

            if value not in count_dict:
                count_dict[value] = 0
                count_dict[value] += weight
            else:
                count_dict[value] +=weight
        
        return [[key, value] for key, value in sorted(count_dict.items())]
