# pygame
Extra: Object-Oriented Programming utilizing the Python Pygame module

**Lesson: EXTRA class in object-oriented programming cont.**

In this extra-curricular lecture we will be dicussing classes and objects while utilizing Pythons module Pygame to further improve our understanding and confidence when working with OOP.
Object Oriented programming provides us flexibility in our code allowing us to create reusable code that can be altered without affecting the rest of our program. Using concepts like inheritance and polymorphism we are able to easily create subclasses and overwrite methods
in our children without directly affecting our parent classes. Imagine having the blueprint to a car that allows you to easily recreate different Car types without having to restart from scratch every single time and still have the flexibility to change any features from its parent. That is the power of Classes and objects


**Installing Pygame:**

Pygame is a module that requires Python and Pip. Lucky for you we already installed these during the installfest.


To install pygame use either method 1 or method 2 depending on your system:

Method 1 --> UBUNTU:

	sudo apt-get install python3-pygame

Method 2 --> MAC:

	python3 -m pip install -U pygame --user

After pygame has been installed run the following command on your terminal to test it out. If a window is displayed with a vehicle with a turret and aliens then you're all set ! :

	python3 -m pygame.examples.aliens

**GETTING STARTED**

Now that Pygame is installed we can start putting some code on the screen:

Just like every module up to this point. There are pre-built methods that come with it. When it comes to pygame all these methods can be found on their website under the documentation tab

	https://www.pygame.org/docs/

Unfortunately, this isn't a Pygame lesson. It is an **Object Oriented Programming and Classes** lecture so we won't dwell too much on Pygames library of methods. All the legwork has been done for you and all you need to do is use the boiler plates provided for you. A small description has been added to familiarize you with the module we will be using. Pygame will simply be a tool for us to better visualize classes and objects


Pygame method **CHEATSHEET**


 	# GAME WINDOW

	pygame.init() : Initializes the pygame modules in the code

  	pyame.display.set_mode((size_x, size_y)) : this creates the window and sets its size. Assign this to a variable that will hold your "screen"

   	#IMAGES

   	pygame.image.load("my_image.jpg") : Loads an image. You can assign this to an image variable

     	pygame.Surface((x,y)) : creates a surface that isnt our screen for us to add our hero or enemies on to

      	surface.fill("color") : fills in our surface to make it visible. default color is black

	screen.blit(my_image, (my_image_x, my_image_y)) : Adds the image on to your game screen at the location given

	my_image.get_rect().size[1] : when called on an image variable and assigned to a variable ex: image_heigh,  will return the height of an image

	pygame.transform.flip(my_image, False, True) : used on an image, will flip it on its x axis

	object_one.colliderect(object_two) : detects if one object/rect collides with another

 	#EVENTS

  	events = pygame.event.get() : grabs an event and assigns it to a variable

   	#WRTING TO SCREEN
	# Write size 36 turquoise text to the screen
	colour = (0, 255, 255)
	font = pygame.font.Font(None, 36)
	location = (300, 10)
	screen.blit(font.render(“Flippy Bird”, True,
	colour), location)


	#-----------------------------------------------------
 	# CHECKS TO SEE IF THE EVENT IS A PRESSED OR RELEASED KEY
   	if event[0].type == pygame.KEYDOWN:
    		print("A key was pressed!")
      	elif events[0].type == pygame.KEYUP:
       		print("A key was released!")

  	#-------------------------------------------------
   	# CHECKS TO SEE WHICH KEY WAS PRESSED
	if events[0].key == pygame.K_UP:
		print("The up arrow key was pressed!")
	elif events[0].key == pygame.K_DOWN:
		print("The down arrow key was pressed!")
	elif events[0].key == pygame.K_q:
		print("The letter q was pressed!")
  	
	#-----------------------------------------------
 	#PYGAME EVENTS 
	pygame.QUIT
	pygame.ACTIVEEVENT
	pygame.KEYDOWN
	pygame.KEYUP
	pygame.MOUSEMOTION
	pygame.MOUSEBUTTONUP
	pygame.MOUSEBUTTONDOWN
 	pygame.mouse.get_pos() : returns tuple relative to the 0,0 location
  	pygame.key.get_pressed() : grabs a dictionary of the status of all keys

 	#------------------------------------------------
  	# CLOSE THE WINDOW

   
	# Import the system module
	import sys
	# Close the window and exit
	pygame.display.quit()
	sys.exit()

 	#-------------------------------------------------
  	#COMMON KEY CODES IN PYGAME
	pygame.K_SPACE : spacebar
	pygame.K_a/w/s/d : a/w/s/d
	pygame.K_UP/DOWN/LEFT/RIGHT : up arrow/down arrow/left arrow/right arrow
   	


