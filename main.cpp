#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>
#include <string>

using namespace std;

void filter(cv::Mat image, cv::Mat &result);
void display(cv::Mat &image);
void edge_mask(cv::Mat image, cv::Mat &edges);
int counter = 0;

int main()
{
    cv::Mat image;
    image = cv::imread("test1.jpg", CV_LOAD_IMAGE_COLOR);

    if(!image.data)
    {
        cout << "Error: Could not find or open image." << endl;
        return -1;
    }

    cv::Mat layer2;
    cv::Mat edges;
    cv::Mat layer3 = cv::Mat::zeros(image.rows, image.cols, image.type());

    filter(image, layer2);
    edge_mask(layer2, edges);

    layer3.copyTo(layer2, edges);

    display(layer2);

    cv::waitKey(0);
    return 0;
}


void filter(cv::Mat image, cv::Mat &result)
{
    cv::bilateralFilter(image, result, 10, 90, 10);
}


int threshold1 = 15;

void edge_mask(cv::Mat image, cv::Mat &edges)
{
    cv::Mat gray;
    cv::cvtColor(image, gray, CV_BGR2GRAY);
    cv::medianBlur(gray, image, 5);
    cv::Canny(gray, edges, threshold1, 3 * threshold1);
}


void display(cv::Mat &image)
{
    string name = "image" + to_string(counter);
    counter++;
    cv::namedWindow(name.c_str() , CV_WINDOW_NORMAL);
    cv::imshow(name.c_str(), image);
}
