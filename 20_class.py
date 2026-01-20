# virtual environments in python

# virtual environments are the isolated python environment where we can instal specific packages for our specific projects and manage them accordingly no matter our global system contains what packages and what versions of the packages, virtual environment are fully isolated from theat.

#  to make virtual environments in python we use the command

#    >      python venv (virtual environment name)

#  to install packages in it we use 
#           pip install (package name)  # it will install latest version of the package

#  to install specific version of the package we use

#         >    pi install (package name) == (version)
# example >    pi install (pandas) == (2.3.2)

#  to see that installed packages 

#       pip freeze      # gives the list of all installed packages

# to make a file of installed packages we use command

#     > pip freeze > requirements.txt

# to deactivate the virtual environment in python we use the command
#       deactivate      # deactivates the virtual environment

