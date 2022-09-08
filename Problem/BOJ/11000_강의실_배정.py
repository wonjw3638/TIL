import heapq, sys
input = sys.stdin.readline

N = int(input())
classroom = list()

for _ in range(N):
    heapq.heappush(classroom, list(map(int, input().split())))

classroom.sort()

timetable = list()

heapq.heappush(timetable, (heapq.heappop(classroom))[1])

for _ in range(N-1):
    start, end = heapq.heappop(classroom)
    if start >= timetable[0]:
        heapq.heappop(timetable)
        heapq.heappush(timetable, end)
    else:
        heapq.heappush(timetable, end)

print(len(timetable))