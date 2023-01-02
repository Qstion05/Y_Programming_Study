#include <iostream>
using namespace std;

int main(){
	char operate, yn;
	int num1, num2 = 0;
	while(true){
		cout<<"연산자를 입력해주세요"<<endl;
		cin>>operate;
		cout<<"첫번째 숫자를 입력해주세요"<<endl; 
		cin>>num1;
		cout<<"두번째 숫자를 입력해주세요"<<endl; 
		cin>>num2;
		
		switch(operate){
			
			case '+':
				printf("%d\n", num1 + num2);
				break;
				
			case '-':
				printf("%d\n", num1 - num2);
				break;
			
			case '*':
				printf("%d\n", num1 * num2);
				break;
			
			case '/':
				printf("%d\n", num1 / num2);
				break;
			
			case '%':
				cout<<num1 % num2<<endl;
				break;
				
			default:
				cout<<"잘못된 연산자입니다."<<endl;
		}
		
		cout<<"종료하려면 N을 눌러주세요"<<endl;
		cin>>yn;
		
		if(yn == 'n' || yn == 'N')
			break;
	}
	return 0;
}	
