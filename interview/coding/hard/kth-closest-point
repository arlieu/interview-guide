/*Given a set of 2D points, find the kth closest point to the origin.*/


#include <iostream>
#include <cmath>
#include <queue>
#include <vector>

using namespace std;


struct Point {
    double x, y;
    Point(double a, double b) {
        x = a;
        y = b;
    }
};


double distance(Point a, Point b) {
    return sqrt(pow(a.x-b.x, 2) + pow(a.y-b.y, 2));
}


typedef bool (*comp)(Point, Point);
bool compare(Point a, Point b) {
    return distance(a, Point(0.0, 0.0)) < distance(b, Point(0.0, 0.0));
}


Point kthPoint(Point origin, vector<Point> array, int k) {
    priority_queue<Point, vector<Point>, comp > pq;
    for(vector<Point>::iterator it = array.begin(); it != array.end(); it++) {
        if (pq.size() < k || distance(pq.top(), origin) > distance(*it, origin)) {
            pq.pop();
            pq.push(*it);
        }
    }

    return pq.top();
}


int main() {
    Point p1 = (3.1, 2.2);
    Point p2 = (0.5, 2.0);
    Point p3 = (8.8, 1.8);
    Point p4 = (8.9, 6.4);
    Point p5 = (3.1, 7.3);
    Point p6 = (4.2, 1.2);
    Point p7 = (4.1, 2.3);

    vector<Point> test;
    test.push(p1);
    test.push(p2);
    test.push(p3);
    test.push(p4);
    test.push(p5);
    test.push(p6);
    test.push(p7);

    res = kthPoint(Point(0.0, 0.0), test, 2);

    cout << res.x << ", " << res.y << endl;

    return 0;
}