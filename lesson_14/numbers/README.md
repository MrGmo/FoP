The purpose of this exercise is to get you familiar with setting up python projects, and the basics of writing route handlers. 

## Goals
- create, activate, and understand a virtual environment. The virtual environment should not be committed in git.
- install django in your virtual environment. Save your dependencies in a requirements.txt file, which should be committed in git. 
- Define the following routes in urls.py, that will perform various mathematical calculations:
    - `/sum` (add two integers)
    - `/product` (find the product of two integers)
    - `/factorial` (find the factorial of the single integer in the querystring)
    - `/fibonacci` (find the nth fibonacci number in the sequence)

Each of the above routes will need to access variables in the querystring in order to calculate the result. Return the answer to the client in any HTML tag. Use appropriate status codes. For example, if the server can't process a request because it has too little information from the client, you might respond with a status code of 400 or 409.

- Next, define the following routes in urls.py:
    - `/sum/<int:num1>/<int:num2>`
    - `/product/<int:num1>/<int:num2>`
    - `/factorial/<int:num>`
    - `/fibonacci/<int:num>`

- These routes should behave the same as the above routes, but they should get their input from these ordered URL parameters instead of the querystring.

**Create your Django project within this folder**