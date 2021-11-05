<div id="top"></div>

[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# ParametricVectorOps

https://user-images.githubusercontent.com/40839237/140433617-4ed81716-80bf-4ca1-b8f9-05d0c2245b10.mp4


https://user-images.githubusercontent.com/40839237/140452835-7d9d2d49-3cc2-457d-a5db-d3f995aa0d63.mp4


## About The Project


This is a 3D graphing calculator that can plot and visualize parametric vectors and functions in up to 4 dimensions. (Including time). The program works best with parametricized functions, but a cartesian and polar conversion feature will be added in the near future.

The calculator requires OpenGL and Pygame to run the graphics, while the calculus operationsare handled by my own equation formatting/solving algorithm that uses sympy for someoperations.I hope to develop this into an online (published)  calculator that students can use to visualize themulti-dimensional problems one encounters in physics and calculus.Challenges:Due to the processing-intensive nature of 3D computer graphics, it was hard to make theprogram run for large intervals of time on devices such as tablets. To solve this issue, I createdmy own memory management system that avoids unnecessary calculations by storing the datain a temporary list that is used to pause the program and make it seem as if the program is stillactively calculating values.The greatest challenge with the calculator was ensuring that the users’ typed equations are notmisinterpreted by the algorithms and libraries. As a solution to this issue, I programmed my ownset of vector and parametric algorithms that not only formatted data, but also performed thenecessary scaling with derivatives to provide a seamless user experience.

![Screenshot (19)](https://user-images.githubusercontent.com/40839237/140453833-3eca0725-ebc0-4115-8e97-fab4ee3b5602.png)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* PyOpenGL
* PyOpenGL_accelerate
* pygame
* sympy
* tabulate

### Installation

http://pyopengl.sourceforge.net/

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
1. Select the Parametric Graphing feature by entering "3"
2. Enter the type of function. ex.  x(t), v(t), a(t)
3. Enter the vector function with respect to "t"
4. Provide the initial coordinate   x,y,z
5. Enter Initial time
6. Enter Final time 
7. Use the Arrow keys to rotate the graph.
8. Use Tables in Console to determine magnitudes and components.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/dahvid12/ParametricVectorOps/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/dahvid12/ParametricVectorOps/network/members
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/dahvid12/ParametricVectorOps/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/david-martinez-6785b11a2/
