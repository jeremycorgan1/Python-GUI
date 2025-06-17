#!/usr/bin/env python3
"""Simple GUI to discover and run Python scripts from a dedicated folder.

The folder defaults to ~/pyprojects but can be changed by editing
PROJECTS_DIR below.
"""

import os
import subprocess
import threading
import tkinter as tk
from tkinter import messagebox

# Path where your .py projects live. Adjust if you prefer a different folder.
PROJECTS_DIR = os.path.expanduser("~/pyprojects")

class ProjectRunnerGUI(tk.Tk):
    """Main application window."""

    def __init__(self):
        super().__init__()

        # Window properties
        self.title("Python Project Runner")
        self.geometry("400x300")
        self.resizable(False, False)

        # Listbox to show available projects
        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=(10, 0), pady=10)

        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y, pady=10)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Right‑hand frame for action buttons
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        run_button = tk.Button(button_frame, text="Run", command=self.run_selected)
        run_button.pack(fill=tk.X, pady=(0, 5))

        refresh_button = tk.Button(button_frame, text="Refresh", command=self.populate_projects)
        refresh_button.pack(fill=tk.X)

        # Initial population of listbox
        self.populate_projects()

    def populate_projects(self):
        """Load .py files from PROJECTS_DIR into the listbox."""
        self.listbox.delete(0, tk.END)
        if not os.path.isdir(PROJECTS_DIR):
            # Create the directory if it doesn't exist yet.
            os.makedirs(PROJECTS_DIR, exist_ok=True)
        for filename in sorted(os.listdir(PROJECTS_DIR)):
            if filename.endswith(".py"):
                self.listbox.insert(tk.END, filename)

    def run_selected(self):
        """Run the script that is currently selected in the listbox."""
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("No selection", "Please select a project to run.")
            return

        script_name = self.listbox.get(selection[0])
        script_path = os.path.join(PROJECTS_DIR, script_name)

        # Run in a background thread to keep the GUI responsive
        threading.Thread(target=self._launch_script, args=(script_path,), daemon=True).start()

    def _launch_script(self, script_path: str):
        """Launch the given script using the system's default Python interpreter."""
        try:
            # Opens a subprocess detached from the GUI so it doesn't freeze.
            subprocess.Popen(["python3", script_path])
        except Exception as exc:
            messagebox.showerror("Execution error", f"Could not run {script_path}:\n{exc}")


if __name__ == "__main__":
    app = ProjectRunnerGUI()
    app.mainloop()

