class User:
    id = None
    first_name = ""
    last_name = ""
    gender = ""
    email = ""
    program = ""
    degree = ""
    password = ""
    age = None
    study_year = None

    def __init__(
        self,
        id,
        first_name,
        last_name,
        gender,
        email,
        program,
        degree,
        password,
        age,
        study_year,
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.program = program
        self.degree = degree
        self.password = password
        self.age = age
        self.study_year = study_year
