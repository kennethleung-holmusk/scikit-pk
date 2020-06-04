# =========================
#        Model Class
# =========================
from .compartments import Cmt

class Model:
    '''
    Model class (docstring)
    '''
    list_model_names = []

    def __init__(self, modelname):
        self.list_cmt_links = []
        self.list_cmts = []
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
            raise Exception(f"""Compartment {arg} already exists.
            List of existing compartments:
            'Edit Later' """)


    def __check_link_exist(self, link_input):
        existing_links = [(tuple[0], tuple[1]) for tuple in self.list_cmt_links]
        if (link_input[0],link_input[1]) in existing_links:
            raise Exception(f"""Link ({link_input[0].cmt_name}) -> ({link_input[1].cmt_name}) already exists.
            Use get_link_params to see existing link pairs""")


    def __check_tuple_criteria(self, object):
        if isinstance(object, tuple) == False:
            raise TypeError(f"Input must be a tuple or a list of tuples")
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
                self.__check_link_exist(link_input)
            else:
                # If input is a list
                for object in link_input:
                    self.__check_tuple_criteria(object)
                    self.__check_link_exist(object)


    def __append_link_tuple(self, tuple):
        if len(tuple) == 3:
            self.list_cmt_links.append(tuple)

        # If no k rate constant element stated in link tuple, automatically assign k = 0
        if len(tuple) == 2:
            new_tuple = (tuple[0], tuple[1], 0)
            self.list_cmt_links.append(new_tuple)


    def add_cmt(self, cmt_input):
        if isinstance(cmt_input, (Cmt, list)) == False:
            raise ValueError('Arguments must be of Cmt class or list of Cmt instances')
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
                self.__append_link_tuple(tuple)

        else:
            self.__append_link_tuple(link_input)


    def clear_model(self):
        self.list_cmts = []
        self.list_cmt_links = []
        self.list_model_names = []
        print('Cleared all compartments and links')



    def get_links(self):
        link_list = self.list_cmt_links.copy()
        print(link_list)



    def get_link_params(self):
        link_list_to_print = self.link_list.copy()
        # Sort by first element of tuple i.e. from_cmt (in ascending order)
        sorted_list = sorted(link_list_to_print, key=lambda tup: tup[0])
        print("From CMT      To CMT    k rate constant")
        for ele1,ele2,ele3 in sorted_list:
            print("{:<15}{:<16}{}".format(ele1,ele2,ele3))


    def get_cmt_id(self):
        '''
        Returns list of existing compartments which are connected to at least 1 other compartment
        '''
        # Get first and second elements of all link list_cmt_tuples
        first_elements = [tuple[0] for tuple in self.link_list]
        second_elements = [tuple[1] for tuple in self.link_list]
        combined_elements = first_elements + second_elements
        unique_elements = sorted(list(dict.fromkeys(combined_elements)))
        print(unique_elements)


    def get_cmt_params(self):
        cmt_list_to_print = self.cmt_list.copy()
        # Sort by first element of tuple i.e. from_cmt (in ascending order)
        sorted_list = sorted(cmt_list_to_print, key=lambda tup: tup[0])
        print("Compartment ID     Vd")
        for ele1,ele2 in sorted_list:
            print("{:<19}{:<11}".format(ele1,ele2))


    def get_params(self):
        '''
        Returns the parameters for compartments and links in tabular form
        '''
        print(' ')
        print('-------- Compartment Parameters --------')
        self.get_cmt_params()
        print(' ')
        print('-------- Link Parameters --------')
        self.get_link_params()


    def get_cmt_after(self,cmt_id):
        '''
        Prints the list of compartments linked after the specified input cmt ID
        '''
        list_of_tuples = [tuple for tuple in self.link_list if tuple[0] == cmt_id]
        cmts_after = sorted([i[1] for i in list_of_tuples])
        print(f'List of compartments linked after compartment {cmt_id} = {cmts_after}')


    def get_cmt_prior(self,cmt_id):
        '''
        Prints the list of compartments linked before the specified input cmt ID
        '''
        list_of_tuples = [tuple for tuple in self.link_list if tuple[1] == cmt_id]
        cmts_prior = sorted([i[0] for i in list_of_tuples])
        print(f'List of compartments linked prior to compartment {cmt_id} = {cmts_prior}')


    def get_linked_cmt(self,cmt_id):
        '''
        Prints the list of compartments linked before and after the specified input cmt ID
        '''
        self.get_cmt_prior(cmt_id)
        self.get_cmt_after(cmt_id)


    def has_cmt_after(self, cmt_id):
        list_of_tuples = [tuple for tuple in self.link_list if tuple[0] == cmt_id]
        if list_of_tuples:
            return True
        else:
            return False


    def has_cmt_prior(self, cmt_id):
        list_of_tuples = [tuple for tuple in self.link_list if tuple[1] == cmt_id]
        if list_of_tuples:
            return True
        else:
            return False


    def remove_link(self, _pair_tuples):
        if any(len(tuple) != 2 for tuple in _pair_tuples):
            raise Exception("Link pair should contain only 2 elements in the tuple")
        else:
            tuples_to_remove = []
            for tuple in _pair_tuples:
                for existing_tuple in self.link_list:
                    if (tuple[0],tuple[1]) == (existing_tuple[0],existing_tuple[1]):
                        self.link_list.remove(existing_tuple)
                    else:
                        pass

        # Update list of compartments (if any changes) in the cmt_list
        self.__update_cmt_list()






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
