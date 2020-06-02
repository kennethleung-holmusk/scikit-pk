# Docstring template
"""
numpydoc

Parameters
----------
first : array_like
    the 1st param name `first`
second : {'value', 'other'}, optional
    the 3rd param, by default 'value'

Returns
-------
string
    a value in a string

Raises
------
KeyError
    when a key error
OtherError
    when an other error
"""

# =========================
#     Compartment Class
# =========================

class Cmt:
    '''
    Compartment class
    '''

    def __init__(self, cmt_name, Vd=0):
        '''
        docstring
        '''
        if isinstance(cmt_name, str) == False:
            raise Exception('Compartment name must be a string')
        if isinstance(Vd, (int, float)) == False:
            raise Exception('Vd must be an integer or float')
        self.cmt_name = cmt_name
        self.Vd = Vd
        self.cmt_attr = (cmt_name, Vd)
        print(f'Compartment {cmt_name} has been generated')


    def set_attr(self, new_Vd):
        '''
        Modify the attributes of an existing compartment instance
        '''
        self.Vd = new_Vd
        self.cmt_attr = (self.cmt_name, new_Vd)


    def get_attr(self):
        '''
        Return the attributes of an existing compartment instance
        '''
        print(f"Name of Compartment: {self.cmt_name}")
        print(f"Volume of Distribution (Vd): {self.Vd}L")
