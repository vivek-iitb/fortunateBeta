#include <fstream>
#include <iostream>


// File IO 
class File {
public:
    File(const std::string& filename) {
        file.open(filename);
        if (!file.is_open()) {
            throw std::runtime_error("Unable to open file");
        }
    }

    ~File() {
        if (file.is_open()) {
            file.close();
        }
    }

    void write(const std::string& data) {
        if (file.is_open()) {
            file << data;
        }
    }

private:
    std::ofstream file;
};

int main() {
    try {
        File file("example.txt");
        file.write("Hello, RAII!");
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    // The file is automatically closed when `file` goes out of scope.
    return 0;
}
