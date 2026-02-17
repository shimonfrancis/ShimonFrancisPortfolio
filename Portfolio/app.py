import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
import base64
from PIL import Image

# Import local modules
# Try-except block to handle running from different directories
try:
    import data
except ImportError:
    from Portfolio import data

# --- Page Config ---
st.set_page_config(page_title="Shimon Francis | Portfolio", page_icon="🌟", layout="wide")

# --- Helper Functions ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load CSS
try:
    local_css("Portfolio/styles/main.css")
except FileNotFoundError:
    local_css("styles/main.css") # Fallback if running from inside Portfolio

# --- Assets ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_passport = Image.open("Portfolio/Shimon_Passport_Size_latest.png")

# --- Sidebar ---
with st.sidebar:
    selected = option_menu(
        menu_title="Portfolio",
        options=["Home", "About", "Skills", "Projects", "Contact"],
        icons=["house", "person", "code-slash", "briefcase", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#040404"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )
    
    st.markdown("---")
    st.write("### Connect with me")
    st.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)]({data.social_links['LinkedIn']})")
    st.markdown(f"[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)]({data.social_links['GitHub']})")
    st.markdown(f"[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)]({data.social_links['Email']})")


# --- Home Section ---
if selected == "Home":
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True) # Spacer
        st.title("Hi, I'm Shimon Francis! 👋")
        st.subheader("Spatial Intelligence | Geospatial AI")
        st.write("Im a Geospatial AI professional focused on spatial intelligence, remote sensing, and AI-driven geospatial analytics.Experienced in building deep learning–powered spatial workflows, intelligent geoprocessing pipelines, and decision-support systems using modern geospatial and AI frameworks. Passionate about applying GeoAI to solve real-world challenges.")
        st.markdown("[Check out my projects!](#projects)")
    with col2:
        st_lottie(lottie_coding, height=400, key="coding")

# --- About Section ---
if selected == "About":
    st.title("About Me")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(img_passport, width=250, caption="Shimon Francis")
        with open("Portfolio/Shimon-Francis.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        st.download_button(
            label="📄 Download Resume",
            data=pdf_bytes,
            file_name="Shimon Francis-Resume.pdf",
            mime="application/pdf",
        )
    with col2:
        st.markdown(data.about_text)
        
        st.write("## My Journey")
        for item in data.timeline_data:
            st.markdown(f"""
            <div class="timeline-item">
                <div class="timeline-content">
                    <span class="timeline-date">{item['year']}</span>
                    <h4>{item['title']} @ {item['company']}</h4>
                    <p>{item['description']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- Skills Section ---
if selected == "Skills":
    st.title("Technical Skills")
    st.write("Here are some of the technologies I work with:")
    
    cols = st.columns(3)
    idx = 0
    for category, skills in data.skills_data.items():
        with cols[idx]:
            st.markdown(f"<div class='skill-container'>", unsafe_allow_html=True)
            st.subheader(category)
            for skill, proficiency in skills.items():
                st.write(f"**{skill}**")
                st.markdown(f"""
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {proficiency}%;"></div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        idx = (idx + 1) % 3

# --- Projects Section ---
if selected == "Projects":
    st.title("My Projects")
    
    # Filter
    all_tags = sorted(list(set([tag for project in data.projects_data for tag in project.get("tags", [])])))
    selected_tags = st.multiselect("Filter by Technology", all_tags)
    
    filtered_projects = []
    if not selected_tags:
        filtered_projects = data.projects_data
    else:
        for project in data.projects_data:
            if any(tag in selected_tags for tag in project.get("tags", [])):
                filtered_projects.append(project)
    
    # Display Projects
    for i in range(0, len(filtered_projects), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(filtered_projects):
                project = filtered_projects[i + j]
                with cols[j]:
                    # Image Handling
                    try:
                         # Helper to load image as base64 for HTML embedding if needed, 
                         # but st.image is easier. Transitioning to st.image for cleaner code if possible,
                         # but keeping the custom HTML card structure for better design as per plan.
                         # Need base64 for HTML.
                         with open(project["image_path"], "rb") as img_file:
                             b64_img = base64.b64encode(img_file.read()).decode()
                    except Exception:
                        b64_img = "" # Placeholder or error handling
                    
                    # Tags HTML
                    tags_html = "".join([f"<span style='background-color: #eee; padding: 2px 8px; border-radius: 4px; font-size: 0.8em; margin-right: 5px;'>{tag}</span>" for tag in project.get("tags", [])])

                    st.markdown(f"""
                    <div class="project-card">
                        <img src="data:image/png;base64,{b64_img}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px;">
                        <div class="project-title" style="margin-top: 10px;">{project['name']}</div>
                        <div style="margin-bottom: 10px;">{tags_html}</div>
                        <div class="project-desc">{project['description']}</div>
                        <a href="{project['url']}" target="_blank" style="text-decoration: none; color: #4CAF50; font-weight: bold;">View Project -></a>
                    </div>
                    """, unsafe_allow_html=True)

# --- Contact Section ---
if selected == "Contact":
    st.title("Get In Touch")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Feel free to reach out to me for collaborations or just a friendly hello!")
        st.write(f"📧 **Email:** {data.social_links['Email']}")
        st.write(f"🔗 **LinkedIn:** [Profile]({data.social_links['LinkedIn']})")
        st.write(f"🐙 **GitHub:** [Profile]({data.social_links['GitHub']})")
        
        st_lottie(load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_u25cckyh.json"), height=300)

    with col2:
        st.header("Contact Form")
        contact_form = """
        <form action="https://formsubmit.co/shimon.francis@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;">
            <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;">
            <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px; height: 150px;"></textarea>
            <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
