import pandas as pd

# Function to take an advanced personality quiz and create user_profile.csv
def take_quiz():
    print("Welcome to the Comprehensive Personality Quiz!")
    print("Answer the following questions to help us understand your profile. Choose the number that best represents your answer (1 being the lowest and 10 being the highest).")

    # Questions contributing to each metric
    questions = {
        'social': [
            "How comfortable are you initiating conversations with new people? (1-10): ",
            "How often do you prefer spending time in large groups? (1-10): ",
            "How much do you enjoy attending social events? (1-10): "
        ],
        'occupational': [
            "How satisfied are you with your productivity at work or school? (1-10): ",
            "How motivated do you feel to achieve your career or academic goals? (1-10): ",
            "How effective are you at managing work-related stress? (1-10): "
        ],
        'environmental': [
            "How much do you value spending time outdoors? (1-10): ",
            "How conscious are you about environmental issues and sustainability? (1-10): ",
            "How peaceful do you feel when surrounded by nature? (1-10): "
        ],
        'spiritual': [
            "How important are personal beliefs or spirituality in your life? (1-10): ",
            "How often do you engage in reflective or meditative practices? (1-10): ",
            "How connected do you feel to something greater than yourself? (1-10): "
        ],
        'intellectual': [
            "How frequently do you engage in learning new things, such as reading or taking courses? (1-10): ",
            "How much do you enjoy solving challenging problems or puzzles? (1-10): ",
            "How curious are you about a wide range of topics? (1-10): "
        ],
        'emotional': [
            "How well do you handle stressful situations? (1-10): ",
            "How comfortable are you discussing your feelings with others? (1-10): ",
            "How resilient are you when facing setbacks? (1-10): "
        ],
        'physical': [
            "How often do you exercise or participate in physical activities? (1-10): ",
            "How well do you maintain a balanced diet and healthy lifestyle? (1-10): ",
            "How important is physical health to you in your daily routine? (1-10): "
        ]
    }

    user_profile = {}

    # Iterate over each metric and ask questions
    for metric, metric_questions in questions.items():
        total_score = 0
        for question in metric_questions:
            while True:
                try:
                    score = int(input(question))
                    if 1 <= score <= 10:
                        total_score += score
                        break
                    else:
                        print("Please enter a number between 1 and 10.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 10.")
        
        # Calculate average score for the metric
        average_score = total_score / len(metric_questions)
        user_profile[metric] = round(average_score)

    # Convert to DataFrame and save to CSV
    user_profile_df = pd.DataFrame([user_profile])
    user_profile_df.to_csv('data/user_profile.csv', index=False)

    print("\nThank you! Your profile has been saved successfully.")

# Run the quiz function
take_quiz()
