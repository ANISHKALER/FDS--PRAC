#include <iostream>
#include <map>
using namespace std;

class Node {
    string name;
    int PRN;
    Node* next;

public:
    Node(string name, int prn) {
        this->name = name;
        this->PRN = prn;
        this->next = nullptr;
    }

    int getPRN() {
        return PRN;
    }

    void setPRN(int prn) {
        PRN = prn;
    }

    string getName() {
        return name;
    }

    void setName(string name) {
        this->name = name;
    }

    Node* getNext() {
        return next;
    }

    void setNext(Node* nextNode) {
        next = nextNode;
    }
};

class Club {
private:
    Node* head;
    Node* tail;
    int count;

public:
    Club() {
        head = nullptr;
        tail = nullptr;
        count = 0;
    }

    void addMember(string name, int prn) {
        Node* newNode = new Node(name, prn);
        if (head == nullptr) {
            head = newNode;
            tail = newNode;
        } else {
            tail->setNext(newNode);
            tail = newNode;
        }
        count++;
    }

    void addPresident(string name, int prn) {
        Node* newNode = new Node(name, prn);
        if (head == nullptr) {
            head = newNode;
            tail = newNode;
        } else {
            newNode->setNext(head);
            head = newNode;
        }
        count++;
    }

    void addSecretary(string name, int prn) {
        Node* newNode = new Node(name, prn);
        if (head == nullptr) {
            head = newNode;
            tail = newNode;
        } else {
            tail->setNext(newNode);
            tail = newNode;
        }
        count++;
    }

    void displayMembers() {
        Node* current = head;
        if (current == nullptr) {
            cout << "No members in the club.\n";
            return;
        }
        while (current) {
            cout << "Name: " << current->getName() << ", PRN: " << current->getPRN() << '\n';
            current = current->getNext();
        }
    }

    int getTotalMember() {
        return count;
    }
};

void displayMenu() {
    cout << "\nMenu:\n";
    cout << "1. Create New Division\n";
    cout << "2. Add Member\n";
    cout << "3. Add President\n";
    cout << "4. Add Secretary\n";
    cout << "5. Display Members\n";
    cout << "6. Exit\n";
    cout << "Choose an option: ";
}

int main() {
    map<int, Club> divisions;
    int choice, divisionID;
    string name;
    int prn;

    do {
        displayMenu();
        cin >> choice;

        switch (choice) {
            case 1: {
                cout << "Enter new Division ID: ";
                cin >> divisionID;
                if (divisions.find(divisionID) == divisions.end()) {
                    divisions[divisionID] = Club();
                    cout << "New division " << divisionID << " created.\n";
                } else {
                    cout << "Division ID already exists.\n";
                }
                break;
            }

            case 2: {
                cout << "Enter division ID: ";
                cin >> divisionID;
                if (divisions.find(divisionID) != divisions.end()) {
                    cout << "Enter name: ";
                    cin >> name;
                    cout << "Enter PRN: ";
                    cin >> prn;
                    divisions[divisionID].addMember(name, prn);
                } else {
                    cout << "Division ID does not exist.\n";
                }
                break;
            }

            case 3: {
                cout << "Enter division ID: ";
                cin >> divisionID;
                if (divisions.find(divisionID) != divisions.end()) {
                    cout << "Enter new president's name: ";
                    cin >> name;
                    cout << "Enter new president's PRN: ";
                    cin >> prn;
                    divisions[divisionID].addPresident(name, prn);
                } else {
                    cout << "Division ID does not exist.\n";
                }
                break;
            }

            case 4: {
                cout << "Enter division ID: ";
                cin >> divisionID;
                if (divisions.find(divisionID) != divisions.end()) {
                    cout << "Enter new secretary's name: ";
                    cin >> name;
                    cout << "Enter new secretary's PRN: ";
                    cin >> prn;
                    divisions[divisionID].addSecretary(name, prn);
                } else {
                    cout << "Division ID does not exist.\n";
                }
                break;
            }

            case 5: {
                cout << "Enter division ID: ";
                cin >> divisionID;
                if (divisions.find(divisionID) != divisions.end()) {
                    cout << "Division " << divisionID << " members:\n";
                    divisions[divisionID].displayMembers();
                    cout << "Total club members of Division " << divisionID << ": " << divisions[divisionID].getTotalMember() << endl;
                } else {
                    cout << "Division ID does not exist.\n";
                }
                break;
            }

            case 6:
                cout << "Exiting...\n";
                break;

            default:
                cout << "Invalid choice! Please try again.\n";
        }
    } while (choice != 6);

    return 0;
}
