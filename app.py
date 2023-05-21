import streamlit as st
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
from PIL import Image
from streamlit_elements import elements, mui, html, sync
from streamlit_option_menu import option_menu
import os
import time
# from st_functions import st_button, load_css


# Page config
st.set_page_config(
    page_title="My Webpage",
    page_icon=":tada:",
    layout="wide"
    )

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")        

# lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json")
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_o6spyjnc.json")



# ------------Header Section -------------
with st.container():
    st.subheader("Hi, I am JAGHAN T :wave:")
    st.header("I Have Completed My M.Sc In Data Science From Coimbatore.")
    st.markdown("Ramakrishna Mission Vivekananda Educational and Research Institute (2021-2023)")

with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("What I do")
        st.write("##")
        st.markdown(
            """
            - I have completed one internship training in AES Technologies.
            - Search data science-related jobs.
            - Learn new things and improve my skills.
            """
        )
        
with right_col:
       st_lottie(lottie_coding, height=300, key="coding")  
       
st.markdown("----")  

# ------------ Internship Training -------
with st.container():
    left_col1, right_col1 = st.columns((2,1))
    with left_col1:
        st.write("##")
        st.header("INTERNSHIP TRAINING.")
        st.markdown("""
                    AES Technology / August 2022 - April 2023
                    - Internship in AES Technologies, Coimbatore as Junior Software Engineer.
            - Working M&C Martin Project (Business Intelligence in Power BI Dashboards)
            - Dashboard like - Sports Revenue Analysis - Lottery Revenue Analysis - Hotel Revenue Analysis.
            - Use good user interface - DAX functions - some basic calculations - KPI cards - filters - 
              different visualization - Book mark using visualization - Tool tips.
            - Dashboard publish to Power BI cloud - Dashboard and MySQL database connections using 
              On-premises data gateway - Scheduled based refresh of the dashboard. 
            - Time series forecasting analysis.
            - Python automate - Run the python file watcher - When the file put into the folder - 
              File watcher Push the data into MySQL database.
            - If any error on this file Push the error folder & check the log file using fix the error's - If no error, 
              the file push to the success folder & push to the MySQL database - All of this run on a local server.
            - In production, fix some error - Version problem in python - Python environment issue - Gateway connection - 
              MySQL to Power BI connection error.
                    """)
    
    with right_col1:
        st.write('##')
        st.write('##')
        image = Image.open('image/Internship Certificate.png')
        st.image(image, channels = "RGB", width = 450, use_column_width = False)
