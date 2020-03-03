import csv


def read_test():
    f = open("demo.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)


def write_test():
    f = open("demo.txt", "a")
    f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et "
            "dolore magna aliqua.Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip "
            "ex ea commodo consequat.Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu "
            "fugiat nulla pariatur.Excepteur sint occaect cupidatat non proident, sunt in culpa qui officia deserunt "
            "mollit anim id est laborum.")
    f.close()

    # open and read the file after the appending:
    f = open("demo.txt", "r")
    print(f.read())


def write_Array_testFile():
    

    Items = [
        [
            {"createdAt Number": "1582842845914"},
            {"department String": "ITS"},
            {"email String": "vue0741@stthomas.edu"},
            {"facultyname": "Vicky Vue"},
            {"id String": "434341c8-59b1-11ea-97f1-ae9e17f20819"},
            {"image String": "SPSS-AO"},
            {"indexcode String": "40810"},
            {"numberofinstances": "28"},
            {"starttime": "2020-10-21T13:00"}
        ],
        [
            {"createdAt Number": "1582842845914"},
            {"department String": "ITS1"},
            {"email String": "vue0741@stthomas1.edu"},
            {"facultyname": "Vicky1 Vue1"},
            {"id String": "434341c8-59b1-11ea-97f1-ae9e17f20819"},
            {"image String": "SPSS-AO1"},
            {"indexcode String": "408103"},
            {"numberofinstances": "283"},
            {"starttime": "2020-10-21T13:00"}
        ],
        [
            {"createdAt Number": "1582842845914"},
            {"department String": "ITS2"},
            {"email String": "vue0741@stthomas1.edu"},
            {"facultyname": "Vicky1 Vue2"},
            {"id String": "434341c8-59b1-11ea-97f1-ae9e17f20819"},
            {"image String": "SPSS-AO2"},
            {"indexcode String": "408102"},
            {"numberofinstances": "282"},
            {"starttime": "2020-10-21T13:00"}
        ]
    ]

    with open('Array_Test.txt', 'w') as f:
        csv.writer(f, delimiter=' ').writerows(Items)


write_Array_testFile()


# write_test()

# read_test()
