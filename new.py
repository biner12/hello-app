import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import sqlite3
#Page title #DONE
st.set_page_config(
    page_title ="Connecting Construction Experts: EnhanCEd Online Bidding Platform",
    page_icon="👷‍♀️🤝👷",)

#Sidebar
st.sidebar.title("Connecting Construction Experts: EnhanCEd Online Bidding Platform👷‍♀️‍🤝👷")
st.sidebar.write("🏗Bidding Smarter, Building Together🏗")

with st.sidebar:
    selected= option_menu(
        menu_title= 'Table of Contents',
        options= ["Profile", "Home", "Bidding", "About", "FAQS", "Feedback", "Contacts"])
st.sidebar.header("To reach our company, contact us through: ")
st.sidebar.write("📧Email : civiltech.innovators@gmail.com")
st.sidebar.write("📞Phone # : +639364824532")
st.sidebar.write("☎️Landline : 402 - 2915")
st.sidebar.write("👍Facebook Page: CivilTech Innovators")
st.sidebar.write("🐦Twitter: @CivilTechInnovators")

#Profile page
if selected == "Profile": #INSERT CODE FOR THIS
    st.header("My Profile")

#Home page
elif selected== "Home":  #INSERT CODE FOR ANIMATION, INTRODUCTION, AND PROPOSED PROJECTS
    st.header('Connecting Construction Experts: EnhanCEd Online Bidding Platform👷‍♀️🤝👷')

