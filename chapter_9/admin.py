from user import User
from privileges import Privileges, Admin

my_admin=Admin('lisa','wang',24,'Beijing')
my_admin.privileges.show_privileges()