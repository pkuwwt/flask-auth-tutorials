# Examples for flask authentication

## Install packages

```
pip install -r requirements.txt
```

## Basic Authentication

Start the server
```
python basic_auth.py
```

Testing from CLI
```
curl -v -I -u john:hello 127.0.0.1:5000
```

## Digest Authentification

Start the server
```
python digest_auth.py
```

Testing from CLI
```
curl --digest -v -u john:hello 127.0.0.1:5000 -c ./cookie.txt
```

The Digest Authentication use the cookie-based session by default. We can use server-side sessions with `flask-session`.

## Token Authentication

Start the server
```
python digest_token.py
```

Testing from CLI
```
curl -v -H 'Authorization: Token secret-token-1' 127.0.0.1:5000
```

## Basic + Token Authentication

FROM: [REST-auth](https://github.com/miguelgrinberg/REST-auth)

Start the server
```
python basic_auth_token.py
```

Create a user
```
curl -i -X POST -H "Content-Type: application/json" -d '{"test": "test"}' http://127.0.0.1:5000/api/users
```

Get the user
```
curl http://127.0.0.1:5000/api/users/1
```

Get a token
```
curl -u test:test -i http://127.0.0.1:5000/api/token
```

Get the resource by username/password
```
curl -u test:test http://127.0.0.1:5000/api/resource
```

Get the resource by token
```
curl -u your-token: http://127.0.0.1:5000/api/resource
```

## References

  * [RESTful Authentication with Flask](http://blog.miguelgrinberg.com/post/restful-authentication-with-flask)
  * [flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)

