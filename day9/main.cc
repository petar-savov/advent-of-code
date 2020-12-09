#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<set>
#include<algorithm>

int main() {

    std::ifstream input("input.txt");
    std::vector<long long> data;
    std::string tmp;
    while(std::getline(input,tmp)) {
        data.push_back(std::stoll(tmp));
    }

    //part 1
    long long target = 0;
    for (uint16_t i = 25; i < data.size(); ++i) {
        std::vector<long long> prev (data.begin()+i-25,data.begin()+i+1);
        std::set<long long> pair_sums;
        for (uint16_t j = 0; j<prev.size(); ++j)
            for (uint16_t k=0; k<j; ++k)
                pair_sums.insert(prev[j]+prev[k]);
        
        const bool is_in = pair_sums.find(data.at(i)) != pair_sums.end();
        if (!is_in) {
            target = data.at(i);
            std::cout << "Part 1: " << target << std::endl;
            break;
        }

    }

    //part2
    int start = 0, end = 1;
    long long csum = data.at(0) + data.at(1);

    while(csum!=target) {
        while(csum<target) csum+=data[++end];
        while(csum>target) csum-=data[start++];
    }

    std::vector<long long> subarr(data.begin() + start, data.begin() + end);
    long long min = *std::min_element(data.begin()+start,data.begin()+end);
    long long max = *std::max_element(data.begin()+start,data.begin()+end);
    std::cout << "Part 2: " << min+max << " " << std::endl;

    return 0;
}