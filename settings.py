# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
MONGO_USERNAME = 'sgx_tracker'
MONGO_PASSWORD = 'sgxtracker'

MONGO_DBNAME = 'sgx_tracker'

ITEM_METHODS = ['GET', 'DELETE']
ALLOW_UNKNOWN = True
X_DOMAINS = '*'
X_HEADERS = ['Authorization','Content-type']

schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'username': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
	'required': True,
	'unique': True,
    },
    'password': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
        'unique': True,
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    'futures': {
        'type': 'dict', 
	'schema': {
		'future': {'type': 'list'},
        	'contract': {'type': 'list'},
	}
    },
}

users = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'user',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],
    'allow_unknown': False,
    'schema': schema
}

DOMAIN = {'users': users,
          'data': {},
          'date': {}
         }
