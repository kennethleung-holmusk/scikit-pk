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

    def __check_cmt_vol_dtype(self, cmt_vol):
        """Short summary.
        """
        if isinstance(cmt_vol, (int, float, type(None))) == False:
            raise ValueError('Compartment volume must be an integer or float')
        else:
            pass

    def __check_cmt_id_dtype(self, cmt_id):
        if isinstance(cmt_id, (int, type(None))) == False:
            raise ValueError('Compartment ID (cmt_id) must be an integer')
        else:
            pass


    def __init__(self, cmt_id, cmt_name, cmt_vol = 0):
        """Short summary.
        """
        self.__check_cmt_id_dtype(cmt_id)
        self.__check_cmt_name_dtype(cmt_name)
        self.__check_cmt_vol_dtype(cmt_vol)
        self.__check_cmt_id_exist(cmt_id)
        self.__check_cmt_name_exist(cmt_name)
        self.cmt_attr = (self.cmt_id, self.cmt_name, self.cmt_vol) # Tuple of attributes
        self.list_cmt_ids.append(self.cmt_attr[0]) # Collate compartment IDs in list
        self.list_cmt_names.append(self.cmt_attr[1]) # Collate compartment names in list
        print(f'Compartment {cmt_name} successfully generated')


    def set_attr(self, new_cmt_id = None, new_cmt_name = None, new_cmt_vol = None):
        """Modify attributes of an existing compartment instance

        -------
        type
            Description of returned object.

        """
        # CONTINUE HERE> Convert all to tuple attributes. Remove isolated attributes
        # like cmt_id. Purpose is to allow universal updating (rather than update multiple places)

        if new_cmt_id is None:
            pass # If no new ID input, then keep existing ID
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

        if new_cmt_vol is None:
            self.cmt_vol = self.cmt_vol  # If no new cmt_vol, then keep current value
        else:
            self.__check_cmt_vol_dtype(new_cmt_vol)
            self.cmt_vol = new_cmt_vol # Assign new compartment volume

        self.cmt_attr = (self.cmt_id, self.cmt_name, self.cmt_vol) # Update attributes tuple


    def get_attr(self):
        '''
        Return attributes of an existing compartment instance
        '''
        print(f"Compartment ID: {self.cmt_attr[0]}")
        print(f"Compartment Name: {self.cmt_attr[1]}")
        print(f"Compartment Volume: {self.cmt_attr[2]} L")
