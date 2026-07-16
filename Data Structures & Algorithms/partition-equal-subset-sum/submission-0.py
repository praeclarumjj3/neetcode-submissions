class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        possible_sums = {0}

        for num in nums:
            new_sums = set()

            for old_sum in possible_sums:
                new_sum = old_sum + num

                if new_sum == target:
                    return True

                if new_sum < target:
                    new_sums.add(new_sum)

            possible_sums.update(new_sums)

        return target in possible_sums