# include <iostream>
# include <cstring>
# include <algorithm>
# include <string.h>
using namespace std;

int main()
{
	int initial=0;	
	char ptext[]="HelloWorldLeader";
	cout<<"Plaintext : "<<endl;
	cout<<ptext;
	cout<<endl;
	char key[]="secret";
	cout<<"Key : "<<endl;
	cout<<key<<endl;
	sort(key,key+strlen(key));
	int colmn[strlen(key)];
	memset(colmn,0,sizeof(colmn));
	cout<<endl;
	for (int i=0;i<sizeof(colmn)/sizeof(int);i++)
	{
		initial++;
		colmn[i]=initial;
		cout<<colmn[i];
	}
	char ctext[sizeof(key)][sizeof(key)];
	for (int i=0;i<sizeof(key);i++)
	{
		for (int j=0;j<sizeof(key);j++)
		{
			if (ptext[i]==" ")
			{
				ctext[i][j]="*";
			}
			else
			{
				ctext[i][j]=ptext[i];
			}
		}
		
	}
	cout<<endl;
	cout<<"Cipher text is : "<<endl;
	for (int i=0;i<sizeof(key);i++)
	{
		for (int j=0;j<sizeof(key);j++)
		{
			cout<<ctext[i][j];
		}
	}cout<<endl;
	
	
}
