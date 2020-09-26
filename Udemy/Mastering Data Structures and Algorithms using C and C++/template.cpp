#include<iostream>
using namespace std;

template<class T>
class Arithmatic
{
private:
    T a;
    T b;

public:
    Arithmatic(T a, T b)
    {
        this->a = a;
        this->b = b;
    }
    ~Arithmatic(){}

    T add()
    {
        return a+b;
    }

    T subtract()
    {
        return a-b;
    }
};



int main(int argc, char const *argv[])
{
    Arithmatic<int> x(10,5);
    Arithmatic<float> y(10.2, 5.9);

    cout << x.add() << " " << x.subtract() << endl;
    cout << y.add() << " " << y.subtract() << endl;

    return 0;
}
