import streamlit as st
import json
import os

st.set_page_config(
    page_title="Daily Reflection Tree",
    page_icon="🌱",
    layout="centered"
)

# ---------- LOAD JSON ----------
json_path = os.path.join("tree", "reflection-tree.json")

with open(json_path, "r", encoding="utf-8") as file:
    tree = json.load(file)

# Convert list to dictionary for fast lookup
nodes = {node["id"]: node for node in tree}

# ---------- SESSION STATE ----------
if "current_node" not in st.session_state:
    st.session_state.current_node = "START"

if "answers" not in st.session_state:
    st.session_state.answers = {}

# ---------- FUNCTIONS ----------
def go_next(node_id):
    st.session_state.current_node = node_id
    st.rerun()

def restart():
    st.session_state.current_node = "START"
    st.session_state.answers = {}
    st.rerun()

# ---------- CURRENT NODE ----------
node = nodes[st.session_state.current_node]

st.title("🌱 Daily Reflection Tree")
st.caption("A guided end-of-day reflection tool")

# ---------- START / AUTO NODES ----------
if node["type"] in ["start", "reflection", "bridge", "summary", "end"]:
    st.subheader(node["text"])

    if node["type"] == "end":
        st.success("Session completed.")
        st.button("Restart", on_click=restart)

    else:
        if st.button("Continue"):
            go_next(node["next"])

# ---------- QUESTION NODE ----------
elif node["type"] == "question":
    st.subheader(node["text"])

    for option, next_node in node["options"].items():
        if st.button(option):
            st.session_state.answers[node["id"]] = option
            go_next(next_node)