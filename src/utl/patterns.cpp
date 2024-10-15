#include <fstream>
#include <iostream>
#include <limits>
#include <stdlib.h>

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

  std::cout << "type\t│ lowest()\t│ min()\t\t│ max()\n"
      << "bool\t│ "
      << std::numeric_limits<bool>::lowest() << "\t\t│ "
      << std::numeric_limits<bool>::min() << "\t\t│ "
      << std::numeric_limits<bool>::max() << '\n'
      << "uchar\t│ "
      << +std::numeric_limits<unsigned char>::lowest() << "\t\t│ "
      << +std::numeric_limits<unsigned char>::min() << "\t\t│ "
      << +std::numeric_limits<unsigned char>::max() << '\n'
      << "int\t│ "
      << std::numeric_limits<int>::lowest() << "\t│ "
      << std::numeric_limits<int>::min() << "\t│ "
      << std::numeric_limits<int>::max() << '\n'
      << "float\t│ "
      << std::numeric_limits<float>::lowest() << "\t│ "
      << std::numeric_limits<float>::min() << "\t│ "
      << std::numeric_limits<float>::max() << '\n'
      << "double\t│ "
      << std::numeric_limits<double>::lowest() << "\t│ "
      << std::numeric_limits<double>::min() << "\t│ "
      << std::numeric_limits<double>::max() << '\n';
  return 0 ;
}
