def solution(park, routes):
    # 1 = 장애물
    # 0 = 이동가능
    row, col = len(park), len(park[0]) # 가로, 세로 길이
    grid = [[0 for c_idx in range(col)] for r_idx in range(row)] # grid 그리기
    curr_row, curr_col = 0, 0 # 현재 start 위치
    
    # string 쓰지 않고 이중배열로 grid에 0과 1표시
    for r_idx in range(row):
        for c_idx in range(col):
            if park[r_idx][c_idx] == "X": # 갈 수 없는 곳(X)을 1로 표시
                grid[r_idx][c_idx] = 1
            elif park[r_idx][c_idx] == "S": # 갈 수 있는 곳(S), 0으로 기록했음
                curr_row, curr_col = r_idx, c_idx
                
    dirs = {"N":(-1,0), "S":(1,0), "E":(0,1), "W":(0,-1)} # 방향 미리 설정
    
    for route in routes:
        direction, distance = route.split() # E 2 => 방향과 칸을 split하기
        dir_row, dir_col = dirs[direction] # 방향에 따라 row와 col이 어떻게 변하는지
        # 로봇 강아지는 명령을 수행하기 전에 다음 두가지를 먼저 확인
        is_valid = True
        for offset in range(1, int(distance)+1): # offset을 이용해서 칸 설정
            new_row, new_col = curr_row + dir_row * offset, curr_col + dir_col * offset
            # 새롭게 이동한 곳 = 현재 위치 + 방향 * 이동 칸 수
            
            if new_row in range(row) and new_col in range(col) and grid[new_row][new_col] == 0:
                pass
            # 이동 중에 grid 판을 벗어나지는 않는지, grid 판 안에서 이동하는지 확인
            # and
            # 이동 중에 장애물을 만나는지
            # 이 중 하나만 만족을 못하면(is_valid = False)  명령을 무시하고 다음 명령을 수행
            else:
                is_valid = False
                break
        if is_valid:
            curr_row, curr_col = new_row, new_col
            # is_valid = False면 업데이트 안하고, True면 업데이트
    
    return [curr_row, curr_col]
            
            