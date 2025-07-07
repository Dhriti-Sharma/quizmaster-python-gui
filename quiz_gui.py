import tkinter as tk
from tkinter import messagebox, ttk
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Quiz Application")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Quiz data - aap yaha apne questions add kar sakte hain
        self.questions = [
            {
                "question": "Python mein list ka first element access karne ke liye kya use karte hain?",
                "options": ["list[0]", "list[1]", "list.first()", "list.get(0)"],
                "correct": 0
            },
            {
                "question": "Tkinter kya hai?",
                "options": ["Database", "GUI Library", "Web Framework", "Game Engine"],
                "correct": 1
            },
            {
                "question": "Python mein comment kaise likhte hain?",
                "options": ["// comment", "<!-- comment -->", "# comment", "/* comment */"],
                "correct": 2
            },
            {
                "question": "List mein element add karne ke liye kya use karte hain?",
                "options": ["add()", "append()", "insert()", "push()"],
                "correct": 1
            },
            {
                "question": "Python mein string concatenation kaise karte hain?",
                "options": ["+ operator", "concat()", "join()", "Sabhi sahi hain"],
                "correct": 3
            },
            {
                "question": "Dictionary mein key-value pair access karne ke liye kya use karte hain?",
                "options": ["dict.key", "dict[key]", "dict.get(key)", "B aur C dono"],
                "correct": 3
            },
            {
                "question": "Python mein loop kaise likhte hain?",
                "options": ["for loop", "while loop", "Dono", "Koi nahi"],
                "correct": 2
            },
            {
                "question": "Function define karne ke liye kya keyword use karte hain?",
                "options": ["function", "def", "define", "func"],
                "correct": 1
            },
            {
                "question": "Python mein indentation kya important hai?",
                "options": ["Haan", "Nahi", "Kabhi kabhi", "Pata nahi"],
                "correct": 0
            },
            {
                "question": "Print statement kya karta hai?",
                "options": ["Input leta hai", "Output deta hai", "File banata hai", "Error deta hai"],
                "correct": 1
            }
        ]
        
        self.current_question = 0
        self.score = 0
        self.selected_answer = tk.IntVar()
        self.quiz_started = False
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        self.main_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(self.main_frame, text="🎯 Online Quiz Application", 
                              font=('Arial', 24, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=20)
        
        # Start screen
        self.start_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        self.start_frame.pack(fill=tk.BOTH, expand=True)
        
        welcome_label = tk.Label(self.start_frame, text="Python Quiz mein aapka swagat hai!", 
                                font=('Arial', 16), bg='#f0f0f0', fg='#34495e')
        welcome_label.pack(pady=20)
        
        instructions = tk.Label(self.start_frame, 
                               text="• Total Questions: 10\n• Har question ke liye 4 options hain\n• Correct answer choose karein\n• End mein aapka score dikhega",
                               font=('Arial', 12), bg='#f0f0f0', fg='#7f8c8d', justify=tk.LEFT)
        instructions.pack(pady=20)
        
        start_btn = tk.Button(self.start_frame, text="Quiz Start Karein", 
                             font=('Arial', 14, 'bold'), bg='#3498db', fg='white',
                             padx=30, pady=10, command=self.start_quiz)
        start_btn.pack(pady=30)
        
        # Quiz frame (hidden initially)
        self.quiz_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        
        # Progress bar
        self.progress_frame = tk.Frame(self.quiz_frame, bg='#f0f0f0')
        self.progress_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.progress_label = tk.Label(self.progress_frame, text="Question 1 of 10", 
                                      font=('Arial', 12, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        self.progress_label.pack(side=tk.LEFT)
        
        self.score_label = tk.Label(self.progress_frame, text="Score: 0", 
                                   font=('Arial', 12, 'bold'), bg='#f0f0f0', fg='#e74c3c')
        self.score_label.pack(side=tk.RIGHT)
        
        # Question frame
        self.question_frame = tk.Frame(self.quiz_frame, bg='white', relief=tk.RAISED, bd=2)
        self.question_frame.pack(fill=tk.X, pady=20, padx=10)
        
        self.question_label = tk.Label(self.question_frame, text="", 
                                      font=('Arial', 14, 'bold'), bg='white', fg='#2c3e50',
                                      wraplength=700, justify=tk.LEFT)
        self.question_label.pack(pady=20, padx=20)
        
        # Options frame
        self.options_frame = tk.Frame(self.quiz_frame, bg='#f0f0f0')
        self.options_frame.pack(fill=tk.X, pady=20)
        
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.options_frame, text="", variable=self.selected_answer, 
                               value=i, font=('Arial', 12), bg='#ecf0f1', fg='#2c3e50',
                               selectcolor='#3498db', anchor='w', padx=20, pady=10)
            btn.pack(fill=tk.X, pady=5, padx=20)
            self.option_buttons.append(btn)
        
        # Navigation buttons
        nav_frame = tk.Frame(self.quiz_frame, bg='#f0f0f0')
        nav_frame.pack(fill=tk.X, pady=30)
        
        self.next_btn = tk.Button(nav_frame, text="Next Question", 
                                 font=('Arial', 12, 'bold'), bg='#27ae60', fg='white',
                                 padx=20, pady=10, command=self.next_question)
        self.next_btn.pack(side=tk.RIGHT, padx=20)
        
        self.prev_btn = tk.Button(nav_frame, text="Previous Question", 
                                 font=('Arial', 12, 'bold'), bg='#95a5a6', fg='white',
                                 padx=20, pady=10, command=self.prev_question)
        self.prev_btn.pack(side=tk.LEFT, padx=20)
        
        # Result frame (hidden initially)
        self.result_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        
    def start_quiz(self):
        self.quiz_started = True
        self.current_question = 0
        self.score = 0
        random.shuffle(self.questions)  # Questions ko shuffle kar dete hain
        
        self.start_frame.pack_forget()
        self.quiz_frame.pack(fill=tk.BOTH, expand=True)
        
        self.load_question()
        
    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            
            # Progress update
            self.progress_label.config(text=f"Question {self.current_question + 1} of {len(self.questions)}")
            self.score_label.config(text=f"Score: {self.score}")
            
            # Question text
            self.question_label.config(text=question_data["question"])
            
            # Options
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=f"{chr(65+i)}. {option}")
            
            # Reset selection
            self.selected_answer.set(-1)
            
            # Button states
            self.prev_btn.config(state=tk.NORMAL if self.current_question > 0 else tk.DISABLED)
            self.next_btn.config(text="Next Question" if self.current_question < len(self.questions) - 1 else "Finish Quiz")
            
        else:
            self.show_result()
    
    def next_question(self):
        if self.selected_answer.get() == -1:
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        
        # Check answer
        if self.selected_answer.get() == self.questions[self.current_question]["correct"]:
            self.score += 1
        
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_result()
    
    def prev_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.load_question()
    
    def show_result(self):
        self.quiz_frame.pack_forget()
        self.result_frame.pack(fill=tk.BOTH, expand=True)
        
        # Clear previous results
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        # Result title
        result_title = tk.Label(self.result_frame, text="🎉 Quiz Complete!", 
                               font=('Arial', 24, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        result_title.pack(pady=30)
        
        # Score display
        percentage = (self.score / len(self.questions)) * 100
        score_text = f"Aapka Score: {self.score}/{len(self.questions)} ({percentage:.1f}%)"
        score_label = tk.Label(self.result_frame, text=score_text, 
                              font=('Arial', 18, 'bold'), bg='#f0f0f0', fg='#e74c3c')
        score_label.pack(pady=20)
        
        # Performance message
        if percentage >= 80:
            message = "Excellent! 🌟 Bahut accha performance!"
            color = '#27ae60'
        elif percentage >= 60:
            message = "Good! 👍 Acha hai, aur improve kar sakte hain!"
            color = '#f39c12'
        else:
            message = "Keep practicing! 📚 Aur padhai karo!"
            color = '#e74c3c'
        
        message_label = tk.Label(self.result_frame, text=message, 
                                font=('Arial', 14), bg='#f0f0f0', fg=color)
        message_label.pack(pady=20)
        
        # Progress bar for visual score
        progress_frame = tk.Frame(self.result_frame, bg='#f0f0f0')
        progress_frame.pack(pady=20)
        
        progress_bar = ttk.Progressbar(progress_frame, length=400, mode='determinate')
        progress_bar.pack()
        progress_bar['value'] = percentage
        
        # Buttons
        button_frame = tk.Frame(self.result_frame, bg='#f0f0f0')
        button_frame.pack(pady=30)
        
        retry_btn = tk.Button(button_frame, text="Retry Quiz", 
                             font=('Arial', 12, 'bold'), bg='#3498db', fg='white',
                             padx=20, pady=10, command=self.retry_quiz)
        retry_btn.pack(side=tk.LEFT, padx=10)
        
        exit_btn = tk.Button(button_frame, text="Exit", 
                            font=('Arial', 12, 'bold'), bg='#e74c3c', fg='white',
                            padx=20, pady=10, command=self.root.quit)
        exit_btn.pack(side=tk.LEFT, padx=10)
    
    def retry_quiz(self):
        self.result_frame.pack_forget()
        self.start_frame.pack(fill=tk.BOTH, expand=True)
        self.current_question = 0
        self.score = 0
        self.quiz_started = False

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()