import streamlit as st
import os
from pathlib import Path

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="File Manager",
    page_icon="📁",
    layout="centered"
)

BASE_DIR = Path("workspace")
BASE_DIR.mkdir(exist_ok=True)

# ------------------ HELPERS ------------------
def list_items():
    return [str(p.relative_to(BASE_DIR)) for p in BASE_DIR.rglob("*")]

# ------------------ UI ------------------
st.title("📁 File Management System")
st.caption("A simple, elegant file handling application")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Create Folder",
        "List Files & Folders",
        "Rename Folder",
        "Delete Folder",
        "Create File",
        "Read File",
        "Update File",
        "Delete File"
    ]
)

st.divider()

# ------------------ CREATE FOLDER ------------------
if menu == "Create Folder":
    st.subheader("📂 Create Folder")
    name = st.text_input("Folder name")

    if st.button("Create Folder"):
        path = BASE_DIR / name
        if not path.exists():
            path.mkdir()
            st.success("Folder created successfully")
        else:
            st.error("Folder already exists")

# ------------------ LIST ------------------
elif menu == "List Files & Folders":
    st.subheader("📃 Files & Folders")
    items = list_items()

    if items:
        for i in items:
            st.write(f"• {i}")
    else:
        st.info("Workspace is empty")

# ------------------ RENAME FOLDER ------------------
elif menu == "Rename Folder":
    st.subheader("✏️ Rename Folder")

    folders = [p for p in BASE_DIR.iterdir() if p.is_dir()]
    if folders:
        old = st.selectbox("Select folder", folders)
        new_name = st.text_input("New folder name")

        if st.button("Rename"):
            new_path = BASE_DIR / new_name
            if not new_path.exists():
                old.rename(new_path)
                st.success("Folder renamed successfully")
            else:
                st.error("Folder name already exists")
    else:
        st.info("No folders available")

# ------------------ DELETE FOLDER ------------------
elif menu == "Delete Folder":
    st.subheader("🗑️ Delete Folder")

    folders = [p for p in BASE_DIR.iterdir() if p.is_dir()]
    folder = st.selectbox("Select folder", folders) if folders else None

    if folder and st.button("Delete Folder"):
        if not any(folder.iterdir()):
            folder.rmdir()
            st.success("Folder deleted")
        else:
            st.error("Folder is not empty")

# ------------------ CREATE FILE ------------------
elif menu == "Create File":
    st.subheader("📄 Create File")

    filename = st.text_input("File name (with extension)")
    content = st.text_area("File content")

    if st.button("Create File"):
        path = BASE_DIR / filename
        if not path.exists():
            path.write_text(content)
            st.success("File created successfully")
        else:
            st.error("File already exists")

# ------------------ READ FILE ------------------
elif menu == "Read File":
    st.subheader("📖 Read File")

    files = [p for p in BASE_DIR.rglob("*") if p.is_file()]
    file = st.selectbox("Select file", files) if files else None

    if file:
        st.code(file.read_text(), language="text")

# ------------------ UPDATE FILE ------------------
elif menu == "Update File":
    st.subheader("🛠️ Update File")

    files = [p for p in BASE_DIR.rglob("*") if p.is_file()]
    file = st.selectbox("Select file", files) if files else None

    action = st.radio(
        "Choose action",
        ["Rename File", "Overwrite Content", "Append Content"]
    )

    if file:
        if action == "Rename File":
            new_name = st.text_input("New file name")
            if st.button("Rename"):
                new_path = file.parent / new_name
                if not new_path.exists():
                    file.rename(new_path)
                    st.success("File renamed successfully")
                else:
                    st.error("File name already exists")

        elif action == "Overwrite Content":
            data = st.text_area("New content")
            if st.button("Overwrite"):
                file.write_text(data)
                st.success("File updated successfully")

        elif action == "Append Content":
            data = st.text_area("Content to append")
            if st.button("Append"):
                with open(file, "a") as f:
                    f.write(data)
                st.success("Content appended successfully")

# ------------------ DELETE FILE ------------------
elif menu == "Delete File":
    st.subheader("❌ Delete File")

    files = [p for p in BASE_DIR.rglob("*") if p.is_file()]
    file = st.selectbox("Select file", files) if files else None

    if file and st.button("Delete File"):
        os.remove(file)
        st.success("File deleted successfully")
