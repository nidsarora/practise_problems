class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            smaller = nums2
            larger = nums1
        else:
            smaller = nums1
            larger = nums2
        map1 = self.create_map(smaller)
        map2 = self.create_map(larger)
        result_keys = []
        result_vals_smaller = []
        result_vals_larger = []
        for key in map1.keys():
            if key in map2.keys():
                result_keys.append(key)
                result_vals_smaller.append(map1[key])
                result_vals_larger.append(map2[key])
        list_vals = self.get_smallest_arr(result_vals_smaller, result_vals_larger)
        result = self.gen_array_from_2_arrays(result_keys, list_vals)
        return result

    def create_map(self, nums):
        map1 = {}
        for i in range(0, len(nums)):
            if nums[i] not in map1.keys():
                map1[nums[i]] = 1
            else:
                map1[nums[i]] = map1[nums[i]] + 1
        return map1

    def get_smallest_arr(self, list1, list2):
        list3 = []
        for i in range(0, len(list1)):
            if list1[i] < list2[i]:
                list3.append(list1[i])
            else:
                list3.append(list2[i])
        return list3

    def gen_array_from_2_arrays(self, keys, values):
        result = []
        for key, value in zip(keys, values):
            result += value * [key]
        return result


if __name__ == '__main__':
    sol = Solution()
    two_sum = sol.intersect([4, 9, 5], [9, 4, 9, 8, 4])
    print(two_sum)