st.markdown("----")  
# ------------ My Projects ---------------
with st.container():
    st.header("My Projects")
    # st.write("##")
    
    selected = option_menu(
        menu_title    = None,
        options       = ["Intern Project", "Power BI Project", "Sem Project"],
        icons         = ["diagram-3-fill", "bar-chart-fill", "book-half"],
        menu_icon     = "cast",
        default_index = 0,
        orientation   = "horizontal"
    )
    if selected == "Intern Project":
        st.subheader(f"{selected}")
    
        image_col2, text_col2 = st.columns(2)
    
    # -------------- Sports Revenue Analysis --------------------
    
        with image_col2:
                    IMAGES = [
                "https://user-images.githubusercontent.com/108980892/225910844-589b5dd9-d95d-478e-babd-6c6a41017ec0.png",
                "https://user-images.githubusercontent.com/108980892/225910973-ca77ae75-42f8-48d5-889c-8d6149a16599.png",
                "https://user-images.githubusercontent.com/108980892/226608321-9475c077-60e2-4e59-8f04-3538affd2805.png"
            ]


                    def slideshow_swipeable(images):
            # Generate a session state key based on images.
                        key = f"slideshow_swipeable_{str(images).encode().hex()}"

            # Initialize the default slideshow index.
                        if key not in st.session_state:
                            st.session_state[key] = 0

                # Get the current slideshow index.
                        index = st.session_state[key]

                # Create a new elements frame.
                        with elements(f"frame_{key}"):

                    # Use mui.Stack to vertically display the slideshow and the pagination centered.
                    # https://mui.com/material-ui/react-stack/#usage
                            with mui.Stack(spacing=2, alignItems="center"):

                        # Create a swipeable view that updates st.session_state[key] thanks to sync().
                        # It also sets the index so that changing the pagination (see below) will also
                        # update the swipeable view.
                        # https://mui.com/material-ui/react-tabs/#full-width
                        # https://react-swipeable-views.com/demos/demos/
                                with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key)):
                                    for image in images:
                                        html.img(src=image, css={"width": "100%"})

                        # Create a handler for mui.Pagination.
                        # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                def handle_change(event, value):
                            # Pagination starts at 1, but our index starts at 0, explaining the '-1'.
                                    st.session_state[key] = value-1

                        # Display the pagination.
                        # As the index value can also be updated by the swipeable view, we explicitely
                        # set the page value to index+1 (page value starts at 1).
                        # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)


            # if __name__ == '__main__':
                    slideshow_swipeable(IMAGES)
        with text_col2:
            st.subheader("Sports revenue Analysis")
            st.write(
                """
                - Use good user interface – DAX functions – some basic calculations – KPI cards – Filters -Different 
                    visualization – Book mark using visualization – Tool tips
                - Dashboards publish to Power BI cloud – Dashboard and MySQL database connections using
                    On-premises data gateway – Scheduled based refresh of the dashboard.
                - Time series forecasting analysis and Anomaly detection.    
                """
            )   
            
        st.markdown("----")  
        with st.container():
            text_col3, image_col3 = st.columns(2)
        
        # -------------- Hotel Revenue Analysis --------------------
            with text_col3:
                st.subheader("Hotel Revenue Analysis")
                st.write(
                    """
                    - Use good user interface – DAX functions – some basic calculations – KPI cards – Filters -Different 
                        visualization – Book mark using visualization – Tool tips
                    - Dashboards publish to Power BI cloud – Dashboard and MySQL database connections using
                        On-premises data gateway – Scheduled based refresh of the dashboard.
                    - Time series forecasting analysis and Anomaly detection. 
                    
                    """
                )    
                
            with image_col3:
                        IMAGES = [
                    "https://user-images.githubusercontent.com/108980892/225911314-713904b1-1173-4097-b5c2-fb8264a6bb91.png",
                    "https://user-images.githubusercontent.com/108980892/225911403-95a0c4b7-26a9-4df8-a91b-4bce3e20263f.png",
                    "https://user-images.githubusercontent.com/108980892/225911488-949724d5-a94b-4641-9d66-f20727c7df35.png",
                    "https://user-images.githubusercontent.com/108980892/225911598-4b9e33b6-4cfb-4111-9252-fb4307a88e58.png"
                ]


                        def slideshow_swipeable(images):
                    # Generate a session state key based on images.
                            key = f"slideshow_swipeable_{str(images).encode().hex()}"

                    # Initialize the default slideshow index.
                            if key not in st.session_state:
                                st.session_state[key] = 0

                    # Get the current slideshow index.
                            index = st.session_state[key]

                    # Create a new elements frame.
                            with elements(f"frame_{key}"):

                        # Use mui.Stack to vertically display the slideshow and the pagination centered.
                        # https://mui.com/material-ui/react-stack/#usage
                                with mui.Stack(spacing=2, alignItems="center"):

                            # Create a swipeable view that updates st.session_state[key] thanks to sync().
                            # It also sets the index so that changing the pagination (see below) will also
                            # update the swipeable view.
                            # https://mui.com/material-ui/react-tabs/#full-width
                            # https://react-swipeable-views.com/demos/demos/
                                    with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key)):
                                        for image in images:
                                            html.img(src=image, css={"width": "100%"})

                            # Create a handler for mui.Pagination.
                            # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                    def handle_change(event, value):
                                # Pagination starts at 1, but our index starts at 0, explaining the '-1'.
                                        st.session_state[key] = value-1

                            # Display the pagination.
                            # As the index value can also be updated by the swipeable view, we explicitely
                            # set the page value to index+1 (page value starts at 1).
                            # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                    mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)


                # if __name__ == '__main__':
                        slideshow_swipeable(IMAGES)

            
        st.markdown("----")  
        with st.container():
            image_col4, text_col4 = st.columns(2)
            
            # -------------- Lottery Revenue Analysis --------------------
            
            with image_col4:
                        IMAGES = [
                    "https://user-images.githubusercontent.com/108980892/230578101-e8aac3ad-77d1-40fc-9f05-d39bf0371adc.png",
                    "https://user-images.githubusercontent.com/108980892/230577946-22f09151-cc1a-47e7-9452-8e54a5052148.png"
                ]


                        def slideshow_swipeable(images):
                    # Generate a session state key based on images.
                            key = f"slideshow_swipeable_{str(images).encode().hex()}"

                    # Initialize the default slideshow index.
                            if key not in st.session_state:
                                st.session_state[key] = 0

                    # Get the current slideshow index.
                            index = st.session_state[key]

                    # Create a new elements frame.
                            with elements(f"frame_{key}"):

                        # Use mui.Stack to vertically display the slideshow and the pagination centered.
                        # https://mui.com/material-ui/react-stack/#usage
                                with mui.Stack(spacing=2, alignItems="center"):

                            # Create a swipeable view that updates st.session_state[key] thanks to sync().
                            # It also sets the index so that changing the pagination (see below) will also
                            # update the swipeable view.
                            # https://mui.com/material-ui/react-tabs/#full-width
                            # https://react-swipeable-views.com/demos/demos/
                                    with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key)):
                                        for image in images:
                                            html.img(src=image, css={"width": "100%"})

                            # Create a handler for mui.Pagination.
                            # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                    def handle_change(event, value):
                                # Pagination starts at 1, but our index starts at 0, explaining the '-1'.
                                        st.session_state[key] = value-1

                            # Display the pagination.
                            # As the index value can also be updated by the swipeable view, we explicitely
                            # set the page value to index+1 (page value starts at 1).
                            # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                    mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)


                # if __name__ == '__main__':
                        slideshow_swipeable(IMAGES)
            with text_col4:
                st.subheader("Lottery Revenue Analysis")
                st.write(
                    """
                    - Use good user interface – DAX functions – some basic calculations – KPI cards – Filters -Different 
                        visualization – Book mark using visualization – Tool tips
                    - Dashboards publish to Power BI cloud – Dashboard and MySQL database connections using
                        On-premises data gateway – Scheduled based refresh of the dashboard.
                    - Python automate – Run the python file watcher - When the file put into the folder – File watcher Push the 
                        data into MySQL database – If any error on this file Push the error folder & check the log file using fix the 
                        error’s – If no error, the file push to the success folder & push to the MySQL database – All of this run on a 
                        local server.
                    """
                )        

