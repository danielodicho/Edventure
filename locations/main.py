from gpt import *
from time import sleep
from Edventure.voice.tts import tts_speak

def output_story(city):
    # Get cool things to do in the city from OpenAI's GPT
    context = '''Background and Purpose:
    The Toyota EduVenture App is an innovative platform designed to transform car rides into educational and engaging experiences for families, especially children. The app leverages Toyota's commitment to innovation, education, and environmental awareness by integrating with a vehicle's existing systems to provide dynamic learning opportunities. It uses computer vision, GPS data, and AI to identify surroundings and deliver relevant content.
    
    Target Users:
    The primary users of the app are families with children of varying ages who have a keen interest in learning about the world around them during road trips. The app caters to different learning levels and preferences, ensuring inclusivity.
    
    Content Style:
    The educational content delivered by the app is diverse, ranging from historical facts to scientific information about flora and fauna. The storytelling is designed to be interactive, age-appropriate, and adaptive, with a narrative that weaves in the users' surroundings and inputs.
    
    Interaction Style:
    The app's interaction is voice-based to ensure safety and prevent driver distraction. Users can interact through Q&A sessions, choose-your-own-adventure stories, and quizzes.
    
    Educational Integration:
    Information is presented through engaging stories that relate to the passengers' current location and observed landmarks. The content is generative, ensuring that it is fresh and tailored to the journey. Quizzes and interactive elements are used to reinforce learning.
    
    Customization:
    Parents have control over the content, allowing them to set difficulty levels and monitor interactions. They can also input trip details in advance for a customized learning journey.
    
    Technology Integration:
    The app integrates seamlessly with Toyota vehicle systems, including cameras for CV, GPS for location-based content, the audio system for delivery of educational material, and displays for interactive storytelling.
    
    User Engagement and Gamification:
    The app includes gamified elements to maintain engagement, such as virtual rewards and the ability to track learning progress. Storytelling is dynamic, with stories having branching paths and variable endings based on user interaction.'''

    history_mode_context = context + '''
    Mode: History
    The "history" mode in the Toyota EduVenture App is specifically designed to educate users on the historical significance of the places they are driving through. This mode uses GPS data to identify historical landmarks, sites, or regions and generates content that provides a deep dive into the past, uncovering stories, events, and figures that shaped the location. The narrative is rich and engaging, intended to captivate the family's attention and stimulate curiosity about history.
        '''
    history_prompt = f"The family is currently driving through {city}. Generate a comprehensive and engaging historical narrative about this city, highlighting key events, significant landmarks, and notable historical figures. The narrative should be suitable for a family audience and last for a minimum of five minutes."


    places = get_response(history_mode_context, history_prompt)
    return places
    # places = get_places()
    # print(places)

city = True
prev_city = None
while True:
    location = get_location()
    lat, lng = location['lat'], location['lng']
    city = get_city(lat, lng)
    if city != prev_city:
        print("getting story")
        story = output_story(city)
        print(len(story), "got it")
        tts_speak(story)

    sleep(30000)
    prev_city = city
# print("hello")
# tts_speak("hello")