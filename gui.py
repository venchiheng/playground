import tkinter as tk
from PIL import Image, ImageTk
from bfs import bfsSearch, graph
import tkinter.font

def launch_gui():
    root = tk.Tk()
    root.title("BFS Rental Search")
    root.geometry("1000x850")
    root.configure(bg="#87CEFA")  
    cf = tkinter.font.Font(family='Helvetica', size= 14)

    # ===== Animated GIF Setup =====
    gif = Image.open('E:\TGI\AI\playground\GUI.gif')  

    gif_label = tk.Label(root, bg="#87CEFA")
    gif_label.pack(pady=10)

    def animate_gif(frame_num):
        try:
            gif.seek(frame_num)
            frame = ImageTk.PhotoImage(gif.resize((150, 150)))  
            gif_label.config(image=frame)
            gif_label.image = frame 

            root.after(100, animate_gif, (frame_num + 1) % gif.n_frames)  # Loop frames
        except Exception as e:
            print("GIF Error:", e)

    animate_gif(0)  # Start GIF animation
    # ===== Search Function =====
    def on_search():
        result_text.delete(1.0, tk.END)

        def collect_logs(message):
            result_text.insert(tk.END, message + "\n")
            result_text.see(tk.END)

        bfsSearch(graph, endNode=loc_var.get(), priceRange=price_var.get(), typeAccomadation=type_var.get(), output_func=collect_logs)


    # Create a container frame to align all sections horizontally
    container = tk.Frame(root, background="white", padx=20, pady=20)
    container.pack(pady=30)

    # === Location Section ===
    loc_frame = tk.Frame(container, bg="white")
    tk.Label(loc_frame, text="Location: (e.g. SenSok, ToulKork, BKK,...)", bg="white", font=cf).pack()
    loc_var = tk.StringVar()
    tk.Entry(loc_frame, width=20, textvariable=loc_var, font=cf).pack(pady=5)
    loc_frame.pack(side="left", padx=10)

    # === Divider ===
    tk.Frame(container, bg="black", width=1, height=60).pack(side="left", padx=5)

    # === Price Section ===
    price_frame = tk.Frame(container, bg="white")
    tk.Label(price_frame, text="Price Range: (e.g. 100, 250, 300,...)", bg="white", font=cf).pack()
    price_var = tk.IntVar()
    tk.Entry(price_frame, width=20, textvariable=price_var, font=cf).pack(pady=5)
    price_frame.pack(side="left", padx=10)

    # === Divider ===
    tk.Frame(container, bg="black", width=1, height=60).pack(side="left", padx=5)

    # === Type Section ===
    type_frame = tk.Frame(container, bg="white")
    tk.Label(type_frame, text="House Type: (e.g. apartment, house, or room)", bg="white", font=cf).pack()
    type_var = tk.StringVar()
    tk.Entry(type_frame, width=20, textvariable=type_var, font=cf).pack(pady=5)
    type_frame.pack(side="left", padx=10)
    tk.Button(root, text="Search", command=on_search, font=cf).pack(pady=10)
    
    # ===== Result Text Area =====
    result_text = tk.Text(root,width= 170,height=25, font=cf)
    result_text.pack(pady=10)

    root.mainloop()