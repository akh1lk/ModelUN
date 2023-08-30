def assign_activities(preferences, grade_levels):
    num_students = len(preferences)
    num_activities = len(preferences[0])
    
    # Create a list of student indices
    student_indices = list(range(num_students))
    
    # Sort student indices based on grade levels (seniors first)
    student_indices.sort(key=lambda idx: grade_levels[idx], reverse=True)
    
    # Initialize activity assignment list
    activity_assignment = [-1] * num_activities
    
    # Assign activities to students based on their preferences
    for student_idx in student_indices:
        student_preferences = preferences[student_idx]
        for preference in student_preferences:
            if activity_assignment[preference] == -1:
                activity_assignment[preference] = student_idx
                break
    
    return activity_assignment

# Example data
preferences = [
    [0, 1, 2],  # Student 0 preferences
    [1, 0, 2],  # Student 1 preferences
    [2, 1, 0]   # Student 2 preferences
]



preference_to_number = {
    "Press Corps | Fakt": 0,
    "SOCHUM | Pakistan (This is a Two-Person Role)": 1,
    "Uncovering the Snowden Files | Warren Tucker - Director of the Security Intelligence Service (SIS)": 2,
    "OHCHR | Republic of Korea": 3,
    "Nigeria-Biafra Civil War JCC: Nigeria | Oduduwa Iyanda": 4,
    "Cuban Revolution | Rolando Cubela": 5,
    "The Court of Camelot | Sister Senara of Zennor": 6
}

references = {
    "MoniYah Person-Henderson": [0, 1, 2, 3, 4, 5, 6],
    "David Sun": [4, 5, 6, 2, 3, 1, 0],
    "Muhan Yao": [3, 1, 2, 6, 4, 5, 0],
    "Kiern Lim": [1, 3, 0, 6, 2, 5, 4],
    "Akhil Kagithapu": [2, 5, 3, 6, 0, 1, 4],
    "Arul Jindal": [2, 1, 3, 6, 0, 4, 5],
    "Jeremy Lee": [3, 6, 1, 0, 2, 5, 4]
}

preferences = [[0, 1, 2, 3, 4, 5, 6], [4, 5, 6, 2, 3, 1, 0],[3, 1, 2, 6, 4, 5, 0],[1, 3, 0, 6, 2, 5, 4],[2, 5, 3, 6, 0, 1, 4],[2, 1, 3, 6, 0, 4, 5],[3, 6, 1, 0, 2, 5, 4]]


# Corresponding grade levels (9th to 12th grade)
grade_levels = [12, 11, 10, 10, 11, 9, 11]

activity_assignment = assign_activities(preferences, grade_levels)

num_to_pref = {v: k for k, v in preference_to_number.items()}

activity_assignment_dict = {
    "MoniYah Person-Henderson": activity_assignment[0],
    "David Sun": activity_assignment[1],
    "Muhan Yao": activity_assignment[2],
    "Kiern Lim": activity_assignment[3],
    "Akhil Kagithapu": activity_assignment[4],
    "Arul Jindal": activity_assignment[5],
    "Jeremy Lee": activity_assignment[6]
}
for key,val in activity_assignment_dict.items():
    activity_assignment_dict[key] = num_to_pref[activity_assignment_dict[key]]

print(activity_assignment_dict)
