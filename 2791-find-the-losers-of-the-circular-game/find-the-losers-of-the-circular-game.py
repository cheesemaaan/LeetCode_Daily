class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        while True:
            cur_loc = 1
            cnt = 0
            visted =set([cur_loc])
            answer = set()
            while True:
                cnt +=1
                cur_loc = (cur_loc +(cnt*k)) %n 
                if cur_loc ==0:
                    cur_loc = n
                
                if cur_loc not in visted:
                    visted.add(cur_loc)
                else:
                    break
            for i in range(1,n+1):
                if i not in visted:
                    answer.add(i)
            return list(sorted(answer))