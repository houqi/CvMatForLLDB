#include <vector>
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

const int N = 5;

void test1Channels();
void test2Channels();
void test3Channels();
void test4Channels();
void testROI();

int main(int argc, char** argv) {
    test1Channels();
    test2Channels();
    test3Channels();
    test4Channels();
    testROI();
    return 0;
}

void test1Channels() {
    Mat arr_32f(N, N, CV_32F);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            arr_32f.at<float>(i, j) = i * (j + 1);
        }
    }

    Mat arr_64f;
    arr_32f.convertTo(arr_64f, CV_64F);

    Mat arr_32s;
    arr_32f.convertTo(arr_32s, CV_32S);

    Mat arr_8u;
    arr_32f.convertTo(arr_8u, CV_8U);

    Mat arr_8s;
    arr_32f.convertTo(arr_8s, CV_8S);

    Mat arr_16u;
    arr_32f.convertTo(arr_16u, CV_16U);

    Mat arr_16s;
    arr_32f.convertTo(arr_16s, CV_16S);
}

void test2Channels() {
    Mat arr_32fc1(N, N, CV_32F);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            arr_32fc1.at<float>(i, j) = i * (j + 1);
        }
    }
    vector<Mat> arrs(2);
    arrs[0] = arr_32fc1;
    arrs[1] = arr_32fc1 + 1;

    Mat arr_32f;
    merge(arrs, arr_32f);


    Mat arr_64f;
    arr_32f.convertTo(arr_64f, CV_64FC2);

    Mat arr_32s;
    arr_32f.convertTo(arr_32s, CV_32SC2);

    Mat arr_8u;
    arr_32f.convertTo(arr_8u, CV_8UC2);

    Mat arr_8s;
    arr_32f.convertTo(arr_8s, CV_8SC2);

    Mat arr_16u;
    arr_32f.convertTo(arr_16u, CV_16UC2);

    Mat arr_16s;
    arr_32f.convertTo(arr_16s, CV_16SC2);
}

void test3Channels() {
    Mat arr_32fc1(N, N, CV_32F);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            arr_32fc1.at<float>(i, j) = i * (j + 1);
        }
    }
    vector<Mat> arrs(3);
    arrs[0] = arr_32fc1;
    arrs[1] = arr_32fc1 + 1;
    arrs[2] = arr_32fc1 + 2;

    Mat arr_32f;
    merge(arrs, arr_32f);

    Mat arr_64f;
    arr_32f.convertTo(arr_64f, CV_64FC3);

    Mat arr_32s;
    arr_32f.convertTo(arr_32s, CV_32SC3);

    Mat arr_8u;
    arr_32f.convertTo(arr_8u, CV_8UC3);

    Mat arr_8s;
    arr_32f.convertTo(arr_8s, CV_8SC3);

    Mat arr_16u;
    arr_32f.convertTo(arr_16u, CV_16UC3);

    Mat arr_16s;
    arr_32f.convertTo(arr_16s, CV_16SC3);
}

void test4Channels() {
    Mat arr_32fc1(N, N, CV_32F);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            arr_32fc1.at<float>(i, j) = i * (j + 1);
        }
    }
    vector<Mat> arrs(4);
    arrs[0] = arr_32fc1;
    arrs[1] = arr_32fc1 + 1;
    arrs[2] = arr_32fc1 + 2;
    arrs[3] = arr_32fc1 + 3;

    Mat arr_32f;
    merge(arrs, arr_32f);

    Mat arr_64f;
    arr_32f.convertTo(arr_64f, CV_64FC4);

    Mat arr_32s;
    arr_32f.convertTo(arr_32s, CV_32SC4);

    Mat arr_8u;
    arr_32f.convertTo(arr_8u, CV_8UC4);

    Mat arr_8s;
    arr_32f.convertTo(arr_8s, CV_8SC4);

    Mat arr_16u;
    arr_32f.convertTo(arr_16u, CV_16UC4);

    Mat arr_16s;
    arr_32f.convertTo(arr_16s, CV_16SC4);
}

void testROI() {
    Mat arr_32fc1(N, N, CV_32F);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            arr_32fc1.at<float>(i, j) = i * (j + 1);
        }
    }
    vector<Mat> arrs(3);
    arrs[0] = arr_32fc1;
    arrs[1] = arr_32fc1 + 1;
    arrs[2] = arr_32fc1 + 2;

    Mat arr_32f;
    merge(arrs, arr_32f);
    Mat arr_32f_T = arr_32f.t();

    Mat arr_32f_part1 = arr_32f(Range(0, 2), Range(1, 4));
    Mat arr_32f_part2 = arr_32f(Range(1, 3), Range(1, 4));
    Mat arr_32f_part3 = arr_32f.colRange(1, 4);
    Mat arr_32f_part4 = arr_32f.rowRange(1, 4);
}
