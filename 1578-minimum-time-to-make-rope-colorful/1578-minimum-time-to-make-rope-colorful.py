class Solution:
	def minCost(self, colors: str, time: List[int]) -> int:
		res = 0
		prev = ''
		min_time = 0

		for i,color in enumerate(colors):
			if color == prev:
				res += min(time[i], min_time)
				min_time = max(time[i], min_time)
			else:
				min_time = time[i]
			prev = color
		return res