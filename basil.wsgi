<<<<<<< HEAD
from basil import application

if __name__ == "__main__":
    basil.run()
=======
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
#sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
application.secret_key = 'Add your secret key'
>>>>>>> a349d9f908f5b75be18c2d437b503f0d4f5ff57b
