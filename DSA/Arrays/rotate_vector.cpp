#include <bits/stdc++.h>
using namespace std;

// Function to print the array
void printVector(const vector<int>& v) {
    for (int val : v) {
        cout << val << " ";
    }
    cout << endl;
}

// Left rotate by k using reverse
void leftRotateByK(vector<int>& v, int k) {
    int n = v.size();
    k %= n; // Handles k > n
    reverse(v.begin(), v.begin() + k);
    reverse(v.begin() + k, v.end());
    reverse(v.begin(), v.end());
}

// Right rotate by k using reverse
void rightRotateByK(vector<int>& v, int k) {
    int n = v.size();
    k %= n; // Handles k > n
    reverse(v.begin(), v.end());
    reverse(v.begin(), v.begin() + k);
    reverse(v.begin() + k, v.end());
}

int main() {
    int n, k;
    cout << "Enter size of array: ";
    cin >> n;

    vector<int> v(n);
    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    cout << "Enter value of k: ";
    cin >> k;

    cout << "Original array: ";
    printVector(v);

    // Rotate left by k
    vector<int> leftV = v;
    leftRotateByK(leftV, k);
    cout << "Array after left rotating by " << k << " positions: ";
    printVector(leftV);

    // Rotate right by k
    vector<int> rightV = v;
    rightRotateByK(rightV, k);
    cout << "Array after right rotating by " << k << " positions: ";
    printVector(rightV);

    return 0;
}