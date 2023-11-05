from google.cloud import texttospeech
from google.oauth2 import service_account
import subprocess
import json

# Replace 'path_to_your_service_account.json' with your actual service account file path
credentials = service_account.Credentials.from_service_account_info({
    "type": "service_account",
    "project_id": "braided-turbine-404201",
    "private_key_id": "0fc78282ec095a5ef774eb2178dfebaf231a82b1",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQChrmD4Qm/+SQ3t\n3s8r01dS2jmbJZI/CEt/Yv2bXLaXhiNA8jaEA5xF4WF4sZrXPMm1rea42FayzpUz\nFGfHk8CiWWTSRHjayPd4u1IxO7vP1jMNPhoyb5NCJPkbV5qYB//MrsgE7kcg/ByZ\njMLMKe1+HivODpDGqHwYszaBptmpbqigCwtsztxTRSsTGGwtcCdG6gZO73U3yvcC\ndaDWL0rCx3MJG/rs4vsGjW87KMdISkmQHyyazK8ODbtwyqU8KvMgAto56f9aOpTl\nAi8iWzZanfwfCYHN8CrTIfC+U+pg0+D6ws9iqpGLQI+y1GDGH0SmqmDOTAu7BO4I\nDJJTkXjJAgMBAAECggEAAahoFiOYQmM9YVMHjMt9+buDG7Qm676KB6RcNVueA6+8\nbM4PAQuIbq8A8NvhWpOk/dfqpbqSKQM1RHDRH5rEPuXrwrwxAQ1OfE5vaVHTey4X\nF+urGRlLyUHXzA/55dUvKkogguxujkgHgwuOc8l6RfDJQjOkCGVx4E72IB413Sbh\nJ6q9HuTMA3kD+jUdGCZj2UDGSpT0r07sNaUPOv3TdrocERAibu0qvqtXEQR2/tOM\nlswWOcjd9KiadYMtQE87DcTswFPU6DpafARD4bEhMWK3s8jSK/aoY7K60+qwO6A0\n+/nKqCg5lfJfZaVDDUgTuTr45Cqu8uCmtdY9lQ5agQKBgQDL0RMZn0BC7Kb4MU5r\nAi2QcLGnrh52nsIbrTqTkMt7TZ9uPLWVOm8v5UmJ8QXu+1Emco/Og8rAutMHSs4K\nWsk80XAxb6Y94pZVDjS8MRD4zHAVRD1KwJAy77cBWuF2veE2cc22pmGfvO5QBq8W\nSHvFi5aLK+ARtGBQ/W/BtnAtgwKBgQDLE5SYzNOWQCF0s6i/Ke7HvBP4xzLMNiLx\n+VGTWMwElI6S0/FBe79Y6BcLP6XjPMQGywRPqaONvnHloMrKUG+rQmP8H2A834rV\nyxahb2GFvXOVI73Ba4j6Cdk1/9JlCmY+RmBIwUhH1fTIzvE3PHJaCUniJye+ALM/\nJCez7eqawwKBgQClCrdJvzAdQV7viZWzhz74QJlLa+6VJXePS9YsGkr7nN6mOJjd\nr0TL5wKGpdqlK3MKDCixFP2A1Yf+1q9DqUJdckdEcOGQKUSMuYUwgxb4MSvtvKVZ\nO9dIt95cRYhfS+Dr4nmvFsnkvOvJd7Ad/jHjxGXyamP2UjbQPnlZxm7OGwKBgDzJ\nSqSGQxtpbNpC4NL/2UKeMJg6ACGSXtlxWJKzdLY2RYr7t+5y/S6+og8y6RPg34ht\nAohZ7eQCypMCk1EFzLdFsyoHtkXiX+to1AhUj6t5rvxIa4dXCfRWOFdqkO6/syUW\n6cE9YcZm69Oj5h4zkMMUnrH8KHA+Q2k2CFBaeewDAoGBALFPyr8wLrCgZX53i7+2\n8ddfLKMgmcJMuwhOjRXrdWlwrkEhToJAMNAGHlQR5ORkaWSKfbJkQ+tYfnZpQF3S\nHRND2IS5TzQl2sf36enEUeUSmrF4Yb2tf6wsNYXkZXHCl18KBS2s19npmO0FxsmP\ncrwInfJqrBmrc8XcRpZg2szT\n-----END PRIVATE KEY-----\n",
    "client_email": "gtts-468@braided-turbine-404201.iam.gserviceaccount.com",
    "client_id": "106110204310114411351",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/gtts-468%40braided-turbine-404201.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})

def tts_speak(text):
    # Creates a client
    client = texttospeech.TextToSpeechClient(credentials=credentials)

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code and the ssml gender (female)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        name="en-US-Wavenet-F"  # Specifies a female Wavenet voice
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

    subprocess.call(["afplay", "output.mp3"])