Below, you will find a Boiler Plate template that will open up a BASIC pygame window so that we can begin working. Everything in this code is the necessary foundation for all games using the pygame module. This will be our skeleton for our program.
Begin by creating a directory in which we will hold our game. Within this directory we will create our main.py which will hold our boiler plate. On top of containing our main.py we will be creating other files that will be holding our classes to keep everything seperated and organized. 

	# Example file showing a basic pygame "game loop"
 
	import pygame
	import sys
	
	class Game:

	    def __init__(self):
	        pygame.init()
	        self.screen = pygame.display.set_mode((800,800))
	        pygame.display.set_caption('OOP')
	        self.clock = pygame.time.Clock()

	    def run(self):
	        while True:
	            
	     	    #Every time it loops, it will check if we decided to exit the game or not
	            for event in pygame.event.get():
	                if event.type == pygame.QUIT:
	                    pygame.quit()
	                    sys.exit()

			# <---- WITHIN THIS SPACE WE CAN ADD CODE FOR OUR GAME TO CONDUCT ---->

       
		     
		    #This method is a form of a refresh, and updates our screen
	            pygame.display.update()
	            self.clock.tick(60)

	my_game = Game()
	my_game.run()

Now that we have a window open we can begin working.

First thing we will do is create a Surface that we can work on. Keep in mind that the Display screen is not the same as our working Surface. to create a surface you require the "pygame.Surface command. we will begin by declaring a data member which will hold and initiate our Surface and we will give it the OuterSpace.png file

 	# declare your surface in the init method
	self.space_surface = pygame.Surface((800,800))



	# WITHIN, the Run method inside of our game loop we can to use screen.blit to add the surface to our display, afterwards we can add other items on top of this surface
 
	self.screen.blit(self.space_surface, (0,0))
	self.space_surface.blit(pygame.image.load("OuterSpace.png"),(0,0))


**CREATING OUR CHARACTER**

After creating your main.py file with our template, create a seperate file and name it **hero.py**

We will now isolate our Hero code by creating our class in its individual file. For our Hero to properly work we want to ensure he is able to take as arguments an image, and its x and y coordinates. The image will be used to declare the surface of where he will be working on. Afterwards to be able to precisely manipulate our SpaceShip and to be able to track collisions we need to surround our Hero with a "Rectangle". Think of it as an imaginary box that surrounds the perimeter of our ship. With this rectangle we can track when other objects ( that also have a rectangle around them ) touch or intersect between OUR hero's rectangle. Thats how we determine if we've been hit !

	import pygame

	class SpaceShip:
	
		def __init__(self, image, x, y):
			self._space_ship_surface = pygame.image.load(image)
			self.rect = self._space_ship_surface.get_rect(midbottom = (x, y))
		
		def get_position(self):
			return (self.rect.x, self.rect.y)


After we create our SpaceShip we need to code the functionality to allow it to appear in our screen. We can either do this in our game loop or we can just give our class the method for it. In our example we will create the method within our class. We will use the surface that our image is on, and instead of hand jamming the exact coordinates of our position we can just pass our rectangle that already holds that in

    def draw(self, screen):
        screen.blit(self._space_ship_surface, self._space_ship_rect)


Now that our blueprint ( or CLASS ) for our SpaceShip / Hero has been created we can draw it on our screen: Remember, the way our pixels work on our screen is from top left to bottom right. Therefore if we were to assign our x and y axis as 0,0 our image will appear at the top left corner of our screen. As we increase our x axis it will shift to our right, and going negative will shift it to the left outside of our screen. For the Y axis as we increase the Y axis it will move down our screen and as we go into the negatives it will move up away from our screen. Below is the Code Snippet for what our Spaceship class should look like.

	#DONT FORGET TO IMPORT OUR SHIP CLASS!!!

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption('OOP')
        self.clock = pygame.time.Clock()

 	#We create our space surface
        self.space_surface = pygame.Surface((800,800))

        # Create our hero ship
        self._hero = SpaceShip("DurrrSpaceShip.png", 360, 700)

    def run(self):
        while True:

            #This initiates our game loop. Every time it runs it will go through all these checks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.screen.blit(self.space_surface, (0,0))
            self.space_surface.blit(pygame.image.load("OuterSpace.png"),(0,0))

            
            self._hero.draw(self.space_surface)


