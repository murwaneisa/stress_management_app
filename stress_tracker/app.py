import streamlit as st
import login
import signup


def main():
    st.set_page_config(
        page_title="Stress Tracker | Login",
        page_icon="🐛",
        initial_sidebar_state="expanded",
        menu_items={}
    )

    st.sidebar.title("STRESS TRACKER")

    menu = ["Login","SignUp", "Admin"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    log_in = login.Login()
    sign_up = signup.SignUp()

    if choice == "Login":
        result = log_in.login_form()
        if result:
            print("successfully logged in")
        else:
            print("email or password ")
    elif choice == "SignUp":
        sign_up.sign_up_ui()
    elif choice == "Admin":
        log_in.admin_login_ui()
    
    


if __name__ == "__main__":
    main()
