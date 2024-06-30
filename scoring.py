
# use static methods

class scoring_c():
    def __init__(self):
        pass

    
    def return_scores(filename,formatted_file_contents,points_refference): # file_contents is a list
        # returns the regional association scores with filename
        """
        {
        "1":8,
        "2":7,
        "3":6,
        "4":5,
        "5":4,
        "6":3,
        "7":2,
        "8":1,
        ">":1,

        }
        """
        
        if points_refference.keys()[-1] == ">":
            last_option = True
            last_option_value = points_refference.values()[-1]
            points_refference.pop() # removes the 'last option'
        
        regional_association_scores = {}

        teams_list = list(formatted_file_contents.values())[1] # gets the teams list
        last_points_refference = points_refference.keys()[-1]
        for team_dict in teams_list:
            team_place = team_dict["place"]
            team_regional_association = team_dict["regional_association"]
            for place_refference in points_refference.keys():
                if place_refference == team_place:
                    
                    if team_regional_association in regional_association_scores:
                        regional_association_scores[team_regional_association] += points_refference[place_refference]
                    else:
                        regional_association_scores[team_regional_association] = points_refference[place_refference]

                elif last_option == True and team_place > last_points_refference:
                    if team_regional_association in regional_association_scores:
                        regional_association_scores[team_regional_association] += last_option_value
                    else:
                        regional_association_scores[team_regional_association] = last_option_value

        file_scores = {filename:regional_association_scores}
        return file_scores
        
        
        
        

                    
        




    def return_total_year_score(files_contents_dictionary ): # {filename:{reg1:100,reg2:200},filaname{reg1:100,reg2:200}}
        # returns the total year score e.g. {reg1:500,reg2:600}
        pass
