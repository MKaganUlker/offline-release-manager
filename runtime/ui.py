import tkinter as tk
from tkinter import ttk, messagebox

from runtime.bootstrap import bootstrap
from runtime.release_index import load_index
from runtime.installer import install
from runtime.logger import get_logger
from runtime.paths import CACHE

import subprocess
import shutil

log = get_logger("ui")


class LauncherUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline Release Launcher")
        self.root.resizable(False, False)

        self.releases = []
        self.selected_version = tk.StringVar()

        self._build_ui()
        self._load_releases()

    def _build_ui(self):
        main = ttk.Frame(self.root, padding=10)
        main.grid(row=0, column=0)

        # Versions list
        ttk.Label(main, text="Versions").grid(row=0, column=0, sticky="w")

        self.listbox = tk.Listbox(
            main, width=30, height=6, exportselection=False
        )
        self.listbox.grid(row=1, column=0, sticky="nsew")
        self.listbox.bind("<<ListboxSelect>>", self._on_select)

        # Notes box
        ttk.Label(main, text="Release Notes").grid(
            row=0, column=1, sticky="w", padx=(10, 0)
        )

        self.notes = tk.Text(
            main, width=40, height=6, wrap="word", state="disabled"
        )
        self.notes.grid(row=1, column=1, padx=(10, 0))

        # Launch button
        self.launch_btn = ttk.Button(
            main, text="Launch Selected", command=self._launch
        )
        self.launch_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def _load_releases(self):
        try:
            bootstrap()
            index = load_index()
            self.releases = index["releases"]
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.root.destroy()
            return

        self.listbox.delete(0, tk.END)

        default_index = 0
        for i, r in enumerate(self.releases):
            label = r["version"]
            if r.get("recommended"):
                label += "  (recommended)"
                default_index = i
            self.listbox.insert(tk.END, label)

        self.listbox.select_set(default_index)
        self._show_notes(default_index)

    def _on_select(self, event):
        sel = self.listbox.curselection()
        if not sel:
            return
        self._show_notes(sel[0])

    def _show_notes(self, index):
        release = self.releases[index]

        self.notes.configure(state="normal")
        self.notes.delete("1.0", tk.END)
        self.notes.insert(tk.END, release.get("notes", ""))
        self.notes.configure(state="disabled")

        self.selected_version.set(release["version"])

    def _launch(self):
        version = self.selected_version.get()
        if not version:
            return

        # Remove other cached versions
        for d in CACHE.iterdir():
            if d.is_dir() and d.name != version:
                shutil.rmtree(d)

        try:
            app_dir = install(version)
            subprocess.Popen(
                str(app_dir / "app.exe"),
                shell=True
            )
        except Exception as e:
            messagebox.showerror("Launch failed", str(e))


def main():
    root = tk.Tk()
    LauncherUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
