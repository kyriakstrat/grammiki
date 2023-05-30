# import pymprog modeler functions
import pymprog

# -------------
def solver(): 
    # begin modelling
    model = pymprog.model('ex3')
    model.solver('intopt')
    # variables
    x1 = model.var('x1', kind=int, bounds=(0, None))
    x2 = model.var('x2', kind=int, bounds=(0, None))
    x3 = model.var('x3', kind=int, bounds=(0, None))
    x4 = model.var('x4', kind=int, bounds=(0, None))
    x5 = model.var('x5', kind=int, bounds=(0, None))

    # objective
    model.minimize(170*x1+160*x2+175*x3+180*x4+195*x5, 'z')

    # constraints
    x1>= 48
    x1+x2>=79
    x1+x2+x3 >= 87
    x2+x3>=64
    x3+x4>=82
    x4>=43
    x4+x5>=52
    x5>=15
    model.solve()

    # print objective
    print(f' z = {model.vobj():0.2f}')

    # print the value of the variables
    print('values:')
    print(f'x1 = {x1.primal:.2f}')
    print(f'x2 = {x2.primal:.2f}')
    print(f'x3 = {x3.primal:.2f}')
    print(f'x4 = {x4.primal:.2f}')
    print(f'x5 = {x5.primal:.2f}')

    model.sensitivity()

# --------
if __name__=='__main__':
    solver()
