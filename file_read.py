import os





"""
I made the parent_path as a param instead of an attribute of the class is to
- Flexibility: You can work with different parent_path values without needing to create a new instance of the class each time.
- Modularity: Each method can operate independently, making it easier to test and debug.
- Simplicity: Reduces the complexity of the class, making it easier to maintain and understand.

I am using static methods decorator
@staticmethod
"""


class file_read_c():
    def __init__(self):
        pass

    @staticmethod
    def return_years(parent_path):
        # returns years in a list e.g.[year1,year2]

        years_and_files = {}
        year_list = os.listdir(parent_path)

        for year in year_list:
            years_and_files[year] = len(os.listdir(parent_path + "/" + year)) # put inside the year dict
        
        return years_and_files
        





    @staticmethod
    def find_year_path(parent_path, year, prefix):
        # returns the path of the arguement year
        year_list = os.listdir(parent_path)
        year_path = None

        for i in year_list:
            if i == f"{prefix}{year}":
                year_path = f"{parent_path}/{prefix}{year}"
        return year_path

            
        
        
        
    
    @staticmethod
    def return_files(year_path):
        # returns list of files in a dir e.g.  [file1,file2,file3]

        files_list = os.listdir(year_path)
        
        return files_list

    @staticmethod
    def return_content(parent_path,year,):
        # returns dictionary of the contents of a file. Includes year, filename, and file lines. e.g
        """
        {year:[
            {
            filename:[
                "1,team1,regassoc1",
                "2,team2,regassoc2",
            ]},
            filename:[
                "1,team1,regassoc1",
                "2,team2,regassoc2",
            ]},
            filename:[
                "1,team1,regassoc1",
                "2,team2,regassoc2",
            ]},
        ]}
        """
        pass