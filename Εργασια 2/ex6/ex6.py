import pymprog
import numpy as np

def minimize_weighted_sum(P,C,Q):
    # Create a model
    pymprog.begin('Weighted Sum Minimization')
    # Define variables
    num_vars = len(C)
    x = [pymprog.var(f'x{i+1}',kind=int, bounds=(0, 1)) for i in range(num_vars)]
    # Set the objective function

    pymprog.maximize(np.dot(P, x))

    # Add any additional constraints if required
    # ...
    np.dot(C,x) <= Q
    x[2]+x[3]<=1
    x[4]+x[5]<=1
    x[4]+x[5]-x[2]-x[3] <= 0
    x[0]+x[1]+x[6]+x[7]+x[8]+x[9]<=4
    x[0]+x[1]+x[6]+x[7]+x[8]+x[9]>=2

    # Solve the linear programming problem
    pymprog.solve()

    # Print the optimal solution
    print("Optimal Solution:")
    for i, var in enumerate(x):
        print(f"{var.name} = {var.primal}")

    # Print the objective value
    print("Objective Value:")
    print(f"Minimized Sum = {pymprog.vobj()}")

    # End the model
    pymprog.end()

# Example usage
P = np.random.uniform(5,40,(10)).tolist() 
C = np.random.uniform(5,40,(10)).tolist()

print('P:',P)
print('C:',C)

minimize_weighted_sum(P,C,70)
