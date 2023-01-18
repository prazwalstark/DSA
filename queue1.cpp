#include<iostream>
using namespace std;
#define size 10
class Queue{
    private:
    int* arr;
    int front;
    int rear;
    public:
    Queue()
    {
        arr = new int[size];
        front =-1;
        rear =-1;
    }
    bool c_overflow(){
        if(rear==size-1){
            cout<<"Stack is Full!";
            return false;
        }
        return true;
    }
    bool c_underflow(){
        if(front>rear || front==-1)
        {
            cout<<"Stack is Empty!";
            return false;
        }
        return true;
    }
    void queue(int x)
    {
        if(c_overflow())
        {
            if(front==-1)
            {
                front=0;
            }
        rear++;
        arr[rear]=x;
        }
    }
    int dequeue()
    {
        if(c_underflow())
            return arr[front++];  
    return 0;
    }
    int peek(){
        return arr[front];
    }
};
int main()
{
    Queue Q;
    Q.queue(10);
    Q.queue(11);
    Q.queue(25);
    Q.queue(55);
    cout<<Q.dequeue()<<endl;
    cout<<Q.peek()<<endl<<endl;
    return 0;
}