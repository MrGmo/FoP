Remember that all data members should be **private**. An object can access it's own private data members directly. It can also access the private data members of other objects *of the same class* directly. But when accessing a private data member of an object of *another* class, it needs to call the appropriate get method. If that sounds complicated, just remember this: if a method is in the same class as a private data member, then it can access that data member directly, otherwise, it needs to use a get method (see the hints at the end).

Write a class named **Point** that has two data members, **x_coord** and **y_coord**, representing the two coordinates of the point. It should have:
* an init method that takes two arguments, an x-coordinate and y-coordinate (in that order), and uses them to initialize the two data members.
* get methods for the two data members: **get_x_coord** and **get_y_coord**.
* a method named **distance_to** that takes a Point object as an argument. It returns the distance between the Point object the method is called on (the one in front of the dot) and the Point object passed as the argument. For example, if point_1 and point_2 are both Point objects, then ```point_1.distanceTo(point_2)``` should return the distance between point_1 and point_2 (and ```point_2.distanceTo(point_1)``` should return the same distance). For this method, you'll calculate the distance using the following formula:

distance_formula.png: "formula for distance between two points"
where d is the distance and the two points are (x1, y1) and (x2, y2)

The above formula requires taking the square root. As you might recall, you can just use the exponent of 0.5. For example, the result of 9 ** 0.5 would be 3.0. Python does have a specific sqrt() function, but that involves importing a module, which we haven't covered yet.

Now write a class named **LineSegment** that has two data members, **endpoint_1** and  **endpoint_2**, representing the two endpoints of the line segment. It should have:
* an init method that takes two Point objects as arguments and uses them to initialize the two data members (the endpoints of the LineSegment).
* get methods for the two data members: **get_endpoint_1** and **get_endpoint_2**.
* a method named **length** that takes no arguments and returns the distance between its two endpoints. This can make use of the Point's distance_to method.
* a method named **is_parallel_to** that takes a LineSegment object as an argument. It returns True if the LineSegment the method is being called on is parallel to the one being passed as the argument. Otherwise, it should return False. For example, if line_seg_1 and line_seg_2 are both LineSegment objects, then ```line_seg_1.is_parallel_to(line_seg_2)``` should return True if those two line segments are parallel, but otherwise should return False. For this method, you'll calculate the slopes of the two LineSegments and compare them. If the two slopes are equal, then the two line segments are parallel, otherwise they are not. This can make use of the following slope method. **Remember that you shouldn't test two floats for exact equality because of possible lack of precision or round-off errors. Instead, if you need to compare float values for equality, you can do it like this: abs(num_1 - num_2) < 0.000001**
* a method named **slope** that takes no arguments and returns the slope of the LineSegment. You can find the slope using the following formula:

slope_formula.png: "formula for slope of a line segment"
where m is the slope and again the two points are (x1, y1) and (x2, y2), which in this case are the two endpoints of the LineSegment.

Here's a simple example of how your code might be used:

point_1 = Point(7,4)
point_2 = Point(-6,18)
print(point_1.distance_to(point_2))
line_seg_1 = LineSegment(point_1,point_2)
print(line_seg_1.length())
print(line_seg_1.slope())

point_3 = Point(-2,2)
point_4 = Point(24, 12)
line_seg_2 = LineSegment(point_3,point_4)
print(line_seg_1.is_parallel_to(line_seg_2))

Hint 1: Start with the Point class and make sure it's working correctly before going on to the LineSegment class.

Hint 2: In the distance_to method, you'll be working with two pairs of coordinates. The Point object the method is called on is the one that executes the method, and it can access its own coordinates directly, for example ```self._x_coord```. The other pair of coordinates comes from the Point that was passed in as an argument. Because the distance_to method belongs to the Point class, it can access those Point data members directly, without needing to use a get method. For example, if the parameter name is other_point, you can do ```other_point._x_coord```.

Hint 3: In the methods of the LineSegment class, you'll need to access the coordinates of Point objects. Because those methods are not part of the Point class, they need to call the Point get methods on a Point object to access its coordinates. For example, ```self._endpoint_1.get_x_coord()```.
