#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<sstream>
#include<algorithm>

int main () {

    std::ifstream inp("input.txt");
    std::string line;
    
    int out = 0;

    while(std::getline(inp,line)) {

        std::stringstream ss(line);
        std::string tmp;
        std::vector<std::string> words;

        while(std::getline(ss,tmp,' ')) {
            words.push_back(tmp);
        }

        size_t split_point = words[0].find("-");

        int pos1 = std::stoi(words[0].substr(0,split_point));
        int pos2 = std::stoi(words[0].substr(split_point+1));
    
        std::string password;
        char ch;
        ch = words[1][0];
        password = words[2];

        if((ch == password.at(pos1-1)) ^ (ch == password.at(pos2-1))) out += 1;

    }

    std::cout << out << std::endl;
    return 0;

}