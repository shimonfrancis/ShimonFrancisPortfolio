# Data for the Portfolio

# About Me
about_text = """
Dynamic GeoAI Engineer with over 5 years of experience in Spatial Intelligence and Agentic AI. Expert in building autonomous geospatial agents with LangGraph and developing high-scale SAR/Optical automation pipelines. Proven track record in applying Deep Learning (PyTorch, TorchGeo) to satellite imagery for infrastructure planning and environmental monitoring.
"""

# Timeline Data (Education & Experience)
timeline_data = [
    {
        "year": "2025-Present",
        "title": "GIS Developer",
        "company": "Ubique Systems",
        "description": "Working on Spatial Intelligence and Agentic AI."
    },
    {
        "year": "2023-2025",
        "title": "Senior Data Analyst",
        "company": "Hypervine",
        "description": "Worked on Geospatial Analytics, Remote Sensing, and Geospatial Deep Learning."
    },
    {
        "year": "2020-2022",
        "title": "Senior Process Executive",
        "company": "Cognizant",
        "description": "Handled process execution and data management tasks."
    },
    # Add Education if needed, using placeholder for now as it wasn't in original
]

# Skills Data
skills_data = {
    "Geospatial AI & Deep Learning": {"TorchGeo": 90, "Raster Vision": 45, "Pytorch": 50,"Tensorflow":60,"CNNs":50,},
    "Agentic Workflows": {"Langchain": 90, "LangGraph": 85, "DeepAgent": 90, "State Machines": 80},
    "Geospatial Automation": {"GDAL": 85, "Rasterio": 80, "Shapely": 85, "Geopandas": 75, "Fiona": 60, "Pandas": 85},
    "SAR Engineering":{"pyroSAR":85,"Sentinel-1":80},
    "Softwares":{"QGIS":85,"ESA SNAP":70}
}

# Projects Data
projects_data = [
    {
        "name": "Segmenting Mines From Satellite Imagery",
        "description": "Segmenting mines from Sentinel-2 (True color imagery) using TorchGeo and ResNet101. Achieved 77% accuracy and 47% IoU on Kaggle.",
        "url": "https://github.com/shimonfrancis/Mine-Segmentation-TorchGeo/tree/main/Mine_Segmentation_Training",
        "image_path": "Portfolio_2025/Segmenting_Mines.png",
        "tags": ["Python", "Deep Learning", "Geospatial", "TorchGeo"]
    },
    {
        "name": "Mine Detection Pipeline",
        "description": "Built a mine detection pipeline using Sentinel-2 imagery and trained deep learning models. Implemented preprocessing, inference, and post-processing.",
        "url": "https://github.com/shimonfrancis/Mine-Segmentation-TorchGeo/tree/main/Inference",
        "image_path": "Portfolio_2025/Segmentattion_Vector.png",
        "tags": ["Python", "Pipeline", "Geospatial"]
    },
    {
        "name": "Construction Site Detection",
        "description": "Detecting construction sites from High-Resolution satellite imagery using Raster Vision and segment-geospatial. Useful for urban development tracking.",
        "url": "https://github.com/shimonfrancis/Construction-Detection-RasterVision",
        "image_path": "Portfolio_2025/Construction Detection.png",
        "tags": ["Python", "Raster Vision", "Geospatial", "Computer Vision"]
    },
    {
        "name": "Satellite Imagery Download (Terragon)",
        "description": "Automating satellite imagery download using Terragon from multiple providers effectively for land cover mapping and disaster assessment.",
        "url": "https://github.com/shimonfrancis/Download-Satellite-Imagery/blob/main/Download%20Data%20from%20Planetary%20Computer.ipynb",
        "image_path": "Portfolio_2025/Sentinel.png",
        "tags": ["Python", "Terragon", "Automation"]
    },
    {
        "name": "High-Res Imagery Downloader",
        "description": "Automated extraction of satellite imagery for regions defined in KML files using samgeo. Fetches GeoTIFFs from TMS.",
        "url": "https://github.com/shimonfrancis/Download-High-resolution-Satellite-Imagery",
        "image_path": "Portfolio_2025/HighRes.png",
        "tags": ["Python", "KML", "Automation"]
    },
    {
        "name": "Real Estate Data Cleaning (SQL)",
        "description": "Cleaned and transformed real estate datasets using SQL. Standardized dates, handled missing values, and removed duplicates.",
        "url": "https://github.com/shimonfrancis/SQL_Project/blob/Data_Cleaning/SQL_Data_Cleaning.sql",
        "image_path": "Portfolio_2025/cleaning.png",
        "tags": ["SQL", "Data Cleaning"]
    },
    {
        "name": "COVID-19 Data Exploration (SQL)",
        "description": "In-depth analysis of global COVID-19 data. Calculated death rates, infection trends, and vaccination progress using SQL window functions.",
        "url": "https://github.com/shimonfrancis/SQL_Project/blob/Data_Exploration/Data_Exploration_on_SQL.sql",
        "image_path": "Portfolio_2025/explore.png",
        "tags": ["SQL", "Data Analysis"]
    },
    {
        "name": "Startup Funding Visualization (Tableau)",
        "description": "Interactive Tableau dashboard visualizing startup funding distribution by industry and geography.",
        "url": "https://public.tableau.com/app/profile/shimon.francis/viz/Most_Funded_Ideas_Feb/CategoryVsPledged",
        "image_path": "Portfolio_2025/Idea1.png",
        "tags": ["Tableau", "Visualization"]
    },
    {
        "name": "Tesla Accident Analysis (Tableau)",
        "description": "Tableau dashboard analyzing Tesla-related accidents, visualizing trends and hotspots.",
        "url": "https://public.tableau.com/app/profile/shimon.francis/viz/TeslaDeathcasescenario/TeslaDeathsPerCountry",
        "image_path": "Portfolio_2025/Accident.png",
        "tags": ["Tableau", "Visualization"]
    },
    {
        "name": "Amazon Price Tracker",
        "description": "Web scraper using Python and BeautifulSoup to monitor product prices on Amazon and store history.",
        "url": "https://github.com/shimonfrancis/Python/blob/main/webscrapping.py",
        "image_path": "Portfolio_2025/Amazon.png",
        "tags": ["Python", "Web Scraping", "Automation"]
    },
     {
        "name": "Ocean Wave Detection",
        "description": "Python code for detecting wave spectrum and height from video imagery.",
        "url": "https://github.com/shimonfrancis/Python_for_Detecting-directional-wave-spectrum-using-video-imagery",
        "image_path": "Portfolio_2025/download.png",
        "tags": ["Python", "Computer Vision"]
    }
]

social_links = {
    "LinkedIn": "https://www.linkedin.com/in/shimon-francis-2b3167173/",
    "GitHub": "https://github.com/shimonfrancis",
    "Email": "shimon.francis@gmail.com"
}
