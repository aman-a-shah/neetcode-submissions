class MedianFinder:

    nums: list[int]

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums += [num]

    def findMedian(self) -> float:
        median_list = sorted(self.nums)

        if len(median_list) == 0:
            return 0

        if len(median_list) % 2 == 1:
            med_index = len(median_list) // 2
            return median_list[med_index]
        med_index = len(median_list)//2 - 1
        return (median_list[med_index] + median_list[med_index+1]) / 2