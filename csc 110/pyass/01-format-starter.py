PST = 0.07
GST = 0.05

# Add formating so the output is as follows,
# (without the leading #'s):

#item:  $  87.98
#pst:   $   6.16
#gst:   $   4.40
#------------------
#total: $  94.19

# print the bill breakdown for item of 87.98:
def print_bill():
    price = 87.98
    pst = price * PST
    gst = price * GST
    total = price + pst + gst

    print('item:\t$', format(price, "6.2f"))
    print('pst:\t$', format(pst, "6.2f"))
    print('gst:\t$', format(gst, "6.2f"))
    print("-------------------------")
    print('total:\t$', format(total, "6.2f"))

print_bill()
