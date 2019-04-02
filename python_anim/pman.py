import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(6, 6))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
#ax = fig.add_axes([-5, -5, 5, 5], frameon=False)
#ax.set_xlim(0, 1), ax.set_xticks([])
#ax.set_ylim(0, 1), ax.set_yticks([])
ax.set_xlim(-5, 5), ax.set_xticks([-4,-3,-2,-1,0,1,2,3,4])
ax.set_ylim(-5, 5), ax.set_yticks([-4,-3,-2,-1,0,1,2,3,4])

n_actors = 2
actors = np.zeros(n_actors, dtype=[('position', float, 2),
                                      ('size',     float, 1),
                                      ('color',    float, 4)])


# Initialize the actors in random positions 
#actors['position'] = np.random.uniform(0, 1, (n_actors, 2))
actors['position'][0,0] = 0
actors['position'][0,1] = 0
actors['position'][1,0] = 3
actors['position'][1,1] = 3
#actors['position'][0] = 0
#actors['position'][1] = 0

# Construct the scatter which we will update during animation as actors move.
print(actors['position'][:,0])
scat = ax.scatter(actors['position'][:, 0], actors['position'][:, 1],
                  s=actors['size'], lw=0.5, edgecolors=actors['color'],
                  facecolors='yellow')


def update(frame_number):
    print(frame_number)
    # Get an index which we can use to re-spawn the oldest raindrop.
    current_index = frame_number % n_actors

    # Make all circles bigger.
#    actors['size'] += actors['growth']

    # Pick a new position for oldest rain drop, resetting its size,
    # color and growth factor.
#    actors['position'][current_index] = np.random.uniform(0, 5, 2)
    actors['position'][current_index] = np.random.randint(0, 5, 2)
    actors['size'][current_index] = 350
    actors['color'][current_index] = (0, 0, 0, 1)

    # Update the scatter collection, with the new colors, sizes and positions.
    scat.set_edgecolors(actors['color'])
    scat.set_sizes(actors['size'])
    scat.set_offsets(actors['position'])

# Construct the animation, using the update function as the animation director.
# Lower interval --> faster animation.
plt.grid(True)
animation = FuncAnimation(fig, update, interval=900)

plt.show()
