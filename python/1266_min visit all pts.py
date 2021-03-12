def minTimeToVisitAllPoints(points):
    len_points = len(points)
    counter =0

    for i in range(0,len_points-1):
        x_axis_gap = abs(points[i+1][0] - points[i][0])
        y_axis_gap = abs(points[i+1][1] - points[i][1])
        counter += max(x_axis_gap, y_axis_gap)
    return counter


def main():
    points= [[3,2],[-2,2]]
    print(minTimeToVisitAllPoints(points))

main()
