#                   Recommender
#   The AI system to accelerate knowledge 

##########
#LIBRARIES
##########

import streamlit as st
import pickle
import pandas as pd
import requests





#############
#PAGE SET UP
#############

st.set_page_config(page_title="InsightGenie", 
                   page_icon=":robot_face:",
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )

def p_title(title):
    st.markdown(f'<h3 style="text-align: left; color:#F63366; font-size:28px;">{title}</h3>', unsafe_allow_html=True)

#########
#SIDEBAR 
########

st.sidebar.header('InsightGenie, I want to :crystal_ball:')
nav = st.sidebar.radio('',['Go to homepage', 'Movies Recommendation', 'Paraphrase text', 'Analyze text'])
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')

#CONTACT
########
expander = st.sidebar.expander('Contact')
expander.write("I'd love your feedback :smiley: Want to collaborate? Develop a project? Find me on [LinkedIn] (https://www.linkedin.com/in/md-ali-armaghan/), [Twitter] (https://x.com/armaghan78) and [Gmail] (aliarmaghan78@gmail.com)")

#######
#PAGES
######

#HOME
#####

if nav == 'Go to homepage':

    st.markdown("<h1 style='text-align: center; color: white; font-size:28px;'>Welcome to InsightGenie!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-size:56px;'<p>&#129302;</p></h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: grey; font-size:20px;'> Idea behind InsightGenie is that your app provides valuable insights and solutions, almost like a genie granting wishes with its predictive powers!</h3>", unsafe_allow_html=True)
    """
    [![Star](https://img.shields.io/github/stars/dlopezyse/Synthia.svg?logo=github&style=social)](https://github.com/aliarmaghan)
    [![Follow](https://img.shields.io/twitter/follow/armaghan78?style=social)](https://x.com/armaghan78)
    [![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee--yellow.svg?logo=buy-me-a-coffee&logoColor=orange&style=social)](https://www.buymeacoffee.com/lopezyse)
    """
    st.markdown('___')
    st.write(':point_left: Use the menu at left to select a task (click on > if closed).')
    st.markdown('___')
    st.markdown("<h3 style='text-align: left; color:#F63366; font-size:18px;'><b>What is this App about?<b></h3>", unsafe_allow_html=True)
    st.write("Learning happens best when content is personalized to meet our needs and strengths.")
    st.write("For this reason I created InsightGenie :robot_face:, the AI system to accelerate and design your knowledge in seconds!InsightGenie: Your AI-powered genie for smart predictions and insights. Whether it's recommending the perfect movie, classifying emails, or summarizing text, InsightGenie works like magic to provide accurate and reliable results. Let InsightGenie handle the complex tasks effortlessly, making your experience seamless and efficient.")     
    st.markdown("<h3 style='text-align: left; color:#F63366; font-size:18px;'><b>Who is this App for?<b></h3>", unsafe_allow_html=True)
    st.write("Anyone can use this App completely for free! If you like it :heart:, show your support by sharing :+1: ")
    st.write("Are you into NLP? Our code is 100% open source and written for easy understanding. Fork it from [GitHub] (https://github.com/aliarmaghan), and pull any suggestions you may have. Become part of the community! Help yourself and help others :smiley:")

#-----------------------------------------

#       MOVIES RECOMMENDATION
########----------------------##########


# fetch movie poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# define recommend function
def recommend(movie_name):
    index = movies[movies['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:6]
    
    recommended_movies= []
    recommended_movies_poster= []
    for i in distances:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster
    
if nav == 'Movies Recommendation':    
    st.markdown("<h4 style='text-align: center; color:grey;'>Movies Recommendation with InsightGenie &#129302;</h4>", unsafe_allow_html=True)
    st.text('')
    p_title('Movies Recommender')
    st.text('')





    movies_dict = pickle.load(open('Movies-Recommendation-System/movies_dict.pkl','rb'))
    movies = pd.DataFrame(movies_dict)

    similarity = pickle.load(open('Movies-Recommendation-System/similarity.pkl','rb'))

    selected_movies_name = st.selectbox(
    "Please provide me movie name which you like",
    (movies['title'].values))

    if st.button('Show Recommendation'):
        recommended_movie_names,recommended_movie_posters = recommend(selected_movies_name)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])

        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])

#-----------------------------------------

#PARAPHRASE
###########

# if nav == 'Paraphrase text':
#     st.markdown("<h4 style='text-align: center; color:grey;'>Accelerate knowledge with SYNTHIA &#129302;</h4>", unsafe_allow_html=True)
#     st.text('')
#     p_title('Paraphrase')
#     st.text('')
    
#     p_example = 'Health is the level of functional or metabolic efficiency of a living organism. In humans, it is the ability of individuals or communities to adapt and self-manage when facing physical, mental, or social challenges. The most widely accepted definition of good health is that of the World Health Organization Constitution.'
   
#     input_pa = st.text_area("Use the example below or input your own text in English (maximum 500 characters)", max_chars=500, value=p_example, height=160)

