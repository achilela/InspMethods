import streamlit as st

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
    elif first_digit == options:
    for inspection_type, description in inspection_types.items():
    st.write(f"{inspection_type}: {description}")

    st.write("### Second Digit Classifications")
    for second_digit, description in second_digit_types.items():
    st.write(f"{second_digit}: {description}")

    st.write("### Third & Fourth Digit Classifications")
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
