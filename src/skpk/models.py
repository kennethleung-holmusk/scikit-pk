# =========================
#        Model Class
# =========================

# Pending to do
# - GraphViz
# - Change cmt attributes inside model
# - Remove compartment and links
# - Save and load models
# - Solving ODE function
# - Add CMT ID in table output of .get_links()?
# - Convert all remaining methods in this Model class
# - Docstrings (Sphinx or Numpy?)
# - User defined errors (and review error messages)
# - Unit testing
# - Tutorial (HTML instructions guide)

from .compartments import Cmt

class Model:
    """Short summary.

    :param type modelname: Description of parameter `modelname`.
    :attr type list_cmt_links: Description of parameter `list_cmt_links`.
    :attr type list_cmts: Description of parameter `list_cmts`.
    :attr type __check_model_name_exist: Description of parameter `__check_model_name_exist`.
    :attr type list_model_names: Description of parameter `list_model_names`.
    :attr modelname:

    """
    '''
    Model class (docstring)
    '''
    list_model_names = []

    def __init__(self, modelname):
        self.list_cmt_links = [] # Storing links as original compartment objects
        self.list_cmt_links_tuples = [] # Storing as unpacked tuples
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


    def __check_cmt_exist(self, object):
        if object in self.list_cmts:
            raise Exception(f"""Compartment {object.cmt_name} already exists.
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
            raise Exception(f"""Link ({link_input[0].cmt_name}) -> ({link_input[1].cmt_name}) already exists.
            Use get_link_params to see existing link pairs""")


    def __check_tuple_criteria(self, object):
        if isinstance(object, tuple) == False:
            raise TypeError(f"Input must be a tuple")
        if (len(object) > 3 or len(object) < 2):
            raise Exception(f"""Each link tuple should have either 2 or 3 elements.
            {object} has {len(object)} elements.""")
        if (isinstance(object[0], Cmt) and isinstance(object[1], Cmt)) == False:
            raise Exception('The first two elements of link tuple must be of Cmt class')


    def __check_link_criteria(self, link_input):
        '''
        Check whether the input list of tuples satisfies the existing criteria
        i.e. Tuple length 2 - 3, and link pair should not be existing already
        '''
        if isinstance(link_input, (tuple, list)) == False:
            raise ValueError('Input must be a tuple or a list of tuples')
        else:
            if isinstance(link_input, tuple):
                self.__check_tuple_criteria(link_input)
                self.__check_cmt_initiated(link_input)
                self.__check_link_exist(link_input)
            else:
                # If input is a list
                for object in link_input:
                    self.__check_tuple_criteria(object)
                    self.__check_cmt_initiated(object)
                    self.__check_link_exist(object)


    def __append_link(self, tuple):
        if len(tuple) == 3:
            self.list_cmt_links.append(tuple)
            self.__unpack_link_tuple(tuple)
        # If no k rate constant stated in link tuple, automatically assign k = 0
        if len(tuple) == 2:
            new_tuple = (tuple[0], tuple[1], 0)
            self.list_cmt_links.append(new_tuple)
            self.__unpack_link_tuple(new_tuple)


    def __unpack_link_tuple(self, tuple):
        '''
        Append unpacked 5-element tuple (From ID, From Name, To ID, To Name, k)
        Unpacking from 3-element tuple into 5-element tuple
        5-element link tuple: (From ID, From Name, To ID, To Name, k)
        '''
        unpacked_tuple = (tuple[0].cmt_id,
                            tuple[0].cmt_name,
                            tuple[1].cmt_id,
                            tuple[1].cmt_name,
                            tuple[2])
        self.list_cmt_links_tuples.append(unpacked_tuple)


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


    def get_links(self):
        link_list = self.list_cmt_links_tuples.copy() # Using the list of unwrapped tuples
        # Display tuples in formatted tabular form:
        # Ref: https://stackoverflow.com/questions/53504145/creating-a-formatted-table-from-a-list-of-tuples
        w = {0:0, 3:len(str(' '*5) + "From CMT (ID - Name)" + str(' '*5)),
                    2:len(str(' '*5) + "To CMT (ID - Name)" + str(' '*5)),
                    1:len(str(' '*5) + "k rate constant" + str(' '*5))}
        col1, col2, col3 = ["From CMT (ID - Name)", "To CMT (ID - Name)","k rate constant"]
        print(f"{col1:<{w[3]}}|{col2:<{w[3]}}|{col3:<{w[3]}}")
        print("-" * 75)
        for link in link_list:
            from_cmt = f'{link[0]} - {link[1]}'
            to_cmt = f'{link[2]} - {link[3]}'
            k = link[4]
            print(f"{from_cmt:<{w[3]}}|{to_cmt:<{w[3]}}|{k:<{w[1]}}")


    def clear_model(self):
        self.list_cmts = []
        self.list_cmt_links = []
        self.list_model_names = []
        self.modelname = ''
        print('Cleared all compartments and links')


    def __get_linked_cmts_in_model(self, list_cmt_links):
        linked_cmts_0 = [tuple[0] for tuple in self.list_cmt_links]
        linked_cmts_1 = [tuple[1] for tuple in self.list_cmt_links]
        linked_cmts = list(set(linked_cmts_0 + linked_cmts_1)) # Remove duplicates
        return linked_cmts


    def linked_cmts(self):
        '''
        Returns list of cmts which are linked to any other cmt
        '''
        print('\n--- Linked Compartments ---')
        linked_cmts = self.__get_linked_cmts_in_model(self.list_cmt_links)
        for cmt in linked_cmts:
            print(f"{cmt.cmt_id} - {cmt.cmt_name}")

        print('\n--- Unlinked Compartments ---')
        unlinked_cmts = list(set(self.list_cmts) - set(linked_cmts))
        for cmt in unlinked_cmts:
            print(f"{cmt.cmt_id} - {cmt.cmt_name}")


    def get_all_cmts(self):
        '''
        Return attributes of all compartments added to model
        '''
        cmt_list = [(cmt.cmt_id, cmt.cmt_name, cmt.cmt_vol) for cmt in self.list_cmts.copy()]
        # Display tuples in formatted tabular form:
        # Ref: https://stackoverflow.com/questions/53504145/creating-a-formatted-table-from-a-list-of-tuples
        w = {0:0, 3:len(str(' '*7) + "CMT ID" + str(' '*7)),
                    2:len(str(' '*7) + "CMT Name" + str(' '*7)),
                    1:len(str(' '*7) + "CMT Volume" + str(' '*7))}
        for cmt in cmt_list:
            for i,d in enumerate(cmt):
                w[i] = max(w[i],len(str(d)))
        col1, col2, col3 = ["CMT ID", "CMT Name", "CMT Volume (L)"]
        print(f"{col1:<{w[3]}} | {col2:<{w[2]}} | {col3:<{w[1]}}")
        print("-" * 70)
        for cmt in cmt_list:
            from_cmt, to_cmt, k_constant = cmt[0], cmt[1], cmt[2]
            print(f"{from_cmt:<{w[3]}} | {to_cmt:<{w[2]}} | {k_constant:<{w[1]}}")


    def summary(self):
        '''
        Returns the attributes for compartments and links of model
        '''
        print(f"\nName of Model Instance = {self.modelname}")
        print(f"Number of Compartments = {len(self.list_cmts)}")
        print(f"Number of Links = {len(self.list_cmt_links)}")
        print(f"\n{str('='*23)} Compartment Attributes {str('='*23)}")
        self.get_cmts()
        print(f"\n{str('='*26)} Link Attributes {str('='*26)}")
        self.get_links()





    def set_cmt_attr(self, cmt_id, new_k):
        list_existing_cmt_ids = [cmt.cmt_id for cmt in self.list_cmts]
        if isinstance(cmt_id, int) == False:
            raise ValueError('Compartment ID must be an integer')
        if isinstance(new_k, (int, float)) == False:
            raise ValueError('k constant value must be an integer or a float')
        if cmt_id not in list_existing_cmt_ids:
            raise Exception(f"""Compartment ID does not exist.
            List of existing compartment IDs:{list_existing_cmt_ids}""")
        for cmt_tuple in self.list_cmts:
            if cmt_tuple[0].cmt_id == cmt_id:
                tuple_list_ = list(cmt_tuple) # Convert to list for reassignment
                tuple_list[2] = new_k
                cmt_tuple = tuple(tuple_list)
            else:
                pass


    def set_link_attr(self, cmt_id_1, cmt_id_2):
        pass





    def remove_cmt(self):
        pass

    def remove_link(self):
        pass



    def get_cmt_linked(self, cmt_id):
        if isinstance(cmt_id, int) == False:
            raise ValueError('Compartment ID needs to be an integer')

        linked_cmts = self.__get_linked_cmts_in_model(self.list_cmt_links)
        if (cmt_id in linked_cmts) == False:
            pass




    # def remove_link(self, _pair_tuples):
    #     if any(len(tuple) != 2 for tuple in _pair_tuples):
    #         raise Exception("Link pair should contain only 2 elements in the tuple")
    #     else:
    #         tuples_to_remove = []
    #         for tuple in _pair_tuples:
    #             for existing_tuple in self.link_list:
    #                 if (tuple[0],tuple[1]) == (existing_tuple[0],existing_tuple[1]):
    #                     self.link_list.remove(existing_tuple)
    #                 else:
    #                     pass
        # Update list of compartments (if any changes) in the cmt_list
        # self.__update_cmt_list()





    # def get_cmt_after(self,cmt_id):
    #     '''
    #     Prints the list of compartments linked after the specified input cmt ID
    #     '''
    #     list_of_tuples = [tuple for tuple in self.link_list if tuple[0] == cmt_id]
    #     cmts_after = sorted([i[1] for i in list_of_tuples])
    #     print(f'List of compartments linked after compartment {cmt_id} = {cmts_after}')


    # def get_cmt_prior(self,cmt_id):
    #     '''
    #     Prints the list of compartments linked before the specified input cmt ID
    #     '''
    #     list_of_tuples = [tuple for tuple in self.link_list if tuple[1] == cmt_id]
    #     cmts_prior = sorted([i[0] for i in list_of_tuples])
    #     print(f'List of compartments linked prior to compartment {cmt_id} = {cmts_prior}')



    # def get_linked_cmt(self,cmt_id):
    #     '''
    #     Prints the list of compartments linked before and after the specified input cmt ID
    #     '''
    #     self.get_cmt_prior(cmt_id)
    #     self.get_cmt_after(cmt_id)





    # def has_cmt_after(self, cmt_id):
    #     list_of_tuples = [tuple for tuple in self.link_list if tuple[0] == cmt_id]
    #     if list_of_tuples:
    #         return True
    #     else:
    #         return False
    #
    #
    # def has_cmt_prior(self, cmt_id):
    #     list_of_tuples = [tuple for tuple in self.link_list if tuple[1] == cmt_id]
    #     if list_of_tuples:
    #         return True
    #     else:
    #         return False











# ======================================
#           Archived codes
# ======================================
    # def add_bi_link(self, list_link_tuples):
    #     '''
    #     Creates 2 directional links between the 2 compartments stated in the first 2 elements of input tuples
    #     e.g. If (1,2) is specified, the two links 1->2 and 2->1 will be created. If k constant is specified
    #     as the 3rd element of tuple, it will be included in the links, with the k value switched to negative value
    #     in the reverse link e.g. add_bi_link([(1,2,50)]) will produce 1->2 (k = 50) and 2->1 (k = -50)
    #     '''
    #     self.__check_link_criteria(_tuples)
    #     existing_links = [(tuple[0],tuple[1]) for tuple in self.list_cmt_links]
    #     for tuple in _tuples:
    #             if len(tuple) == 3:
    #                 reverse_tuple = (tuple[1], tuple[0], -tuple[2])
    #                 if (reverse_tuple[0], reverse_tuple[1]) in existing_links:
    #                     raise Exception("The reverse link pair already exists")
    #                 else:
    #                     self.list_cmt_links.append(tuple)
    #                     self.list_cmt_links.append(reverse_tuple)
    #             if len(tuple) == 2:
    #                 reverse_tuple = (tuple[1], tuple[0], 0)
    #                 if (reverse_tuple[0], reverse_tuple[1]) in existing_links:
    #                     raise Exception("The reverse link pair already exists")
    #                 else:
    #                     new_tuple = (tuple[0], tuple[1], 0)
    #                     self.list_cmt_links.append(new_tuple)
    #                     self.list_cmt_links.append(reverse_tuple)
    #
    #     # Add newly created compartments (if any) into the cmt_list
    #     self.__update_cmt_list()
    #
    #
    #
    # def add_path(self, list_cmt_ids, list_k_constants):
    #     len_cmt = len(list_cmt_ids)
    #     len_k = len(list_k_constants)
    #     if len_k >= len_cmt:
    #         raise Exception('Number of k constants should be less than the number of compartments')
    #     else:
    #         # Pad the list of k constants with zeros at the tail end (if len_k << len_cmt)
    #         list_k_constants += [0] * (len_cmt - len_k - 1)
    #         list_new_tuples = []
    #
    #         for j in range(1, len_cmt):
    #             new_tuple = (list_cmt_ids[j-1], list_cmt_ids[j], list_k_constants[j-1])
    #             list_new_tuples.append(new_tuple)
    #
    #         # Check if any of the link pair already exist. If yes, raise error and don't add any link to link list
    #         self.__check_link_criteria(list_new_tuples)
    #         for new_tuple in list_new_tuples:
    #             self.link_list.append(new_tuple)
    #
    #     # Add newly created compartments (if any) into the cmt_list
    #     self.__update_cmt_list()
