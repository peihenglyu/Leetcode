class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """
        cand = 1
        k = k
        re = goal - n
        # 0 - k
        for i in range(k):
            cand *= (n-i)
        
        free_choice = goal - n
        non_present = n - k

        dict_song = {}
        def solver(i, non_present, freed):
            if i == goal-1:
                if non_present:
                    return 0
                else:
                    return 1
            
            if i+1 in dict_song and non_present-1 in dict_song[i+1]:
                choice_1 = dict_song[i+1][non_present-1]
            else:
                choice_1 = non_present * solver(i+1, non_present-1)
                if i in dict_song:
                    dict_song[i][non_present] = choice_1
                else:
                    dict_song[i] = {}
                    dict_song[i][non_present] = choice_1

            if i+1 in dict_song and non_present in dict_song[i+1]:
                choice_2 = dict_song[i+1][non_present]
            else:
                choice_2 = solver(i+1, non_present)
                if i in dict_song:
                    dict_song[i][non_present] = choice_2
                else:
                    dict_song[i] = {}
                    dict_song[i][non_present] = choice_2
            
            return choice_1 + choice_2
        
        cand += solver(k, non_present)
  
        return cand % (10**9 + 7)
    
obj = Solution()
print(obj.numMusicPlaylists(3,3,1))
print(obj.numMusicPlaylists(2,3,0))
print(obj.numMusicPlaylists(2,3,1))
    
# ini = [6]
# count_list = [[0]*6 for i in range(6)]
# for i in range(5):
#     for j in range(6):
#         count_list[i][j] = ini.count(j+1)
#     temp = []
#     for num in ini:
#         temp.append(num)
#         temp.append(num-1)
#     ini = temp
#     print(ini)
    
# for i in range(len(count_list)):
#     print(count_list[i])
