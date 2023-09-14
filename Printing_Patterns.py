""" Printing Patterns """

""" First Pattern """
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
# Wrong 
# n = 6
# for i in range(n):
#     for j in range (0, i+1):
#         print("*", end=" ")

""" Second Pattern """
# *
# * *
# * * *
# * * * *
# * * * * *

n = 5
for i in range (0, n):
    print("\r")
    for j in range (0, i+1):
        print("*", end = " ")