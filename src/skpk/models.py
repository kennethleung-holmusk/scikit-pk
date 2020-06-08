# =========================
#        Model Class
# =========================
# Fold all functions: Ctrl + Alt + Shift + [
# Pending to do
# - GraphViz
# - Solving ODE function
# - Docstrings (Numpy)
# - Create modlib folder to save and store pre-built PK models
# - User defined errors (and review error messages)
# - Unit testing
# - Tutorial (HTML instructions guide)

import numpy as np
from .compartments import Cmt
import graphviz
import pydot

class Model:

    list_model_names = []

    def __init__(self, modelname):
        self.list_cmt_links = [] # Storing links as original compartment objects
        self.list_cmt_link_tuples = [] # Storing as unpacked tuples
        self.list_cmts = [] # Storing compartmant instance objects
        self.__check_model_name_exist(modelname)
        self.modelname = modelname
        self.list_model_names.append(self.modelname)
        print(f" Model named {modelname} successfully generated. Start by adding compartments")


    def __check_model_name_exist(self, modelname):
        if modelname in self.list_model_names:
            raise Exception(f"""Model name {modelname} already exists
            List of existing model names:
            {self.list_model_names}""")


    def __check_cmt_exist(self, cmt):
        cmt_id = cmt.cmt_attr[0]
        existing_cmt_ids = [cmt.cmt_attr[0] for cmt in self.list_cmts]
        if cmt_id in existing_cmt_ids:
            raise Exception(f"""Compartment {cmt.cmt_name} already exists.
            List of existing compartments:
            'Edit Later' """)


    def __check_cmt_initiated(self, link_input):
        if (link_input[0] in self.list_cmts) == False:
            raise Exception(f"""
            Compartment {link_input[0].cmt_id}-{link_input[0].cmt_name} does not exist in model instance.
            Add compartment instance into model with the .add_cmt method
            """)
        if (link_input[1] in self.list_cmts) == False:
            raise Exception(f"""
            Compartment {link_input[1].cmt_id}-{link_input[1].cmt_name} does not exist in model instance.
            Add compartment instance into model with the .add_cmt method
            """)


    def __check_link_exist(self, link_input):
        existing_links = [(tuple[0], tuple[1]) for tuple in self.list_cmt_links]
        if (link_input[0],link_input[1]) in existing_links:
            raise Exception(f"""Link ({link_input[0].cmt_attr[0]}) -> ({link_input[1].cmt_attr[0]}) already exists.
            List of existing links: {existing_links}""")


    def __check_tuple_criteria(self, object):
        if isinstance(object, tuple) == False:
            raise TypeError(f"Input must be a tuple")
        if (len(object) > 3 or len(object) < 2):
            raise Exception(f"""Each link tuple should have either 2 or 3 elements.
            {object} has {len(object)} elements.""")
        if (isinstance(object[0], Cmt) and isinstance(object[1], Cmt)) == False:
            raise Exception('The first two elements of link tuple must be of Cmt class')


    def __check_k_dtype(self, k):
        if isinstance(k, (float, int)) == False:
            raise ValueError("k rate constant value needs to be integer or float")


    def __check_link_criteria(self, link_input):
        '''
        Check whether the input list of tuples satisfies the existing criteria
        i.e. Tuple length 2 - 3, and link pair should not be existing already
        '''
        if isinstance(link_input, (tuple, list)) == False:
            raise ValueError('Input must be a tuple or a list of tuples')
        else:
            if isinstance(link_input, tuple):
                k = link_input[2]
                self.__check_k_dtype(k)
                self.__check_tuple_criteria(link_input)
                self.__check_cmt_initiated(link_input)
                self.__check_link_exist(link_input)
            else:
                # If input is a list
                for link_tuple in link_input:
                    k = link_tuple[2]
                    self.__check_k_dtype(k)
                    self.__check_tuple_criteria(link_tuple)
                    self.__check_cmt_initiated(link_tuple)
                    self.__check_link_exist(link_tuple)


    def __append_link(self, tuple):
        if len(tuple) == 3:
            self.list_cmt_links.append(tuple)
            self.__update_cmt_link_tuples()
        # If no k rate constant stated in link tuple, automatically assign k = 0
        if len(tuple) == 2:
            new_tuple = (tuple[0], tuple[1], 0)
            self.list_cmt_links.append(new_tuple)
            self.__update_cmt_link_tuples()


    def __update_cmt_link_tuples(self):
        '''
        Append unpacked 5-element tuple (From ID, From Name, To ID, To Name, k)
        Unpacking from 3-element tuple into 5-element tuple
        5-element link tuple: (From ID, From Name, To ID, To Name, k)
        '''
        self.list_cmt_link_tuples = [] # Reset list first since there will be changes
        for link in self.list_cmt_links:
            unpacked_tuple = (link[0].cmt_attr[0], # First element of Cmt attr is ID
                            link[0].cmt_attr[1], # Second element of Cmt attr is Name
                            link[0].cmt_attr[2], # Third element of Cmt attr is Volume
                            link[1].cmt_attr[0],
                            link[1].cmt_attr[1],
                            link[1].cmt_attr[2],
                            link[2])
            self.list_cmt_link_tuples.append(unpacked_tuple)


    def add_cmt(self, cmt_input):
        if isinstance(cmt_input, (Cmt, list)) == False:
            raise ValueError("""
            Arguments must be of Cmt class or list of Cmt instances
            """)
        else:
            if isinstance(cmt_input, Cmt):
                self.__check_cmt_exist(cmt_input)
                self.list_cmts.append(cmt_input)
            else:
                for cmt in cmt_input:
                    self.__check_cmt_exist(cmt)
                    self.list_cmts.append(cmt)


    def add_link(self, link_input):
        '''
        Adds a single-directional link between the 2 compartments listed in first 2 elements of input tuple,
        and includes the k-constant attribute to the link if specified as the 3rd element in the input tuple.
        If no 3rd element stated, the k constant for the link automatically defaults to a value of 0
        '''
        self.__check_link_criteria(link_input)
        if isinstance(link_input, list):
            for tuple in link_input:
                self.__append_link(tuple)
        else:
            self.__append_link(link_input)


    def get_all_links(self):
        link_list = self.list_cmt_link_tuples.copy() # Using the list of unwrapped tuples
        # Display tuples in formatted tabular form:
        # Ref: https://stackoverflow.com/questions/53504145/creating-a-formatted-table-from-a-list-of-tuples
        w = {0:0, 3:len(str(' '*5) + "From CMT (ID - Name)" + str(' '*5)),
                    2:len(str(' '*5) + "To CMT (ID - Name)" + str(' '*5)),
                    1:len(str(' '*5) + "k rate constant" + str(' '*5))}
        col1, col2, col3 = ["From CMT (ID - Name)", "To CMT (ID - Name)",\
                            "k rate constant"]
        print(f"{col1:<{w[3]}}|{col2:<{w[3]}}|{col3:<{w[3]}}")
        print("-" * 75)
        for link in link_list:
            from_cmt = f'{link[0]} - {link[1]}'
            to_cmt = f'{link[3]} - {link[4]}'
            k = link[6]
            print(f"{from_cmt:<{w[3]}}|{to_cmt:<{w[3]}}|{k:<{w[1]}}")


    def __get_linked_cmts_in_model(self):
        linked_cmts_0 = [tuple[0] for tuple in self.list_cmt_links]
        linked_cmts_1 = [tuple[1] for tuple in self.list_cmt_links]
        linked_cmts = list(set(linked_cmts_0 + linked_cmts_1)) # Remove duplicates
        return linked_cmts


    def linked_cmts(self):
        '''
        Returns list of cmts which are linked to any other cmt
        '''
        print('\n--- Linked Compartments ---')
        linked_cmts = self.__get_linked_cmts_in_model()
        for cmt in linked_cmts:
            print(f"{cmt.cmt_attr[0]} - {cmt.cmt_attr[1]}")

        print('\n--- Unlinked Compartments ---')
        unlinked_cmts = list(set(self.list_cmts) - set(linked_cmts))
        for cmt in unlinked_cmts:
            print(f"{cmt.cmt_attr[0]} - {cmt.cmt_attr[1]}")


    def get_all_cmts(self):
        '''
        Return attributes of all compartments added to model
        '''
        cmt_list = [(cmt.cmt_attr[0], cmt.cmt_attr[1], cmt.cmt_attr[2]) for cmt in self.list_cmts]
        # Display tuples in formatted tabular form:
        # Ref: https://stackoverflow.com/questions/53504145/creating-a-formatted-table-from-a-list-of-tuples
        w = {0:0, 3:len(str(' '*7) + "CMT ID" + str(' '*7)),
                    2:len(str(' '*7) + "CMT Name" + str(' '*7)),
                    1:len(str(' '*7) + "CMT Volume" + str(' '*7))}
        col1, col2, col3 = ["CMT ID", "CMT Name", "CMT Volume (L)"]
        print(f"{col1:<{w[3]}} | {col2:<{w[2]}} | {col3:<{w[1]}}")
        print("-" * 70)
        for cmt in cmt_list:
            from_cmt, to_cmt, k = cmt[0], cmt[1], cmt[2]
            print(f"{from_cmt:<{w[3]}} | {to_cmt:<{w[2]}} | {k:<{w[1]}}")


    def summary(self):
        '''
        Returns the attributes for compartments and links of model
        '''
        print(f"\nName of Model Instance = {self.modelname}")
        print(f"Number of Compartments = {len(self.list_cmts)}")
        print(f"Number of Links = {len(self.list_cmt_links)}")
        print(f"\n{str('='*23)} Compartment Attributes {str('='*23)}")
        self.get_all_cmts()
        print(f"\n{str('='*29)} Link Attributes {str('='*29)}")
        self.get_all_links()


    def __check_new_attr_input(self, cmt_id, cmt_name, cmt_vol):
        existing_cmt_ids = [cmt.cmt_attr[0] for cmt in self.list_cmts]
        existing_cmt_names = [cmt.cmt_attr[1] for cmt in self.list_cmts]
        if isinstance(cmt_id, int) == False:
            raise ValueError('Compartment ID must be an integer')
        if isinstance(cmt_name, (str, type(None))) == False:
            raise ValueError('Compartment name must be a string')
        if isinstance(cmt_vol, (int, float, type(None))) == False:
            raise ValueError('Compartment volume must be an integer or a float')
        if cmt_id not in existing_cmt_ids:
            raise Exception(f"""Compartment ID {cmt_id} does not exist.
            List of existing compartment IDs:{existing_cmt_ids}""")
        if cmt_name in existing_cmt_names:
            raise Exception(f"""Compartment name {cmt_name} already exists. Please choose another name.
            If you wish to keep the existing name, leave default cmt_name = None
            List of existing compartment names:{existing_cmt_names}""")


    def __update_cmt_attr_in_links(self, cmt, cmt_id, cmt_name, cmt_vol):
        if isinstance(cmt, Cmt) == True: # Only modify if object is compartment class
            if cmt.cmt_attr[0] == cmt_id:
                tuple_as_list = list(cmt.cmt_attr) # Convert to list for reassignment
                if cmt_name is not None:
                    tuple_as_list[1] = cmt_name
                if cmt_vol is not None:
                    tuple_as_list[2] = cmt_vol
                new_cmt_tuple = tuple(tuple_as_list) # Revert to tuple form
                cmt.cmt_attr = new_cmt_tuple
            else:
                pass
        else:
            pass


    def set_cmt_attr(self, cmt_id, cmt_name = None, cmt_vol = None):
        self.__check_new_attr_input(cmt_id, cmt_name, cmt_vol)
        for cmt in self.list_cmts:
            self.__update_cmt_attr_in_links(cmt, cmt_id, cmt_name, cmt_vol)

        # Update the cmt objects within the list_cmt_links
        for link_tuple in self.list_cmt_links:
            for cmt in link_tuple:
                self.__update_cmt_attr_in_links(cmt, cmt_id, cmt_name, cmt_vol)
                self.__update_cmt_link_tuples()


    def set_link_attr(self, cmt_id_from, cmt_id_to, new_k):
        self.__check_k_dtype(new_k) # Check k is integer or float
        existing_links = [(tuple[0],tuple[3]) \
                            for tuple in self.list_cmt_link_tuples]
        if (cmt_id_from, cmt_id_to) not in existing_links:
            raise Exception(f""" Link does not exist. Use .add_link to add a new link
            List of existing compartment ID link pairs: {existing_links}""")

        for index, link_tuple in enumerate(self.list_cmt_links):
            if (link_tuple[0].cmt_attr[0] == cmt_id_from and
                link_tuple[1].cmt_attr[0] == cmt_id_to):
                    tuple_as_list = list(link_tuple)
                    tuple_as_list[2] = new_k
                    new_link_tuple = tuple(tuple_as_list)
                    self.list_cmt_links[index] = new_link_tuple # Update list_cmt_links
        #Update list_cmt_link_tuples
        self.__update_cmt_link_tuples()


    def clear_model(self):
        self.list_cmts = []
        self.list_cmt_links = []
        self.list_cmt_link_tuples = []
        self.list_model_names = []
        self.modelname = ''
        print('Cleared all compartments and links')


    def remove_cmt(self, *cmt_ids):
        existing_cmt_ids = [cmt.cmt_attr[0] for cmt in self.list_cmts]
        for cmt_id in cmt_ids:
            if isinstance(cmt_id, int) == False:
                raise Exception('Compartment ID must be an integer:')
            if cmt_id not in existing_cmt_ids:
                raise Exception(f"""Compartment ID {cmt_id} does not exist.
                List of existing compartment IDs: {existing_cmt_ids}""")
            for cmt in self.list_cmts:
                if cmt.cmt_attr[0] == cmt_id:
                    self.list_cmts.remove(cmt)

            for link_tuple in self.list_cmt_links:
                if (link_tuple[0].cmt_attr[0] == cmt_id):
                    self.list_cmt_links.remove(link_tuple)

            for link_tuple in self.list_cmt_links:
                if (link_tuple[1].cmt_attr[0] == cmt_id):
                    self.list_cmt_links.remove(link_tuple)

        self.__update_cmt_link_tuples()

        #Or conditional did not work, so above repeat code for 2nd Cmt of tuple
        # for link_tuple in self.list_cmt_links:
            # if (link_tuple[0].cmt_attr[0] == cmt_id) or \
            #       (link_tuple[1].cmt_attr[0] == cmt_id):
            #     self.list_cmt_links.remove(link_tuple)


    def remove_link(self, cmt_id_from, cmt_id_to):
        existing_links = [(tuple[0].cmt_attr[0], tuple[1].cmt_attr[0]) \
                        for tuple in self.list_cmt_links]
        if (cmt_id_from,cmt_id_to) not in existing_links:
            raise ValueError(f"""
            Link pair ({cmt_id_from},{cmt_id_to}) does not exists.
            List of existing link pairs: {existing_links}""")
        for link_tuple in self.list_cmt_links:
            if (link_tuple[0].cmt_attr[0] == cmt_id_from and
                link_tuple[1].cmt_attr[0] == cmt_id_to):
                self.list_cmt_links.remove(link_tuple)
        self.__update_cmt_link_tuples()


    def get_matrix(self):
        # Convert list of tuples to list of arrays
        array_list = [list(tuple) for tuple in self.list_cmt_link_tuples]

        # Matrix dimensions = n x n, where n is number of linked compartments
        matrix_dim = len(self.__get_linked_cmts_in_model())

        # Generate empty matrix (shape n x n)
        matrix = np.zeros(shape=(matrix_dim, matrix_dim))

        # Get smallest compartment ID Value in model
        min_dim = min(min([array[0] for array in array_list]),
                        min([array[3] for array in array_list]))

        for array in array_list:
            # Subtract min_dim to allow correct (zero-) indexing in matrix
            row = array[0] - min_dim
            col = array[3] - min_dim
            matrix[row][col] = array[6]

        print(matrix)







    def diagram(self):
        # GraphViz
        pass
