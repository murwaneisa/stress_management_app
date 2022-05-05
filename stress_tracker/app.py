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
        try:
            result = log_in.login_form()
            if result:
                st.success(f"successfully logged in as {result[1]} {result[2]}")
        except Exception as error:
            st.error(error)
    elif choice == "SignUp":
        sign_up.sign_up_ui()
    elif choice == "Admin":
        try:
            result = log_in.admin_login_form()
            if result:
                st.success(f"successfully logged in as {result[1]} {result[2]}")
        except Exception as error:
            st.error(error)


if __name__ == "__main__":
    main()
