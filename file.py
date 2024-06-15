import pandas as pd

# Load the original data
file_path = '/root/distanceBetweenStates/uscities.csv'  # Make sure this path is correct
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Select necessary columns and potentially preprocess data
selected_data = data[['city', 'state_id', 'lat', 'lng', 'population', 'density']].copy()  # Including 'density'

# Create a new column combining city and state abbreviation
selected_data['city_with_state'] = selected_data['city'] + ', ' + selected_data['state_id']

# Save the processed data
processed_file_path = '/root/distanceBetweenStates/processed_uscities.csv'
selected_data.to_csv(processed_file_path, index=False)
# After loading the data
print(data.columns)
