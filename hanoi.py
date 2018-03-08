def hanoi(n,x,y,z):
    #汉诺塔游戏：n表示汉诺塔的层数，x,y,z表示柱子
    #函数功能：将柱子x上的盘子借助柱子y移动到柱子z上去
    
    if n==1:
        print(x,'-->',z)#将x上的盘子移到z上去
    else:
        hanoi(n-1,x,z,y)#将x上n-1个盘子借助z移到y
        print(x,'-->',z)#将x上的盘子移到z上去
        hanoi(n-1,y,x,z)#将y上n-1个盘子借助x移到z

n=int(input("请输入汉诺塔的层数："))
hanoi(n,'X','Y','Z')
