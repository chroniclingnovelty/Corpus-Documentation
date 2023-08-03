import pandas as pd
import os

# Define the subtitles
subtitle1 = "Auteur"
subtitle2 = "Kroniek"

# Create markdown template
def create_md_file(directory, call_number, content1, content2):
    filename = f"{call_number}.md"
    filepath = os.path.join(directory, filename)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(f"# {call_number}\n\n")
        file.write(f"## {subtitle1}\n\n")
        file.write(f"naam: {content1}\n\n")
        file.write(f"geboortejaar: {content2}\n\n")
        file.write(f"## {subtitle2}\n\n")
        file.write(f"motief: {content3}\n\n")
        

def main():
    excel_file = "/Users/alielassche/surfdrive/Shared/[Chronicles] team proceedings/Metadata kronieken/Authors_metadata.xlsx"
    sheet_name = "Authors"
    output_directory = "test"  # Directory where the Markdown files will be saved

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Read the Excel sheet into a pandas DataFrame
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    for index, rostw in df.iterrows():
        if index >= 10:
            break

        call_number = row["Kronieken"]
        content1 = row["full_name"]
        content2 = row["year_birth"]
        content3 = row["Motive"]

        # Convert content1 and content2 to Markdown format if needed
        # If the content is already in Markdown format, you can skip this step

        # Create the Markdown file in the output directory
        create_md_file(output_directory, call_number, content1, content2)

if __name__ == "__main__":
    main()
