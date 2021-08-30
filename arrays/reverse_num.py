class Solution:
    def reverse_num(self, number):
        nums = ""
        nums = nums + (self.get_div(number))
        return int(nums)

    def get_div(self, num):
        print("num is ", num)
        if num // 10 != 0:
            return str(num % 10) + str(self.get_div(num // 10))
        else:
            return str(num % 10)


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse_num(123456789))
