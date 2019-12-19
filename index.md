---
layout: default
title: School Projects
---

# Tetris AI
<video controls autoplay>
  <source src="/assets/tetris.ogg" type="video/ogg">
  Your browser does not support the video tag.
</video> 

In this project, I developed an AI which can play Tetris indefinitely by using a genetic algorithm. 

The AI looks for the best move for a given Tetris piece by trying out all the possible moves. The score of one move is computed by doing the dot product between a vector of parameters of the AI and a vector of grid data, composed of the aggregate height, complete lines, holes and bumpiness. The genetic algorithm then gets the best parameters for the AI.


# Superpixels
<!-- ![Superpixels](/assets/poisson.jpeg) -->

 <img src="assets/poisson.jpeg" alt="Poisson" style="height:323px;width:533px;"> 

Image segmentation with superpixels allows for a great simplification of images while keeping their visual characteristics, making it a highly valued asset in computer vision and learning applications. Two types of such methods are outlined : graph-based and gradient-ascent-based algorithms. 

In this paper we focus on the gradient-ascent-based SLIC
(Simple Linear Image Clustering), which offers segmentation based on a given relative weight of proximity over similarity for pixel clustering and given number of superpixels. This ensures uniformity and compactness of the resulting superpixels, which is quite relevant for shape recognition purposes. The SCALP (Super Pixels with Contour Adherence using Linear Path) takes into account a contour map of the picture for higher visual accuracy in the segmentation. You can [get the PDF](/assets/superpixels.pdf) in French.


# Inpainting

 <img src="assets/inpainting.jpg" alt="Inpainting"> 
 
We studied an image inpainting algorithm. This algorithm removes large objects from digital images, while filling the hole that is left behind in a visually plausible way by propagating texture and structure information simultaneously. You can [get the PDF](/assets/inpainting.pdf) in French.


