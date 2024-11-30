import streamlit as st

# Editable Title
st.title("My Biography")

# Editable Name
name = st.text_input("Enter your name:", value="Tj")

# Editable About Section
st.subheader("About Me")
about = st.text_area(
    "Write a short introduction about yourself:", 
    value=f"Hi, my name is {name}! 18, I live at Santiago Loreto, Dinagat Islands, I was born at January 27, 2006. I'm currently a college student passionate about programming, problem-solving, and making a positive impact on my community. I enjoy working on creative projects like coding and writing policy papers while balancing my studies."
)

st.write(about)

# Editable Profile Picture
st.subheader("Profile Picture")
image_url = st.text_input(
    "Enter the URL of your profile picture:", 
    value="./assests/shesh.jpg"
)
st.image(image_url, caption=f"This is {name}!", use_column_width=True)

# Editable Hobbies and Interests
st.subheader("Hobbies and Interests")
hobbies = st.text_area(
    "List your hobbies and interests (one per line):", 
    value="- 📚 Reading\n- ✍️ Writing letters\n- 🐾 Taking care of dogs\n- programming"
)

st.write("Your hobbies and interests:")
st.write(hobbies)

# Editable Achievements
st.subheader("Achievements")
achievements = st.text_area(
    "List your achievements (one per line):", 
    value=f"- 🏅 Elected as Vice-President in the school SSLG in S.Y. 2023-2024\n- 🖋️ Attended journalism\n- 🧠 Graduated as an Honor student in SHS"
)

st.write("Your achievements:")
st.write(achievements)

# Editable Contact Information
st.subheader("Get in Touch")
contact_info = st.text_area(
    "Enter your contact details (e.g., email, social media links):", 
    value="- 📧 Email: bagaotj@gmail.com\n- 📱 Instagram: tj@gmail.com\n- 🐦 Twitter: tj2.com"
)

st.write("Your contact information: 09091995958")
st.write(contact_info)

# Final Message
st.subheader("Thank You Message")
final_message = st.text_area(
    "Write your closing message:", 
    value="Thank you for visiting!"
)
st.write(final_message)

