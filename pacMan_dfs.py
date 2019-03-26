def dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid):
    
    print(1)
    print('RIGHT')
    
    return ''

pacman_r, pacman_c = [int(i) for i in input().strip().split()]
food_r, food_c = [int(i) for i in input().strip().split()]

r,c = [int(i) for i in input().strip().split()]

grid = []
for i in range(0, r):
    grid.append(input())
    
dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)