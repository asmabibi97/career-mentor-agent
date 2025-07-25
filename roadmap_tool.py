from agents import function_tool

@function_tool
def get_career_roadmap(field: str) -> str:
    maps = {
        "software engineer": "Learn Python, Data Structures, Algorithms, System Design",
        "web dev": "Learn HTML, CSS, JavaScript, React or Next.js, then backend like Node.js or Django",
        "data science": "Master Python, Pandas, NumPy, ML with Scikit-learn, and deep learning with TensorFlow or PyTorch",
        "ui/ux designer": "Learn Figma, Adobe XD, UX Research, and Prototyping tools",
        "ai engineer": "Study Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, and LLMs"
    }

    return maps.get(field.lower(), "No roadmap found for this field.")
