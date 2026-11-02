
import pandas as pd


df = pd.read_csv("student_data.csv")

df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
df["attendance"] = pd.to_numeric(df["attendance"], errors="coerce")


df["grade"] = df["marks"].apply(
    lambda x: "A" if pd.notna(x) and x >= 90 else
              "B" if pd.notna(x) and x >= 80 else
              "C" if pd.notna(x) and x >= 70 else
              "D" if pd.notna(x) else "Not Available"
)


df["result"] = df["marks"].apply(
    lambda x: "Pass" if pd.notna(x) and x >= 40 else
              "Fail" if pd.notna(x) else "Not Available"
)


df["attendance_status"] = df["attendance"].apply(
    lambda x: "Good" if pd.notna(x) and x >= 75 else
              "Low" if pd.notna(x) else "Not Available"
)


print(df)


df.to_csv("updated_student_data.csv", index=False)

print("\nNew columns added successfully!")
