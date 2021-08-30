class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fibo(n)

    def fibo(self, num):
        if num > 2:
            return self.fibo(num - 2) + self.fibo(num - 1)
        else:
            return num


if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(39))
