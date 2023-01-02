  
#include<bits/stdc++.h>


using namespace std;
// function protypes
const string get_keyword(); // Get Keyword and return key string
string encrypt(string, const vector<char> table); //encrypt the string
string decrypt(string, const vector<char> table); //decrypt the string
const vector<char> gen_table(const string);//generates key table with given key
//상수 문자열을 입력 받는 함수, 리턴값:char로 이루어진 동적 배열(verctor)

//function defnitions
const string get_keyword(){
   
    cout<<"키워드를 입력하세요 : ";
    string key, keyword;
    cin>>keyword;
    for(int i = 0; i < keyword.size(); i++)
        if (key.find(keyword[i]) == string::npos) // 중복된 단어제거
            key.append(string{keyword[i]});  //입력된 키워드를 하나씩 문자열로 저장
    return key;
    /*
    Ex)
    keyword = apple
    key = aple
    */
}
const vector<char> gen_table(const string key){
    vector<char> table; // table라는 이름의 vector 생성.
    for(int i = 0; i < key.size(); i++)
        table.push_back(key[i]); // 마지막 원소 뒤에 key[i]를 추가 = 벡터의 크기가 1 증가함.  
    for(int i = table[key.size()-1]; i <= 'z'; i++ )
        if(key.find(i) == string::npos)
            table.push_back(i);
    for(int i = 'a'; i != table[key.size()-1]; i++ )
        if(key.find(i) == string::npos)
            table.push_back(i);
    return table;
    /*Ex)
    1.for -> table = [a.p.l.e]
    2.for -> table = [a p l e f g h i j k m n o q r s t u v w x y z b c d]
    */
}

string encrypt(string target, const vector<char> table){
    string retval;
    for(int i = 0; i < target.size(); i++){
            if(target[i] == ' '){
                retval.append(string{target[i]});
            }
            else{
            int index = target[i] - 'a'; //0~25(알파벳 순서)로 나옴.
            char tempChar  = table[index];//table을 거쳐index가 알파벳으로 변경
            retval.append(string{tempChar});//tempChar값을 문자열로 바꾼후, retval에 저장.
            }
        }
    return retval;
    /*
    Ex)
    table = [a p l e f g h i j k m n o q r s t u v w x y z b c d]
    target = [h, e, l, l, o]
    index = [7, 4, 11, 11, 14]
    tempchar = [i, f, m, m, q]
    retval = "ifmmq"  
    */
}

string decrypt(string target, const vector<char> table){
    string deretval;
    for(int i = 0; i < target.size(); i++){ 
        for(int j = 0; j<table.size(); j++){
            if(target[i] == table[j]){
                if(target[i] == ' '){
                    deretval.append(string{target[i]});

                }
                else{
                char tempChar = j + 97;
                deretval.append(string{tempChar});
                }
            }
        }

    }
    return deretval;
}


int main(){
    string str, retval, deretval;
    char select;
    cout<<"암호화 할 문장을 입력해주세요. : ";
    char temp;
    while( ( temp = getchar()) != '\n')
        str.append(string{temp});
    const string key = get_keyword();
    const vector<char> table = gen_table(key);
    retval = encrypt(str, table);
    cout<<"암호화 된 문장은"<<retval<<"입니다."<<endl;
    cout<<"해독하시려면 Y를 눌러주세요. :";
    cin >> select;
    if(select == 'Y' || select == 'y'){
        deretval = decrypt(retval, table);
        cout<<"해독한 문장은"<<deretval<<"입니다"<<endl;
        cout<<"프로그램을 종료합니다"<<endl;
        return 0;
    }
    else{
        cout<<"프로그램을 종료합니다"<<endl;
        return 0;
    }     
}