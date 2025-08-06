import google.generativeai as genai

# Configure the Gemini API with your API key
genai.configure(api_key="AIzaSyAFmeY_jByrBZHI9YjHupgstKCWAlrgW3g")

# Initialize the generative model
model = genai.GenerativeModel("gemini-1.5-flash")

def silly_joke_generator(topic):
  """
  Generates a silly joke about a given topic using the Gemini API.

  Args:
    topic: The topic for the joke.

  Returns:
    A string containing the generated joke.
  """
  prompt = f"Tell me a silly, kid-friendly joke about {topic}."
  response = model.generate_content(prompt)
  return response.text

#to get input from the user
topic = input("Enter a topic for the joke: ")
joke = silly_joke_generator(topic)

# Print the generated joke
print(f"Here's a joke about {topic}:")
print(joke)