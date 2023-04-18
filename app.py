import streamlit as st
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
from PIL import Image
from streamlit_elements import elements, mui, html, sync
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

lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json")


# ------------Header Section -------------
with st.container():
    st.subheader("Hi, I am JAGHAN T :wave:")
    st.title("M.Sc Data Science From Coimbatore.")

with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("What I do")
        st.write("##")
        st.write("INTERNSHIP TRAINING.")
        st.markdown(
            """
            AES Technology / August 2022 - Present
            - Currently intern in AES Technologies, Coimbatore as Junior Software Engineer.
            - M&C Project (Business Intelligence in Power BI Dashboards.)
            """
        )
        
with right_col:
       st_lottie(lottie_coding, height=300, key="coding")  
       
st.markdown("----")  
# ------------ My Projects ---------------
with st.container():
    st.header("My Projects")
    st.write("##")
    image_col1, text_col1 = st.columns(2)
    
    # -------------- Sports Revenue Analysis --------------------
    
    with image_col1:
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
    with text_col1:
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
    text_col2, image_col2 = st.columns(2)
    
    # -------------- Hotel Revenue Analysis --------------------
    with text_col2:
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
        
    with image_col2:
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
    image_col3, text_col3 = st.columns(2)
    
    # -------------- Lottery Revenue Analysis --------------------
    
    with image_col3:
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
    with text_col3:
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

st.markdown("----")  
with st.container():
    text_col4, image_col4 = st.columns(2)
    
    # -------------- Super Market Revenue Analysis --------------------
    with text_col4:
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
        
    with image_col4:
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
    image_col5, text_col5 = st.columns(2)
    
    # -------------- People Counting Dashboard --------------------
    
    with image_col5:
                IMAGES = [
            "https://user-images.githubusercontent.com/108980892/232694842-1f74fdcb-52db-4d53-9193-a975590afef9.png",
            "https://user-images.githubusercontent.com/108980892/231670172-52028f01-4145-474a-ba00-5274ed17c337.png",
            "https://user-images.githubusercontent.com/108980892/231670051-f1622f16-0ddc-4cf6-8e7c-8c2cbe0b3437.png"
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
    with text_col5:
        st.subheader("People Counting Dashboard")
        st.write(
            """
            - Use good user interface – DAX functions – some basic calculations – KPI cards – Filters -Different 
                visualization – Book mark using visualization – Tool tips.
            - Power BI is a popular business intelligence solution that is comprised of services, apps, and 
                connectors that allow you to pull the data from various sources and create meaningful reports. To connect Power BI to a data source such as MySQL,  
                you can use a corresponding ODBC driver.  
            - Template created in Microsoft power point with background animation.
            """
        )
        link = "https://app.powerbi.com/view?r=eyJrIjoiZjQzMTI0MmMtYWZhNy00MmJiLTk1OTktN2I5YjcyODNjZjgwIiwidCI6IjJkMWUxN2Q0LWRlYzMtNGM4NS05MjcxLTIzYjIxZmM5ODhkMCJ9"
        st.write(f" - [Dashboard Link]({link})")
          
        
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
