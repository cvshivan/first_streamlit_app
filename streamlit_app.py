import streamlit

streamlit.title('My Mom\'s New Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruites:", list(my_fruit_list.Fruit),['Avocado','Strawberries'])
#fruits_selected = streamlit.multiselect("Pick some fruites:", list(my_fruit_list.index),index(['Avocado','Strawberries']))
#fruits_selected = streamlit.multiselect("Pick some fruites:", list(my_fruit_list.index),[1,16])

#streamlit.dataframe(fruits_selected)


#fruits_to_show = my_fruit_list.loc[[1,16]]
fruits_to_show = my_fruit_list.iloc[fruits_selected]
#fruits_to_show = my_fruit_list
# print(fruits_to_show)

# display the table on the page
streamlit.dataframe(fruits_to_show)


#good_keys = df.index.intersection(all_keys)
#df.loc[good_keys]
