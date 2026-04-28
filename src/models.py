class Course:
    def __init__(self, title, description, instructor, duration, topics=None):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.duration = duration
        self.topics = topics or []

    def __repr__(self):
        return f"<Course {self.title} by {self.instructor}>"

courses = [
    Course(
        "Introduction to Python",
        "Learn the basics of Python programming.",
        "John Doe",
        "4 weeks",
        topics=["Variables and Data Types", "Control Flow", "Functions", "Modules"],
    ),
    Course(
        "Web Development with Flask",
        "Build web applications using Flask.",
        "Jane Smith",
        "6 weeks",
        topics=["Routing", "Templates", "Forms", "Databases"],
    ),
    Course(
        "Data Science Fundamentals",
        "An introduction to data science concepts and tools.",
        "Alice Johnson",
        "8 weeks",
        topics=["NumPy", "Pandas", "Matplotlib", "Machine Learning Basics"],
    ),
    Course(
        "Go Programming Language",
        "Learn Go from the ground up: syntax, concurrency, and building production-ready services.",
        "Bob Lee",
        "5 weeks",
        topics=["Syntax and Types", "Goroutines and Channels", "Interfaces", "Building REST APIs"],
    ),
]