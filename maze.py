import os
os.system('cls')

import random
import time
from collections import deque


def load_maze(file_path):
    maze = []
    with open(file_path, 'r') as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze


def find_start_goal(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'S':
                start = (row, col)
            elif maze[row][col] == 'G':
                goal = (row, col)
    return start, goal


def get_maze_size(maze):
    size = 0
    for rows in range(len(maze)):
        for columns in range(len(maze[rows])):
            if (maze[rows][columns] == '*'):
                size+=1
    return size


actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
action_names = ['Left', 'Right', 'Up', 'Down']


def bfs(maze, start, goal):
    queue = deque([(start, [])])
    visited = set()

    start_time = time.time()

    while queue:
        current, path = queue.popleft() # FIFO
        row, col = current

        if current == goal:
            end_time = time.time()
            return path, end_time - start_time

        for i in range(len(actions)):
            action, action_name = actions[i], action_names[i]
            new_row, new_col = row + action[0], col + action[1]
            new_pos = (new_row, new_col)

            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#' and new_pos not in visited:
                visited.add(new_pos)
                queue.append((new_pos, path + [action_name])) 
                
    return "Path not found", time.time() - start_time


def dfs(maze, start, goal):
    stack = [(start, [])]
    visited = set()

    start_time = time.time()
 
    while stack:
        current, path = stack.pop() # LIFO
        row, col = current

        if current == goal:
            end_time = time.time()
            return path, end_time - start_time

        for i in range(len(actions)):
            action, action_name = actions[i], action_names[i]
            new_row, new_col = row + action[0], col + action[1]
            new_pos = (new_row, new_col)

            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#' and new_pos not in visited:
                visited.add(new_pos)
                stack.append((new_pos, path + [action_name]))

    return "Path not found", time.time() - start_time


def ucs(maze, start, goal):
    queue = [(0, start, [])]
    visited = set()

    start_time = time.time()

    while queue:
        cost, current, path = queue.pop(0)
        row, col = current

        if current == goal:
            end_time = time.time()
            return path, end_time - start_time

        for i in range(len(actions)):
            action, action_name = actions[i], action_names[i]
            new_row, new_col = row + action[0], col + action[1]
            new_pos = (new_row, new_col)

            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#' and new_pos not in visited:
                visited.add(new_pos)
                new_cost = cost + 1  
                queue.append((new_cost, new_pos, path + [action_name]))
                queue.sort()

    return "Path not found", time.time() - start_time



if __name__ == '__main__':
    num = random.randint(1, 8)
    path = os.path.join("mazes", f"maze{num}.txt")
    print(f"Running on maze: ", path.split("\\")[-1])
    maze = load_maze(path)
    start, goal = find_start_goal(maze)

    size = get_maze_size(maze)
    

    bfs_path, bfs_time = bfs(maze, start, goal)
    print("BFS Path: ", bfs_path)
    print("BFS Running Time: ", bfs_time)


    dfs_path, dfs_time = dfs(maze, start, goal)
    print("\nDFS Path:", dfs_path)
    print("DFS Running Time:", dfs_time)


    ucs_path, ucs_time = ucs(maze, start, goal)
    print("\nUCS Path:", ucs_path)
    print("UCS Running Time:", ucs_time)