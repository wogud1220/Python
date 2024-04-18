class State:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.moves = moves
        self.goal = goal

# i1과 i2를 교환하여서 새로운 상태를 반환한다. 
    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)

    def expand(self, moves):
        result = []
        i = self.board.index(0)		# 숫자 0(빈칸)의 위치를 찾는다. 
        if not i in [0, 1, 2] :		# UP 연산자 
            result.append(self.get_new_board(i, i-3, moves)) # 0이 맨 윗줄에 없다면 Index-3(위로 1칸 올리기)를 한다.
            
        if not i in [0, 3, 6] :		# LEFT 연산자 
            result.append(self.get_new_board(i, i-1, moves))
        
        if not i in [2, 5, 8]:		# RIGHT 연산자 
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6, 7, 8]:		# DOWN 연산자 
            result.append(self.get_new_board(i, i+3, moves))
        return result

    def __str__(self):
        return str(self.board[:3]) +"\n"+\
        str(self.board[3:6]) +"\n"+\
        str(self.board[6:]) +"\n"+\
        "------------------"

puzzle = [1, 2, 3, 
          0, 4, 6, 
          7, 5, 8]

# 목표 상태
goal = [1, 2, 3, 
        4, 5, 6, 
        7, 8, 0]

open_stack = []
open_stack.append(State(puzzle, goal))

closed_stack = []
moves = 0
while len(open_stack) != 0:
    current = open_stack.pop()  # 리스트 마지막 pop
    print(current)
    if current.board == goal:
        print("탐색 성공")
        break
    moves = current.moves + 1
    if current.board not in closed_stack:
        closed_stack.append(current.board)
        expanded_states = current.expand(moves)
        for state in expanded_states:
            open_stack.append(state)  #스택의 마지막에 푸시