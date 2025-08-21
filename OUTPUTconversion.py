# OUTPUTconversion.py
import json
import csv
import streamlit as st

def convert_json_to_csv(json_file, csv_file):
    # Load JSON data
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Open CSV file for writing
    with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        # Define CSV headers
        headers = [
            "name", "email", "phone", "address", "other_details",
            "education", "experience", "total_years_experience",
            "programming_languages", "bi_tools", "version_control_systems",
            "testing_and_automation", "cloud", "frameworks_libraries",
            "databases", "secondary_skills"
        ]
        writer.writerow(headers)

        # Write rows
        for person in data:
            # Extract personal info
            pi = person.get("personal_information", {})
            name = pi.get("name", "")
            email = pi.get("email", "")
            phone = pi.get("phone", "")
            address = pi.get("address", "")
            other_details = pi.get("other_details", "")

            # Flatten education
            education = "; ".join([
                f'{ed.get("degree_and_field", "")} at {ed.get("institution", "")} '
                f'({ed.get("start_date", "")}-{ed.get("end_date", "")})'
                for ed in person.get("education", [])
            ])

            # Flatten experience
            experience = "; ".join([
                f'{ex.get("job_title", "")} at {ex.get("company_name", "")}, {ex.get("job_location", "")} '
                f'({ex.get("start_date", "")}-{ex.get("end_date", "")})'
                for ex in person.get("experience", [])
            ])

            # Total years of experience
            total_years_experience = person.get("total_years_experience", "")

            # Extract skills
            skills = person.get("skills", {})
            programming_languages = ", ".join(skills.get("programming_languages", []))
            bi_tools = ", ".join(skills.get("bi_tools", []))
            version_control_systems = ", ".join(skills.get("version_control_systems", []))
            testing_and_automation = ", ".join(skills.get("testing_and_automation", []))
            cloud = ", ".join(skills.get("cloud", []))
            frameworks_libraries = ", ".join(skills.get("frameworks_libraries", []))
            databases = ", ".join(skills.get("databases", []))
            secondary_skills = ", ".join(skills.get("secondary_skills", []))

            # Write row to CSV
            writer.writerow([
                name, email, phone, address, other_details,
                education, experience, total_years_experience,
                programming_languages, bi_tools, version_control_systems,
                testing_and_automation, cloud, frameworks_libraries,
                databases, secondary_skills
            ])

    st.success(f"✅ Data has been successfully converted and saved to {csv_file}")


# ✅ Only runs when you click the button in Streamlit
if __name__ == "__main__":

    # --- Streamlit UI ---
    st.markdown(
    """
    <div style="text-align: center;">
        <img src="data:image/png;base64,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" width="400">
    </div>
    """,
    unsafe_allow_html=True
)
    st.title("Resume Parser - POC Tool")

    # File/folder inputs from user
    json_file = st.text_input("Enter Output JSON File Path", value="")
    csv_file = st.text_input("Enter Output CSV File Path", value="")
    folder_path = st.text_input("Enter Resumes Folder Path", value="")
    failed_dir = st.text_input("Enter Folder Path For Manual Resume Parsing", value="")
    processed_dir = st.text_input("Enter Folder Path For Processed Resumes", value="")

    # Button to confirm and save
    if st.button("Save Paths"):
        if not all([json_file, csv_file, folder_path, failed_dir, processed_dir]):
            st.error("⚠️ Please provide all paths before saving.")
        else:
            # Save variables to includes.py (overwrite)
            with open("includes.py", "w") as f:
                f.write(f'json_file = r"{json_file}"\n')
                f.write(f'csv_file = r"{csv_file}"\n')
                f.write(f'folder_path = r"{folder_path}"\n')
                f.write(f'failed_dir = r"{failed_dir}"\n')
                f.write(f'processed_dir = r"{processed_dir}"\n')
            import main_with_json
            main_with_json.run_pipeline(
                json_file,
                csv_file,
                folder_path,
                failed_dir,
                processed_dir,
            )
            st.success(f"✅ Parsing complete! JSON saved at: {json_file}")

            st.success("Paths saved successfully to includes.py ✅")
            # 👉 Only run conversion after paths are saved
            convert_json_to_csv(json_file, csv_file)
