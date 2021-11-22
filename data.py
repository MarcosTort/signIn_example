# this file will create the data we will use for the tests
from faker import Faker
import countries
import random
import string
import cons

# this class will modal a user
class Data:

    def __init__(self, a, b, c, d, e, f, g):
        self.CompanyName = a
        self.FirstName = b
        self.LastName = c
        self.Email = d
        self.Pass = e
        self.CPass = f
        self.Country = g


# this constant will define the amount of iterations
validData = []
withoutName = []
withoutEmail = []
withoutCompany = []
withoutPassword = []
withoutLastName = []
confirmPassWrong = []
negative = [withoutName, withoutEmail, withoutCompany, withoutPassword, withoutLastName, confirmPassWrong]
for i in range(cons.iterations):
    # generating fake data
    fak = Faker()
    company = fak.name()
    # splitting fullname into two elements
    fullname = fak.name()
    fullname = fullname.split(' ')
    name = fullname[0]
    lastname = fullname[1]
    #
    email = fak.safe_email()

    # random password
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choice(characters) for x in range(random.randint(8, 16)))

    # picking a random country
    country = random.choice(countries.countries)

    # creating final object and add it to the list
    final = Data(company, name, lastname, email, password, password, country)
    validData.append(final)
    # creating wrong data for negative behaviour
    final = Data(company, name, lastname, '', password, password, country)
    withoutEmail.append(final)
    final = Data(company, name, lastname, email, password + random.choice(string.ascii_letters), password, country)
    confirmPassWrong.append(final)
    final = Data('', name, lastname, email, password, password, country)
    withoutCompany.append(final)
    final = Data(company, '', lastname, email, password, password, country)
    withoutName.append(final)
    final = Data(company, name, '', email, password, password, country)
    withoutLastName.append(final)
    final = Data(company, name, lastname, email, '', '', country)
    withoutPassword.append(final)
