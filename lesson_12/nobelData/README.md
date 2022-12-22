For this project, you will import the **json** module.

Write a class named NobelData that reads the nobels.json file and allows the user to search that data.

Your class should have:
* an init method that reads the file and stores it in whatever data member(s) you prefer. Any data members of the NobelData class must be **private**.
* a method named search_nobel that takes as parameters a year and a category, and returns a sorted list (in normal English dictionary order) of the surnames for the winner(s) in that category for that year (up to three people can share the prize). The year will be a string (e.g. "1975"), not a number. The categories are: "chemistry", "economics", "literature", "peace", "physics", and "medicine".

For example, your class could be used like this:

nd = NobelData()
nd.search_nobel("2001", "economics")
