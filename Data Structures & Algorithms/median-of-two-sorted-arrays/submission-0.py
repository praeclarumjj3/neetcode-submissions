class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # Binary search the smaller array
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        total = m + n
        half = total // 2

        low, high = 0, m

        while True:
            i = (low + high) // 2   # partition in A
            j = half - i            # partition in B

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            # correct partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                high = i - 1
            else:
                low = i + 1