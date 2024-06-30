import file_read as fr
import gui
import scoring
import csv_export


GUI_Screen = gui()









































points_refference = {
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




# get years
# ask_parent_path = input("Type your parent folder >> ")
parent_path = "waka_parent"
print(fr.file_read_c.return_years(parent_path))


# get all the files
# ask_year = int(input("Type your year >> "))
ask_year = "2018"
target_year_path = fr.file_read_c.find_year_path(parent_path,ask_year,"WakaNats")
files_list = fr.file_read_c.return_files(target_year_path)

# find specific keyword only
# ask_keyword = input("filter keyword >> ")
ask_keyword = "final"
filtered_files_list = []
for file in files_list:
    if ask_keyword in file.lower():
        filtered_files_list.append(file)
    else:
        continue
print(len(filtered_files_list), ask_keyword, "found")




files_regional_association_score_list = []

# get contents
for filename in filtered_files_list:
    try:
        filepath = f"{target_year_path}/{filename}"
        file_contents = fr.file_read_c.return_content(filepath)
    

        # get formatted version
    
        formatted_file_contents = fr.file_read_c.format_content(file_contents,filename)
    
        # check if there are errors
        if type(formatted_file_contents) is tuple:
            print(formatted_file_contents)
            continue

        # get the regional assocation scores of the file
        file_regional_association_scores = scoring.scoring_c.return_scores(formatted_file_contents,points_refference)
        files_regional_association_score_list.append(file_regional_association_scores)

    except Exception as e:
        print(f"ERROR | {filename} | {e}")
        continue


# get sum of all the regional assocation scores
year_regional_association_scores = scoring.scoring_c.return_year_sum_score(files_regional_association_score_list)


# sort the file (descending)
year_regional_association_scores = scoring.scoring_c.sort_score(year_regional_association_scores)
"""
# format the scores
Regional_Associations = list(year_regional_association_scores.keys())
Regional_Associations_Scores = list(year_regional_association_scores.values())"""




# get the csv export option
ask_csv_export = input("Do you wish to save as CSV?(Y/N) >> ")
if ask_csv_export == "Y":
    ask_csv_filename = input("Type filename >> ")
    csv_export.csv_c.csv_export(year_regional_association_scores,ask_csv_filename)