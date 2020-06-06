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
        self.cmt_attr = (cmt_id, cmt_name, cmt_vol) # Tuple of attributes
        self.list_cmt_ids.append(self.cmt_attr[0]) # Collate compartment IDs in list
        self.list_cmt_names.append(self.cmt_attr[1]) # Collate compartment names in list
        print(f'{cmt_name} compartment successfully generated')


    def set_attr(self, new_cmt_id = None, new_cmt_name=None, new_cmt_vol=None):
        """Modify attributes of an existing compartment instance

        -------
        type
            Description of returned object.

        """
        if new_cmt_id is None:
            pass # If no new ID input, then keep existing ID
        else:
            self.__check_cmt_id_dtype(new_cmt_id)
            self.__check_cmt_id_exist(new_cmt_id)

            # Remove current ID that is about to be replaced
            current_cmt_id = self.cmt_attr[0]
            self.list_cmt_ids.remove(current_cmt_id)

            tuple_as_list = list(self.cmt_attr)
            tuple_as_list[0] = new_cmt_id
            self.cmt_attr = tuple(tuple_as_list)

            # Append new cmt_id in list of cmt ids (list_cmt_ids)
            self.list_cmt_ids.append(new_cmt_id)

        if new_cmt_name is None:
            pass
        else:
            self.__check_cmt_name_dtype(new_cmt_name)
            self.__check_cmt_name_exist(new_cmt_name)
            current_cmt_name = self.cmt_attr[1]
            self.list_cmt_names.remove(current_cmt_name)

            tuple_as_list = list(self.cmt_attr)
            tuple_as_list[1] = new_cmt_name
            self.cmt_attr = tuple(tuple_as_list)

            # Append new cmt_id in list of cmt ids (list_cmt_ids)
            self.list_cmt_names.append(new_cmt_name)

        if new_cmt_vol is None:
            pass  # If no new cmt_vol, then keep current value
        else:
            self.__check_cmt_vol_dtype(new_cmt_vol)
            tuple_as_list = list(self.cmt_attr)
            tuple_as_list[2] = new_cmt_vol
            self.cmt_attr = tuple(tuple_as_list)


    def get_attr(self):
        '''
        Return attributes of an existing compartment instance
        '''
        print(f"Compartment ID: {self.cmt_attr[0]}")
        print(f"Compartment Name: {self.cmt_attr[1]}")
        print(f"Compartment Volume: {self.cmt_attr[2]} L")
