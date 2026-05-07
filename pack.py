 
# import random

# number = random.randint(1, 5)


# print(number)




from payment.phone_pay import check_balance as p_cb

from payment.google_pay import check_balance as g_cb


my_g_balance = g_cb()
my_p_balance = p_cb()


print(my_g_balance)
print(my_p_balance)