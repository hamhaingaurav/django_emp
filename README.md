# django_emp
Showing table data of all the Users in the db of EmpowerU on the basis of certain parameters.

# Inorder to run this project you should have database table with these mentioned columns
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"username"	text NOT NULL,
	"contact"	integer NOT NULL,
	"primary_role"	text NOT NULL,
	"school_id"	integer NOT NULL,
	"school_name"	text NOT NULL,
	"block_name"	text NOT NULL,
	"district_name"	text NOT NULL,
	"dise_code"	integer NOT NULL,
	"additional_role"	text NOT NULL
  
# Then run this command with terminal or cmd inside the root directory of this project inorder to run the projcet-
    $ python manage.py runserver
