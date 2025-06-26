#include <bits/stdc++.h>
using namespace std;

// Function to print the array
void printVector(const vector<int>& v) {
    for (int val : v) {
        cout << val << " ";
    }
    cout << endl;
}

// Right shift by 1
void rightShift(vector<int>& v) {
    int last = v.back();
    for (int i = v.size() - 1; i > 0; i--) {
        v[i] = v[i - 1];
    }
    v[0] = last;
}

// Left shift by 1
void leftShift(vector<int>& v) {
    int first = v[0];
    for (int i = 0; i < v.size() - 1; i++) {
        v[i] = v[i + 1];
    }
    v[v.size() - 1] = first;
}

int main() {
    int n;
    cout << "Enter size of array: ";
    cin >> n;

    vector<int> v(n);
    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    cout << "Original array: ";
    printVector(v);

    rightShift(v);
    cout << "After right shift: ";
    printVector(v);

    leftShift(v);
    cout << "After left shift (back to original): ";
    printVector(v);

    return 0;
}
