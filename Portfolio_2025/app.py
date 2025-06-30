import streamlit as st
from base64 import b64encode
import base64
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

def portfolio():
    st.set_page_config(page_title='Shimon Francis-Portfolio',page_icon='🌟')
    st.write(f"""
             <div class='title' style="text-align: center;">
             <span style='font-size:50px;'>Hi! My name is Shimon Francis</span>👋
             </div>
             """,unsafe_allow_html=True)
    st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)
    with open("Portfolio_2025/Shimon_Passport_Size_latest.png","rb") as img_file:
        img="data:image/png;base64," + b64encode(img_file.read()).decode()
    
    with open("Portfolio_2025/Shimon-Francis.pdf","rb") as pdf_file:
        linkedin_pdf=pdf_file.read()
    st.write(f"""
             <div style="display: flex; justify-content:center;">
             <div class="box">
             <img src="{img}" alt="Shimon Francis" style="width: 150px; height: 180px;">
             </div>
             </div>
             """,
             unsafe_allow_html=True)
    st.write(f"""
             <div class= "subtitle" style="text-align: center;">Senior Data Analyst</div>""",
             unsafe_allow_html=True)
    social_icons_data={
        "Linkedin":["https://www.linkedin.com/in/shimon-francis-2b3167173/","https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
        "GitHub":["https://github.com/shimonfrancis","https://cdn-icons-png.flaticon.com/128/733/733609.png"]
    }
    social_icons_html = [
    f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'>"
    f"<img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'"
    f" style='width: 30px; height: 30px;'></a>"
    for platform in social_icons_data
]
    st.write(f"""
    <div style="display: flex; justify-content: center;margin-bottom:20px;">
    {''.join(social_icons_html)}
    </div>""",
    unsafe_allow_html=True)

    st.write("##")
    st.subheader("About Me")
    st.markdown("""
                - 💻🌎 I am a Senior Data Analyst  at [Hypervine](https://www.hypervine.io/),
                where I am currently working on Geospatial Analytics,RemoteSensing,Geospatial Deep Learning etc.
                - 🚀 Previously, I served as Senior Process Executive [Cognizant](https://www.cognizant.com/us/en).
                - ❤️ I am Passionate about GeoAI(Geospatial AI),Geospatial Intelligence,Computer Vision,RemoteSensing,GIS,Automation,Generative AI,Data Analytics, and more.
                - 📧 You can reach me at shimon.francis@gmail.com.
                - 🏡 Based in India
                """)
    st.download_button(label='Download my Resume',data=linkedin_pdf,file_name='Shimon Francis-Resume.pdf',mime='application/pdf')
    st.write('##')
    st.markdown(
                "<h2 style='text-align: center; font-size: 36px;'>Projects</h2>",
                unsafe_allow_html=True
            )

    projects = [
        {
            "name": "Segmenting Mines From Satellite Imagery",
            "description": "Segmenting mines from sentinel-2 (True colour imagery)  using <a href='https://pytorch.org/blog/geospatial-deep-learning-with-torchgeo/' target='_blank'>TorchGeo</a> and resnet101 using geojson polygons as masks. I have collected datasets from North America,South America,Europe. Training the data returned me with an accuracy of 77% and IoU of 47% using Kaggle for 50 epochs.",
            "url": "https://github.com/shimonfrancis/Mine-Segmentation-TorchGeo/tree/main/Mine_Segmentation_Training",
            "image_path": "Portfolio_2025/Segmenting_Mines.png"
            
        },
        {
            "name": "Detecting Mines using the Trained Segmentation Model",
            "description": "Built a mine detection pipeline using Sentinel-2 satellite imagery and the trained deep learning model with <a href='https://pytorch.org/blog/geospatial-deep-learning-with-torchgeo/' target='_blank'>TorchGeo</a>. Implemented preprocessing, model inference, and post-processing in Python to identify mine locations with geospatial accuracy.",
            "url": "https://github.com/shimonfrancis/Mine-Segmentation-TorchGeo/tree/main/Inference",
            "image_path": "Portfolio_2025/Segmentattion_Vector.png"
        },
        {
            "name": "Construction Site Detection from High Resolution Satellite Imagery",
            "description": "Detecting Construction sites from High-Resolution satellite imagery using <a href='https://rastervision.io/' target='_blank'>Raster Vision</a>.The samples are taken around Scotland using <a href='https://samgeo.gishub.org/' target='_blank'>segment-geospatial</a>.The objective of this project is to detect locations where construction activity is taking place. Such insights can support applications like business expansion planning, government infrastructure monitoring, urban development tracking, and policy decision-making.The below project is an example workflow to train the model and predict construction sites from High-Resolution satellite images using Python",
            "url": "https://github.com/shimonfrancis/Construction-Detection-RasterVision",
            "image_path": "Portfolio_2025/Construction Detection.png"
        },
         {
            "name": "Downloading Satellite Imagery using Terragon",
            "description": "This section demonstrates how to download satellite imagery using <a href='https://terragon.readthedocs.io/en/stable/index.html' target='_blank'>Terragon</a>, an open-source Python library designed for easy access to high-resolution satellite data. Terragon simplifies querying, filtering, and downloading imagery from multiple providers, including Sentinel, Landsat, and other sources from google Earth Engine,Copernicus Data Space Ecosystem and Planetary Computer.With Terragon, you can define an Area of Interest (AOI), select date ranges, set cloud cover thresholds, and automatically fetch imagery directly into your local or cloud workspace. This is particularly useful for applications like land cover mapping, construction monitoring, environmental studies, and disaster assessment.",
            "url": "https://github.com/shimonfrancis/Download-Satellite-Imagery/blob/main/Download%20Data%20from%20Planetary%20Computer.ipynb",
            "image_path": "Portfolio_2025/Sentinel.png"
        },
        {
            "name": "Downloading High-Resolution Satellite Imagery",
            "description": "This Python script automates the process of extracting satellite imagery for specific geographic regions defined in KML files. It reads each .kml file from a given folder, parses it to extract the bounding box coordinates of the defined area, and then uses the samgeo library's tms_to_geotiff function to download high-resolution satellite imagery (GeoTIFF format) based on those coordinates. The imagery is fetched from a tile map service (TMS) at a specified zoom level (e.g., 18) and saved into a designated output directory. This workflow is particularly useful for geospatial analysts or researchers who need satellite data for multiple areas defined in KML format, enabling efficient and automated data collection.",
            "url": "https://github.com/shimonfrancis/Download-High-resolution-Satellite-Imagery",
            "image_path": "Portfolio_2025/HighRes.png"
        },
        {
            "name": "Data Cleaning Using SQL",
            "description": "Cleaned and transformed a real estate dataset using SQL by converting and standardizing sale dates, filling missing addresses via self-joins, and splitting property and owner addresses into structured components. Standardized categorical values, identified duplicates using window functions, and removed redundant fields to optimize the dataset for analysis.",
            "url": "https://github.com/shimonfrancis/SQL_Project/blob/Data_Cleaning/SQL_Data_Cleaning.sql",
            "image_path": "Portfolio_2025/cleaning.png"
        },
        {
            "name": "Data Exploration using SQL",
            "description": "Conducted in-depth analysis of global COVID-19 data using SQL. Calculated death rates, identified countries with the highest case and death ratios, and performed continent-level aggregations. Joined vaccination and death datasets to track vaccination progress and infection trends. Created views and temporary tables to monitor daily new cases and vaccinations, using window functions for cumulative calculations.",
            "url": "https://github.com/shimonfrancis/SQL_Project/blob/Data_Exploration/Data_Exploration_on_SQL.sql",
            "image_path": "Portfolio_2025/explore.png"
        },
        {
            "name": "Data visualization of most funded idea dataset using Tableau",
            "description": "Developed interactive Tableau dashboards to visualize the Most Funded Idea dataset. Analyzed funding distribution by industry, geography, and startup stage. Created bar charts, heatmaps, and trend lines to highlight top-funded sectors, investor patterns, and funding over time.",
            "url": "https://public.tableau.com/app/profile/shimon.francis/viz/Most_Funded_Ideas_Feb/CategoryVsPledged",
            "image_path": "Portfolio_2025/Idea1.png"
        },
        {
            "name": "Analysis of Tesla death cases using Tableau",
            "description": "Built an interactive Tableau dashboard to analyze Tesla-related death cases. Visualized trends over time, identified accident hotspots, and categorized incidents by autopilot involvement, location, and vehicle model. Enabled stakeholders to explore patterns and assess safety concerns through clear, data-driven storytelling.",
            "url": "https://public.tableau.com/app/profile/shimon.francis/viz/TeslaDeathcasescenario/TeslaDeathsPerCountry",
            "image_path": "Portfolio_2025/Accident.png"
        },
        {
            "name": "WebScraping Using Python",
            "description": "Developed a web scraper using Python, BeautifulSoup, and requests to monitor the price of an ASUS Zenbook on Amazon. The script extracts product title and price data, cleans it, and stores it in a CSV file with the current date. A check_price() function automates periodic checks, enabling future integration with alert systems like email or SMS. This project showcases skills in web scraping, data parsing, and automation.",
            "url": "https://github.com/shimonfrancis/Python/blob/main/webscrapping.py",
            "image_path": "Portfolio_2025/Amazon.png"
        },
        {
            "name": "Ocean Wave Detection using python",
            "description": "Python code for image slicing,rectification of images and detection of wave spectrum and height of ocean waves from video imagery.",
            "url": "https://github.com/shimonfrancis/Python_for_Detecting-directional-wave-spectrum-using-video-imagery",
            "image_path": "Portfolio_2025/download.png"
        },

    ]
    for i in range(0, len(projects), 2):
        cols = st.columns(2)

        for j in range(2):
            if i + j < len(projects):
                project = projects[i + j]
                img_base64 = get_image_base64(project["image_path"]) if "image_path" in project else ""

                with cols[j]:
                    st.markdown(f"""
                        <div style="
                            background-color: #f9f9f9;
                            padding: 20px;
                            border-radius: 12px;
                            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                            margin-bottom: 30px;
                            text-align: center;
                            min-height: 720px;
                            display: flex;
                            flex-direction: column;
                            justify-content: space-between;
                        ">
                            <div>
                                <h4 style="margin-bottom: 10px;">{project['name']}</h4>
                                <p style="text-align: justify; font-size: 14px;">{project['description']}</p>
                            </div>
                            <div>
                                <img src="{img_base64}" alt="{project['name']}" 
                                    style="width: 260px; height: 160px; object-fit: cover;
                                    border-radius: 10px; margin: 20px 0;" />
                                <a href="{project['url']}" target="_blank" style="
                                    background-color: #4CAF50;
                                    color: white;
                                    padding: 10px 20px;
                                    text-decoration: none;
                                    font-size: 14px;
                                    border-radius: 6px;">
                                    View Project
                                </a>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)







    



    
    
    
    
if __name__ == "__main__":
    portfolio()
