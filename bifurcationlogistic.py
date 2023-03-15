import matplotlib.pyplot as plt
import math
import numpy as np

print("Hey, welcome to my program! Choose an option:")
print("(1) The Logistic Equation")
print("(2) An undamped oscillator")
print("(3) A damped oscillator")
print("(4) A driven damped oscillator")
print("(5) Bifurcation Diagram of the logistic equation")
try:
	option = int(input("Enter option: "))
	if (option in [1, 2, 3, 4, 5]) == False: print("Please choose appropriately")

	if option == 1:
		r = float(input("Enter r for the logistic equation:"))
		x0 = float(input("Enter x0 (n/N) for the logistic equation:"))
		t = []
		x = []
		def L(x):
			return r*x*(1 - x)

		for i in range(100):
			x.append(x0)
			t.append(i)
			x0 = L(x0)

		plt.plot(t, x)
		plt.xlabel('x - axis')
		plt.ylabel('y - axis')
		plt.title('Logistic equation')
		plt.show()

	elif option == 2: #undamped oscillator
		dt = 0.001
		time = 0
		t = []
		x = []
		k = 1
		x0 = 1
		v = 0
		m = 1
		def D2(x):
			return -k*x
		while time < 100:
			x.append(x0)
			t.append(time)
			v = v + D2(x0)*dt
			x0 = x0 + v*dt
			time += dt
		plt.plot(t, x)
		plt.xlabel('x - axis (t)')
		plt.ylabel('y - axis (x)')
		plt.title('plot of mx\'\' = -kx')
		plt.show()

	elif option == 3: # damped oscillator
		dt = 0.0001
		time = 0
		t = []
		x = []
		k = 3
		x0 = 1
		b = 0.5
		v = 0
		m = 1
		def D2(x, v):
			return -k*x - b*v
		while time < 100:
			x.append(x0)
			t.append(time)
			v = v + D2(x0, v)*dt
			x0 = x0 + v*dt
			time += dt

		plt.plot(t, x)
		plt.xlabel('x - axis (t)')
		plt.ylabel('y - axis (x)')
		plt.title('plot of mx\'\' = -kx - bv')
		plt.show()

	elif option == 4: # driven damped pendulum x = angular displacement, mL^2x'' + bL^2x' + Lmgsin(x) = F(t) => x'' = -(b/m)x' - gsin(x) + F(t)/mL  
		dt = 0.01
		time = 0
		t = []
		x = []
		x0 = 1
		b = 0.5
		v = 0
		m = 1
		L = 1
		g = 9.8
		A = 20
		def F(t):
			return A*math.cos(t)

		def D2(x, v, t):
			return -(g/L)*math.sin(x) - (b/m)*v + (F(t)/(m*L))
		while time < 300:
			x.append(x0)
			t.append(time)
			v = v + D2(x0, v, time)*dt
			x0 = x0 + v*dt
			time += dt

		plt.plot(t, x)
		plt.xlabel('x - axis (t)')
		plt.ylabel('y - axis (x)')
		plt.title('plot of mLx\'\' + bLx\' + Lmgsin(x) = F(t)')
		plt.show()

	elif option == 5: #bifurcation diagram for the logistic equation

		def L(r, x):
			return r*x*(1 - x)

		periodDriver = 0.01
		periodFunction = 2
		iteration = 0
		Driver = 1.7 #R for logistic equation
		x0 = 0.2 #n/N in the logistic equation

		while Driver < 4: # choosing a variation of r 
			while iteration < 20: # plotting the values for each "r" period
				if iteration > 5:
					plt.scatter(Driver, x0, c="blue")
				x0 = L(Driver, x0)
				iteration += 1
			iteration = 0
		Driver += periodDriver

		plt.xlabel('r of the logistic equation')
		plt.ylabel('x (n/N) of the logistic equation')
		plt.title('bifurcation diagram for the logistic equation (x_{k+1}=rx_{k}(1-x_{k}))')
		plt.show()

except:
	print("Please choose appropriately")

