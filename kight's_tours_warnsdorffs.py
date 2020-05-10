class Chess_board:
    def __init__(self,wei,hei):
        self.w=wei
        self.h=hei

        self.move=[(1, 2), (1, -2), (-1, 2), (-1, -2),
                (2, 1), (2, -1), (-2, 1), (-2, -1)]
        self.board=[]
        self.path=[]
        self.creat_broad()

    def creat_broad(self):
        for i in range(0,self.h):
            self.board.append([0]*self.w)

    def check_move(self,x,y):
        return ((x >= 0 and x < self.w) and (y >= 0  and y < self.h))

    def square_valid(self,x,y):
        return self.check_move(x,y) and self.board[x][y]==0

    def check_square_adjacent(self,x,y):
        count=0
        for move in self.move:
            if(self.square_valid(x+move[0],y+move[1])):
                count=count+1
        return count

    def next_mov(self,to_visit):
        min_deg=self.h+1
        nx=ny=0
        min_deg_arr=[]
        for move in self.move:
            nx=to_visit[0]+move[0]
            ny=to_visit[1]+move[1]
            c=self.check_square_adjacent(nx,ny)
            if(self.square_valid(nx,ny) and c < min_deg ):
                min_deg_arr=move
                min_deg=c

        if(min_deg_arr==[]):
            print("flase")
            return False ,(-1,-1)

        nx=to_visit[0]+min_deg_arr[0]
        ny=to_visit[1]+min_deg_arr[1]
        self.board[nx][ny]=self.board[to_visit[0]][to_visit[1]]+1
        to_visit=(nx,ny)
        # print(type(to_visit))
        return True , to_visit

    def tour(self,n,to_visit):
        self.board[to_visit[0]][to_visit[1]]=n
        n=n+1
        self.path.append(to_visit)
        # b=to_visit
        while(n!=self.w*self.h):
            a,to_visit=self.next_mov(to_visit)
            if(a):
                n=n+1
                self.path.append(to_visit)
            else:
                return 

    def print_board(self):
        print ("  ")
        print ("------")
        for elem in self.board:
            print (elem)
        print ("------")
        print ("  ")

    def get_path(self):
        return self.path