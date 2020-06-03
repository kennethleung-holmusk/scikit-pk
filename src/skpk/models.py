# =========================
#        Model Class
# =========================

class Model:
    '''
    Model class (docstring)
    '''
    list_model_names = []

    def __check_model_name_exist(self, modelname):
        if modelname in list_model_names:
            raise Exception(f'Model name {modelname} already exists')
        else:
            pass


    def __init__(self, modelname):
        self.link_list = []
        self.cmt_list = []

        self.__check_model_name_exist(modelname)
        self.modelname = modelname
        list_model_names.append(self.modelname)

        print(f'''
        The model named {modelname} has been generated'
        Start by adding compartment link(s) with the add_link method
        ''')


    def __check_link_criteria(self, list_of_link_tuples):
        '''
        Check whether the input list of tuples satisfies the existing criteria
        i.e. Tuple length 2 - 3, and link pair should not be existing already
        '''
        if any(len(tuple) >3 or len(tuple) < 2 for tuple in list_of_link_tuples):
            raise Exception("Each link tuple should have only either 2 or 3 elements")
        else:
            existing_links = [(tuple[0],tuple[1]) for tuple in self.link_list]
            new_links = [(tuple[0],tuple[1]) for tuple in list_of_link_tuples]
            # Check if link pair of from_cmt and to_cmt already exists in the link_list
            if any(link_pair in new_links for link_pair in existing_links) == True:
                raise Exception("Link pair already exists. Use get_link_params to see existing link pairs")
            else:
                return list_of_link_tuples


    def add_link(self, list_of_link_tuples):
        '''
        Adds a single-directional link between the 2 compartments listed in first 2 elements of input tuple,
        and includes the k-constant attribute to the link if specified as the 3rd element in the input tuple.
        If no 3rd element stated, the k constant for the link automatically defaults to a value of 0
        '''
        # Check that link tuples have 3 elements
        self.__check_link_criteria(list_of_link_tuples)
        for tuple in list_of_link_tuples:
            if len(tuple) == 3:
                self.link_list.append(tuple)
            # If no k constant element stated in tuple, automatically assign a zero value
            if len(tuple) == 2:
                new_tuple = (tuple[0], tuple[1], 0)
                self.link_list.append(new_tuple)

        # Add newly created compartments (if any) into the cmt_list
        self.__update_cmt_list()


    def add_bi_link(self, list_of_link_tuples):
        '''
        Creates 2 directional links between the 2 compartments stated in the first 2 elements of input tuples
        e.g. If (1,2) is specified, the two links 1->2 and 2->1 will be created. If k constant is specified
        as the 3rd element of tuple, it will be included in the links, with the k value switched to negative value
        in the reverse link e.g. add_bi_link([(1,2,50)]) will produce 1->2 (k = 50) and 2->1 (k = -50)
        '''
        self.__check_link_criteria(list_of_link_tuples)
        existing_links = [(tuple[0],tuple[1]) for tuple in self.link_list]
        for tuple in list_of_link_tuples:
                if len(tuple) == 3:
                    reverse_tuple = (tuple[1], tuple[0], -tuple[2])
                    if (reverse_tuple[0], reverse_tuple[1]) in existing_links:
                        raise Exception("The reverse link pair already exists")
                    else:
                        self.link_list.append(tuple)
                        self.link_list.append(reverse_tuple)
                if len(tuple) == 2:
                    reverse_tuple = (tuple[1], tuple[0], 0)
                    if (reverse_tuple[0], reverse_tuple[1]) in existing_links:
                        raise Exception("The reverse link pair already exists")
                    else:
                        new_tuple = (tuple[0], tuple[1], 0)
                        self.link_list.append(new_tuple)
                        self.link_list.append(reverse_tuple)

        # Add newly created compartments (if any) into the cmt_list
        self.__update_cmt_list()


    def add_path(self, list_of_cmt_ids, list_of_k_constants):
        len_cmt = len(list_of_cmt_ids)
        len_k = len(list_of_k_constants)
        if len_k >= len_cmt:
            raise Exception('Number of k constants should be less than the number of compartments')
        else:
            # Pad the list of k constants with zeros at the tail end (if len_k << len_cmt)
            list_of_k_constants += [0] * (len_cmt - len_k - 1)
            list_of_new_tuples = []

            for j in range(1, len_cmt):
                new_tuple = (list_of_cmt_ids[j-1], list_of_cmt_ids[j], list_of_k_constants[j-1])
                list_of_new_tuples.append(new_tuple)

            # Check if any of the link pair already exist. If yes, raise error and don't add any link to link list
            self.__check_link_criteria(list_of_new_tuples)
            for new_tuple in list_of_new_tuples:
                self.link_list.append(new_tuple)

        # Add newly created compartments (if any) into the cmt_list
        self.__update_cmt_list()


    # # Do we need an add_cmt method when we already have add_link, and every cmt is to be linked
    # def add_cmt(self, list_of_cmt_tuples):
    #     '''
    #     docstring
    #     '''
    #     # Check that cmt tuple has 2 elements
    #     if any(len(tuple) != 2 for tuple in list_of_cmt_tuples):
    #         raise Exception('ERROR: Each CMT tuple should have 2 elements')
    #     else:
    #         existing_cmt = self.get_cmt_list()
    #         new_cmt = [tuple[0] for tuple in list_of_cmt_tuples]
    #         if (cmt in new_cmt for cmt in existing_cmt) is True:
    #             raise Exception('Error: Compartment ID already exists. Use update_cmt to modify CMT instead')
    #         else:
    #             for tuple in list_of_cmt_tuples:
    #                  self.cmt_list.append(tuple)



    def __update_cmt_list(self):
        '''
        Updates cmt list after adding new link/path
        '''
        cmt_list = []
        first_elements = [tuple[0] for tuple in self.link_list]
        second_elements = [tuple[1] for tuple in self.link_list]
        combined_elements = first_elements + second_elements
        unique_elements = sorted(list(dict.fromkeys(combined_elements)))

        # Identifying the list of unique compartment IDs
        for i in unique_elements:
            if i in [tuple[0] for tuple in self.cmt_list]:
                pass
            else:
                # Generating a new tuple for the new compartment, with Vd defaulted to 0
                new_tuple = (i,0)
                self.cmt_list.append(new_tuple)


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
        # Get first and second elements of all link list_of_cmt_tuples
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


    def remove_link(self, list_of_link_pair_tuples):
        if any(len(tuple) != 2 for tuple in list_of_link_pair_tuples):
            raise Exception("Link pair should contain only 2 elements in the tuple")
        else:
            tuples_to_remove = []
            for tuple in list_of_link_pair_tuples:
                for existing_tuple in self.link_list:
                    if (tuple[0],tuple[1]) == (existing_tuple[0],existing_tuple[1]):
                        self.link_list.remove(existing_tuple)
                    else:
                        pass

        # Update list of compartments (if any changes) in the cmt_list
        self.__update_cmt_list()



    def clear_all(self):
        self.cmt_list = []
        self.link_list = []
        print('Cleared all compartments and links')