If done corretly, when our main.py runs it should open up a game window with our SpaceShip dead center and a cool looking space background!!

Now all this is cool and all but our ship doesnt do anything just yet, so lets add some functionality. We would like for our spaceship to be able to move left and right to allow it to aim around around screen. To do this we need to be able to capture certain input like either using the arrow keys on our keyboard of the w,a,s,d.

First thing first we can to create a method that is unique only to our SpaceShip that will allow it to move. This method will take in a Str argument which could be "a","d","w","s" and change our x and y coordinates. Think of it as a setter method:

    def move(self, direction):
        if direction == "a":
            if self.rect.x >= 20:
                self.rect.x -= 5
        elif direction == "d":
            if self.rect.x <= 700:
                self.rect.x += 5
        elif direction == "w":
            if self.rect.y >=  300:
                self.rect.y -= 5
        elif direction == "s":
            if self.rect.y <= 700:
                self.rect.y += 5

Once our SpaceShip has a method to move we can begin capturing the necessary Events for it within our Game Loop;

	# The key.get_pressed() method returns a dictionary of status of all keys
	# which we can access to see if theyre pressed or not. Depending on their status
	# we want to move left or move right
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.hero.move("a")
            if keys[pygame.K_d]:
                self.hero.move("d")
            if keys[pygame.K_w]:
                self.hero.move("w")
            if keys[pygame.K_s]:
                self.hero.move("s")
 		
AWESOME our SpaceShip has lift off! At this point in our code we've reached modern space exploration, but its time to kick it up a notch. We need to be able to defend ourselves from any possible threat, so for that our spaceship needs to be able to shoot some form of projectile! For this exercise we wont need anything fancy. Pygame allows us to create shapes which we can use as a form of projectile. To begin you need to create a Bullet class

**Bullet Class**

Create a new file called Bullet.py. This new file will hold the code needed for our ammunition. In this class we are going to introduce inheritance. One of the amazing traits of Classes and Objects is the ability to be able to inherit from other class. Our bullet will have to be a special type of class, because unlike our ship, we will require multiple bullets every time we fire and we need to be able to track each instance of every bullet and update it as necessary. Luckily pygame has a built in class we can utilize and inherit from. This is called our Sprite class. Within our Bullet class we will inherit from the Sprite class specific methods that will allow us to manipulate every bullet


	#within our class name we will add the class we will inherit from. this will be "pygame.sprite.Sprite" Think of this step as importing a module**DO NOT FORGET TO CAPITALIZE THE SECOND SPRITE**
	class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):

    	#within our init method, before we begin defining our bullet class we need to initiate the sprite class we inherit from. think of it as starting up your computer or tv
        pygame.sprite.Sprite.__init__(self)
	#Afterwards we can begin defining out Bullet class like normal. Only difference now is that when using our Bullet class instances we not have access to methods belonging to our Parent Class
        self.image = pygame.Surface((10,10), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0, 255), (5, 5), 5)
        self.rect = self.image.get_rect(midbottom = (x,y))	


 Now that our bullet class is written Import it into our main.py

 Within The init method of our Game class we need to create a variable that will HOLD all our Bullet SPRITES ( Objects of Bullets )

	# Thanks to the inheritance from our parent class we can use methods like the one below. 
 	# This creates almost like a dictionary that works specifically to objects and assigns 
  	# it to our variable data member called all_bullets
 	self.all_bullets = pygame.sprite.Group()

Now lets actually pull the trigger! We want to be able to shoot at a click of a button, we have already worked with our keyboard, now lets attempt to use our mouse instead. Mouse clicking is a type of event that pygame can listen for. Think of it very similar to using js on our websites and adding event listeners to our buttons

	if event.type == pygame.MOUSEBUTTONDOWN:
		## we want to know the location of where our ship is so we know where the bullet needs to be fired from
		current_ship_location = self.hero.get_position()
		 
		# we create an instance of a bullet and pass it the location of our ship firing barrel, to compensate for the location / size of our ship
		# I added some adjustments to ensure it lines up with the firing barrel
		bullet_object = Bullet(current_ship_location[0] + 40, current_ship_location[1] + 10)
		
		## Now that our bullet is instantated we add it to our sprite Group
		self.all_bullets.add(bullet_object)

