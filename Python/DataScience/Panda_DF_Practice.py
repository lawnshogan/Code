import pandas as pd

high_schools = ["Huang High School",  "Figueroa High School", "Shelton High School", "Hernandez High School","Griffin High School","Wilson High School", "Cabrera High School", "Bailey High School", "Holden High School", "Pena High School", "Wright High School","Rodriguez High School", "Johnson High School", "Ford High School", "Thomas High School"]

school_series = pd.Series(high_schools)

school_series

high_school_dicts = [{"School ID": 0, "school_name": "Huang High    School", "type": "District"},
                   {"School ID": 1, "school_name": "Figueroa High School", "type": "District"},
                    {"School ID": 2, "school_name":"Shelton High School", "type": "Charter"},
                    {"School ID": 3, "school_name":"Hernandez High School", "type": "District"},
                    {"School ID": 4, "school_name":"Griffin High School", "type": "Charter"}]

school_df = pd.DataFrame(high_school_dicts)
school_df

school_id = [0,1,2,3,4]
school_name = ["Huang High School", "Figueroa High School", "Shelton High School", "Hernandez High School", "Griffin High School"]
type_of_school = ["District", "District", "Charter", "District", "Charter"]
schools_df = pd.DataFrame(school_name)
schools_df["School Name"] = school_name
schools_df

# Get Column attributes
school_df.columns

# Get Index attributes
school_df.index

# Get Value attributes
school_df.values

