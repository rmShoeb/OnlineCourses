#include<iostream>
using namespace std;

class Rectangle
{
private:
    int length;
    int breadth;

public:
    Rectangle()
    {
        this->length = this->breadth = 1;
    }
    Rectangle(int length, int breadth)
    {
        this->length = length;
        this->breadth = breadth;
    }
    ~Rectangle(){};

    int getLength()
    {
        return this->length;
    }

    int area(void)
    {
        return this->length*this->breadth;
    }

    void changeLength(int length)
    {
        this->length = length;
    }
};


int main(int argc, char const *argv[])
{
    // Rectangle r = new Rectangle(10, 5);
    Rectangle r(10, 5);

    cout << r.area() << endl;
    r.changeLength(15);
    cout << r.getLength() << endl;

    return 0;
}
