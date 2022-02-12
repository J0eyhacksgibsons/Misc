#include <iostream> 
#include <string.h>
using namespace std;
void print(const string &);
int  compare(const string &,const string &,string &);
int main(int argc, char** argv){
    string key,answers,score;
    int keySiz = 21;
    string keys [keySiz];
    int ansSiz = 21;
    float co = 0;
    string ans [ansSiz];
    for(int a = 0; a < keySiz; a++){
        cin >> keys[a];
    }
    for(int a = 0; a < ansSiz; a++){
        cin >> ans[a];
    }
    cout<<"C/W     ";
    for(int a = 1; a < ansSiz; a++){
        if(keys[a] == ans[a]){
            cout << "C ";
            co += 1;
        } else{
            cout << "W ";
        }
    }
    cout << endl;
    co /= ansSiz - 1;
    cout<<"Percentage Correct = " << co * 100 << "%" << endl;
    return 0;
}
