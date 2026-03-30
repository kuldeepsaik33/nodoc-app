import tkinter as tk

# -------- ORIGINAL DICTIONARY -------- #
diseases = {
    "fever": ("Rest, fluids", "Paracetamol", "Tulsi + ginger"),
    "cold": ("Steam inhalation", "Benadryl", "Honey"),
    "cough": ("Warm fluids", "Ascoril", "Ginger"),
    "sore throat": ("Salt gargle", "Strepsils", "Turmeric milk"),
    "headache": ("Rest", "Paracetamol", "Oil massage"),
    "migraine": ("Dark room", "Combiflam", "Peppermint oil"),
    "stomach pain": ("Avoid spicy food", "Gelusil", "Jeera water"),
    "indigestion": ("Light food", "Digene", "Ajwain"),
    "vomiting": ("ORS", "Electral", "Ginger juice"),
    "diarrhea": ("ORS", "Electral", "Rice water"),
    "constipation": ("Fiber food", "Laxative", "Warm water"),
    "gas": ("Avoid oily food", "Antacid", "Jeera"),
    "food poisoning": ("Hydration", "ORS", "Mint water"),
    "dehydration": ("Water + ORS", "ORS", "Coconut water"),
    "back pain": ("Rest", "Volini", "Oil massage"),
    "joint pain": ("Rest", "Pain relief", "Turmeric milk"),
    "muscle pain": ("Rest", "Spray", "Salt bath"),
    "allergy": ("Avoid allergen", "Cetzine", "Neem"),
    "skin rash": ("Keep clean", "Calamine", "Aloe vera"),
    "itching": ("Keep dry", "Antihistamine", "Neem water"),
    "eye infection": ("Clean eyes", "Eye drops", "Rose water"),
    "ear pain": ("Keep dry", "Drops", "Garlic oil"),
    "tooth pain": ("Salt rinse", "Combiflam", "Clove oil"),
    "asthma": ("Sit upright", "Inhaler", "Steam"),
    "breathing problem": ("Stay calm", "Inhaler", "Tulsi tea"),
    "burn": ("Cool water", "Silverex", "Aloe vera"),
    "cut": ("Clean + bandage", "Antiseptic", "Turmeric"),
    "bleeding": ("Apply pressure", "Bandage", "Cloth"),
    "dizziness": ("Sit down", "ORS", "Sugar water"),
    "fatigue": ("Rest", "Multivitamin", "Dates"),
    "low bp": ("Salt water", "ORS", "Salt water"),
    "high bp": ("Relax", "Doctor meds", "Garlic"),
    "anxiety": ("Relax", "Mild meds", "Breathing"),
    "stress": ("Rest", "None", "Meditation"),
    "insomnia": ("Sleep routine", "Warm milk", "Milk"),
    "acidity": ("Avoid spicy", "Antacid", "Cold milk"),
    "fungal infection": ("Keep dry", "Cream", "Neem"),
    "boils": ("Clean area", "Cream", "Turmeric"),
    "nose bleeding": ("Tilt forward", "Cold compress", "Ice"),
    "sunburn": ("Cool skin", "Aloe gel", "Aloe vera"),
    "heat stroke": ("Cool place", "ORS", "Water"),
    "cramps": ("Rest", "Pain relief", "Warm compress"),
    "fracture": ("Immobilize", "Emergency", "NONE"),
    "snake bite": ("Keep still", "Emergency", "NONE"),
    "insect bite": ("Wash area", "Antihistamine", "Ice"),
}

# -------- AUTO DETAILS -------- #
details = {}
for d in diseases:
    details[d] = (
        f"{d.title()} is commonly caused by infections, lifestyle or environmental factors.\nIt may also result from internal imbalance.",
        f"Common symptoms include discomfort or irritation related to {d}.\nSeverity varies depending on the condition."
    )

# -------- APP -------- #
app = tk.Tk()
app.title("NODOC")
app.geometry("380x650")
app.configure(bg="#eef2ff")

