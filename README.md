# Numerical Modelling
This is a repository for the codes that I have used to numerically model, most often, physics situations.

## bifurcationlogistic.py
![intro](https://github.com/stangeqwq/NumericalModelling/blob/main/images/bifurcationlogistic.png)
This is a program that uses `matplotlib` to plot different equations such as `differential equations` for different types of oscillators and the `logistic equation`. In addition, the program handles some basic `chaos theory` in the form of `bifurcation` of the logistic equation and the chaotic driven damped pendulum.
The code has some initial constants given which print out standard graphs of the differential equations. These constants can be edited from the program to suit the physical models that one might need in a class.
For example, for the driven damped pendulum, given by the differential equation, $$mL^2\theta'' + bL^2\theta' + Lmgsin(\theta) = F(t)$$ where $F(t)$ is a periodic driving force, the graph is given by below with the following constants $\theta = 1$, b = 0.5, $\theta'$ = 0, m = 1, L = 1, g = 9.8. This is a system which exhibits chaotic motion as a result of the non-linear term `sin𝚹` in the differential equation.

![chaos](https://github.com/stangeqwq/NumericalModelling/blob/main/images/drivendamped.png)
### User interface of the program

```console
(base) stange@ericjoshua Desktop % python3 program.py
Hey, welcome to my program! Choose an option:
(1) The Logistic Equation
(2) An undamped oscillator
(3) A damped oscillator
(4) A driven damped oscillator
(5) Bifurcation Diagram of the logistic equation
Enter option: 
```

### LaplaceEquation.ipynb
My project submission for the course `FY1003` Electricity and Magnetism at NTNU Spring 2024 where we had to plot the potential of a parallel plate capacitor using laplace equation $\nabla^2 V = 0$ given some boundary conditions.
![pot](https://github.com/stangeqwq/NumericalModelling/blob/main/images/Potential.png)

![quiv](https://github.com/stangeqwq/NumericalModelling/blob/main/images/quiverplotE.png)


