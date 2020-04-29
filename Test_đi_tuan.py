class ngua_di_tuan:
    def __init__(self,n):
        self.n=n
        self.X=[-2 , -2 , -1 , -1 , 1 , 1 , 2 , 2 ]
        self.Y=[ -1,  1 , -2 , 2 , -2 , 2 ,-1 , 1 ]
        self.dem=1  
        self.arr = [[0 for i in range(n)] for j in range(n)]
    def xuat(self):
        print("----------")
        for i in self.arr:
            print(i)
        print("----------")
    def Di_tuan(self,x,y,duongdi=0):
        self.arr[x][y]=self.dem
        self.dem+=1
        if self.dem==self.n*self.n+1:
                print("cac duong di la")
                self.xuat()
                exit()
        for i in range(0,8):
            u=x+self.X[i]
            v=y+self.Y[i]
            print(duongdi,u,v)
            if u>=0 and u<8 and v>=0 and v<8 and self.arr[u][v]==0 :
                self.Di_tuan(u,v,duongdi+1)               
        self.arr[x][y]=0
        self.dem=self.dem-1
    def get_arr(self):
        return self.arr