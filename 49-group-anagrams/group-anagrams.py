
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        
        for s in strs:
            # 문자열을 정렬한 값을 키로 하여 그룹화
            sorted_str = "".join(sorted(s))
            temp[sorted_str].append(s)
        
        # 결과를 리스트로 반환
        return list(temp.values())