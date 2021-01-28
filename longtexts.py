# import datetime

# x = datetime.datetime.now()
# print(x)

# print(
# '''
# So it works like a multi-line
# comment, but it will print out.

# You can make kewl designs like this:

# ==============
# |            |
# |            |
# |    BOX     |
# |            |
# |            |
# ==============
# '''
#     )

print "{:<8} {:<15} {:<10}".format('Key','Label','Number')
for k, v in d.iteritems():
    label, num = v
    print "{:<8} {:<15} {:<10}".format(k, label, num)