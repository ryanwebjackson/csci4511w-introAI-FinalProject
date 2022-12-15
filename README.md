# csci4511w-introAI-FinalProject

IMMEDIATE TODOs:  
I. Determine by terminal_test result is always false.  
1. ~~Ensure Goal state is not pruned.~~
  - Not sure how to guarantee this. Made a comment.
  - Tried changing some code to get terminal_test to be true.
3. ~~Change terminal_test back to old logic - to get it working and not have conflicting goals.~~

II. **Write GENETIC algorithm solution**

## Search for optimal fitness plan for pet animal

TODO:
1. ~~Determine algorithms used for solution search - adversarial search first~~  
1.5. Define the problem ("game") formally: What are the states and actions? What is the initial state, goal state, and what are the constraints on transitions between states?
2. Determine how to interact with the user/consuming researcher/peer - candidate: Jupyter IPython notebooks
3. Run experiments (simulations and real-world)
4. Analyze results
5. Draw conclusions, and finish write-up

*Through iterative experimentation, several specific approaches will be tried, and the results will be compared. Below are the current ideas I have for these:*
- Mini-Max (with and without A-B pruning, to see the performance (comp. and memory) difference)
- Genetic algorithms (2 forms)  
Note on verbiage (problem framing): https://www.sciencedirect.com/science/article/pii/S016518890000066X
- Reinforcement learning
- Monte-Carlo Tree Search
- Random activity from both agents - serves as a control group
