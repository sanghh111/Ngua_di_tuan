#include<iostream>
using namespace std;
int a[8][8]={-1};
int X[8]={-2 , -2 , -1 , -1 , 1 , 1 , 2 , 2 };
int Y[8]={ -1,  1 , -2 , 2 , -2 , 2 ,-1 , 1 };
int dem=1;
void khoi_tao()
{
	for(int i=0;i<8;i++)
		for(int j=0;j<8;j++)
			a[i][j]=-1;
}
void xuat()
{
	for(int i=0;i<8;i++){
		for(int j=0;j<8;j++)
			cout<<a[i][j]<<"	";
		cout<<endl;
	}
	
}
int Di_tuan(int x,int y)
{
a[x][y]=dem;
dem++;
	for(int z=0;z<8;z++)
	{
		if(dem==8*8+1)
		{
			cout<<"Cac buoc di la\n";
			xuat();
			exit(0) ;
		}
		int u=x+Y[z];
		int v=y+X[z];
		if(u>=0 && u<8 && v>=0 && v<8 &&a[u][v]==-1)
		Di_tuan(u,v);
	}
a[x][y]=-1;
dem--;
}
main()
{
	khoi_tao();
	Di_tuan(7,7);
}
