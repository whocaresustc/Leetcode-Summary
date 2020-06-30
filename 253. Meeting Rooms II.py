# O(NlgN) O(N)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetings = []
        min_rooms = temp = 0
        for interval in intervals:
            meetings.append((interval[0], 1))
            meetings.append((interval[1], -1))

        for _, delta in sorted(meetings):
            temp += delta
            min_rooms = max(min_rooms, temp)

        return min_rooms