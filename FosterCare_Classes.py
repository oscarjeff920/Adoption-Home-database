import pandas as pds

class Foster_Children:
	children_in_care = {}
	adopted_children = {}

	def __init__(self, name, age, gender, years_in_foster_care):
		self.name = name
		self.age = age
		self.gender = gender
		self.years_in_foster_care = years_in_foster_care
		Foster_Children.children_in_care[name] = {"name" : self.name, "age" : self.age, "gender" : self.gender, "years in foster care" : self.years_in_foster_care}	

	@classmethod
	def foster(cls, parents, child):
		cls.adopted_children[child] = cls.children_in_care[child]
		cls.adopted_children[child].update( {"parents" : parents})
		cls.adopted_children[child].update( {"adopted" : True})
		cls.children_in_care.pop(child)

	@classmethod
	def Print_adopted_children(cls):
		print("There are currently %s adopted children:\n\n"%len(cls.adopted_children))
		for Child in cls.adopted_children:
			print("%s is a %s year old %s living with the %s family."
				%(cls.adopted_children[Child]["name"], cls.adopted_children[Child]["age"],cls.adopted_children[Child]["gender"].lower(), cls.adopted_children[Child]["parents"]))

	@classmethod
	def Print_children_in_care(cls):
		print("There are currently %s children in care:\n\n"%len(cls.children_in_care))
		for Child in cls.children_in_care:
			print("%s is a %s year old %s who has been in foster care for %s years\n"
				%(cls.children_in_care[Child]["name"], cls.children_in_care[Child]["age"],cls.children_in_care[Child]["gender"].lower(), cls.children_in_care[Child]["years in foster care"]))


class Parents:
	max_children = 4
	foster_families = {}

	def __init__(self, name, parent1, age1, parent2, age2):
		self.name = name
		self.parent1 = parent1
		self.age1 = age1
		self.parent2 = parent2
		self.age2 = age2
		self.children = {}
		Parents.foster_families[self.name] = dict(name = self.name, parent1 = self.parent1, age1 = self.age1, parent2 = self.parent2, age2 = self.age2, children = self.children)

	def current_children(self, name = "List", age = 0, gender = 0, adopted = False, years_in_foster_care = 0):
		if name == "List":
			print("The %s family currently have %s children under their care:"%(self.name, len(self.children)))
			for child in self.children:
				if self.children[child]["adopted"] == False:
					print("%s is an %s year old %s and was not adopted\n"%(self.children[child]["name"], self.children[child]["age"], self.children[child]["gender"]))
				else:
					print("%s is an %s year old %s that was adopted by the %s family and has spent %s years in foster care.\n"
						%(self.children[child]["name"], self.children[child]["age"],
							self.children[child]["gender"], self.name, self.children[child]["years in foster care"]))
		else:
			self.children[name] = {"name" : name, "age" : age, "gender" : gender, "adopted" : adopted, "years in foster care" : years_in_foster_care}

	def number_of_children(self):
		return len(self.children)

	def adopt(self, *Child):
		if self.number_of_children() == Parents.max_children or (len(Child) + len(self.children)) > Parents.max_children:
			if len(Child) > 1:
				return print("Our policy on maximum family size means the %s family are unable to adopt more than %s children.\n\n"%(self.name, (Parents.max_children - len(self.children))))
			else:
				return print("The %s's are unable to adopt %s because our policies only allow families with less than 4 children to adopt.\n\n"%(self.name, name))
		else:
			for kid in Child:
				Foster_Children.foster(self.name.capitalize(), kid)
			self.children[kid] = Foster_Children.adopted_children[kid]
			self.children[kid.capitalize()].pop("parents")

	
Foster_Children("Stevie", 6, "Boy", 3)
Foster_Children("Jack", 5, "Boy", 4)
Foster_Children("Paula", 8, "Girl", 7)
Foster_Children("Pierre", 20, "Boy", 15)
Foster_Children("Gertude", 17, "Girl", 4)
Foster_Children("Elizabeth", 10, "Girl", 3)
Foster_Children("Molly", 8, "Girl", 3)
Foster_Children("Billy", 8, "Boy", 3)

Smith = Parents("Smith","Paul", 35, "Susan", 32)
Smith.current_children("Jean-Paul", 8, "Boy")
Smith.current_children("Sandrine", 3, "Girl", True, 1)

#print(Smith.number_of_children())

Smith.adopt("Pierre")
print(Smith.current_children("List")) #this lists off all the current children under the 'Smith' family's care
Smith.adopt("Molly", "Billy")
print(Smith.current_children("List")) #this lists off all the current children under the 'Smith' family's care

