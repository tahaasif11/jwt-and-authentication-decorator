# jwt-and-authentication-decorator

Login API:
Handles user authentication with email and password, returning a JWT upon successful login.

JWT Handling:
Utilizes the JWT library to encode user information and expiration time during login and decode tokens for route protection.

Token-based Authentication Decorator :
Implements a token_required decorator to secure routes, checking for a valid JWT in the "Authorization" header for user authentication.
