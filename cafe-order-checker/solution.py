def check_orders(take_out_orders, dine_in_orders, served_orders):
    
    # Iterate through every served order
    for order in served_orders:
        # Make sure it is next up either in take-out or dine-in
        if take_out_orders and order == take_out_orders[0]:
            # To do that, make sure to remove the front order when you account for it
            take_out_orders = take_out_orders[1:]
        elif dine_in_orders and order == dine_in_orders[0]:
            dine_in_orders = dine_in_orders[1:]
        # If its not next up in either queue, when the orders were not first-come-first-serve
        else: return False
        
    return True