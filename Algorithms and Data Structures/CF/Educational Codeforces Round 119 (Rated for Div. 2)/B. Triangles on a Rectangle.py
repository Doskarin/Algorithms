'''
A rectangle with its opposite corners in (0,0) and (w,h) and sides parallel to the axes is drawn on a plane.

You are given a list of lattice points such that each point lies on a side of a rectangle but not in its corner. Also, there are at least two points on every side of a rectangle.

Your task is to choose three points in such a way that:

exactly two of them belong to the same side of a rectangle;
the area of a triangle formed by them is maximum possible.
Print the doubled area of this triangle. It can be shown that the doubled area of any triangle formed by lattice points is always an integer.

Input
The first line contains a single integer t (1≤t≤104) — the number of testcases.

The first line of each testcase contains two integers w and h (3≤w,h≤106) — the coordinates of the corner of a rectangle.

The next two lines contain the description of the points on two horizontal sides. First, an integer k (2≤k≤2⋅105) — the number of points. Then, k integers x1<x2<⋯<xk (0<xi<w) — the x coordinates of the points in the ascending order. The y coordinate for the first line is 0 and for the second line is h.

The next two lines contain the description of the points on two vertical sides. First, an integer k (2≤k≤2⋅105) — the number of points. Then, k integers y1<y2<⋯<yk (0<yi<h) — the y coordinates of the points in the ascending order. The x coordinate for the first line is 0 and for the second line is w.

The total number of points on all sides in all testcases doesn't exceed 2⋅105.

Output
For each testcase print a single integer — the doubled maximum area of a triangle formed by such three points that exactly two of them belong to the same side.

Example
inputCopy
3
5 8
2 1 2
3 2 3 4
3 1 4 6
2 4 5
10 7
2 3 9
2 1 7
3 1 3 4
3 4 5 6
11 5
3 1 6 8
3 3 6 8
3 1 3 4
2 2 4
outputCopy
25
42
35
Note
The points in the first testcase of the example:

(1,0), (2,0);
(2,8), (3,8), (4,8);
(0,1), (0,4), (0,6);
(5,4), (5,5).
The largest triangle is formed by points (0,1), (0,6) and (5,4) — its area is 252. Thus, the doubled area is 25. Two points that are on the same side are: (0,1) and (0,6).


'''

t = int(input())

for _ in range(t):
    width, height = map(int, input().split())

    bottom_arr_x = list(map(int, input().split()))
    top_arr_x = list(map(int, input().split()))
    left_arr_y = list(map(int, input().split()))
    right_arr_y = list(map(int, input().split()))

    print(max((max(bottom_arr_x[1:]) - min(bottom_arr_x[1:]))*height,
     (max(top_arr_x[1:]) - min(top_arr_x[1:]))*height,
      (max(left_arr_y[1:]) - min(left_arr_y[1:])) * width,
      (max(right_arr_y[1:]) - min(right_arr_y[1:])) * width))