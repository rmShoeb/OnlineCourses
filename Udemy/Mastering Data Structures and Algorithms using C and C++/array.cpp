#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;

class Array
{
private:
    int *p;
    int length;
    int size;
public:
    Array(int size)
    {
        this->size = size;
        this->p = new int[size];
        this->length = 0;
        cout << "creating" << endl;
    }
    ~Array()
    {
        delete []p;
        cout << "destroying" << endl;
    }

    void append(void)
    {
        if(this->length < this->size)
        {
            cout << "Enter element: ";
            cin >> this->p[this->length];
            this->length++;
        }
        else
            cout << "No more space." << endl;
    }
    void insert(int position, int data)
    {
        if(position < this->length)
        {
            for(int iter= this->length-1; iter==position; iter--)
                this->p[iter+1] = this->p[iter];
            this->p[position] = data;
            this->length++;
        }
        else if(position == this->length)
        {
            this->p[position] = data;
            this->length++;
        }
        else
            cout << "Invalid position." << endl;
    }

    void del(void)
    {
        if(this->length > 0)
            this->length--;
        else
            cout << "Array is empty." << endl;
    }
    void del(int position)
    {
        if(position < this->length)
        {
            this->length--;
            for(int iter=position; iter < this->length; iter++)
                this->p[iter] = this->p[iter+1];
        }
        else
            cout << "Invalid position." << endl;
    }

    int len(void){return this->length;}

    void sortArray(void)
    {
        sort(this->p, this->p +this->length -1);
    }

    void print(void)
    {
        if(this->length>0)
        {
            for(int iter=0; iter < this->length; iter++)
                cout << this->p[iter] << " ";
            cout << endl;
        }
        else
            cout << "Empty" << endl;
    }

    bool linearSearch(int x)
    {
        for(int iter=0; iter < this->length; iter++)
        {
            if(this->p[iter] == x)
                return true;
        }
        return false;
    }

    void increaseCapacity(int size)
    {
        int *q;

        q = new int[this->length + size];
        for(int iter=0; iter<this->length; iter++)
            q[iter] = p[iter];
        p = q;
        q = 0;
        this->length += size;
        delete q;
    }

    int get(int index){return this->p[index];}
    void set(int index, int data){this->p[index] = data;}

    double avg(void)
    {
        int temp = 0;
        for(int iter=0; iter<this->length; iter++)
            temp += this->p[iter];
        
        return temp/(double)this->length;
    }

    int max(void)
    {
        int max = this->p[0];
        for(int iter=1; iter<this->length; iter++)
        {
            if(this->p[iter] > max)
                max = this->p[iter];
        }

        return max;
    }

    int min(void)
    {
        int min = this->p[0];
        for(int iter=1; iter<this->length; iter++)
        {
            if(this->p[iter] < min)
                min = this->p[iter];
        }

        return min;
    }

    void swap(int& a, int& b)
    {
        int temp;

        temp = a;
        a = b;
        b = temp;
    }

    void reverseArray(void)
    {
        int i = 0;
        int j = this->length-1;

        while(i<j)
        {
            swap(this->p[i], this->p[j]);
            i++;
            j--;
        }
    }
    void shiftArray(void);
};


int main(int argc, char const *argv[])
{
    int size;
    char choice;
    int data;

    cout << "Enter initial size of array: ";
    cin >> size;
    Array a(size);

    while(1)
    {
        cout << "1. Insert element\n" <<
                "2. Insert element at a specific position\n" <<
                "3. Delete element\n" <<
                "4. Delete element from a specific position\n" <<
                "5. Print array\n" <<
                "6. Find length\n" <<
                "7. Sort the array\n" <<
                "8. Search element (lenear search)\n" <<
                "9. Reverse the elements\n" <<
                "Press 'q/Q' to Quit" << endl;
        cin >> choice;

        if(choice == 'q' || choice == 'Q')
            break;

        switch(choice)
        {
            case '1':
                a.append();
                break;
            
            case '2':
                cout << "Enter position: ";
                cin >> size;
                cout << "Enter element: ";
                cin >> data;
                a.insert(size, data);

                break;

            case '3':
                a.del();
                break;

            case '4':
                cout << "Enter position: ";
                cin >> size;
                a.del(size);
                break;
            
            case '5':
                a.print();
                break;
            
            case '6':
                cout << a.len() << endl;
                break;
            
            case '7':
                a.sortArray();
                a.print();
                break;
            
            case '8':
                cout << "Enter element: ";
                cin >> data;
                if(a.linearSearch(data))
                    cout << "Found" << endl;
                else
                    cout << "Not found" << endl;
                break;
            
            case '9':
                a.reverseArray();
                a.print();
                break;

            default:
                cout << "Wrong input" << endl;
                break;
        }
    }

    return 0;
}
