import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Page setup
st.set_page_config(page_title="WB Motion - Text-to-Motion Playground", layout="wide")
st.title("WB Motion: Text-to-Motion Playground")
st.subheader("Tencent Hunyuan 3D Digital Human Team")

# Predefined motion descriptions
MOTION_DESCRIPTIONS = [
    "A person jumps upward with both legs twice.",
    "A person jumps on their right leg.",
    "A person climbs upward, moving up the slope.",
    "A person climbs an obstacle.",
    "A person walks forward.",
    "A person walks forward, moving arms and legs while...",
    "A person walks unsteadily, then slowly sits down.",
    "A person turns backward 180 degrees, then walks forward.",
    "A person walks in a catwalk style, swinging their hips.",
    "A person squats down on tiptoe",
    "A person sits down on a chair.",
    "A person runs forward.",
    "A person jumps up.",
    "A person jumps forward lightly, taking two steps.",
    "A person shoots a basketball.",
    "A person finishes freestyle swimming, then surfaces.",
    "A person swings a golf club, hitting the ball forward.",
    "A person runs forward, then kicks a soccer ball.",
    "A person walks on a tightrope.",
    "A person performs a yoga camel pose, extending their back.",
    "A person performs a sit-up, holding their head with both hands.",
    "A person performs a lunge stretch, hands on hips.",
    "A person performs a deadlift, lifting a barbell from the ground.",
    "A person marches in place, swinging their arms forward.",
    "A person performs a squat, not standing up.",
    "A person performs a squat.",
    "A person performs a front arm raise, then does a side arm raise.",
    "A person performs a squat, raising both arms forward.",
    "A person does a squat, balling both hands into fists.",
    "A person plays the piano.",
    "A person dances bachata, executing rhythmic hip movements.",
    "A person plays the drums while sitting down, with both hands.",
    "A person plays the drums while sitting down, with one hand."
]

# Sidebar controls
st.sidebar.header("Select or Enter Motion Description")
selected_motion = st.sidebar.selectbox("Choose a predefined motion:", MOTION_DESCRIPTIONS, index=0)
custom_motion = st.sidebar.text_input("Or enter a custom motion description:")

# Final motion text
final_motion = custom_motion.strip() if custom_motion.strip() else selected_motion

# Generate button
generate = st.sidebar.button("Generate Motion")

# Layout
left_col, right_col = st.columns([2, 3])

with left_col:
    st.markdown("### Motion details")
    st.write(f"**Selected motion:** {final_motion}")
    st.caption("Tip: Use custom input to try your own motion prompt.")

with right_col:
    st.markdown("### Motion display")
    if generate:
        st.success("Generating motion...")
        st.write(f"**Motion Description:** {final_motion}")

        # Simple stick figure demo (jumping motion)
        fig, ax = plt.subplots()
        ax.set_xlim(0, 2)
        ax.set_ylim(0, 2)
        ax.axis("off")

        # Draw stick figure (basic pose)
        head = plt.Circle((1, 1.5), 0.1, color="black")
        ax.add_patch(head)
        ax.plot([1, 1], [1.5, 1], color="black")  # body
        ax.plot([1, 0.8], [1.3, 1.1], color="black")  # left arm
        ax.plot([1, 1.2], [1.3, 1.1], color="black")  # right arm
        ax.plot([1, 0.9], [1, 0.7], color="black")  # left leg
        ax.plot([1, 1.1], [1, 0.7], color="black")  # right leg

        st.pyplot(fig)

        st.info("Demo stick figure shown. Replace with real 3D motion renderer later.")
    else:
        st.warning("Select or enter a motion, then click 'Generate Motion' to preview.")

# Footer
st.caption("WB Motion — prototype build. Replace the demo with your 3D renderer when ready.")
