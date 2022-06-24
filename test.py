class Person:
    def __init__(self, firstName, lastName, title):
        self.firstName = firstName
        self.lastName = lastName
        self.title = title
        
class Family:
    def __init__(self, father, mother, children, familyName):
        self.father = father
        self.mother = mother
        self.children = children
        self.familyName = familyName

"""

koliko vidim python nema toString() metodu, to bi bilo ovako nekako u javi

public String toString(){ 
  return "In the " + familyName + "family Mother " +  mother + "and Father " + father + 
    "have" + children.length + "children:\n + Arrays.toString(children)";
 }  


console.log(families[0].toString());
console.log(families[1].toString());

nisam siguran u Arrays.toString(children) kad mjenjamo toString() metodu, tako se inace ispisuju 
array-i u javi ili preko for petlje

"""


def parseFamilies(inputStr):
    splitArray = inputStr.split(',')
    titleArray = []
    getNamesArray = []
    firstNames = []
    lastNames = []
    families = []
    
    for ele in splitArray: 
        if "Mr." in ele:
            titleArray.append("Father")
        elif "Mrs." in ele:
            titleArray.append("Mother")
        else:
            titleArray.append("Child")         
    
    for ele in splitArray:
        getNamesArray.append(ele.split())
    
    length = len(getNamesArray)
    for i in range (length):  
        tempLastName = getNamesArray[i][-1]
        tempName = getNamesArray[i][-2]
        firstNames.append(tempName)
        lastNames.append(tempLastName)
    
    people = []
    for i in range(length):
        people.append(Person(firstNames[i], lastNames[i], titleArray[i]))
        print('Person', i+1,":", people[i].firstName, people[i].lastName, "-", people[i].title)
    
    for i in people:
        if i.lastName not in families:
            families.append(i.lastName)
    print('\nFamilies: ', families, '\n')
    familyLength = len(families)

    tempFather = ''
    tempMother = ''
    tempLastName = ''
    tempChildrenNames = []
    family = []  
    
    while (familyLength > 0):
        for i in range (length):
            if people[i].lastName == families[familyLength-1]:
                tempLastName = people[i].lastName
                if people[i].title == 'Father':
                    tempFather = people[i].firstName
                if people[i].title == 'Mother':
                     tempMother = people[i].firstName
                if people[i].title == 'Child':
                    tempChildrenNames.append(people[i].firstName)
                        
        family.append(Family(tempFather, tempMother, tempChildrenNames, tempLastName))
        tempFather = ''
        tempMother = ''
        tempLastName = ''
        tempChildrenNames = []
        familyLength -= 1


    
    for i in range(len(families)):
        print('In the', family[i].familyName, 'family Mother', family[i].mother, 'and Father', family[i].father, 'have', len(family[i].children), 'children:')

        for j in range(len(family[i].children)):
            if j==len(family[i].children)-1:
                print (family[i].children[j], '\n')
            elif j==len(family[i].children)-2:  
                print(family[i].children[j], 'and ', end = '')
            else:
                print(family[i].children[j], '',sep=', ', end = '')
        
            

families = ('Mr. Mario Mucalo, Mrs. Paola Gemić, Mrs. Ana Mucalo, Tonka Mucalo, Mr. Juraj Gemić, Lara Gemić, Toma Mucalo, Taka Mucalo, Raka Mucalo, Mr. Thomas Gemulo, Anna Gemulo, Petar Gemulo, Mrs. Lanna Gemulo');
families2 = ('Mr. Mario Mucalo, Mrs. Paola Gemić, Mrs. Ana Mucalo, Tonka Mucalo, Mr. Juraj Gemić, Lara Gemić, Toma Mucalo');
parseFamilies(families)
parseFamilies(families2)