class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if math.sqrt(num).is_integer():
            return True
        else:
            return False