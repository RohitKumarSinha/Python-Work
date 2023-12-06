class profile():

    def __init__(self, name, age, father_name, mother_name, sex, married, equational_qualification):

        self.name = name
        self.age = age
        self.sex = sex
        self.father_name = father_name
        self.mother_name = mother_name
        self.married = married
        self.equational_qualification = equational_qualification

    def get(self):

        self.name = input("enter your name :- ")
        self.age = input("enter your age :- ")
        self.sex = input("enter your sex :- ")
        self.father_name = input("enter your father's name :- ")
        self.mother_name = input("enter your mother's name :- ")
        self.married = input("you are married or not :- ")
        self.equational_qualification = input("enter your equational_qualification :-")

    def post(self):

        print(
        f"""let's recheck your form ....
        your name is {self.name}
        your age is {self.age}
        your sex is {self.sex}
        your father's name is {self.father_name}
        your mother's name is {self.mother_name}
        your married status is {self.married}
        your equational_qualification is {self.equational_qualification}
        """)


class mobile():

    def __init__(self, mobile_name, processor, ram, rom, front_camera, back_camera, screen_size):

        self.mobile_name = mobile_name
        self.processor = processor
        self.ram = ram
        self.rom = rom
        self.front_camera = front_camera
        self.back_camera = back_camera
        self.screen_size = screen_size

    def get(self):

        self.mobile_name = input("Which mobile do you want ? :-")
        self.processor = input("which type of processor you want in that mobile :- ")
        self.ram = input("How many ram you want in that mobile :- ")
        self.rom = input("How many rom you want in that mobile :- ")
        self.back_camera = input("How many mega pixel you want in back camera :- ")
        self.front_camera = input("How many mega pixel you want in front camera :- ")
        self.screen_size = input("how many inches you want the screen size :- ")

    def post(self):

        print(f""" let's recheck your mobile specification ....
        you want {self.mobile_name}
        mobile has {self.processor} processor
        mobile has {self.ram} ram
        mobile has {self.rom} rom
        mobile has {self.back_camera} mega pixel back camera
        mobile has {self.front_camera} mega pixel front camera
        mobile has {self.screen_size} inch screen
        i hope your wish come into reality
        """)
