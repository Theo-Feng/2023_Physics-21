import matplotlib.pyplot as plt

print("The mass of the object is:")
mass = float(input())

print("The spring constant is:")
spring_constant = float(input())

print("The damping coefficient is:")
damping_coefficient = float(input())

print("The initial position is:")
initial_position = float(input())

print("The initial velocity is:")
initial_velocity = float(input())



total_time = 10.0  
time_step = 0.01  


time_values = []
position_values = []


position = initial_position
velocity = initial_velocity


for t in range(int(total_time / time_step)):
    force = -spring_constant * position - damping_coefficient * velocity
    acceleration = force / mass
    velocity += acceleration * time_step
    position += velocity * time_step
    time_values.append(t * time_step)
    position_values.append(position)


plt.plot(time_values, position_values)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Vibration Position vs. Time")
plt.grid(True)
plt.show()