#     if st.button('Paraphrase'):
#         if input_pa =='':
#             st.error('Please enter some text')
#         else:
#             with st.spinner('Wait for it...'):
#                     time.sleep(2)
#                     translator = Translator()
#                     mid = translator.translate(input_pa, dest="fr").text
#                     mid2 = translator.translate(mid, dest="de").text
#                     back = translator.translate(mid2, dest="en").text
#                     st.markdown('___')
#                     st.write('Back Translation Model')
#                     st.success(back)
#                     # e_augmenter = EmbeddingAugmenter(transformations_per_example=1, pct_words_to_swap=0.3)
#                     # e_a = e_augmenter.augment(input_pa)
#                     # st.markdown('___')
#                     # st.write('Embedding Augmenter Model')
#                     # st.success(e_a)
#                     # w_augmenter = WordNetAugmenter(transformations_per_example=1, pct_words_to_swap=0.3)
#                     # w_a = w_augmenter.augment(input_pa)
#                     # st.markdown('___')
#                     # st.write('WordNet Augmenter Model')
#                     # st.success(w_a)
#                     st.balloons()

#-----------------------------------------
   
#ANALYZE
########
       
# if nav == 'Analyze text':
#     st.markdown("<h4 style='text-align: center; color:grey;'>Accelerate knowledge with SYNTHIA &#129302;</h4>", unsafe_allow_html=True)
#     st.text('')
#     p_title('Analyze text')
#     st.text('')
    
#     a_example = "Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by humans or animals. Leading AI textbooks define the field as the study of 'intelligent agents': any system that perceives its environment and takes actions that maximize its chance of achieving its goals. Some popular accounts use the term 'artificial intelligence' to describe machines that mimic cognitive functions that humans associate with the human mind, such as learning and problem solving, however this definition is rejected by major AI researchers. AI applications include advanced web search engines, recommendation systems (used by YouTube, Amazon and Netflix), understanding human speech (such as Siri or Alexa), self-driving cars (such as Tesla), and competing at the highest level in strategic game systems (such as chess and Go). As machines become increasingly capable, tasks considered to require intelligence are often removed from the definition of AI, a phenomenon known as the AI effect. For instance, optical character recognition is frequently excluded from things considered to be AI, having become a routine technology."

#     source = st.radio("How would you like to start? Choose an option below",
#                           ("I want to input some text", "I want to upload a file"))
#     st.text('')

#     if source == 'I want to input some text':
#         input_me = st.text_area("Use the example below or input your own text in English (maximum of 10,000 characters)", max_chars=10000, value=a_example, height=330)
#         if st.button('Analyze'):
#             if len(input_me) > 10000:
#                 st.error('Please enter a text in English of maximum 1,000 characters')
#             else:
#                 with st.spinner('Processing...'):
#                     time.sleep(2)
#                     nltk.download('punkt')
#                     rt = readtime.of_text(input_me)
#                     tc = textstat.flesch_reading_ease(input_me)
#                     tokenized_words = word_tokenize(input_me)
#                     lr = len(set(tokenized_words)) / len(tokenized_words)
#                     lr = round(lr,2)
#                     n_s = textstat.sentence_count(input_me)
#                     st.markdown('___')
#                     st.text('Reading Time')
#                     st.write(rt)
#                     st.markdown('___')
#                     st.text('Text Complexity: from 0 or negative (hard to read), to 100 or more (easy to read)')
#                     st.write(tc)
#                     st.markdown('___')
#                     st.text('Lexical Richness (distinct words over total number of words)')
#                     st.write(lr)
#                     st.markdown('___')
#                     st.text('Number of sentences')
#                     st.write(n_s)
#                     st.balloons()

#     if source == 'I want to upload a file':
#         file = st.file_uploader('Upload your file here',type=['txt'])
#         if file is not None:
#             with st.spinner('Processing...'):
#                     time.sleep(2)
#                     stringio = StringIO(file.getvalue().decode("utf-8"))
#                     string_data = stringio.read()
#                     if len(string_data) > 10000:
#                         st.error('Please upload a file of maximum 10,000 characters')
#                     else:
#                         nltk.download('punkt')
#                         rt = readtime.of_text(string_data)
#                         tc = textstat.flesch_reading_ease(string_data)
#                         tokenized_words = word_tokenize(string_data)
#                         lr = len(set(tokenized_words)) / len(tokenized_words)
#                         lr = round(lr,2)
#                         n_s = textstat.sentence_count(string_data)
#                         st.markdown('___')
#                         st.text('Reading Time')
#                         st.write(rt)
#                         st.markdown('___')
#                         st.text('Text Complexity: from 0 or negative (hard to read), to 100 or more (easy to read)')
#                         st.write(tc)
#                         st.markdown('___')
#                         st.text('Lexical Richness (distinct words over total number of words)')
#                         st.write(lr)
#                         st.markdown('___')
#                         st.text('Number of sentences')
#                         st.write(n_s)
#                         st.balloons()

#-----------------------------------------