#Bidding page
elif selected== "Bidding": #AAYUSIN PA
    # Create a SQLite database and table to store project details
    conn = sqlite3.connect('construction_bidding.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            budget REAL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bids (
            id INTEGER PRIMARY KEY,
            project_id INTEGER,
            bidder_name TEXT,
            bid_amount REAL
        )
    ''')

    conn.commit()
    # Function to add a new project
    def add_project(name, description, budget):
        cursor.execute('INSERT INTO projects (name, description, budget) VALUES (?, ?, ?)', (name, description, budget))
        conn.commit()
    # Function to place a bid for a project
    def place_bid(project_id, bidder_name, bid_amount):
        cursor.execute('INSERT INTO bids (project_id, bidder_name, bid_amount) VALUES (?, ?, ?)',
                       (project_id, bidder_name, bid_amount))
        conn.commit()
    # Function to get project details and associated bids
    def get_project_details(project_id):
        cursor.execute('SELECT name, description, budget FROM projects WHERE id = ?', (project_id,))
        project_details = cursor.fetchone()

        cursor.execute('SELECT bidder_name, bid_amount FROM bids WHERE project_id = ?', (project_id,))
        bids = cursor.fetchall()

        return project_details, bids

    st.title("Construction Bidding Project")
    # Add a new project
    st.header("Add a New Project")
    project_name = st.text_input("Project Name")
    project_description = st.text_area("Project Description")
    project_budget = st.number_input("Project Budget", min_value=0)
    if st.button("Add Project"):
        add_project(project_name, project_description, project_budget)
        st.success(f"Project '{project_name}' added successfully.")

    # Display a list of projects
    st.header("List of Projects")
    projects_df = pd.read_sql_query('SELECT id, name, description, budget FROM projects', conn)
    st.table(projects_df)

    # Allow bidders to place bids for a project
    st.header("Place a Bid")
    selected_project_id = st.selectbox("Select a Project", projects_df["name"], format_func=lambda x: f"{x}")
    bidder_name = st.text_input("Your Name")
    bid_amount = st.number_input("Bid Amount", min_value=0)
    if st.button("Place Bid"):
        place_bid(selected_project_id, bidder_name, bid_amount)
        st.success(
            f"{bidder_name} placed a bid of ${bid_amount} for '{projects_df[projects_df['id'] == selected_project_id]['name'].values[0]}'")

    # Display bids for a selected project
    st.header("Bids for Selected Project")
    selected_project_id = st.selectbox("Select a Project to View Bids", projects_df["name"],
                                       format_func=lambda x: f"{x}")
    project_details, bids = get_project_details(selected_project_id)
    st.write("Project Details:")
    st.write(f"Name: {project_details[0]}")
    st.write(f"Description: {project_details[1]}")
    st.write(f"Budget: ${project_details[2]:,.2f}")
    st.write("Bids:")
    if bids:
        bids_df = pd.DataFrame(bids, columns=["Bidder Name", "Bid Amount"])
        st.table(bids_df)
    else:
        st.info("No bids have been placed for this project yet.")

    # Close the database connection when done
    conn.close()

#About page
elif selected == "About": #DONE SA CONTENT
    st.title("ABOUT US🤔💭")
    #INSERT CODE FOR ANIMATION
    st.title("📌VISION")
    st.write("To be the leading and most innovative Online Construction Project Bidding Platform, connecting contractors and subcontractors worldwide, revolutionizing the construction industry through collaboration, efficiency, and value-driven solutions.")

    st.title("📌MISSION")
    st.write("To provide a user-friendly and efficient online platform that bridges the gap between contractors and subcontractors, offering a seamless experience for project owners and bidders. We strive to enable project owners to find the best teams for their construction projects and empower subcontractors to grow their businesses. We are committed to facilitating competitive bidding, enhancing project transparency, and driving down costs, ultimately ensuring the success of every construction endeavor.")

    st.title("📌GOAL")
    st.write("To enable seamless collaboration between contractors (project owners) and subcontractors through our online construction project bidding platform, fostering a thriving construction ecosystem. The platform aims to provide a user-friendly interface where contractors can showcase their projects, including project details and bid deadlines, while subcontractors can efficiently submit their bids, complete with pricing details and necessary documents. The ultimate goal is to expand the network of subcontractors available to contractors, promoting effective project development and encouraging competitive bidding to optimize project costs, thereby delivering the best value for construction projects.")

    st.title("📌VALUES")
    st.header("Collaboration ")
    st.write("We value fostering partnerships and teamwork between contractors and subcontractors, promoting synergy and shared success.")

    st.header("Efficiency  ")
    st.write("We are committed to streamlining the project bidding process, making it easier for users to manage projects and submit bids swiftly and effectively.")

    st.header("Transparency ")
    st.write("We prioritize open communication and transparency in project details and pricing, ensuring trust and fairness in the bidding process.")

    st.header("Quality ")
    st.write("We strive to facilitate the selection of the most qualified subcontractors, leading to high-quality construction outcomes for project owners.")

    st.header("Innovation ")
    st.write("We continuously seek innovative solutions to enhance the construction industry, providing tools and features that adapt to evolving needs.")

    st.header("Cost-Effectiveness ")
    st.write("We aim to drive down project costs by promoting competitive bidding, helping project owners obtain the best value for their construction projects.")

    st.header("Community Building ")
    st.write("We aim to drive down project costs by promoting competitive bidding, helping project owners obtain the best value for their construction projects.")

#FAQS page
elif selected == "FAQS": #DADAGDAGAN PA AND MAY INSERT CODE FOR ANIMATION
    st.title("FREQUENTLY ASKED QUESTIONS")
    st.write("Your questions, answered. ")

    st.header("1. What exactly is Connecting Construction Experts: EnhanCEd Online Bidding Platform? ")
    st.write("This online construction project bidding platform connects contractors (project owners) with subcontractors. Contractors can list their projects with details like project name, description, location, budget range, and bid deadline. Subcontractors can bid on projects and upload pricing and documents. The platform encourages collaboration, broadens subcontractor networks, and promotes competitive bidding to reduce project costs, providing the best value for owners. It streamlines project bidding, fostering cooperation and cost-efficiency in the construction industry.")

    st.header("2. How does competitive bidding work on the platform? ")
    st.write("Competitive bidding is facilitated by allowing subcontractors to submit their bids, driving down project costs. This helps contractors get the best value for their construction projects. ")

    st.header("3. ")

#Feedback page
elif selected == "Feedback": #INSERT CODE FOR ANIMATION
    feedback = st.text_area("Your Feedback")
    rating = st.slider("⭐️Rate the Application (1-5)⭐️", 1, 5)
    if st.button("Submit Feedback"):
        if rating == 5:
            st.write("Wow! Thanks for the 5-star rating! We're thrilled to have exceeded your expectations. Your support is greatly appreciated. ")
        elif rating == 4:
            st.write("We're glad you had a positive experience! Your 4-star rating motivates us to continue providing great service. ️")
        elif rating == 3:
            st.write("Thank you for your feedback, it helps us identify areas for improvement and provide a better experience. ")
        elif rating == 2:
            st.write("We apologize for falling short of your expectations. Your feedback will help us enhance our application. ")
        elif rating == 1:
            st.write("We're truly sorry for your disappointing experience. Your feedback is invaluable to us and will be used to make improvements. ")

#Contacts Page
elif selected == "Contacts" :
    st.header("CivilTech Innovators🦺")
    st.header("Please Contact Us If You Have Any Concern")
    st.subheader("👷Engr. Clarince Julius S. Canillo")
    st.write("📱Contact Number: ")
    st.write("📧Email: 22-05547@g.batstate-u.edu.ph ")
    st.write("-------------------------------------")
    st.subheader("👷Kim Biner G. Deomampo")
    st.write("📱Contact Number: ")
    st.write("📧Email: 22-03442@g.batstate-u.edu.ph ")
    st.write("-------------------------------------")
    st.subheader("👷‍♀️Engr. Kaye Aira P. De Leon")
    st.write("📱Contact Number: 09602115398")
    st.write("📧Email: 22-01191@g.batstate-u.edu.ph ")
    st.write("-------------------------------------")
    st.subheader("👷Engr. Rainiel E. Reyes")
    st.write("📱Contact Number: ")
    st.write("📧Email: 22-04086@g.batstate-u.edu.ph ")
    st.write("-------------------------------------")
    st.subheader("👷Engr. Kim James Rodriguez")
    st.write("📱Contact Number: ")
    st.write("📧Email: 22-06174@g.batstate-u.edu.ph ")
