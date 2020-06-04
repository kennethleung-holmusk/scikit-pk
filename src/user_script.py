# ****************************************
#          Front-End User Script
# ****************************************

# Import necessary libraries
import os
#os.chdir(r'/home/klty0988/Desktop/scikit-pk/src')
#os.chdir(r'C:\Users\klty0\Desktop\scikit-pk\src')
os.chdir(r'C:\Users\Kenneth Leung\Desktop\scikit-pk\src')

# Main script for testing classes and functions
import skpk

# ===========================================
#    Generating Compartment (CMT) Instances
# ===========================================

C1 = skpk.Cmt(1, 'A1', 1)
C2 = skpk.Cmt(2, 'First-Pass', 10)
C3 = skpk.Cmt(3, 'Free Plasma Drug')
C4 = skpk.Cmt(4, 'Protein Bound Plasma', 20)
C5 = skpk.Cmt(5, 'Peripheral Tissues', 15)

C1.get_attr()
C2.get_attr()
C3.get_attr()
C4.get_attr()
C5.get_attr()

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

saved_cmts = skpk.main.load_all_cmt()

# Testing Zone



# ===================================
#         Testing Model Class
# ===================================

A = skpk.Model('Model_Test')

A.get_links()

saved_cmts = skpk.main.load_all_cmt()

A.add_cmt(C1)  # Single item
A.add_cmt([C2,C3])   # If multiple instances, put into list
A.add_cmt(C4, C5)  # Error if not in list

test_list_tuples = [(C1,C2,1), (C2,C1,2)]

A.add_link((C2, C1, 25))
A.add_link((C3, C1, 50))
A.add_link([(C1,C2,10), (C3,C4,50)])
A.add_link([(4,)])


# Testing cmt not added to model
C99 = skpk.Cmt(99, 'Brain ECF', 10)

A.add_link((C99, C1, 10))

A.linked_cmts()
A.get_links()
A.get_cmts()

A.list_cmt_links

A.summary()

A.clear_model()



A.get_cmt_after(4)

A.get_cmt_prior(4)

A.get_linked_cmt(4)

A.has_cmt_after(2)

A.has_cmt_prior(4)

A.remove_link([(1,2),(3,4),(4,5)])

A.get_params()
