---
layout: default
title: 
---

# Tetris AI
<video controls autoplay>
  <source src="/assets/tetris.ogg" type="video/ogg">
  Your browser does not support the video tag.
</video> 

# Superpixels
<!-- ![Superpixels](/assets/poisson.jpeg) -->

 <img src="assets/poisson.jpeg" alt="Poisson" style="height:323px;width:533px;"> 
 
# Inpainting

 <img src="assets/inpainting.jpg" alt="Inpainting"> 

 
# Navigation
{% include navigation.html %}

# Posts
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

