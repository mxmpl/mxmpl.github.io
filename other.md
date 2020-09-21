---
layout: perso
title: Other 
---

# Tetris AI
<video controls autoplay>
  <source src="/assets/tetris.ogg" type="video/ogg">
  Your browser does not support the video tag.
</video> 

In this project, I developed a model that can play Tetris by using a genetic algorithm.

Before getting the final model, we consider one "generation" that consists of multiple "genomes" that each have their own parameters $$\theta \in \mathbb{R}^4$$ with $$ -1 \leq \theta_i \leq 1$$. 

Each genome plays a certain amount of moves. At the end, we cross the parameters of the best genomes to obtain a new generation. We repeat this until we have a genome that plays well enough.

I used 10 generations, each with 100 genomes that plays at most 500 moves (less if they lose the game). For the next generation, I kept the 70% best genomes. The 30% left are new genomes that are children of two parent genomes, with their parameters as the sum of the parents' parameters weighted by their respective score. For each child, I randomly select 10% of the current genomes and the two best genomes are the future parents.

At each turn $$t$$, the genome knows the state of the game (for every cell it knows if it contains a block or not), the tetromino that is coming and the next one. This is used to know what are the valid moves, and to get a "data vector" $$x^{m} \in \mathbb{R}^4$$ after the move $$m$$ is played. We have for a data vector obtained after playing a move $$m$$:

* $$x^m_1$$ is the sum of the heights of each column of the grid.
* $$x^m_2$$ is the number of lines that are completed by playing the move $$m$$.
* $$x^m_3$$ is the number of holes in the grid (one cell is a hole if it has at least one occupied cell above it).
* $$x^m_4$$ is the *bumpiness* of the grid, ie the sum of height differences between two adjacent columns.

The best move to play at time $$t$$ given the information at this time is defined as follows:

\\[m_t^* = \arg \max_{m_t | m_t, m_{t+1} \text{valid}}  \< \theta, x^{m_t} \> + \< \theta, x^{m_{t+1}} \> \\]
It is implicit that we check for the validity one move after the other, so that the validity of a move $$m_{t+1}$$ is computed after a move $$m_t$$ has been played.
Thus, we play at each turn the best move that can be done given the parameters of the genome, the current tetromino and the one to come, without taking into account what can come after that or some knowledge about the distribution of tetrominoes, etc.

The parameters converged surprisingly quickly, at in just three generations I had the optimal parameters for this framing of the problem. I had introduced a mutation factor, but it was not very useful here. In the end, I had:

\\[ \theta = \begin{pmatrix} -0.590814 & \\ 0.491538 & \\ -0.337213 & \\ -0.517931 \end{pmatrix}\\]

A genome with those parameters can play indefinitely.
# Generating all tilings of rectangles by dominos

Coming soon 
