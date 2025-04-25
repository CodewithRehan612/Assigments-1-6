import streamlit as st

def main():
    st.title("🎭 Mad Libs Generator")
    st.write("Fill in the blanks to create your own silly story!")

    # Story templates
    stories = {
        "Space Adventure": "One day, a {adjective} astronaut named {name} went on a mission to {place}. "
        "They brought their trusty {noun} and a {color} spacesuit. "
        "During the journey, they encountered a {adjective2} alien who wanted to {verb} with them. "
        "Together, they discovered a {adjective3} planet made entirely of {noun2}!",
        
        "Pirate Tale": "Captain {name} was the most {adjective} pirate to ever sail the {color} seas. "
        "Their ship, the {noun}, was known for its {adjective2} crew and {adjective3} treasure. "
        "One day, they found a map leading to {place}, where they discovered a {noun2} that could {verb}.",
        
        "Dinosaur Discovery": "In a {adjective} jungle, a {adjective2} scientist named {name} found a {color} dinosaur egg. "
        "When it hatched, out came a {adjective3} baby {noun} that loved to {verb}. "
        "They took it to {place} where it became famous for its ability to {verb2}."
    }

    # Sidebar for story selection
    story_choice = st.sidebar.selectbox("Choose a story template:", list(stories.keys()))
    
    # Get user inputs
    st.subheader("Fill in the blanks:")
    
    # Common inputs
    name = st.text_input("Enter a name:")
    place = st.text_input("Enter a place:")
    color = st.text_input("Enter a color:")
    verb = st.text_input("Enter a verb:")
    
    # Story-specific inputs
    if story_choice == "Space Adventure":
        adjective = st.text_input("Enter an adjective:")
        noun = st.text_input("Enter a noun:")
        adjective2 = st.text_input("Enter another adjective:")
        adjective3 = st.text_input("Enter one more adjective:")
        noun2 = st.text_input("Enter another noun:")
        
    elif story_choice == "Pirate Tale":
        adjective = st.text_input("Enter an adjective:")
        noun = st.text_input("Enter a noun:")
        adjective2 = st.text_input("Enter another adjective:")
        adjective3 = st.text_input("Enter one more adjective:")
        noun2 = st.text_input("Enter another noun:")
        
    else:  # Dinosaur Discovery
        adjective = st.text_input("Enter an adjective:")
        adjective2 = st.text_input("Enter another adjective:")
        adjective3 = st.text_input("Enter one more adjective:")
        noun = st.text_input("Enter a noun:")
        verb2 = st.text_input("Enter another verb:")

    # Generate story button
    if st.button("Generate Story!"):
        if all([name, place, color, verb]):
            # Get the selected story template
            story = stories[story_choice]
            
            # Fill in the blanks
            if story_choice == "Space Adventure":
                filled_story = story.format(
                    adjective=adjective,
                    name=name,
                    place=place,
                    noun=noun,
                    color=color,
                    adjective2=adjective2,
                    verb=verb,
                    adjective3=adjective3,
                    noun2=noun2
                )
            elif story_choice == "Pirate Tale":
                filled_story = story.format(
                    name=name,
                    adjective=adjective,
                    color=color,
                    noun=noun,
                    adjective2=adjective2,
                    adjective3=adjective3,
                    place=place,
                    noun2=noun2,
                    verb=verb
                )
            else:  # Dinosaur Discovery
                filled_story = story.format(
                    adjective=adjective,
                    adjective2=adjective2,
                    name=name,
                    color=color,
                    adjective3=adjective3,
                    noun=noun,
                    verb=verb,
                    place=place,
                    verb2=verb2
                )
            
            # Display the story
            st.subheader("Your Story:")
            st.write(filled_story)
        else:
            st.error("Please fill in all the blanks!")

if __name__ == "__main__":
    main() 