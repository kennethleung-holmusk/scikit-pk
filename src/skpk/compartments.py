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
    id_counter = 1 # Assigning incremental ID to compartment instances
    list_cmt_ids = []
    list_cmt_names = []

    def __check_cmt_id_exist(self, cmt_id):
        if cmt_id in self.list_cmt_ids:
            raise Exception(f'Compartment ID {cmt_id} already exists')

    def __check_cmt_name_exist(self, cmt_name):
        if cmt_name in self.list_cmt_names:
            raise Exception(f'Compartment name {cmt_name} already exists')

    def __check_cmt_name_dtype(self, cmt_name):
        if isinstance(cmt_name, (str, type(None))) == False:
            raise ValueError('Compartment name (cmt_name) must be a string')
        else:
            pass

    def __check_cmt_Vd_dtype(self, Vd):
        if isinstance(Vd, (int, float, type(None))) == False:
            raise ValueError('Vd must be an integer or float')
        else:
            pass

    def __check_cmt_id_dtype(self, cmt_id):
        if isinstance(cmt_id, (int, type(None))) == False:
            raise ValueError('Compartment ID (cmt_id) must be an integer')
        else:
            pass


    def __init__(self, cmt_name, Vd = 0):
        '''
        docstring
        '''
        self.__check_cmt_name_dtype(cmt_name)
        self.__check_cmt_Vd_dtype(Vd)
        self.__check_cmt_name_exist(cmt_name)

        self.cmt_name = cmt_name
        self.Vd = Vd
        self.cmt_id = Cmt.id_counter

        self.list_cmt_ids.append(self.cmt_id) # Collate compartment IDs in list
        self.list_cmt_names.append(self.cmt_name) # Collate compartment names in list

        Cmt.id_counter += 1
        self.cmt_attr = (self.cmt_id, self.cmt_name, self.Vd)
        print(f'Compartment {cmt_name} has been generated')



    def set_attr(self, cmt_id = None, cmt_name = None, Vd = None):
        '''
        Modify the attributes of an existing compartment instance
        '''

        if cmt_id is None:
            self.cmt_id = self.cmt_id # If no new ID input, then keep existing ID
        else:
                self.__check_cmt_id_dtype(cmt_id)
                self.__check_cmt_id_exist(cmt_id)
                self.cmt_id = cmt_id # Assign new ID

        if cmt_name is None:
            self.cmt_name = self.cmt_name # If no new name input, then keep existing name
        else:
            self.__check_cmt_name_dtype(cmt_name)
            self.__check_cmt_name_exist(cmt_name)
            self.cmt_name = cmt_name # Assign new name

        if Vd is None:
            self.Vd = self.Vd  # If no new Vd input, then keep existing Vd value
        else:
            self.__check_cmt_Vd_dtype(Vd)
            self.Vd = Vd # Assign new Vd

        self.cmt_attr = (self.cmt_id, self.cmt_name, self.Vd) # Update attributes tuple


    def get_attr(self):
        '''
        Return attributes of an existing compartment instance
        '''
        print(f"Compartment ID: {self.cmt_id}")
        print(f"Compartment Name: {self.cmt_name}")
        print(f"Volume of Distribution (Vd): {self.Vd} L")