if selected == "Power BI Project":
    st.subheader(f"{selected}")
    
    with st.container():
        text_col5, image_col5 = st.columns(2)
        
        # -------------- Super Market Revenue Analysis --------------------
        with text_col5:
            st.subheader("Super Market Sales Analysis")
            st.write(
                """
                - Use good user interface – DAX functions – some basic calculations – KPI cards – Filters -Different 
                    visualization – Book mark using visualization – Tool tips
                - Use Month on Month Growth Rate.
                - Metrics in Power BI let customers curate their metrics and track them against key business objectives, in a single pane.
                - In this Power BI used to create views of report pages that are optimized for viewing on mobile devices.    
                - Template created in Figma
                """
            )    
            link = "https://app.powerbi.com/view?r=eyJrIjoiMmQyMzA4YWYtNjAxYS00YzY1LWJhYTgtOWFiZGU3YmM3MWEzIiwidCI6IjJkMWUxN2Q0LWRlYzMtNGM4NS05MjcxLTIzYjIxZmM5ODhkMCJ9"
            st.write(f" - [Dashboard Link]({link})")
            
        with image_col5:
                    IMAGES = [
                "https://user-images.githubusercontent.com/108980892/229756282-167d4377-6352-4d8b-839e-535a68e5d91f.png",
                "https://user-images.githubusercontent.com/108980892/229756466-d04c3c2d-2508-49cf-b892-16999e3598ff.png",
                "https://user-images.githubusercontent.com/108980892/229756627-e3ff9dc1-87fe-4d58-bead-e4c0233ef8e3.png",
                "https://user-images.githubusercontent.com/108980892/229760122-ec455396-c268-4a99-ab00-1ac30ea45c81.png"
            ]


                    def slideshow_swipeable(images):
                # Generate a session state key based on images.
                        key = f"slideshow_swipeable_{str(images).encode().hex()}"

                # Initialize the default slideshow index.
                        if key not in st.session_state:
                            st.session_state[key] = 0

                # Get the current slideshow index.
                        index = st.session_state[key]

                # Create a new elements frame.
                        with elements(f"frame_{key}"):

                    # Use mui.Stack to vertically display the slideshow and the pagination centered.
                    # https://mui.com/material-ui/react-stack/#usage
                            with mui.Stack(spacing=2, alignItems="center"):

                        # Create a swipeable view that updates st.session_state[key] thanks to sync().
                        # It also sets the index so that changing the pagination (see below) will also
                        # update the swipeable view.
                        # https://mui.com/material-ui/react-tabs/#full-width
                        # https://react-swipeable-views.com/demos/demos/
                                with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key)):
                                    for image in images:
                                        html.img(src=image, css={"width": "100%"})

                        # Create a handler for mui.Pagination.
                        # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                def handle_change(event, value):
                            # Pagination starts at 1, but our index starts at 0, explaining the '-1'.
                                    st.session_state[key] = value-1

                        # Display the pagination.
                        # As the index value can also be updated by the swipeable view, we explicitely
                        # set the page value to index+1 (page value starts at 1).
                        # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)


            # if __name__ == '__main__':
                    slideshow_swipeable(IMAGES)
                    
                    
    st.markdown("----")  
    with st.container():
        image_col6, text_col6 = st.columns(2)
        
        # -------------- People Counting Dashboard --------------------
        
        with image_col6:
                    IMAGES = [
                "https://user-images.githubusercontent.com/108980892/233640907-6d141133-08db-44a0-a842-c27c14cbdc94.png",
                "https://user-images.githubusercontent.com/108980892/233641017-aee4599a-9aef-4887-8549-a8851dee5e72.png",
                "https://user-images.githubusercontent.com/108980892/233641105-06f285c1-112e-46f0-b4aa-ad10495fa7d7.png"
            ]


                    def slideshow_swipeable(images):
                # Generate a session state key based on images.
                        key = f"slideshow_swipeable_{str(images).encode().hex()}"

                # Initialize the default slideshow index.
                        if key not in st.session_state:
                            st.session_state[key] = 0

                # Get the current slideshow index.
                        index = st.session_state[key]

                # Create a new elements frame.
                        with elements(f"frame_{key}"):

                    # Use mui.Stack to vertically display the slideshow and the pagination centered.
                    # https://mui.com/material-ui/react-stack/#usage
                            with mui.Stack(spacing=2, alignItems="center"):

                        # Create a swipeable view that updates st.session_state[key] thanks to sync().
                        # It also sets the index so that changing the pagination (see below) will also
                        # update the swipeable view.
                        # https://mui.com/material-ui/react-tabs/#full-width
                        # https://react-swipeable-views.com/demos/demos/
                                with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key)):
                                    for image in images:
                                        html.img(src=image, css={"width": "100%"})

                        # Create a handler for mui.Pagination.
                        # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                def handle_change(event, value):
                            # Pagination starts at 1, but our index starts at 0, explaining the '-1'.
                                    st.session_state[key] = value-1

                        # Display the pagination.
                        # As the index value can also be updated by the swipeable view, we explicitely
                        # set the page value to index+1 (page value starts at 1).
                        # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)


            # if __name__ == '__main__':
                    slideshow_swipeable(IMAGES)
        with text_col6:
            st.subheader("People Counting Dashboard")
            st.write(
                """
                - Use good user interface – DAX functions – some basic calculations – KPI cards – Filters -Different 
                    visualization – Book mark using visualization – Tool tips.
                - Visualize the people counting data in the Power BI dashboard.
                - Visualize this week's count and this month's count. Visualize the overall summary.
                - A good user interface - DAX measures - basic calculations - visualize different plots - filters and easy to understand this dashboard.
                - Power BI dashboard and MySQL database connections using On-premises data gateway.  
                - Template created in Microsoft power point with background animation.
                """
            )
            link = "https://app.powerbi.com/view?r=eyJrIjoiZjQzMTI0MmMtYWZhNy00MmJiLTk1OTktN2I5YjcyODNjZjgwIiwidCI6IjJkMWUxN2Q0LWRlYzMtNGM4NS05MjcxLTIzYjIxZmM5ODhkMCJ9"
            st.write(f" - [Dashboard Link]({link})")
            
