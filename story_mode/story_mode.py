import tkinter as tk
from tkinter import PhotoImage, Label, Entry, Button, messagebox
from PIL import Image, ImageTk
from skills import generate_and_save_images

def story_mode(ai_message):
    # Use the imported function to generate an image based on ai_message
    image_files = generate_and_save_images(ai_message)
    if not image_files:
        print("Failed to generate image.")
        return

    window = tk.Tk()
    window.title("Adventure Storybook")

    # Handle window close event
    def on_window_close():
        print("Please exit story mode.")
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_window_close)

    img_path = image_files[0]
    img = Image.open(img_path)
    img = img.resize((800, 600), Image.LANCZOS)
    photo_img = ImageTk.PhotoImage(img)

    canvas = tk.Canvas(window, width=800, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=photo_img)

    # Overlay the AI message over the image
    ai_message_text = canvas.create_text(400, 30, text=ai_message, fill="white", font=('Helvetica', 15, 'bold'), width=780)

    user_input = Entry(window, bg="#aaaaaa", fg="white", width=50)
    user_input_canvas = canvas.create_window(400, 550, window=user_input, width=400)

    def submit_input():
        user_response = user_input.get()
        print(f"User response: {user_response}")
        window.destroy()

    submit_button = Button(window, text="Submit", command=submit_input)
    submit_btn_canvas = canvas.create_window(400, 590, window=submit_button)

    window.mainloop()

# test case
if __name__ == "__main__":
    story_mode("Welcome to the gateway of adventures! What will you do?")

# EXAMPLE USE
# from skills import story_mode
# opening_message = "With the map in hand, Alex steps into the Whispering Woods. The path ahead is shrouded in mystery. How do you proceed?"  
# story_mode(opening_message)