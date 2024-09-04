class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        answer = False
        # s1_temp_list1 =list(s1)
        # s1_temp_list1[0],s1_temp_list1[2] = s1_temp_list1[2],s1_temp_list1[0]
        # s1_temp1 = ''.join(s1_temp_list1)
        
        # s1_temp_list2 =list(s1)
        # s1_temp_list2[1],s1_temp_list2[3] = s1_temp_list2[3],s1_temp_list2[1]
        # s1_temp2 = ''.join(s1_temp_list2)
        
        # s1_temp_list3 =list(s1_temp_list1)
        # s1_temp_list3[1],s1_temp_list3[3] = s1_temp_list3[3],s1_temp_list3[1]
        # s1_temp3 = ''.join(s1_temp_list3)
        new_str_1 = s1[2] + s1[1] + s1[0] + s1[3]
        new_str_2 = s1[0] + s1[3] + s1[2] + s1[1]
        new_str_3 = s1[2] + s1[3] + s1[0] + s1[1]
        if s1 == s2 or new_str_1 == s2 or new_str_2 == s2 or new_str_3 == s2 :
            answer =True 
        return answer