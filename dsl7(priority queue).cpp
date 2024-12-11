#include <iostream>
#include <list>
#include <stdexcept>  // for exception handling

using namespace std;

// Class template for the priority queue node
template <typename T>
class PriorityQueueNode {
public:
    T data;
    int priority;

    // Constructor
    PriorityQueueNode(T d, int p) : data(d), priority(p) {}

    // Overload the <= operator to compare priority
    bool operator <= (const PriorityQueueNode<T>& other) const {
        return priority <= other.priority;
    }
};

// Class template for Priority Queue
template <typename T>
class PriorityQueue {
private:
    list<PriorityQueueNode<T>> pqList;  // List to hold the priority queue items

public:
    // Function to insert an item into the priority queue
    void insert(T data, int priority) {
        PriorityQueueNode<T> newNode(data, priority);
        auto it = pqList.begin();

        // Find the correct position to insert (in descending priority order)
        while (it != pqList.end() && *it <= newNode) {
            ++it;
        }

        pqList.insert(it, newNode);  // Insert at the correct position
    }

    // Function to remove the highest priority item
    void remove() {
        if (!pqList.empty()) {
            pqList.pop_front();  // Remove the front item (highest priority)
        } else {
            cout << "Queue is empty!" << endl;
        }
    }

    // Function to display the queue
    void display() {
        if (pqList.empty()) {
            cout << "Queue is empty!" << endl;
            return;
        }

        for (const auto& node : pqList) {
            cout << "Data: " << node.data << ", Priority: " << node.priority << endl;
        }
    }

    // Function to get the highest priority item
    T getHighestPriority() {
        if (!pqList.empty()) {
            return pqList.front().data;
        } else {
            throw runtime_error("Queue is empty!");
        }
    }
};

void priorityQueueMenu() {
    PriorityQueue<string> pq;
    int choice, priority;
    string data;

    do {
        cout << "\nPriority Queue Menu: ";
        cout << "\n1. Insert item";
        cout << "\n2. Remove highest priority item";
        cout << "\n3. Display queue";
        cout << "\n4. Exit";
        cout << "\nEnter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter the data (string): ";
                cin >> data;
                cout << "Enter the priority (int): ";
                cin >> priority;
                pq.insert(data, priority);
                break;

            case 2:
                pq.remove();
                break;

            case 3:
                pq.display();
                break;

            case 4:
                cout << "Exiting program..." << endl;
                break;

            default:
                cout << "Invalid choice!" << endl;
        }
    } while (choice != 4);
}

int main() {
    priorityQueueMenu();
    return 0;
}
