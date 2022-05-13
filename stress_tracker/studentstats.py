import streamlit as st
import global_vars


class StudentStatistics:

    def __init__(self,db):
        self.db = db
        self.program = None
        self.degree = None

    def on_confirm(self):
        pass


    # student stats widget
    def showStats(self,program,degree):
        st.header("View student statistics")

        st.metric(label="Program", value=program)
        st.metric(label="Degree", value=degree)
        