After we create our Bullet and add it to our group we finally want to draw it on our screen and this is once again when the parent class that we inherited from will come into play. The sprite parent class from pygame comes with a .draw method that takes ALL the sprites in its group and draws it onto our screen. The only argument it takes is the surface we want to add it to but remember that placement is important. Think of all our surfaces almost like layers. We have our display layer which is our base, on top of the display we want to have our background. We cant place our hero before our background because it will lay over it and not show. so the order of how we lay stuff down goes as follows : display -> space layer -> ship -> bullet

	self.screen.blit(self.space_surface, (0,0))
	self.space_surface.blit(pygame.image.load("OuterSpace.png"),(0,0))

	self.hero.draw(self.space_surface)

	self.all_bullets.draw(self.space_surface)   

We can now see our bullet. But no matter how many times we click to shoot it only shows one? Well thats because every single sprite is being drawn at the same location. But we want them to move across the screen the moment its fired. Well our sprite parent class has a method for that too and its called "update()"!. This really doesnt do much for us so we want to overrride it and give it some unique functionality that only belongs to a bullet. This is called POLYMORPHISM!

We can take original methods that we received from our parent and morph it into something new that we as children can use.

Within the Bullet class define the update method to override it:

	def update(self):
 		self.rect.y -= 5

Now within our Game loop in out main.py, every time it runs our loop i want to call the update method

 	#calls our update method on EVERY BULLET OBJECT within our SPRITE GROUP
        self.all_bullets.update()
        self.all_bullets.draw(self.space_surface)   

But what happens to the bullet after the screen? Well nothing. It keeps moving off the screen infinitely and that isn't too good for performance. Well once again thanks to inheritance we also have a method that deletes our sprite and this is the .kill() method


	#within the Bullet class in the update condition
	def update(self):
		self.rect.y -= 10
		if self.rect.y == 10:
			self.kill()

