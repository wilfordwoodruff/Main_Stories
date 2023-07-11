#%%
'''
Imports
'''
import pandas as pd
import nltk
nltk.download('averaged_perceptron_tagger')

#%%
url = "https://raw.githubusercontent.com/wilfordwoodruff/Main-Data/main/data/derived/derived_data.csv"
df = pd.read_csv(url)
# %%
df.head()
# %%
df.info()
#%%
df['Current Location'] = None
df['Mentioning Location'] = None

# %%
df['Document Type'].unique()
# %%
df['Text Only Transcript'][0]
# %%
# Create a new dataframe with non-null 'Places' values
df_places = df[df['Places'].notnull()]
#%%
# Create a new column 'Locations' by splitting 'Places' on '|'
df_places['Locations'] = df_places['Places'].str.split('|')
#%%
# Flatten the list of locations
locations = [item.strip() for sublist in df_places['Locations'].tolist() for item in sublist]
#%%
# Print unique locations
print(set(locations))
# %%
# define a list of prepositions that might be used to denote a current location
current_prepositions = ['in', 'at', 'on']

# define a list of verbs and prepositions that might be used to denote a mentioning location
mentioning_words = ['from', 'about', 'via', 'send', 'talk']

# %%
# iterate over df_places
for index, row in df_places.iterrows():
    # tokenize the transcript into sentences
    sentences = nltk.tokenize.sent_tokenize(row['Text Only Transcript'])

    current_locations = []
    mentioning_locations = []

    # check each sentence
    for sentence in sentences:
        words = nltk.tokenize.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)

        # Create a dictionary to store word-position pairs
        word_pos_dict = {word.lower(): pos for word, pos in tagged_words}

        # check each location
        for location in row['Locations']:  # now 'Locations' exists in df_places
            # if location is mentioned in the sentence
            if location in sentence:
                # check if it's a current location
                for word in current_prepositions:
                    if word in word_pos_dict and word_pos_dict[word] == 'IN':
                        current_locations.append(location)
                # check if it's a mentioning location
                for word in mentioning_words:
                    if word in word_pos_dict and (word_pos_dict[word] == 'IN' or word_pos_dict[word] == 'VB'):
                        mentioning_locations.append(location)

    # Now, store the lists of locations in the dataframe, using '|' as a separator
    if current_locations:
        df_places.at[index, 'Current Location'] = '|'.join(current_locations)
    if mentioning_locations:
        df_places.at[index, 'Mentioning Location'] = '|'.join(mentioning_locations)
#%%
def remove_duplicates(locations):
    if locations is not None:
        # Split the string into a list
        locations_list = locations.split('|')
        
        # Transform the list into a set to remove duplicates
        locations_set = set(locations_list)
        
        # Join the set back into a string
        cleaned_locations = '|'.join(locations_set)
        
        return cleaned_locations
    else:
        return None
#%%
df_places['Current Location'] = df_places['Current Location'].apply(remove_duplicates)
df_places['Mentioning Location'] = df_places['Mentioning Location'].apply(remove_duplicates)
#%%
df_places['Current Location']
# %%
df_places['Mentioning Location']
# %%
df_places.to_csv('df_places.csv', index=False)
# %%