# ------------------- Sem Project ---------------------------           
if selected == "Sem Project":
    st.subheader(f"{selected}")
    st.header("People Counting & Tracking Streamlit Web Application")
    
    # ------------ Internship Training -------
    with st.container():
        left_col7, right_col7 = st.columns(2)
    with left_col7:
        st.write("##")
        st.markdown("""
                    - Open CV using people counting & tracking streamlit web application. In this project main purpose of counting the people
                      in and people out in our campus or any organization.
                    - Technologies used in this project - Python, Streamlit, Power BI, MySQL database, On-premises data gateway.
                    - Python to access CCTV cameras, people enter the boundary line, can detect the people same as counting the people in and people out.
                    - People count data stored in an Excel file after Excel data 24 hours once updated to MySQL database.
                    - Visualize the people counting data in the Power BI dashboard.
                    - Visualize this week's count and this month's count. Visualize the overall summary.
                    - A good user interface - DAX measures - basic calculations - visualize different plots - filters and easy to understand this dashboard.
                    - Power BI dashboard and MySQL database connections using On-premises data gateway.
                    """)
    with right_col7:
        st.write('##')
        IMAGES = [
                "https://github.com/jaghant/images/blob/main/Sem%20IV/Workflow.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20IV/Login.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20IV/main.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20IV/Power-BI.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20IV/Home.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20IV/Weekly%20report.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20IV/Overall%20report.png?raw=true"
    ]
        def slideshow_swipeable(images):
                # Generate a session state key based on images.
                        key = f"slideshow_swipeable_{str(images).encode().hex()}"

                # Initialize the default slideshow index.
                        if key not in st.session_state:
                            st.session_state[key] = 0

                # Get the current slideshow index.
                        index = st.session_state[key]

                # Create a new elements frame.
                        with elements(f"frame_{key}"):

                    # Use mui.Stack to vertically display the slideshow and the pagination centered.
                    # https://mui.com/material-ui/react-stack/#usage
                            with mui.Stack(spacing=2, alignItems="center"):

                        # Create a swipeable view that updates st.session_state[key] thanks to sync().
                        # It also sets the index so that changing the pagination (see below) will also
                        # update the swipeable view.
                        # https://mui.com/material-ui/react-tabs/#full-width
                        # https://react-swipeable-views.com/demos/demos/
                                with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key)):
                                    for image in images:
                                        html.img(src=image, css={"width": "100%"})

                        # Create a handler for mui.Pagination.
                        # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                def handle_change(event, value):
                            # Pagination starts at 1, but our index starts at 0, explaining the '-1'.
                                    st.session_state[key] = value-1

                        # Display the pagination.
                        # As the index value can also be updated by the swipeable view, we explicitely
                        # set the page value to index+1 (page value starts at 1).
                        # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)


            # if __name__ == '__main__':
        slideshow_swipeable(IMAGES)  
    st.markdown("---") 
    st.header("Sales Forecasting Time Series Analysis")
    with st.container():
        left_col8, right_col8 = st.columns(2)
               
        
        with left_col8:
            IMAGES = [
                "https://github.com/jaghant/images/blob/main/Sem%20III/Data.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20III/Ship%20modes.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20III/Total%20sales%20per%20year.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20III/Total%20sales%20trend.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20III/Monthly%20sales.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20III/Yearly%20trend.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20III/Sales%20trend%20.over%20dayspng.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20III/Distribution.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20III/Sales%20count.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20III/Sales%20value.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20III/Mean%20test.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20III/Trend_seasonality.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20III/Model%20buildingpng.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20III/Sales%20forecast.png?raw=true"
            ]
            def slideshow_swipeable(images):
                # Generate a session state key based on images.
                        key = f"slideshow_swipeable_{str(images).encode().hex()}"

                # Initialize the default slideshow index.
                        if key not in st.session_state:
                            st.session_state[key] = 0

                # Get the current slideshow index.
                        index = st.session_state[key]

                # Create a new elements frame.
                        with elements(f"frame_{key}"):

                    # Use mui.Stack to vertically display the slideshow and the pagination centered.
                    # https://mui.com/material-ui/react-stack/#usage
                            with mui.Stack(spacing=2, alignItems="center"):

                        # Create a swipeable view that updates st.session_state[key] thanks to sync().
                        # It also sets the index so that changing the pagination (see below) will also
                        # update the swipeable view.
                        # https://mui.com/material-ui/react-tabs/#full-width
                        # https://react-swipeable-views.com/demos/demos/
                                with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key)):
                                    for image in images:
                                        html.img(src=image, css={"width": "100%"})

                        # Create a handler for mui.Pagination.
                        # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                def handle_change(event, value):
                            # Pagination starts at 1, but our index starts at 0, explaining the '-1'.
                                    st.session_state[key] = value-1

                        # Display the pagination.
                        # As the index value can also be updated by the swipeable view, we explicitely
                        # set the page value to index+1 (page value starts at 1).
                        # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)


            # if __name__ == '__main__':
            slideshow_swipeable(IMAGES)
        with right_col8:
            st.markdown("""
                    - The details of 9800 record and have 4 years of sales data in United States.
                    - Data column using add some new columns month and year using the trend and seasonality of thee sales analysis
                      in month and year wise.
                    - Visualize the shipping time according to ship modes.
                    - Plot monthly observation of total sales.
                    - Find some same patterns observed in each year rise in December, November, and September.
                    - Sales trend over days.
                    - Plot the sales distribution.
                    - Rolling mean test.
                    - ARIMA Model - Visualization of the performance of our model.
                    - Visualize the sales forecasting.
                    - XG Boost Model.
                    - Root mean squared error for XG Boost.
                    - Model Evalustion.
                    """)    
    st.markdown("---")      
    st.header("Health Data Analysis - EDA & Decision Tree Classification")
    with st.container():
        left_col9, right_col9 = st.columns(2)
        
        with left_col9:
            st.markdown("""
                        - The details of 7304 records and have one-year data with some NA values.
                        - In the patients ages between 18 to 96 years.
                        - Some patient's health data are present in the diagnosis and the diagnosis.
                        - EDA - Matplotlib - Seaborn - Numpy - Pandas - Data Visualization - Analysis of the data.
                        - Drop some unnecessary columns - Date columns using add some new columns day and month using Trend Analysis in Diagnosis or Not Diagnosis in month wise.
                        - Decision Tree Classifier - Export the feature data - and load the feature data - Fix the target variable and features.
                        - Testing & Training the data - Create decision tree classifier object - Train Decision Tree Classifier.
                        - Predict the response for thee test dataset - Find the Accuracy - Visualizing the decision tree graph.
                        """)
            
        with right_col9:
            IMAGES = [
                "https://github.com/jaghant/images/blob/main/Sem%20II/13.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20II/1%20Month%20Wise%20Diagnosis%20Yes%20or%20No%20In%20Male.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20II/2%20Month%20Wise%20Diagnosis%20Yes%20or%20No%20In%20Female.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20II/3.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20II/4.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20II/5.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20II/6.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20II/7.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20II/8.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20II/9.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20II/10.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20II/11.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20II/12.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20II/14.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20II/15.png?raw=true"
            ]
            def slideshow_swipeable(images):
                # Generate a session state key based on images.
                        key = f"slideshow_swipeable_{str(images).encode().hex()}"

                # Initialize the default slideshow index.
                        if key not in st.session_state:
                            st.session_state[key] = 0

                # Get the current slideshow index.
                        index = st.session_state[key]

                # Create a new elements frame.
                        with elements(f"frame_{key}"):

                    # Use mui.Stack to vertically display the slideshow and the pagination centered.
                    # https://mui.com/material-ui/react-stack/#usage
                            with mui.Stack(spacing=2, alignItems="center"):

                        # Create a swipeable view that updates st.session_state[key] thanks to sync().
                        # It also sets the index so that changing the pagination (see below) will also
                        # update the swipeable view.
                        # https://mui.com/material-ui/react-tabs/#full-width
                        # https://react-swipeable-views.com/demos/demos/
                                with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key)):
                                    for image in images:
                                        html.img(src=image, css={"width": "100%"})

                        # Create a handler for mui.Pagination.
                        # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                def handle_change(event, value):
                            # Pagination starts at 1, but our index starts at 0, explaining the '-1'.
                                    st.session_state[key] = value-1

                        # Display the pagination.
                        # As the index value can also be updated by the swipeable view, we explicitely
                        # set the page value to index+1 (page value starts at 1).
                        # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)


            # if __name__ == '__main__':
            slideshow_swipeable(IMAGES)  

    st.markdown("---") 
    st.header("Bike Buyer's Data Analysis")
    with st.container():
        left_col10, right_col10 = st.columns(2)
               
        with left_col10:
            IMAGES = [
                "https://github.com/jaghant/images/blob/main/Sem%20I/1.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20I/2.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20I/3.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20I/4.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20I/5.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20I/6.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20I/7.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20I/8.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20I/9.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20I/10.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20I/11.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20I/12.png?raw=true",
                "https://github.com/jaghant/images/blob/main/Sem%20I/13.png?raw=true"
            ]
            def slideshow_swipeable(images):
                # Generate a session state key based on images.
                        key = f"slideshow_swipeable_{str(images).encode().hex()}"

                # Initialize the default slideshow index.
                        if key not in st.session_state:
                            st.session_state[key] = 0

                # Get the current slideshow index.
                        index = st.session_state[key]

                # Create a new elements frame.
                        with elements(f"frame_{key}"):

                    # Use mui.Stack to vertically display the slideshow and the pagination centered.
                    # https://mui.com/material-ui/react-stack/#usage
                            with mui.Stack(spacing=2, alignItems="center"):

                        # Create a swipeable view that updates st.session_state[key] thanks to sync().
                        # It also sets the index so that changing the pagination (see below) will also
                        # update the swipeable view.
                        # https://mui.com/material-ui/react-tabs/#full-width
                        # https://react-swipeable-views.com/demos/demos/
                                with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key)):
                                    for image in images:
                                        html.img(src=image, css={"width": "100%"})

                        # Create a handler for mui.Pagination.
                        # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                def handle_change(event, value):
                            # Pagination starts at 1, but our index starts at 0, explaining the '-1'.
                                    st.session_state[key] = value-1

                        # Display the pagination.
                        # As the index value can also be updated by the swipeable view, we explicitely
                        # set the page value to index+1 (page value starts at 1).
                        # https://mui.com/material-ui/react-pagination/#controlled-pagination
                                mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)


            # if __name__ == '__main__':
            slideshow_swipeable(IMAGES)
        with right_col10:
            st.markdown("""
                    - The details of 1000 users from different backgrounds with some injected NA values and output
                      variables as to whether or not they buy a bike.
                    - EDA - Matplotlib - Seaborn - Numpy - Pandas - Data Visualization - Analysis the data - Bike Purchase Trend Analysis.
                    - Bike purchasing trend according to gender - region.
                    - Bike purchasing trend according occupation.
                    - Bike purchasing trend according to age.
                    - Bike purchasing trend according to marital status.
                    - Bike purchasing trend according to salary - education.
                    - Bike purchasing trend according to numbers of their children.
                    - Bike purchasing trend according to number of cars they own.
                    - Bike purchasing trend of home owners - commuting distance.
                    """)
              
        
        
        
# ------------Contact ------------
with st.container():
    st.write("---") 
    st.header("Get In Touch With Me!")  
    st.write("##")  
    contact_form = """<form action="https://formsubmit.co/jaghanvv@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name="message" placeholder = "Your message here" required></textarea>
     <button type="submit">Send</button>
</form>"""  

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
    
with right_column:
    st.empty()                    