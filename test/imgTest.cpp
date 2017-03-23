#include <iostream>
#include <string>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

void testImageShow(const string &img_name);

int main(int argc, char** argv) {
    testImageShow(argv[1]);
    return 0;
}

void testImageShow(const string &img_name) {
    Mat img = imread(img_name);
    if (!img.data) {
        cerr << "read image " << img_name << " error" << endl;
        return;
    }
}
