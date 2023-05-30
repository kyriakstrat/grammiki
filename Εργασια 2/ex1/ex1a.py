# import pymprog modeler functions
import pymprog
'''
# max z = 2x1 + 4x2+x3+x4
# st
#      x1 + 3x2 + x4<=  8
#     2x1 + x2 <= 6
#      x2+4x3+x4 <=  6
# x1, x2,x3,x4 >= 0
'''
# -------------
def solver(): 
    # begin modelling
    model = pymprog.model('ex1a')
    model.solver('simplex')
    # variables
    x1 = model.var('x1', kind=float, bounds=(0, None))
    x2 = model.var('x2', kind=float, bounds=(0, None))
    x3 = model.var('x3', kind=float, bounds=(0, None))
    x4 = model.var('x4', kind=float, bounds=(0, None))
    # objective
    model.maximize(2*x1+4*x2+x3+x4, 'z')

    # constraints
    y1 = x1+3*x2+x4<= 8
    y2 = 2*x1 + x2<= 6
    y3 = x2+4*x3+x4<=6
    # solve the problem
    model.solve()

    # print objective
    print(f' z = {model.vobj():0.2f}')

    # print the value of the variables
    print('values:')
    print(f'x1 = {x1.primal:.2f}')
    print(f'x2 = {x2.primal:.2f}')
    print(f'x3 = {x3.primal:.2f}')
    print(f'x4 = {x4.primal:.2f}')
    model.sensitivity()

# --------
if __name__=='__main__':
    solver()
