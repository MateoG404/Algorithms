def print_lcrs_tree(T):
    x = T.root
    if x is not None:
        print(x.key)
        lc = x.left_child
        if lc is not None:
            print_lcrs_tree(lc)
            rs = lc.right_sibling
            while rs is not None:
                print_lcrs_tree(rs)
                rs = rs.right_sibling
