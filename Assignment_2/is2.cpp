#include <iostream>
#include <map>
#include <vector>

using namespace std;

string encrypt_transposition(const string& text, const string& key) {
    // Generate the order of columns based on the key
    map<char, int> order_dict;
    for (int i = 0; i < key.length(); ++i) {
        order_dict[key[i]] = i + 1;
    }

    // Calculate the number of rows needed in the table
    int num_rows = text.length() / key.length();
    if (text.length() % key.length() != 0) {
        num_rows += 1;
    }

    // Create the table
    vector<vector<char>> table(num_rows, vector<char>(key.length(), ' '));

    // Fill in the table with the characters from the text
    int index = 0;
    for (int row = 0; row < num_rows; ++row) {
        for (int col = 0; col < key.length(); ++col) {
            if (index < text.length()) {
                table[row][col] = text[index];
                ++index;
            }
        }
    }

    // Create the encrypted text based on the column order
    string encrypted_text = "";
    for (auto& entry : order_dict) {
        char col = entry.first;
        int col_index = entry.second - 1;
        for (int row = 0; row < num_rows; ++row) {
            char current_char = table[row][col_index];
            encrypted_text += (current_char != ' ') ? current_char : '*';
        }
    }

    return encrypted_text;
}

string decrypt_transposition(const string& encrypted_text, const string& key) {
    // Generate the order of columns based on the key
    map<char, int> order_dict;
    for (int i = 0; i < key.length(); ++i) {
        order_dict[key[i]] = i + 1;
    }

    // Calculate the number of rows needed in the table
    int num_rows = encrypted_text.length() / key.length();

    // Create the table
    vector<vector<char>> table(num_rows, vector<char>(key.length(), ' '));

    // Fill in the table with the characters from the encrypted text
    int index = 0;
    for (auto& entry : order_dict) {
        char col = entry.first;
        int col_index = entry.second - 1;
        for (int row = 0; row < num_rows; ++row) {
            table[row][col_index] = encrypted_text[index];
            ++index;
        }
    }

    // Create the decrypted text
    string decrypted_text = "";
    for (int row = 0; row < num_rows; ++row) {
        for (int col = 0; col < key.length(); ++col) {
            decrypted_text += table[row][col];
        }
    }

    // Replace '*' with space
    size_t pos = decrypted_text.find('*');
    while (pos != string::npos) {
        decrypted_text.replace(pos, 1, " ");
        pos = decrypted_text.find('*', pos + 1);
    }

    return decrypted_text;
}

int main() {
    string text = "MESWCOE PUNE";
    string key = "HACK";
    string encrypted_text = encrypt_transposition(text, key);
    cout << "Encrypted Text: " << encrypted_text << endl;

    string decrypted_text = decrypt_transposition(encrypted_text, key);
    cout << "Decrypted Text: " << decrypted_text << endl;

    return 0;
}