# -------- MAIN SCREEN -------- #
def main_screen():
    for widget in app.winfo_children():
        widget.destroy()

    frame = tk.Frame(app, bg="#eef2ff")
    frame.pack(fill="both", expand=True)

    header = tk.Frame(frame, bg="#4f46e5")
    header.pack(fill="x")

    tk.Label(header, text="NODOC",
             bg="#4f46e5", fg="white",
             font=("Segoe UI", 16, "bold")).pack(pady=(8,0))

    tk.Label(header, text="Offline Smart Health Assistant",
             bg="#4f46e5", fg="#e0e7ff").pack(pady=(0,8))

    card = tk.Frame(frame, bg="white")
    card.pack(padx=10, pady=15, fill="both", expand=True)

    tk.Label(card, text="Patient Name", bg="white").pack(anchor="w", padx=8, pady=4)
    name_entry = tk.Entry(card)
    name_entry.pack(fill="x", padx=8, ipady=5)

    tk.Label(card, text="Search Disease", bg="white").pack(anchor="w", padx=8, pady=4)
    search_entry = tk.Entry(card)
    search_entry.pack(fill="x", padx=8, ipady=5)

    listbox = tk.Listbox(card, height=6)
    listbox.pack(fill="x", padx=8, pady=8)

    def update_suggestions(event):
        typed = search_entry.get().lower()
        listbox.delete(0, tk.END)
        for d in diseases:
            if typed in d:
                listbox.insert(tk.END, d)

    def fill_selection(event):
        if listbox.curselection():
            selected = listbox.get(listbox.curselection())
            search_entry.delete(0, tk.END)
            search_entry.insert(0, selected)

    search_entry.bind("<KeyRelease>", update_suggestions)
    listbox.bind("<<ListboxSelect>>", fill_selection)

    tk.Button(card, text="Get Advice",
              command=lambda: show_result(name_entry.get(), search_entry.get()),
              bg="#4f46e5", fg="white",
              font=("Segoe UI", 10, "bold")).pack(pady=8)

# -------- RESULT SCREEN -------- #
def show_result(name, query):
    name = name or "Patient"
    query = query.strip().lower()

    matched = None
    for d in diseases:
        if query in d:
            matched = d
            break

    for widget in app.winfo_children():
        widget.destroy()

    frame = tk.Frame(app, bg="#eef2ff")
    frame.pack(fill="both", expand=True)

    header = tk.Frame(frame, bg="#4f46e5")
    header.pack(fill="x")

    tk.Label(header, text="Medical Report",
             bg="#4f46e5", fg="white",
             font=("Segoe UI", 14, "bold"),
             pady=8).pack(fill="x")

    if matched:
        aid, med, ayur = diseases[matched]
        cause, symp = details[matched]

        tk.Label(frame, text=f"Patient: {name}",
                 bg="#eef2ff",
                 font=("Segoe UI", 9)).pack(fill="x", padx=8, pady=3)

        tk.Label(frame, text=matched.title(),
                 bg="#eef2ff",
                 font=("Segoe UI", 15, "bold"),
                 fg="#1e293b").pack(fill="x", padx=8)

        tk.Frame(frame, height=1, bg="#d1d5db").pack(fill="x", padx=8, pady=4)

        def section(title, content, color):
            box = tk.Frame(frame, bg=color)
            box.pack(fill="x", padx=6, pady=4)

            tk.Label(box, text=title,
                     bg=color, fg="white",
                     font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=8, pady=(4,1))

            tk.Label(box, text=content,
                     bg=color, fg="white",
                     font=("Segoe UI", 9),
                     wraplength=350,
                     justify="left").pack(fill="x", padx=8, pady=(0,5))

        section("Causes", cause, "#ef4444")
        section("Symptoms", symp, "#f59e0b")
        section("First Aid", aid, "#10b981")
        section("Medication", med, "#3b82f6")
        section("Ayurvedic Support", ayur, "#8b5cf6")

        tk.Label(frame,
                 text="Prototype only. Consult doctor for accurate diagnosis.",
                 bg="#eef2ff", fg="#6b7280",
                 font=("Segoe UI", 8)).pack(pady=3)

    else:
        tk.Label(frame, text="Sorry for the inconvenience , disease not found\n Please Consult a doctor.",
                 fg="red", bg="#eef2ff").pack(pady=20)

    tk.Button(frame, text="Back",
              command=main_screen,
              bg="#111827", fg="white",
              font=("Segoe UI", 9)).pack(fill="x", padx=8, pady=6)

# -------- START -------- #
main_screen()
app.mainloop()