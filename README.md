# 2021SpringGroup1 Cmpe 352 Term Assignment
This branch is outdated version of our original app. It only contains 3 django apps inside: person, login and post. You can learn how to use apps features here. For the final version of our app, go check [MainApp](https://github.com/bounswe/2021SpringGroup1/tree/MainApp) branch.
<br>
In order to start this application, traverse to the root directory from the command line. To make sure, type dir (or ls if you are on Linux) and if you see manage.py, post, person and login files; then you are in the right place. In the root, type this command:
> python3 manage.py runserver 

If you see this line, that means server started successfully: 
> Starting development server at http://127.0.0.1:8000/

You can go to that address from your browser.
<hr>
Now, let's talk about django apps inside our project.

## Person
Person part of this Django app is basically creates a Person model and Person attributes. You can create new Person by giving attributes manually, or you can create a random person with a third party api. I am not going into details because i didn't implement this part of the app. You can check [MainApp](https://github.com/bounswe/2021SpringGroup1/tree/MainApp) for further information.

## Login
### Creating account:
Login part of the app is quite simple. It allows users to log in to their accounts and let them interact with posts (We will come to this later). Of course, in order to log in to the system, you need to have an account. You can create your account adding something like this to base url:
> person/createPerson?title=(Title)&firstname=(FirstName)&lastname=(LastName)&location=(Location)&email=somemail@mail.com&age=30&phone=05553332211&imageUrl=image.url

Here, you can fill the parts with parenthesis however you like but you need to be careful about age field. Because it will only accept integer inputs. After typing this, you will see a json response which shows you created person.

### Logging in:
When you go to the url you get after starting the program, you will need to provide firstname and lastname to log in. Since i didn't create person, i didn't want to change it and add a password field so it is what it is. You can create an account or use someone from the database. Manuel Flores is one of them. If there is no person in the database with your inputs, then you will be sent to errorpage and it will warn you. You can go back and reenter.
And that is all about login part. 
<br>
Next stop is the Post.

## Post
