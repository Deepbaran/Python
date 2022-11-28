# Context managers are a great tool for resource management. They allow you to allocate and release resources precisely when you want.
# A well known example is the with open statement.

# with open('notes.txt', 'w') as f:
#     f.write('some todo...')

# The above snippet will open a file and make sure to automatically close it after program execution leaves the context of the with statement.
# It also handles exceptions and makes sure to properly close the file even in case of an exception.
# Internally the aboe code translated to:

# f = open('notes.txt', 'w')
# try:
#     f.write('some todo...')
# finally:
#     f.close()

# Best way to use context is when opening a file and accessing the database as well in the lock of a thread
# so that exceptions are handled as well as the connection is closed after use.

"""
from threading import Lock
lock = Lock()
# error-prone:
lock.acquir()
# do stuff
# lock should always be released!
lock.release()

# Better:
with lock:
    print('Hello')
"""
