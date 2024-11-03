import numpy as np
import pandas as pd


# Scoring functions
def calculate_gap_score(user_profile, activity):
    return sum([abs(user_profile[key] - activity[key]) for key in user_profile])

def find_similar_users(user_profile, past_user_data):
    # Find users with similar profiles based on Euclidean distance
    past_user_data['similarity'] = past_user_data['profile'].apply(
        lambda x: np.linalg.norm(np.array(list(x.values())) - np.array(list(user_profile.values())))
    )
    similar_activities = past_user_data.sort_values(by='similarity').head(3)['activity'].tolist()
    return similar_activities

def adjust_for_swipes(activity, swiped_right, swiped_left):
    # Penalize activities swiped left and boost activities swiped right
    if activity['name'] in swiped_right:
        return -5  # Boost score for liked activities
    elif activity['name'] in swiped_left:
        return 5  # Penalize score for disliked activities
    else:
        return 0

# Recommendation function
def recommend_activity(user_profile, activities, past_user_data, swiped_right, swiped_left):
    similar_activities = find_similar_users(user_profile, past_user_data)
    
    activities['gap_score'] = activities.apply(lambda row: calculate_gap_score(user_profile, row), axis=1)
    activities['similar_user_score'] = activities['name'].apply(lambda x: -2 if x in similar_activities else 0)
    activities['swipe_score'] = activities.apply(lambda row: adjust_for_swipes(row, swiped_right, swiped_left), axis=1)

    # Calculate final score by weighting the scores (weights can be tuned)
    activities['final_score'] = activities['gap_score'] * 0.5 + activities['similar_user_score'] * 0.3 + activities['swipe_score'] * 0.2
    
    recommended_activity = activities.sort_values(by='final_score').iloc[0]
    return recommended_activity['name']

# Simulate user swiping on a recommended activity
def user_swipe(activity_name, direction, swiped_right, swiped_left):
    if direction == 'right':
        swiped_right.add(activity_name)
    elif direction == 'left':
        swiped_left.add(activity_name)

def swiping():
    # Sample user profile and activities database
    activities = pd.read_csv('data/dummy_activities.csv')
    past_user_data = pd.read_csv('data/dummy_past_user_data.csv')
    user_profile = pd.read_csv('data/user_profile.csv').iloc[0].to_dict()

    # Load swiped right and swiped left data from CSV
    try:
        swiped_right = set(pd.read_csv('swiped_right.csv')['activity'].tolist())
        swiped_left = set(pd.read_csv('swiped_left.csv')['activity'].tolist())
    except FileNotFoundError:
        swiped_right = set()
        swiped_left = set()

    user_swiping = True
    while user_swiping: 
        # Get initial recommendation
        recommended = recommend_activity(user_profile, activities, past_user_data, swiped_right, swiped_left)
        print(f"Recommended activity: {recommended}")

        # User swipes on the activity
        direction = input("Swipe right or left?")
        user_swipe(recommended, direction, swiped_right, swiped_left)

        # Get a new recommendation based on updated data
        new_recommended = recommend_activity(user_profile, activities, past_user_data, swiped_right, swiped_left)
        print(f"New recommended activity: {new_recommended}")
        user_swiping = bool(input("Do you want another recommendation?"))


    # Save swiped right and swiped left back to CSVs
    pd.DataFrame({'activity': list(swiped_right)}).to_csv('swiped_right.csv', index=False)
    pd.DataFrame({'activity': list(swiped_left)}).to_csv('swiped_left.csv', index=False)