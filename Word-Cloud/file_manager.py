import streamlit as st


class FileManager:
    @staticmethod
    def make_file(file_format: str, file: bytes, name: str):
        file_name = f"{name}.{file_format}"

        if file_format == "mp3":
            st.download_button(label="Download Audio", data=file, file_name=file_name, mime='audio/mpeg')
        if file_format == "mp4":
            st.download_button(label="Download file", data=file, file_name=file_name, mime='video/mp4')
        if file_format == "jpg":
            st.download_button(label="Download file", data=file, file_name=file_name, mime='image/jpeg')
        if file_format == "png":
            st.download_button(label="Download file", data=file, file_name=file_name, mime='image/png')
