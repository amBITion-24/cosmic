import streamlit as st
from citymate import CityMateRecommender, load_model, save_model
from utils import load_citymate_data

st.set_page_config(page_title="CityMate", page_icon="🏙", layout="wide")

st.title("AI Powered - CityMate Recommendaion")

# Load CityMate data
citymate_df = load_citymate_data('data/citymate_data.csv')

# Create and train the model
citymate_recommender = CityMateRecommender()
citymate_recommender.preprocess_data(citymate_df)
citymate_recommender.train_model()

# User Input
user_languages = st.multiselect(
    "Languages you speak",
    sorted(set(citymate_df['languages_spoken'].str.split(',').sum())),
    default=['English'])
user_age_group = st.selectbox("Your Age Group",
                              citymate_df['age_group'].unique())

# Generate recommendations
# if st.button("Find Your CityMate"):
#     recommendations = citymate_recommender.get_recommendations(
#         user_languages, user_age_group)

#     # Display Recommendations
#     st.subheader("Recommended CityMates:")
#     for index, row in recommendations.iterrows():
#         if row['gender'] == 'Male':
#             st.image('LOGO.jpg')
#         else:
#             st.image('LOGO2.jpg')
#         st.write(f"*Name:* {row['name']}")
#         #st.write(f"**Name: **{row['name']}")
#         st.write(f"*Age:* {row['age_group']}")
#         st.write(f"*Gender:* {row['gender']}")
#         st.write(f"*Languages:* {row['languages_spoken']}")
#         st.write(f"*About:* {row['about']}")
#         st.write(f"*Phone NO.* {row['phone_number']}")
#         st.write(f"*Email ID:* {row['email']}")
#         st.write(f"*Similarity Score:* {row['similarity_score']:.2f}")
#         st.write("---")

recommendations = citymate_recommender.get_recommendations(
    user_languages, user_age_group)

st.markdown("""
    <style>
    .card-container {
    display: flex;
    flex-wrap: wrap;
    width: 80vw;
    margin: auto;
    justify-content: space-between;
    gap: 20px; /* Adjust spacing between cards */
}

.card {
    background: #f5f5f5;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 20px;
    color: black;
    width: calc(50% - 10px); /* Calculate 50% width minus gap */
    box-sizing: border-box; /* Ensure padding is included in width */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 30px;
}

.card-content {
    margin-left: 60px; /* Ensures content is beside the image */
}

.card-content h3 {
    margin: 0;
    color: black;
    font-size: 1.5rem;
}

.card-content p {
    font-size: 16px;
    margin: 5px 0;
    line-height: 1.3rem;
}

img {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    object-fit: cover;
    margin-right: 20px;
}

/* Responsive styling for mobile devices */
@media (max-width: 768px) {
    .card {
        width: calc(100% - 10px); /* Full width on mobile minus gap */
    }

    .card-content {
        margin-left: 0; /* Align content with the card on mobile */
        margin-top: 10px; /* Add some space between image and text */
    }

    img {
        width: 60px; /* Slightly smaller image on mobile */
        height: 60px;
        margin-right: 10px;
    }

    .card-content h3 {
        font-size: 1.2rem; /* Slightly smaller heading on mobile */
    }

    .card-content p {
        font-size: 14px; /* Slightly smaller text on mobile */
        line-height: 1.2rem;
    }
}

    
    </style>
    """,
            unsafe_allow_html=True)

# Display recommendations as styled cards
st.markdown('<div class="card-container">', unsafe_allow_html=True)
for index, row in recommendations.iterrows():
    st.markdown(f"""
        <div class="card">
            {'<img src="https://img.freepik.com/premium-vector/businessman-avatar-illustration-cartoon-user-portrait-user-profile-icon_118339-5507.jpg" alt="Male" class="team-image">' if row['gender'] == 'Male' else '<img src="https://www.shutterstock.com/image-vector/young-smiling-woman-mia-avatar-600nw-2127358541.jpg" alt="Female" class="team-image">'}
            <div class="card-content">
                <h3>{row['name']}</h3>
                <p><strong>Age:</strong> {row['age_group']}</p>
                <p><strong>Gender:</strong> {row['gender']}</p>
                <p><strong>Languages:</strong> {row['languages_spoken']}</p>
                <p><strong>About:</strong> {row['about']}</p>
                <p><strong>Phone:</strong> {row['phone_number']}</p>
                <p><strong>Email:</strong> {row['email']}</p>
                <p><strong>Similarity Score:</strong> {row['similarity_score']:.2f}</p>
                <button style="background-color: lightgreen; color: white; padding: 10px 20px; border: none; cursor: pointer; border-radius: 5px; transition: background-color 0.3s ease; margin-top:20px;">
                    <a href="/payment-gateway.html" style="text-decoration: none; color: black; font-weight:bold">Book Guide</a>
                </button>
            </div>
        </div>
        """,
                unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)