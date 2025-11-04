\# Maze Solver Game (Tkinter + Pathfinding Algorithms)



!\[Python](https://img.shields.io/badge/Python-3.8%2B-blue)

!\[GUI](https://img.shields.io/badge/GUI-Tkinter-green)

!\[License](https://img.shields.io/badge/License-MIT-orange)

!\[Algorithms](https://img.shields.io/badge/Algorithms-BFS%20%7C%20DFS%20%7C%20Dijkstra%20%7C%20A\*-yellow)



An interactive \*\*maze-solving game\*\* built using \*\*Python (Tkinter)\*\*.  

Navigate a randomly generated maze and compare your path with classic pathfinding algorithms like \*\*BFS\*\*, \*\*DFS\*\*, \*\*Dijkstra\*\*, and \*\*A\\\*\*\*!







\# Features



\- 🎲 \*\*Random Maze Generation\*\* — every playthrough is unique  

\- 🧭 \*\*4 Pathfinding Algorithms\*\* — BFS, DFS, Dijkstra, and A\*  

\- ⚙️ \*\*Weighted Grids\*\* — random movement costs for realism  

\- 🕹️ \*\*Interactive Gameplay\*\* — move with arrow keys  

\- 🧩 \*\*Dynamic Levels\*\* — maze size increases with each level  

\- 🎨 \*\*Real-Time Visualization\*\* — watch algorithms solve the maze  

\- ✅ \*\*Solvability Check\*\* — ensures all mazes can be completed  







\# Algorithms Implemented



| Algorithm | Type | Weighted | Heuristic | Description |

|------------|-------|-----------|------------|--------------|

| \*\*BFS\*\* | Uninformed | ❌ | ❌ | Finds shortest path in unweighted grids |

| \*\*DFS\*\* | Uninformed | ❌ | ❌ | Explores deep paths first; not guaranteed optimal |

| \*\*Dijkstra\*\* | Informed | ✅ | ❌ | Finds lowest-cost path considering weights |

| \*\*A\\\*\*\* | Informed | ✅ | ✅ | Uses cost + heuristic for efficient shortest path |







\# Installation



\### Clone the Repository

'''bash

git clone https://github.com/<your-username>/maze-solver-game.git

cd maze-solver-game













2\.  Run the Game

Make sure you have Python installed
				<python maze\_solver\_game.py>



Tkinter comes pre-installed with most Python distributions.

If missing, install it manually:
				<sudo apt install python3-tk>

			**(Windows users usually have it by default.)**













3\. How to Play

A- Use arrow keys to move the blue ball:


↑ Up

↓ Down

← Left

→ Right



B- Start from the green cell and reach the red cell.



C- Once you reach the goal:



	The game checks if your path matches the algorithm’s optimal path.



	If incorrect, it will visualize the correct route.



D- Choose algorithms from the dropdown menu:



		***BFS, DFS, Dijkstra, or A\****



E- Buttons available:



🔁 Regenerate Maze – create a new maze



💡 Show Solution – display algorithm path



⏭️ Next Level – increase maze size



🔄 Retry – restart the current maze











4\. Project Structure



DAA PROJECT.py

│

├── Maze Generation

│   ├── generate\_maze()     # Creates random walls

│   └── generate\_weights()  # Assigns random weights to cells

│

├── Algorithms

│   ├── bfs()

│   ├── dfs()

│   ├── dijkstra()

│   └── astar()

│

└── GUI + Gameplay

   ├── draw\_maze(), draw\_player()

   ├── move\_player(), check\_player\_path()

   ├── show\_correct\_path(), regenerate\_maze(), next\_level()

   └── Tkinter window setup















5\. Example

Start (Green) 	Goal (Red)	 Player (Blue)  	Path (Orange)
    🟩				       🟥				  🔵				        🟧







6\. Future Enhancements

	1..Add diagonal movement
	2..Show cell weights visually
  3..Add scoring and timer system
	4..Create leaderboard or time-based challenges
	5..Package as a standalone .exe or .app



👨‍💻 Author

DIVYANSH SINGH PARMAR

📧 divyanshsingh2875@gmail.com

💼 LinkedIn -www.linkedin.com/in/divyansh-singh-parmar-745205368



⭐ If you like this project, give it a star on GitHub!

