class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        count_dict = defaultdict(int)
        for value,weight in items1+items2:
            count_dict[value] +=weight
        print(count_dict)
        
        return [[key, value] for key, value in sorted(count_dict.items())]
