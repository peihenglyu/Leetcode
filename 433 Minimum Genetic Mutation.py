class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        def dif(str_1, str_2):
            sum = 0
            for i in range(len(str_1)):
                if str_1[i] != str_2[i]:
                    sum+=1
            return sum
        
        visited = {startGene:0}
        cur_queue = [startGene]
        while len(cur_queue):
            cur_gene = cur_queue.pop(0)
            for gene in bank:
                if dif(cur_gene, gene) == 1:
                    if gene not in visited:
                        visited[gene] = visited[cur_gene] + 1
                        cur_queue.append(gene)
                        if gene == endGene:
                            return visited[gene]
            
        return -1

startGene = "AACCTTGG"
endGene = "AATTCCGG"
bank = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]
obj = Solution()
print(obj.minMutation(startGene,endGene,bank))