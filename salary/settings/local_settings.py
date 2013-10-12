DATABASES = {

#look on geodjango tutorial and there's a specific things...
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
      #  'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'salary',
		'USER': 'salary',
		'PASSWORD': 'password',
        'PORT': '5432',
        'HOST': 'localhost',
    }
}