Up to this point in our code we have a working SpaceShip with the ability to defend itself if needed, but NO hero story is ever complete with having an enemy to quarrel with so next we are going to work on our Enemy.py. Create a seperate file were we can create our Alien class. Very similar to our Bullet class, we are going to treat the enemies as a subclass of the sprite class so therefore it will require to inherit from "pygame.sprite.Sprite" and have it initialized within the init method

	import pygame
 	import random

	class Alien(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

  		# we need to load our images for our 3 individual aliens and assign it into a data member
		self.green_alien = pygame.image.load("assets/GreenAlien.png")
		self.red_alien = pygame.image.load("assets/RedAlien.png")
		self.yellow_alien = pygame.image.load("assets/YellowAlien.png")

  		#After creating our 3 aliens we will add them to a list that we are able to search through by index randomly
		self.spawnable_aliens = [self.yellow_alien, self.red_alien, self.green_alien]

  		# utilizing the random module, we will use a random number with its .randint() method to grab a number from 
		# 0-2 therefore randomizing which type of alien we will spawn
		# after every instance creation
		self.image = self.spawnable_aliens[random.randint(0,2)]

  		#Finally assign it a rect to better define collision later and to better place it
		self.rect = self.image.get_rect(center = (20,20))

With the Alien class created we want to create a new Sprite Group in our Game Class to track all our Alien Objects

        self.all_aliens = pygame.sprite.Group()

Now how do we trigger the enemy spawning ? Well pygame provides us with the ability to create certain events using the "pygame.USEREVENT". Within our Game class in our init method we want to create a timer

	# create a data member for your timer and add + 1 after pygame.USEREVENT to let it know you are creating an addional one
	self.enemy_spawn_timer = pygame.USEREVENT + 1

 	#now to set the time using the method below that takes two arguments: the timer to be set, and the time in MILLIseconds
  	pygame.time.set_timer(self.enemy_spawn_timer, 2000)

After creating and setting up our timer we can actually check this event wihin our game loop in the run method

	if event.type == self.enemy_spawn_timer:
	    alien_object = Alien()
	    self.all_aliens.add(alien_object)
And finally draw your alien like everything else

	self.hero.draw(self.space_surface)
	
	self.all_aliens.draw(self.space_surface)
	
	self.all_bullets.update()
	self.all_bullets.draw(self.space_surface)     

This is cool and all but no one likes a stationary target. We enjoy the thrill of the hunt so lets give these bad boys some movement. Essentially we want to instantiate our Alien Objects at the top left of our screen and go from left to right top to bottom until reaching our hero like the Classic Space Invaders Arcade game that most of us grew up with. To add that we need a way to update them so we will use our inhertid metho update() and override it with some unique code only to our alien


First: We want to create a data member within the Alien Init class that we can track to see if hes moving left or moving right

	self.going_right == True


Afterwards we can use that data member within our update method to check what way we are moving and depending what way that is we will adjust our x or y coordinate accordingly

	def update(self):
		if self.going_right == True:
		    self.rect.x += 5
		    if self.rect.x == 760:
			self.rect.y += 50
			self.going_right = False
		else:
		    self.rect.x -= 5
		    if self.rect.x == 0:
			self.going_right = True
			self.rect.y += 50

Finally we can draw our aliens and update them in our game loop 

	self.all_aliens.draw(self.space_surface)
	self.all_aliens.update()

A movable space ship with firing capabilities and a dangerous foe. It feels like we are almost at the end but the key core concept isnt there. Our objects exist but they can't interact with each other. Lets fix that

A unique method to the sprite class allows for a group of sprites to check if theyve collided with another group of sprites and thats the "pygame.spritecollide(self, sprite_group_to_compare_to, Boolean=(to destroy or not)

We want to see if our bullets actually hit our targets or not. To do that, within our Bullet class we are going to tweak our update code only slightly

 	#add a new parameter to our update class, which will be the group we will compare it agaisnt to
	def update(self, alien_group):
		self.rect.y -= 10

		# we add this line checking if our alien group collided with our bullet and if so, 
		# adding true to the third argument will self.kill that object
		pygame.sprite.spritecollide(self, alien_group, True)
		if self.rect.y == -50:
		    self.kill()
	
Okay so that takes care of destroying the enemy but now we need a way to lose. Well it turns out we can use the same spritecollide method but with just or SpaceShip object.

Within the game loop we should check if our hero has made contact with any aliens. If so we want to stop the game

	self.hero.draw(self.space_surface)
	
	self.all_aliens.draw(self.space_surface)
	self.all_aliens.update()
	
	self.all_bullets.update(self.all_aliens)
	self.all_bullets.draw(self.space_surface)

 	# Adding this line will close our game if our hero collides with the aliens
	if pygame.sprite.spritecollide(self.hero, self.all_aliens, False):
		pygame.quit()
		sys.exit()

**CONGRATULATIONS! YOUVE COMPLETED YOUR FIRST GAME!!**

Now obviously this isn't the best game off the block. It definitely needs improvements. We wouldn't want our game to close down every time we lost and had to restart it. We could also use a game window, a way to win, maybe a way to keep score, and if possible maybe some health packs or power ups. If you've made it up to this point you now have everything you need to replicate your own game or make improvements to this one. For some additional practice try out the exercises below

Add a feature that allows the enemy class to attack our player. Ensure that each instance of the enemy can attack, create an event for it, and add some collisions to their attack to hurt us. Feel free to add your own images or just create another shape like our bullet but change its color.

EXERCISE 2

Add a Scoreboard. Pygame has methods that allow you to write on the screen and even keep count. Attempt to increase your score count every time you destroy one of the enemy. Pygame comes with default fonts or you can download some of your own.

EXERCISE 3

Add music and sound effects to our classes. The game doesn't really have much of a mood and seems kind of dull. You can even attempt to make a death screen and a death sound animation.

EXERCISE 4

Give our player more lives. Up to this point if we get hit once our animation window closes up and that's no fun. Allow the player to be able to have a couple more chances if he messed up. It would also be nice to be able to see what our lives counter looks like.

EXERCISE 5

Are the enemies too slow? Do you not attack fast enough? Add a powerup that spawns randomly around the game at random times and random locations that can either increase your movement speed or attack speed temporarily or even slow the enemies' movements for some time to allow for easier kills.
 
