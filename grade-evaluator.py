import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    # Check if all scores are percentage based (0-100)
    for assignment in data:
    	score = assignment["score"]

    if score < 0 or score > 100:
        print("Error: Invalid score found.")
        return
    # Validate total weights (Total=100, Summative=40, Formative=60)
    total_weight = 0
    formative_weight = 0
    summative_weight = 0
    for assignment in data:

    	weight = assignment["weight"]

    	total_weight += weight

    	if assignment["group"] == "Formative":
        	formative_weight += weight

    	elif assignment["group"] == "Summative":
        	summative_weight += weight

    if total_weight != 100:
    	print("Error: Total weight must equal 100.")
    	return

    if formative_weight != 60:
    	print("Error: Formative weight must equal 60.")
    	return

    if summative_weight != 40:
    	print("Error: Summative weight must equal 40.")
    	return
    #Weight validation
    total_grade = 0
    for assignment in data:

    	weighted_mark = (assignment["score"] * assignment["weight"]) / 100

    	total_grade += weighted_mark
    print("Total Grade:", total_grade)
   
    #Calulation of GPA
    gpa = (total_grade / 100) * 5
    print("Final Grade:", total_grade)
    print("GPA:", round(gpa, 2))

    # Calculate the Final Grade and GPA
    
    formative_marks = 0
    summative_marks = 0
   
    for assignment in data:

    	mark = assignment["score"] * assignment["weight"] / 100

    	if assignment["group"] == "Formative":
        	formative_marks += mark

    	else:
        	summative_marks += mark
    #converting the summative and formative into percentages
    formative_percentage = (formative_marks / 60) * 100
    summative_percentage = (summative_marks / 40) * 100

    print("Formative Percentage:", round(formative_percentage, 2), "%")
    print("Summative Percentage:", round(summative_percentage, 2), "%")
    # Determine Pass/Fail status (>= 50% in BOTH categories)
    if formative_percentage >= 50 and summative_percentage >= 50:
    	print("Status: PASSED")
    else:
    	print("Status: FAILED")

    # Check for failed formative assignments (< 50%)
    # and determine which one(s) have the highest weight for resubmission.
    failed = []
    for assignment in data:

    	if assignment["group"] == "Formative":

        	if assignment["score"] < 50:
            		failed.append(assignment)
    if len(failed) == 0:
    	print("No resubmission required.")

    highest_weight = 0

    for assignment in failed:

    	if assignment["weight"] > highest_weight:
        	highest_weight = assignment["weight"]
    print("Eligible for resubmission:")

    for assignment in failed:

    	if assignment["weight"] == highest_weight:
        	print("-", assignment["assignment"])
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    
if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)
