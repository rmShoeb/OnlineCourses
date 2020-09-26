#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

class Node
{
public:
    int data;
    Node *next;

    Node(int data)
    {
        this->data = data;
        this->next = NULL;
    }
};


class LinkedList
{
private:
    Node *head;
    int length;
public:
    LinkedList()
    {
        this->head = NULL;
        this->length = 0;
    }
    LinkedList(int data)
    {
        Node *temp = new Node(data);

        this->head = temp;
        this->length = 1;
    }
    // ~LinkedList();

    int len(void){return this->length;}

    void insert(int data)
    {
        if(this->head != NULL)
        {
            Node *last;
            Node *temp = new Node(data);

            last = this->head;
            while(last->next != NULL)
            {
                last = last->next;
            }
            last->next = temp;
            this->length++;
        }
        else
        {
            Node *last = new Node(data);
            this->head = last;
            this->length = 1;
        }
    }
    void insert(int data, int position)
    {
        if(position > this->len())
        {
            cout << "Invalid position" << endl;
        }
        else
        {
            // x 
        }
    }

    void print(void)
    {
        if(this->len() > 0)
        {
            Node *temp;
            temp = this->head;

            do
            {
                cout << temp->data << " ";
                temp = temp->next;
            } while(temp != NULL);
            cout << endl;
        }
        else
        {
            cout << "List is empty" << endl;
        }
    }
};



int main(int argc, char const *argv[])
{
    LinkedList list;
    char choice;
    int data;
    int position;

    while(true)
    {
        cout << "1. Enter data\n"
             << "2. Enter data in a specific position\n"
             << "3. Show data\n"
             << "Press 'q/Q' to quit" << endl;
        cin >> choice;

        if(choice=='q' || choice=='Q')
            break;
        
        switch (choice)
        {
        case '1':
            cout << "Enter data: ";
            cin >> data;
            list.insert(data);
            break;
        
        case '2':
            cout << "Enter data: ";
            cin >> data;
            cout << "Enter position: ";
            cin >> position;
            list.insert(data, position);
            break;
        
        case '3':
            list.print();
            break;
        
        default:
            cout << "wrong choice" << endl;
            break;
        }
    }


    return 0;
}
