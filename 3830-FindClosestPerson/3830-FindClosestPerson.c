// Last updated: 3/31/2026, 9:28:29 PM
#include <stdlib.h> 
int findClosest(int x, int y, int z) {
    return ((abs(x-z)>abs(y-z))?2:(abs(x-z)==abs(y-z)?0:1));
}