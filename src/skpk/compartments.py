# =========================
#     Compartment Class
# =========================

class Cmt:
    '''
    Compartment class
    '''
    list_cmt_ids = []
    list_cmt_names = []

    def __check_cmt_id_exist(self, cmt_id):
        """Short summary.

        Parameters
        ----------
        cmt_id : type
            Description of parameter `cmt_id`.

        Returns
        -------
        type
            Description of returned object.
        """
        if cmt_id in self.list_cmt_ids:
            raise Exception(f"""Compartment ID {cmt_id} already exists.
            List of existing compartment IDs:
            {self.list_cmt_ids}""")

    def __check_cmt_name_exist(self, cmt_name):
        if cmt_name in self.list_cmt_names:
            raise Exception(f"""Compartment name {cmt_name} already exists.
            List of existing compartment names:
            {self.list_cmt_names}""")

    def __check_cmt_name_dtype(self, cmt_name):
        if isinstance(cmt_name, (str, type(None))) == False:
            raise ValueError('Compartment name (cmt_name) must be a string')
        else:
            pass

    def __check_cmt_Vd_dtype(self, Vd):
        """Short summary.

        Parameters
        ----------
        Vd : type
            Description of parameter `Vd`.

        Returns
        -------
        type
            Description of returned object.

        """
        if isinstance(Vd, (int, float, type(None))) == False:
            raise ValueError('Vd must be an integer or float')
        else:
            pass

    def __check_cmt_id_dtype(self, cmt_id):
        if isinstance(cmt_id, (int, type(None))) == False:
            raise ValueError('Compartment ID (cmt_id) must be an integer')
        else:
            pass


    def __init__(self, cmt_id, cmt_name, Vd = 0):
        """Short summary.

        Parameters
        ----------
        cmt_name : type
            Description of parameter `cmt_name`.
        Vd : type
            Description of parameter `Vd`.

        Returns
        -------
        type
            Description of returned object.

        """
        self.__check_cmt_id_dtype(cmt_id)
        self.__check_cmt_name_dtype(cmt_name)
        self.__check_cmt_Vd_dtype(Vd)
        self.__check_cmt_id_exist(cmt_id)
        self.__check_cmt_name_exist(cmt_name)
        self.cmt_id = cmt_id
        self.cmt_name = cmt_name
        self.Vd = Vd

        self.list_cmt_ids.append(self.cmt_id) # Collate compartment IDs in list
        self.list_cmt_names.append(self.cmt_name) # Collate compartment names in list

        self.cmt_attr = (self.cmt_id, self.cmt_name, self.Vd) # Tuple of attributes
        print(f'Compartment {cmt_name} successfully generated')


    def set_attr(self, new_cmt_id = None, new_cmt_name = None, new_Vd = None):
        """Modify attributes of an existing compartment instance

        Parameters
        ----------
        cmt_id : type
            Description of parameter `cmt_id`.
        cmt_name : type
            Description of parameter `cmt_name`.
        Vd : type
            Description of parameter `Vd`.

        Returns
        -------
        type
            Description of returned object.

        """
        if new_cmt_id is None:
            self.cmt_id = self.cmt_id # If no new ID input, then keep existing ID
        else:
            self.__check_cmt_id_dtype(new_cmt_id)
            self.__check_cmt_id_exist(new_cmt_id)
            for i, id in enumerate(self.list_cmt_ids): # Update list of cmt ID
                if id == self.cmt_id:
                    self.list_cmt_ids[i] = new_cmt_id # Replace list value with new ID
            self.cmt_id = new_cmt_id # Assign new ID

        if new_cmt_name is None:
            self.cmt_name = self.cmt_name # If no new name input, then keep existing name
        else:
            self.__check_cmt_name_dtype(new_cmt_name)
            self.__check_cmt_name_exist(new_cmt_name)
            for i, name in enumerate(self.list_cmt_names): # Update list of cmt names
                if name == self.cmt_name:
                    self.list_cmt_names[i] = new_cmt_name # Replace list value with new name
            self.cmt_name = new_cmt_name # Assign new name

        if new_Vd is None:
            self.Vd = self.Vd  # If no new Vd input, then keep existing Vd value
        else:
            self.__check_cmt_Vd_dtype(new_Vd)
            self.Vd = new_Vd # Assign new Vd

        self.cmt_attr = (self.cmt_id, self.cmt_name, self.Vd) # Update attributes tuple


    def get_attr(self):
        '''
        Return attributes of an existing compartment instance
        '''
        print(f"Compartment ID: {self.cmt_id}")
        print(f"Compartment Name: {self.cmt_name}")
        print(f"Volume of Distribution (Vd): {self.Vd} L")
