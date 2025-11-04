import tkinter as tk
import random, heapq, time

# ---------------- Maze Generation ----------------
def generate_maze(rows, cols, wall_prob=0.25):
    maze = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Outer boundary always walls
            if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                row.append(1)
            else:
                row.append(1 if random.random() < wall_prob else 0)
        maze.append(row)
    # Start and end are always open
    maze[1][1] = 0
    maze[rows - 2][cols - 2] = 0
    return maze

# ---------------- Weighted Grid ----------------
def generate_weights(maze):
    weights = []
    for row in maze:
        w_row = []
        for cell in row:
            if cell == 1:
                w_row.append(999)
            else:
                w_row.append(random.randint(1, 5))
        weights.append(w_row)
    return weights

# ---------------- Algorithms ----------------
def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = [(start, [start])]
    visited = [[False] * cols for _ in range(rows)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        (x, y), path = queue.pop(0)
        if (x, y) == end:
            return path
        if not visited[x][y]:
            visited[x][y] = True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and not visited[nx][ny]:
                    queue.append(((nx, ny), path + [(nx, ny)]))
    return None

def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = [[False] * cols for _ in range(rows)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while stack:
        (x, y), path = stack.pop()
        if (x, y) == end:
            return path
        if not visited[x][y]:
            visited[x][y] = True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and not visited[nx][ny]:
                    stack.append(((nx, ny), path + [(nx, ny)]))
    return None

def dijkstra(maze, start, end, weights):
    rows, cols = len(maze), len(maze[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = 0
    pq = [(0, start, [start])]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while pq:
        d, (x, y), path = heapq.heappop(pq)
        if (x, y) == end:
            return path
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                new_d = d + weights[nx][ny]
                if new_d < dist[nx][ny]:
                    dist[nx][ny] = new_d
                    heapq.heappush(pq, (new_d, (nx, ny), path + [(nx, ny)]))
    return None

def astar(maze, start, end, weights):
    rows, cols = len(maze), len(maze[0])
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    open_set = [(heuristic(start, end), 0, start, [start])]
    g_score = {start: 0}
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while open_set:
        _, g, current, path = heapq.heappop(open_set)
        if current == end:
            return path
        for dx, dy in dirs:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                new_g = g + weights[nx][ny]
                if (nx, ny) not in g_score or new_g < g_score[(nx, ny)]:
                    g_score[(nx, ny)] = new_g
                    f = new_g + heuristic((nx, ny), end)
                    heapq.heappush(open_set, (f, new_g, (nx, ny), path + [(nx, ny)]))
    return None

# ---------------- GUI + Gameplay ----------------
def draw_maze():
    canvas.delete("all")
    for i in range(rows):
        for j in range(cols):
            color = "black" if maze[i][j] == 1 else "white"
            canvas.create_rectangle(
                j * cell_size, i * cell_size,
                (j + 1) * cell_size, (i + 1) * cell_size,
                fill=color, outline="gray"
            )

    # Draw start (green)
    sx, sy = start
    canvas.create_rectangle(sy * cell_size, sx * cell_size,
                            (sy + 1) * cell_size, (sx + 1) * cell_size,
                            fill="lime", outline="black")

    # Draw end (red) last so it's always visible
    ex, ey = end
    canvas.create_rectangle(ey * cell_size, ex * cell_size,
                            (ey + 1) * cell_size, (ex + 1) * cell_size,
                            fill="red", outline="black")

def draw_player():
    x, y = player_pos
    canvas.create_oval(
        y * cell_size + 5, x * cell_size + 5,
        (y + 1) * cell_size - 5, (x + 1) * cell_size - 5,
        fill="blue"
    )

def move_player(dx, dy):
    global player_pos, player_path
    nx, ny = player_pos[0] + dx, player_pos[1] + dy
    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
        player_pos = (nx, ny)
        player_path.append(player_pos)
        draw_maze()
        draw_player()
        if player_pos == end:
            check_player_path()
    else:
        info_label.config(text="❌ You hit a wall!")

def check_player_path():
    correct_path = get_algo_path()
    if player_path == correct_path:
        info_label.config(text="🎉 Well done! You matched the algorithm!")
    else:
        info_label.config(text="⚠️ Wrong path! Showing correct path...")
        show_correct_path(correct_path)
    show_end_buttons()

def get_algo_path():
    algo = algo_var.get()
    if algo == "BFS":
        return bfs(maze, start, end)
    elif algo == "DFS":
        return dfs(maze, start, end)
    elif algo == "Dijkstra":
        return dijkstra(maze, start, end, weights)
    else:
        return astar(maze, start, end, weights)

def show_correct_path(path):
    draw_maze()
    for (x, y) in path:
        canvas.create_rectangle(
            y * cell_size, x * cell_size,
            (y + 1) * cell_size, (x + 1) * cell_size,
            fill="orange"
        )
        window.update()
        time.sleep(0.03)
    draw_maze()
    for (x, y) in path:
        canvas.create_rectangle(
            y * cell_size, x * cell_size,
            (y + 1) * cell_size, (x + 1) * cell_size,
            fill="orange"
        )
    draw_player()
    window.update()

def show_solution():
    info_label.config(text=f"Showing {algo_var.get()} solution...")
    path = get_algo_path()
    show_correct_path(path)

def show_end_buttons():
    next_btn = tk.Button(control_frame, text="Next Level", font=("Helvetica", 12),
                         command=next_level, bg="#00CC66", fg="white")
    retry_btn = tk.Button(control_frame, text="Retry", font=("Helvetica", 12),
                          command=regenerate_maze, bg="#FF3333", fg="white")
    next_btn.pack(pady=5, fill="x")
    retry_btn.pack(pady=5, fill="x")

def next_level():
    global rows, cols
    rows += 2
    cols += 2
    regenerate_maze()

def regenerate_maze():
    global maze, weights, player_pos, player_path, start, end
    while True:
        maze = generate_maze(rows, cols)
        start, end = (1, 1), (rows - 2, cols - 2)
        maze[start[0]][start[1]] = 0
        maze[end[0]][end[1]] = 0
        weights = generate_weights(maze)
        if bfs(maze, start, end):  # ensure solvable
            break

    player_pos = start
    player_path = [start]
    draw_maze()
    draw_player()
    info_label.config(text="Use arrow keys to reach the red cell!")

# ---------------- Main ----------------
window = tk.Tk()
window.title("Maze Solver Game")
window.configure(bg="black")

rows, cols = 12, 12
cell_size = 35

maze = generate_maze(rows, cols)
weights = generate_weights(maze)
start, end = (1, 1), (rows - 2, cols - 2)
player_pos = start
player_path = [start]

canvas = tk.Canvas(window, width=cols * cell_size, height=rows * cell_size, bg="white")
canvas.grid(row=0, column=0, padx=10, pady=10)

control_frame = tk.Frame(window, bg="black")
control_frame.grid(row=0, column=1, padx=15)

tk.Label(control_frame, text="Maze Game", font=("Helvetica", 18, "bold"), fg="#00FF80", bg="black").pack(pady=10)
tk.Button(control_frame, text="Regenerate Maze", font=("Helvetica", 12), command=regenerate_maze).pack(pady=5, fill="x")

algo_var = tk.StringVar(value="BFS")
tk.OptionMenu(control_frame, algo_var, "BFS", "DFS", "Dijkstra", "A*").pack(pady=5, fill="x")

tk.Button(control_frame, text="Show Solution", font=("Helvetica", 12),
          command=show_solution, bg="#3399FF", fg="white").pack(pady=5, fill="x")

info_label = tk.Label(control_frame, text="Use arrow keys to move!", fg="yellow", bg="black", font=("Helvetica", 12))
info_label.pack(pady=10)

# Bind movement keys
window.bind("<Up>", lambda e: move_player(-1, 0))
window.bind("<Down>", lambda e: move_player(1, 0))
window.bind("<Left>", lambda e: move_player(0, -1))
window.bind("<Right>", lambda e: move_player(0, 1))

draw_maze()
draw_player()
window.mainloop()
