# ****************************************
#          Front-End User Script
# ****************************************

# Import necessary libraries
import os
#os.chdir(r'/home/klty0988/Desktop/scikit-pk/src')
os.chdir(r'C:\Users\klty0\Desktop\scikit-pk\src')

# Main script for testing classes and functions
import skpk

# ===========================================
#    Generating Compartment (CMT) Instances
# ===========================================

C1 = skpk.Cmt(1, 'A1', 1)
C2 = skpk.Cmt(2, 'First-Pass', 10)
C3 = skpk.Cmt(3, 'Free Plasma Drug')
C4 = skpk.Cmt(4, 'Protein Bound Plasma', 20)

C1.get_attr()
C2.get_attr()
C3.get_attr()
C4.get_attr()

C2.set_attr(new_cmt_name = 'First-Pass Metabolism')
C2.get_attr()

C2.cmt_name
C2.Vd

C1.set_attr(new_cmt_name = 'Absorption')
C1.get_attr()

C1.set_attr(new_cmt_id = 15)
C1.get_attr()
C1.cmt_attr

C3.cmt_attr

skpk.Cmt.list_cmt_ids
skpk.Cmt.list_cmt_names

# ===========================
#     Saving compartments 
# ===========================

skpk.main.save_cmt(C1, C2, C3, C4)

skpk.main.list_cmt(folder_path = './skpk_saved_cmts')


# ===========================
#     Loading compartments 
# ===========================

D1 = skpk.main.load_cmt('First-Pass')

D2 = skpk.main.load_cmt('First-Pass', folder_path = './wrongpath')

E1, E2 = skpk.main.load_cmt('Absorption', 'First-Pass')

D1.get_attr()

A1, A2, A3 = skpk.main.load_all_cmt()

# Testing Zone

del A1

# ===================================
#         Testing Model Class
# ===================================


skpk.Model.__check_cmt_class(C1, C2)

A = skpk.Model('Model1')

A.add_link([(3,4,5), (1,2,3)])

A.add_link([(4,)])

A.add_link([(4,7)])

# A.add_cmt([(3,22)])

A.add_bi_link([(6,4)])

A.cmt_list

A.link_list

A.get_link_params()

A.get_cmt_params()

A.get_cmt_id()

A.clear_all()

A.add_path([1,2,3,4,5,6], [23,25,44,33,24])

A.get_params()

A.get_cmt_after(4)

A.get_cmt_prior(4)

A.get_linked_cmt(4)

A.has_cmt_after(2)

A.has_cmt_prior(4)

A.remove_link([(1,2),(3,4),(4,5)])

A.get_params()
