class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx > 0 and ty > 0:
            if tx == sx and ty == sy:
                return True
            if tx > ty:
                if (tx-sx) / ty > 1:
                    tx = sx + (tx-sx) % ty
                else:
                    tx = tx - ty
            else:
                if (ty-sy) / tx > 1:
                    ty = sy + (ty-sy) % tx
                else:
                    ty = ty - tx
        
        return False
        
    
obj = Solution()
print(obj.reachingPoints(1,1,3,5))
print(obj.reachingPoints(1,1,2,2))
print(obj.reachingPoints(1,1,1,1))