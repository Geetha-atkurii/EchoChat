class StatusCodes:
    SUCCESS = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

class Messages:
    USER_CREATED = "User registered successfully."
    LOGIN_SUCCESS = "Login successful."
    INVALID_CREDENTIALS = "Invalid email or password."
    USER_ALREADY_EXISTS = "Email already registered."
    USER_NOT_FOUND = "User not found."
    USER_UPDATED = "User profile updated successfully."
    INTERNAL_SERVER_ERROR = "Something went wrong. Please try again later."
    USERNAME_ALREADY_EXISTS = "Username already taken. Please choose another one."
    CONFIRM_PASSWORD_VALIDATION_ERROR = "Password and Confirm Password should match."