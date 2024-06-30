
# use static methods

class scoring_c():
    def __init__(self):
        pass

    
    def return_scores(filename,file_contents): # file_contents is a list
        
        """# returns the scores in a dictionary. Includes the filename {filename:{reg1:100,reg2:200}}
        file_headers = file_contents[0] # first
        file_body = file_contents[1:-1] # second to the last
        
        # 2,57145,3,HEKE  Kura,,Kaihoe o Ngati Rehia Trust,3:10.92,,4.28,,,16:14:09.09,,,,4.28,4.28\n

        # Convert to list and remove the additional commas
        for team in file_body:
            team_split = team.split(',')
            for i in team_split:
                if i == "":
                    team_split.remove(i or "")
                    team_place = team_split[0]
                    team_lane = team_split[3]
                    team_name = team_split[4]
                    team_regional_association = team_split[5]
"""
                    
        
        
        

                    
        




    def return_total_year_score(files_contents_dictionary ): # {filename:{reg1:100,reg2:200},filaname{reg1:100,reg2:200}}
        # returns the total year score e.g. {reg1:500,reg2:600}
        pass
