# import pymprog modeler functions
import pymprog
'''

'''
# -------------
def solver(): 
    # begin modelling
    model = pymprog.model('ex1a')
    model.solver('simplex')
    # variables
    x1 = model.var('x1', kind=float, bounds=(-2,10))
    x2 = model.var('x2', kind=float, bounds=(5,25))
    x3 = model.var('x3', kind=float, bounds=(0, None))
    x4 = model.var('x4', kind=float, bounds=(0, None))
    x5 = model.var('x5', kind=float, bounds=(None, None))

    # objective
    model.maximize(3*x1-2*x2-5*x3+7*x4+8*x5, 'z')

    # constraints
    x2-x3+3*x4-4*x5==-6
    2*x1 +3*x2-3*x3-x4 >= 2
    x1+2*x3-2*x4<=-5
    # solve the problem
    model.solve()

    # print objective
    print(f' z = {model.vobj():0.2f}')

    # print the value of the variables
    print('values:')
    print(f'x1 = {x1.primal:.2f}')
    print(f'x2 = {x2.primal:.2f}')
    print(f'x3 = {x3.primal:.2f}')
    print(f'x4= {x4.primal:.2f}')
    print(f'x5= {x5.primal:.2f}')
    model.sensitivity()

# --------
if __name__=='__main__':
    solver()
