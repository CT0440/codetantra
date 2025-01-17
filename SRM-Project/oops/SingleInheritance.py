# #Scenario-Based Question:

# In a company, the TeamLead is responsible for a project and has several TeamMembers working under them.

# TeamLead:

# Has a property project representing the project name.
# TeamMember:

# Has two properties: name and salary.
# Does not know the project name initially but can access it by inheriting from the TeamLead.
# Write a Python program to implement the relationship where the TeamMember inherits the project property from TeamLead. The program should include:

# A method in TeamMember to display their name, salary, and the project inherited from TeamLead.
# Ensure that the TeamMember accesses the project property without being explicitly passed during initialization.


class TeamLead:
    def __init__(self,project):
        self.project = project
    

class TeamMember(TeamLead):
    def __init__(self, name, salary, project):
        super().__init__(project)
        self.name = name
        self.salary = salary
    
    def showDetails(self):
        return f"Team member Name: {self.name}\n TeamMember Salary: {self.salary}\n Project: {self.project}"
        

lead = TeamLead("Python Project")

mem = TeamMember("susruthi", 15000, lead.project)
print(mem.showDetails())



