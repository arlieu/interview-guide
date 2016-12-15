/*Given the coordinates of the top left corner and bottom right corner of two rectangles, determine if the rectangles
overlap.*/


#include <iostream>
using namespace std;


struct Point {
    int x;
    int y;
};


bool overlap(Point l1, Point r1, Point l2, Point r2) {
    if (r2.y > l1.y || l2.y < r1.y) {
        return false;
    }

    else if (l1.x > r2.x || r1.x < l2.x) {
        return false;
    }

    return true;
}


int main() {
    return 0;
}