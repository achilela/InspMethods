import streamlit as st

  # Second digit
second_digit_types = {
        3: "MP related to general damage assessment",
        4: "MP related to FAME+ Damage Families",
        5: "MP on fittings",
        6: "MP on internal parts",
        7: "MP on supports and structures",
        8: "MP on Coatings (internal and external) and insulation",
        9: "MP on Welds"
    }

def classify_mp(code):
    if len(code) != 4 or not code.isdigit():
        return "Invalid input. Please enter a 4-digit code."

    first_digit = int(code[0])
    second_digit = int(code[1])
    third_digit = int(code[2])
    fourth_digit = int(code[3])

    classification = []

    # First digit
    if first_digit == 1:
        classification.append("MP External (Inspection performed from outside: non intrusive inspection)")
    elif first_digit == 2:
        classification.append("MP Internal (Inspection performed from inside: intrusive inspection)")
    else:
        classification.append("Unknown inspection type")

  
    classification.append(second_digit_types.get(second_digit, "Unknown MP type"))

    # Third and Fourth digits
    if second_digit == 4:  # FAME+ Damage Families
        fame_types = {
            "00": "Thinning-External Damage",
            "10": "Cracking-External Damage",
            "11": "Cracking-Internal, Intermediate insp.",
            "20": "Mechanical Damage"
        }
        classification.append(fame_types.get(f"{third_digit}{fourth_digit}", "Unknown FAME+ damage type"))
    else:
        classification.append(f"Subfamily: {third_digit}, Specific location: {fourth_digit}")

    return ", ".join(classification)

def main():
    st.title("Measuring Point (MP) Classification")

    st.write("Enter a 4-digit MP code to classify it.")
    code = st.text_input("MP Code", max_chars=4)

    if st.button("Classify"):
        result = classify_mp(code)
        st.write("### Classification Result:")
        st.write(result)

    st.write("### Classification System Explanation")

    st.write("#### First Digit Classifications")
    inspection_types = {
        "1": "MP External (Inspection performed from outside: non intrusive inspection)",
        "2": "MP Internal (Inspection performed from inside: intrusive inspection)"
    }
    for inspection_type, description in inspection_types.items():
        st.write(f"{inspection_type}: {description}")

    st.write("#### Second Digit Classifications")
    for second_digit, description in second_digit_types.items():
        st.write(f"{second_digit}: {description}")

    st.write("#### Third & Fourth Digit Classifications")
    st.write("For general qualitative points, the Third Digit usually represents a subfamily within the main families identified above.")
    st.write("The Fourth Digit is normally Zero to indicate that this MP is a general point representing the complete subfamily. Where specific Measuring Point locations are selected, they are identified with the Fourth Digit.")

    st.write("### Examples")
    st.write("180n: External Coating; Thinning External Damage")
    st.write("280n: Internal Coating; Thinning Internal Damage")
    st.write("281n: Internal Cladding")
    st.write("181n: External Insulation")

    st.write("### Quantitative MP Examples")
    st.write("0014: First MP of the piping group located upstream of a Girth Weld")
    st.write("0016: First MP of the piping group located downstream of a Girth Weld")
    st.write("0010: First MP of the piping group located on a tube (away from girth welds)")
    st.write("0024: Second MP of the piping group located upstream of a Girth Weld")

if __name__ == "__main__":
    main()
